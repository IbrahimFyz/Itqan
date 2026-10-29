# Itqan class diagram — Task 8 review notes

**Source of truth:** [final requirements](Itqan_Requirements.md), [reviewed scenarios](docs/updated-diagrams/scenarios/USE_CASE_SCENARIOS.md), [architecture](docs/updated-diagrams/architecture/ARCHITECTURE.md), [approved ERD](docs/updated-diagrams/erd/itqan-erd.mmd), and [relational schema](itqan-relational-schema.md). The older `docs/diagrams/class/` files describe superseded roles and features and were not reused.

## Read the four views

| View | Editable source | SVG | What it explains |
|---|---|---|---|
| 1. Accounts and Quran content | [Mermaid](itqan-class-01-account-content.mmd) | [SVG](itqan-class-01-account-content.svg) | One fixed account type; conditional Teacher detail; dated consent; read-only Juz Amma reference classes; anonymous deletion log. |
| 2. Recitation flow | [Mermaid](itqan-class-02-recitation-flow.mmd) | [SVG](itqan-class-02-recitation-flow.svg) | App capture/feedback; Recitation Service with its Comparison Engine; transient Analysis Service. |
| 3. Session data and progress | [Mermaid](itqan-class-03-session-progress.mmd) | [SVG](itqan-class-03-session-progress.svg) | Ended sessions, word-linked mistakes, optional Tajweed rules and derived progress. |
| 4. Classes and messaging | [Mermaid](itqan-class-04-class-messaging.mmd) | [SVG](itqan-class-04-class-messaging.svg) | Teacher-owned classes, Reader enrolments, access checks, one-way messages, recipient read dates. |

The diagrams are **four views of one model**, not four systems. A `«reference: view N»` box repeats a class name so a cross-view dependency or association is readable; its complete definition appears in view N. Solid lines are UML associations with multiplicities, dashed arrows are service dependencies, and the filled diamond means the Comparison Engine is contained in the Recitation Service. No inheritance is shown: an Account has exactly one immutable type, and only Teachers have `TeacherDetail` (FR-01, BR-15). The `Account`–`TeacherDetail` `0..1` multiplicity applies across all Accounts; it is exactly one for Teachers and zero for Readers. `?` marks a nullable attribute. Names use UML camel case while the [schema](itqan-relational-schema.md) uses PostgreSQL snake case.

## Responsibilities and boundaries

- `AccountService` manages account/profile data, both consent purposes, the stored-data summary and deletion. It works with the managed `IdentityProvider` for registration and account removal. The app signs in and out through the provider; no password is an Itqan attribute (FR-01–FR-03, FR-27–FR-29).
- `ItqanApp` displays bundled Juz Amma text offline, captures verse audio, shows feedback while recitation continues, detects pauses and shows the next-word hint, and plays **bundled reference audio only on request**. Its audio and hint behavior is transient. Inactivity logout is suppressed during an active session; explicit logout interrupts it (FR-04–FR-06, FR-12, FR-16–FR-18, FR-26, FR-29).
- `RecitationService` receives **all session traffic**, checks Reader role and active recitation consent before starting, keeps Surah and mode fixed, calls the stateless `AnalysisService` per verse, uses its contained `ComparisonEngine` to locate errors against read-only text, and finalizes summary plus Mistakes on completed, early or interrupted endings. Failed verse analysis yields no Mistake or counted words (FR-07–FR-20, BR-01–BR-02, BR-05, BR-07, BR-18).
- `ProgressService` reads ended sessions for history/results, best score per Surah, full mastery, average mastery and practice streak. It is notified after each session end; it creates **no progress table** (FR-20–FR-22, BR-03–BR-04, BR-06).
- `ClassService` owns create/rename, code-based join and leave, dashboard authorization, message delivery and read status. `getVisibleSessions(teacherId, classId, readerId)` first checks that the Teacher owns the selected Class and the Reader is actively enrolled there, then uses the **earliest active join date across that Teacher's classes** and returns only sessions ended on or after it. Recheck on every drill-down read (FR-23–FR-25, BR-08–BR-13).

The operations are use-case responsibilities, not an API contract or a new storage model. A `verseAudio` argument and phonemes exist only in memory. In view 3, `RecitationSession` shows the fields of its **ended persisted form**; Started and Active are transient runtime states. `endSession` performs score calculation and atomic persistence through the shown responsibilities. A zero-word session has NULL score. Each Mistake points to exactly one expected Word in the session's Surah; an added-word error points to the following expected Word. Tajweed-only penalties are 0.5 for Ghunnah, Qalqalah or Madd; whole-word penalties are 1; a Word contributes at most 1 effective error (BR-01, FR-14–FR-15).

For view 4, one active Enrolment per Reader/Class is allowed; a rejoin creates a new row with a new join date. Teacher-sharing consent is required to join and withdrawal ends all active enrolments. Class names may repeat; the unique join code never changes, and a class is erased only with its Teacher. A whole-class message snapshots currently active recipients, refuses an empty class, and records one `MessageRecipient` per Reader. A single-reader send requires that Reader's active enrolment. Read dates serve both inbox and sent views; Readers cannot reply and retain delivered messages after leaving a class. Reader and Teacher deletion follow FR-28; `DeletionLog` has **no association** to `Account` (FR-24–FR-28, BR-09–BR-13, BR-16–BR-17).

Surah, Verse, Word and TajweedRule are read-only database reference classes; Quran text is also bundled in the app. Reference audio is app-bundled only. The Database is an architecture component, not a domain class; the managed Identity Provider and stateless Analysis Service are explicitly marked external. There are no audio-segment, phoneme, feedback-text, prompt-event, assignment, challenge, reward or performance-snapshot persistence classes (§8.3).

## ERD entity mapping (§8.1–8.2)

| ERD entity | UML class and view | Relationship checked |
|---|---|---|
| ACCOUNT | `Account`, 1 (referenced in 3–4) | Teacher detail, Reader consents/sessions/enrolments/recipients, Teacher classes/messages. |
| TEACHER_DETAIL | `TeacherDetail`, 1 | Conditional 1–1 with Teacher Account. |
| CONSENT_RECORD | `ConsentRecord`, 1 (referenced in 4) | Reader 1–0..*. |
| SURAH | `Surah`, 1 (referenced in 3) | Verse 1–1..*; session 1–0..*. |
| VERSE | `Verse`, 1 | Word 1–1..*. |
| WORD | `Word`, 1 (referenced in 2–3) | Mistake 1–0..*. |
| TAJWEED_RULE | `TajweedRule`, 3 | Optional rule per Tajweed Mistake. |
| RECITATION_SESSION | `RecitationSession`, 3 (referenced in 2) | Reader 1–0..*; Mistake 1–0..*. |
| MISTAKE | `Mistake`, 3 | Session, Word and optional Rule. |
| QURAN_CLASS | `QuranClass`, 4 | Teacher 1–0..*; enrolments and messages 0..*. |
| ENROLMENT | `Enrolment`, 4 | Class and Reader, each 1–0..*. |
| MESSAGE | `Message`, 4 | Teacher and Class, each 1–0..*; recipient 1–1..*. |
| MESSAGE_RECIPIENT | `MessageRecipient`, 4 | Message 1–1..*; Reader 1–0..*. |
| DELETION_LOG | `DeletionLog`, 1 | Deliberately no Account link. |

**Every §8.1 ERD entity has a corresponding class.** There is no omitted entity to justify. Composite FK and deletion details remain in the schema; an association line alone does not enforce them.

## Functional-requirement coverage

| Requirement | Class-diagram responsibility |
|---|---|
| FR-01 Create Account | `AccountService.registerAccount`, `Account`, `TeacherDetail`, `IdentityProvider`. |
| FR-02 Login | `IdentityProvider.authenticate`, immutable `Account.accountType`; App routes by type. |
| FR-03 Manage Profile | `AccountService.updateProfile`; email stays provider-managed. |
| FR-04 Browse Juz Amma | `ItqanApp.browseAndReadSurah`, `Surah`. |
| FR-05 Select Surah | `RecitationService.startSession`, `Surah`. |
| FR-06 Display Verses | `ItqanApp.browseAndReadSurah`, `Verse`. |
| FR-07 Select AI Mode | App selection passed to `startSession`; only Mujawwid/Mushajji stored. |
| FR-08 Al-Mujawwid | `RecitationService` and `ComparisonEngine`; direct feedback shown by App. |
| FR-09 Al-Mushajji | Same analysis/scoring; App words feedback encouragingly. |
| FR-10 Al-Mu'allim | Teacher `Account.accountType` enables `ClassService`; no selected Teacher mode. |
| FR-11 Start Session | `RecitationService.startSession` checks consent; App checks microphone permission. |
| FR-12 Capture Audio | `ItqanApp.captureVerseAudio`; transient `analyseVerse` argument. |
| FR-13 Analyze Recitation | `RecitationService.analyseVerse` → `AnalysisService`; failed verse excluded. |
| FR-14 Detect Errors | `ComparisonEngine`, `Mistake`, `TajweedRule`. |
| FR-15 Locate Error | `Mistake` → exact `Word`, including added-word position rule. |
| FR-16 Provide Feedback | `ItqanApp.showVerseFeedback` while recitation continues. |
| FR-17 Audio Assistance | `ItqanApp.playBundledWordAudio` on highlighted/prompted tap. |
| FR-18 Continue Recitation | App and Recitation Service continue per verse without restart. |
| FR-19 End Session | `RecitationService.endSession` for all three reasons. |
| FR-20 Results/History | `RecitationSession`, `Mistake`, `ProgressService.getSessionResults/getSessionHistory`. |
| FR-21 Progress | `ProgressService.getBestScores/getFullMasteryCount/getAverageMastery`. |
| FR-22 Streak | `ProgressService.getPracticeStreak` from ended scored sessions. |
| FR-23 Teacher Dashboard | `ClassService.getClassDashboard/getVisibleSessions`; BR-08 filter. |
| FR-24 Manage Class | `QuranClass`, `Enrolment`, create/rename/join/leave operations. |
| FR-25 Student Messages | `Message`, `MessageRecipient`, inbox/sent/unread/send/open operations. |
| FR-26 Smart Prompting | `ItqanApp.showNextWordHint` after transient pause detection. |
| FR-27 Consent/Privacy | `ConsentRecord`, Account Service grant/withdraw/summary. |
| FR-28 Delete Account | `AccountService.deleteAccount`, anonymous `DeletionLog`; cascade behavior in schema. |
| FR-29 Logout | `IdentityProvider.logout`; `endSession` with interrupted reason if active. |

## Review status and limits

- The four SVGs were rendered from the Mermaid sources and inspected for legibility. Each is intended as its own report figure; do not shrink all four onto one page.
- The approved ERD and Task 7 schema agree on all 14 persistent classes and relationships. Service operations follow the reviewed scenarios and architecture. Task 5 sequence diagrams are still Open, so their eventual message names should be checked against these operations when Task 5 is made.
- The device-local practice-day ambiguity already flagged in the schema remains: §8.1 stores no historical device time zone. No extra field or product decision is introduced here.
- The class diagram does not claim measured AI accuracy, latency, audio source, join-code format or identity-provider vendor; requirements §11 leaves them to IS499.
