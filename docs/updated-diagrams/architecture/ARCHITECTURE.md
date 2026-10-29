# System Architecture and Technology Justification

**Task 4** in [`DIAGRAM_TASKS.md`](../../../DIAGRAM_TASKS.md).
**Built from:** [`Itqan_Requirements.md`](../../../Itqan_Requirements.md), using §10 (system parts), §8 (stored and never-stored data), §5 (NFRs), §1 (scope and connectivity) and §11 (items left to IS499).

**Files:**
- `itqan-architecture.puml`: editable source.
- `itqan-architecture.svg` and `itqan-architecture.png`: rendered with PlantUML 1.2026.9.

**Page fit:** 1123 × 847 px. Place it on an **A4 landscape** page, where it scales to 0.94 (about 8.5 pt text).

## 1. Purpose

The diagram shows Itqan's major parts, where each one runs, and how they communicate. It also marks where recitation audio exists only temporarily and what is stored. It is a component view: the step-by-step order of calls belongs to the sequence diagrams (Task 5).

## 2. Parts

Every part in requirements §10 appears in the diagram.

| Part (§10) | Runs on | Responsibility | FRs |
|---|---|---|---|
| **Itqan App** | Phone, Android or iOS (Flutter) | **Screens:** Arabic right-to-left and English, per-verse feedback and next-word hints. **Microphone capture:** 16 kHz mono, segmented by verse, plus pause detection for Smart Prompting. **Bundled Juz Amma text and reference audio:** offline reading and word audio. | All (user interface), FR-17, FR-26 |
| **Identity Provider** | External managed service (vendor: O-5) | Credentials, sign in and out, account removal; returns the identity subject. | FR-01, FR-02, FR-28, FR-29 |
| **Account Service** | Application backend (FastAPI) | Accounts, profiles, language, consent records, data summary, account deletion and the deletion log. | FR-01–FR-03, FR-10, FR-27, FR-28 |
| **Recitation Service** | Application backend | Runs each session; **all session traffic goes through it**. Its *session control* part starts the session, sends each verse for analysis, returns feedback, ends the session, calculates the score and stores the results. | FR-11–FR-20 |
| **Comparison Engine** | Inside the Recitation Service | Aligns the returned phonemes with the expected verse, classifies errors and links each error to a word. | FR-14, FR-15 |
| **Analysis Service** | Separate stateless Python/GPU service (`obadx/muaalem-model-v3_2`) | Receives one verse's audio and returns phonemes with articulation attributes. Keeps nothing. | FR-13 |
| **Progress Service** | Application backend | Results, session history, best score per surah, full mastery, average mastery and streak. Recalculated after each session. | FR-20–FR-22 |
| **Class Service** | Application backend | Classes, join codes, enrolments, the teacher dashboard with enrolment and join-date checks, and messages with read status. | FR-23–FR-25 |
| **Database** | PostgreSQL | Stores only §8.1: accounts, consents, sessions and mistakes, classes, enrolments, messages, the deletion log, and the read-only Juz Amma reference tables. | All stored data |

"Session control" names the Recitation Service's own orchestration work. It is drawn as a separate box only so that its arrows can be told apart from the Comparison Engine's.

## 3. Connections

| From → To | What passes | Kind |
|---|---|---|
| Screens → Identity Provider | Sign in and out | HTTPS |
| Account Service → Identity Provider | Remove the account on deletion (FR-28) | HTTPS |
| Screens → Account Service | Profile, consent, data summary, deletion | HTTPS / REST |
| Screens → Class Service | Classes, join, leave, dashboard, messages | HTTPS / REST |
| Screens → Progress Service | Results, history, progress, streak | HTTPS / REST |
| Microphone capture → Recitation Service | One verse's audio + verse ID | HTTPS, **transient** |
| Recitation Service → Screens | Per-verse feedback | HTTPS / REST |
| Recitation Service → Analysis Service → Recitation Service | Verse audio in; phonemes out | **Transient**, in memory |
| Comparison Engine → Database (Juz Amma reference) | Expected verse and word positions (read-only) | SQL read |
| Recitation Service → Database | Session summary + mistakes at session end (no audio) | SQL write |
| Account, Class and Progress Services → Database | Their own data | SQL |
| Screens ↔ Bundled Juz Amma | Verse text, word reference audio | On the phone, offline |

**Not drawn as an arrow:** at the end of a session, the Recitation Service asks the Progress Service to recalculate (§10 main path). An arrow inside the backend node could not be laid out without crossing other lines, so the Progress Service label says "recalculated after each session" instead. The call is shown step by step in the recitation sequence diagram (Task 5).

## 4. Processing and storage boundaries

| Data | Where it exists | Stored? |
|---|---|---|
| Recitation audio | Phone microphone buffer → in transit → Recitation Service memory → Analysis Service memory | **Never** (dashed arrows). It is never written to disk, the database or logs (NFR-07). |
| Phonemes (analysis output) | Analysis Service → Recitation Service memory | **Never**. Discarded after comparison. |
| Feedback, praise, hints, audio-assistance requests | Recitation Service → phone screen | **Never** (§8.3). |
| Session summary + mistakes | Recitation Service → Database | **Stored** (BR-05). |
| Progress figures (best score, mastery, streak) | Progress Service | **Derived** from stored sessions; may be cached (§8.1). |
| Juz Amma text | Phone bundle (offline display) **and** Database (read-only reference for comparison and mistake links) | Read-only reference data. |
| Reference word audio | Phone bundle only | Bundled with the app, not in the database. |
| Credentials and passwords | Identity Provider only | Never stored by Itqan. |

**Offline behaviour (§1):** browsing and reading surahs, and playing word audio, use only the phone bundle. Recitation, results, classes and messages need the backend.

## 5. Security and privacy in the architecture

| Concern | How the architecture handles it | Requirement |
|---|---|---|
| No stored audio | Audio only travels along the dashed path and stays in memory. The Analysis Service is stateless. | NFR-07, FR-12 |
| No passwords | Authentication is delegated to the Identity Provider. Itqan keeps only the identity subject. | FR-01, NFR-06 |
| Teacher access | The Class Service checks the active enrolment and join date on every read, in the data layer. | BR-08, NFR-06 |
| Transport | All phone ↔ backend traffic uses HTTPS. | NFR-06 |
| Deletion | The Account Service erases data in the Database and removes the identity-provider account. | FR-28, BR-17 |

## 6. Technology justification

These are the choices in requirements §10. The reasons below relate each choice to Itqan's requirements; none of them is a measured result.

| Layer | Choice | Alternatives considered | Why it fits Itqan |
|---|---|---|---|
| Mobile app | **Flutter** | Native Android + native iOS; web app | One codebase for both target platforms (NFR-10) is realistic for a three-person team. Microphone capture, offline bundled content and right-to-left Arabic layout (NFR-11) are more dependable in a mobile app than in a browser. |
| Application backend | **FastAPI (Python)** | Node.js; Django | The analysis tooling is Python, so one language serves the backend and the analysis integration. The backend only serves a REST API (no web pages), which suits a lightweight API framework. Separate services match NFR-09. |
| Recitation analysis | **Separate stateless service running `obadx/muaalem-model-v3_2`** | Training a new model; a third-party correction API; on-device analysis | A ready, openly published Quran pronunciation model avoids a training project. Keeping it in its own stateless service isolates the GPU workload, keeps audio out of storage (NFR-07), and lets reading, progress and classes work when analysis is unavailable (FR-13). A third-party API would send learner audio to an outside party. On-device analysis was not chosen because running a model of this size on phones is unproven for this project. |
| Database | **PostgreSQL** | MySQL; a document database | The data is relational (accounts, sessions, mistakes, classes, enrolments, messages), and the key access rule (a teacher sees a reader only through an active enrolment and its join date) is a join that can be enforced in one place (NFR-06). |
| Authentication | **Managed identity provider** (vendor in IS499, O-5) | Building an own login system; social sign-in only | Removes password storage and reset handling from Itqan (FR-01), supports logout and session expiry (FR-29), and supports account removal (FR-28). |
| Quran content | **Bundled Juz Amma text** from the King Fahd Glorious Quran Printing Complex, plus reference audio | An online Quran service; serving text only from the backend | Authoritative text; offline reading and word audio (§1). Juz Amma (37 surahs, 564 verses, 2,308 words) is small enough to bundle. |

**Limits stated honestly:**
- The model's published results are not Itqan results. Detection accuracy for Ghunnah, Qalqalah and Madd, and per-verse latency, must be measured in IS499 (NFR-01, NFR-02, O-2).
- The model's licence and the Quran source's terms of use must be confirmed before any public release.
- Automatic end-of-verse detection and pause detection (FR-13, FR-26) are design requirements whose feasibility is tested during implementation.

## 7. Left open (requirements §11)

| ID | Item | Effect on the diagram |
|---|---|---|
| O-1 | Production hosting, including the GPU host for the Analysis Service | None: nodes are shown without a vendor. |
| O-4 | Reference audio source and word timings | None: shown as "bundled reference audio". |
| O-5 | Identity provider vendor | None: shown as "Managed Identity Provider". |

## 8. Task 4 checklist

- [x] Parts grouped by phone, backend, managed identity provider, analysis service and database.
- [x] Exact §10 names; Comparison Engine inside the Recitation Service.
- [x] Major connections labelled; all session traffic goes through the Recitation Service.
- [x] Bundled Quran text and reference audio shown, with offline reading and word audio.
- [x] Temporary audio and phonemes (dashed) distinguished from stored summaries and mistakes; no audio path to the database.
- [x] Technology justification with alternatives, without presenting assumptions as facts.
- [x] Hosting and identity-provider vendor kept generic (§11).

## 9. Requirement added during this task

The requirements did not say where the Quran text lives on the server. The Comparison Engine needs the expected verse, and every mistake links to a word, so the decision is: **the Juz Amma text is bundled in the app and also held as read-only reference tables in the Database; reference audio is in the app only.** It was added to requirements §8.1, §10 and §12 before the diagram was drawn.
