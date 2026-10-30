# Itqan Task 5 — Sequence diagram coverage and review

**Sources of truth:** [final requirements](../../../Itqan_Requirements.md), [reviewed Task 1 scenarios](../scenarios/USE_CASE_SCENARIOS.md), [Task 4 architecture](../architecture/ARCHITECTURE.md), [approved ERD](../erd/itqan-erd.mmd), [Task 7 schema](../../../itqan-relational-schema.md), and [Task 8 class diagram](../class/itqan-class-diagram.mmd). Older `docs/diagrams/sequence/` drawings are historical and were not copied. These eight diagrams cover separate interactions.

## Diagrams

| View | Editable source | SVG | Coverage |
|---|---|---|---|
| SEQ-01 Account | [Mermaid](seq-01-account.mmd) | [SVG](seq-01-account.svg) | Register, login, logout, profile. |
| SEQ-02 Consent | [Mermaid](seq-02-consent.mmd) | [SVG](seq-02-consent.svg) | Stored-data summary, grant, withdrawal, correction/deletion handoff. |
| SEQ-03 Recitation | [Mermaid](seq-03-recitation.mmd) | [SVG](seq-03-recitation.svg) | Offline browsing, mode selection, consent/permission, per-verse analysis, feedback, hints/audio, all endings, failures and scoring. |
| SEQ-04 Results and progress | [Mermaid](seq-04-results-progress.mmd) | [SVG](seq-04-results-progress.svg) | Results, history, mastery and streak. |
| SEQ-05 Classes and enrolment | [Mermaid](seq-05-class-enrolment.mmd) | [SVG](seq-05-class-enrolment.svg) | Class creation/rename, code-based join, consent, leave and rejoin rules. |
| SEQ-06 Teacher dashboard | [Mermaid](seq-06-teacher-dashboard.mmd) | [SVG](seq-06-teacher-dashboard.svg) | Class → Reader → Session with access rechecks and join-date filter. |
| SEQ-07 Messaging | [Mermaid](seq-07-messaging.mmd) | [SVG](seq-07-messaging.svg) | Single/whole-class sends, recipient snapshot, inbox and read status. |
| SEQ-08 Deletion | [Mermaid](seq-08-deletion.mmd) | [SVG](seq-08-deletion.svg) | Reader and Teacher deletion, anonymous audit, provider removal and logout. |

## Use-case coverage

Every one of the 22 reviewed Task 1 scenarios appears below. A scenario named inside another sequence uses that view rather than creating a redundant file.

| Use case | View | Scope in that view |
|---|---|---|
| UC-01 Register | SEQ-01 | Both account types, required Teacher detail, identity-provider failures. |
| UC-02 Login | SEQ-01 | Provider, role routing, wrong-role denial. |
| UC-03 Logout | SEQ-01, SEQ-03 | Ordinary/inactivity logout and interruption during recitation. |
| UC-04 Manage Profile | SEQ-01 | Editable profile and language, provider-managed email. |
| UC-05 Manage Consent and Privacy | SEQ-02 | Summary, both purposes, withdrawal effects. |
| UC-06 Delete Account | SEQ-08 | Cancel, Reader and Teacher erasure paths. |
| UC-07 Browse and Read Surah | SEQ-03 | Bundled offline Juz Amma before any session. |
| UC-08 Select Surah | SEQ-03 | Selected before mode and fixed for session. |
| UC-09 Select AI Mode | SEQ-03 | Mujawwid or Mushajji before session. |
| UC-10 Recite Surah | SEQ-03 | Main loop, analysis, endings, failures, scoring and persistence. |
| UC-11 Receive Audio Assistance | SEQ-03 | Tap only on highlighted or prompted Word; bundled audio. |
| UC-12 View Session Results | SEQ-03, SEQ-04 | End-of-session handoff and detailed results. |
| UC-13 View Session History | SEQ-04 | Newest first, empty state and reopen results. |
| UC-14 View User Progress | SEQ-04 | Full mastery, average and best score per Surah. |
| UC-15 View Practice Streak | SEQ-04 | Device-local scored practice days. |
| UC-16 View Teacher Messages | SEQ-07 | Inbox, unread count, read date and no reply. |
| UC-17 Manage Class | SEQ-05 | Create/rename, code immutability and ownership. |
| UC-18 View Teacher Dashboard | SEQ-06 | Three drill-down levels and repeated access checks. |
| UC-19 Send Student Messages | SEQ-07 | Single/whole-class audience and refusal cases. |
| UC-26 Join Class via Code | SEQ-05 | Invalid/already joined/consent decline/rejoin. |
| UC-27 Leave Class | SEQ-05 | Confirmation, end date and loss of Teacher access. |
| UC-28 Receive Smart Prompting | SEQ-03 | Automatic next-Word hint, optional requested audio. |

## Functional and business-rule trace

| ID | Diagram(s) | Required behavior represented |
|---|---|---|
| FR-01 | SEQ-01 | Reader or Teacher registration; school name and no Itqan password. |
| FR-02 | SEQ-01 | Identity-provider login and account-type routing. |
| FR-03 | SEQ-01, SEQ-07 | Profile changes and Teacher display name on messages. |
| FR-04 | SEQ-03 | 37 bundled Juz Amma Surahs browsed offline. |
| FR-05 | SEQ-03 | Surah selected before session. |
| FR-06 | SEQ-03 | Bundled Uthmani verses displayed. |
| FR-07 | SEQ-03 | Reader chooses Mujawwid or Mushajji. |
| FR-08 | SEQ-03 | Direct Mujawwid correction. |
| FR-09 | SEQ-03 | Same analysis and score, encouraging Mushajji wording. |
| FR-10 | SEQ-01, SEQ-05–SEQ-07 | Teacher account has Al-Mu'allim functions without selection. |
| FR-11 | SEQ-03 | Consent and microphone permission before start. |
| FR-12 | SEQ-03 | Verse audio in memory only. |
| FR-13 | SEQ-03 | Automatic verse-end detection, one-verse analysis and failure case. |
| FR-14 | SEQ-03 | Word and three Tajweed-rule error detection. |
| FR-15 | SEQ-03 | Errors linked to expected Word reference. |
| FR-16 | SEQ-03 | Mode-specific feedback while Reader continues. |
| FR-17 | SEQ-03 | Bundled Word audio only on highlighted/prompted tap. |
| FR-18 | SEQ-03 | Per-verse continuation after feedback, hint or audio. |
| FR-19 | SEQ-03 | Completed, early and interrupted endings, including zero words. |
| FR-20 | SEQ-03, SEQ-04 | Stored results and reopened history. |
| FR-21 | SEQ-04 | Full mastery, average and best Surah scores. |
| FR-22 | SEQ-04 | Consecutive device-local practice days. |
| FR-23 | SEQ-06 | Teacher dashboard with active-enrolment and date filter. |
| FR-24 | SEQ-05 | Class lifecycle, join and leave. |
| FR-25 | SEQ-07 | One-way sends, inbox and per-recipient read status. |
| FR-26 | SEQ-03 | Automatic transient Smart Prompting. |
| FR-27 | SEQ-02, SEQ-03, SEQ-05 | Dated consent, privacy summary and withdrawal effects. |
| FR-28 | SEQ-02, SEQ-08 | Permanent deletion and anonymous log. |
| FR-29 | SEQ-01, SEQ-03, SEQ-08 | Logout, inactivity exception and active-session interruption. |

| ID | Diagram(s) | Required rule represented |
|---|---|---|
| BR-01 | SEQ-03, SEQ-04 | Score formula, 0.5/1 penalty, per-Word cap and one-decimal result. |
| BR-02 | SEQ-03, SEQ-04 | Count only reached/analysed Words; zero Word yields no score. |
| BR-03 | SEQ-04, SEQ-06 | Whole Surah and at least 90 percent for full mastery. |
| BR-04 | SEQ-04, SEQ-06 | Average of best score per practised Surah. |
| BR-05 | SEQ-03, SEQ-04 | Only ended summary and Mistakes kept. |
| BR-06 | SEQ-04 | Ended scored Sessions in device-local calendar. |
| BR-07 | SEQ-03 | Surah → mode → start, both fixed. |
| BR-08 | SEQ-05, SEQ-06 | Active access and earliest active join date across Teacher's Classes. |
| BR-09 | SEQ-02, SEQ-05 | Code/consent join, one active enrolment, leave/rejoin. |
| BR-10 | SEQ-05 | Unique immutable join code. |
| BR-11 | SEQ-05, SEQ-08 | No single-Class deletion, erase with Teacher. |
| BR-12 | SEQ-07 | One-way recipient snapshot, empty-Class refusal, retention after leave. |
| BR-13 | SEQ-07 | Unread until open, shared read date. |
| BR-14 | SEQ-03 | Requested audio and automatic hint, neither stored. |
| BR-15 | SEQ-01 | One fixed account type and Teacher Al-Mu'allim. |
| BR-16 | SEQ-02, SEQ-05 | Two dated consent purposes and regrant history. |
| BR-17 | SEQ-08 | Permanent deletion with anonymous log. |
| BR-18 | SEQ-03 | Unreliable verse produces no Mistake or counted Words. |

The processing path supports NFR-03, the access checks support NFR-06, and the storage boundary supports NFR-07. The diagrams account for the modular §10 parts and for persisted results after interruption (NFR-05). Accuracy (NFR-01), measured latency (NFR-02), usability (NFR-04), scalability (NFR-08), maintainability (NFR-09), device compatibility (NFR-10) and language quality (NFR-11) still require implementation and testing. A sequence diagram does not prove measured targets.

## Consistency and limits

- All recitation traffic goes through Recitation Service. Its Comparison Engine reads expected Verse/Word and rule references. Analysis Service is stateless. The app alone uses bundled reference Word audio. No arrow carries audio, phonemes, feedback or prompts into Database; only ended Session summaries and Mistakes are written.
- The Recitation Service finalizes an interrupted session on analysed Words, including connection loss or app closure. The scenarios allow finalization when the app next opens if needed. They do not specify the durable handoff mechanism that guarantees NFR-05 if both app and backend disappear; none was invented in these diagrams.
- The requirements require immediate deletion in both Database and Identity Provider but do not define a compensation procedure if the provider fails after database deletion. SEQ-08 shows the required successful path and cancellation, without inventing a recovery rule.
- The [schema](../../../itqan-relational-schema.md) records the existing device-local practice-day ambiguity: historical time zones are not stored. SEQ-04 uses the device-local calendar stated in BR-06 and does not add a field.
- Task 1 and Task 4 are in Review on the task board. These diagrams follow their current reviewed contents; message names can be reconciled if those artifacts change.

**Task status:** Review, awaiting Abdulaziz Alfarhood's review. No requirement or product decision was silently dropped.
