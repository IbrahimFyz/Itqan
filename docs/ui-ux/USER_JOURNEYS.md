# Itqan User Journeys

## Status and Scope

* **Phase:** IS498 / Phase One analysis and design; this document does not claim an implemented application.
* **Owner:** Abdulaziz.
* **Status key:** 🟢 Confirmed means explicitly stated in a reviewed current artifact; 🟡 Proposed means a design detail awaiting approval; 🔴 Unresolved means a decision has not been made.
* **Sources reviewed:** `PROJECT\\\\\\\_CONTEXT.md`, `REQUIREMENTS.md`, `OPEN\\\\\\\_QUESTIONS.md`, `DECISION\\\\\\\_LOG.md`, `phase-one-project-plan.md`, the use-case, user-flow, activity, and recitation-sequence diagrams, `system-architecture.pdf`, `CLASS\\\\\\\_DIAGRAM\\\\\\\_NOTES.md`, and the current ERD traceability.
* **Privacy constraint (🟢):** learner recitation audio is held only in memory while it is analysed, then discarded. It is never written to a database, object storage, files, or backups, and is never exposed to teachers. Stored recitation results are not recordings.

## Journey Map

|Journey|Primary actor|Goal|Trigger|Successful outcome|Requirement / use-case links|
|-|-|-|-|-|-|
|Learner recitation and feedback|Learner|Practise a Juz Amma Surah and receive recitation feedback|The learner chooses to practise|Feedback and a session result are shown; permitted result/progress data may be retained|FR-01 to FR-09, FR-11 to FR-21; Browse Juz Amma, Select Surah, Select AI Mode, Start/Continue/End Recitation Session, Capture/Analyse Audio, Detect/Locate Errors, Provide Feedback, View Session Results, View User Progress|
|Teacher class monitoring|Teacher|Review authorised learner practice and progress|The teacher opens teacher features|The teacher sees only authorised stored learning results for an owned class and actively enrolled learner|FR-10, FR-23, FR-24; Teacher Dashboard, Student Recitation Activity, Student Completion, Student Score, Manage Class|

## Journey 1: Learner Recitation and Feedback

|Step|Learner action|System response|Information / state involved|Exception or decision point|Traceability|Status|
|-:|-|-|-|-|-|-|
|1|Registers or signs in when account access is needed.|Presents registration or login; the learner reaches the practice entry point.|Account and learner role context. The final authentication mechanism is not settled.|A learner may be new or returning.|FR-01, FR-02; use-case diagram; learner user-flow.|🟢 Access requirements; 🔴 final authentication behaviour (OQ-14).|
|2|Opens Juz Amma and selects a Surah.|Displays the available Surahs and the selected Surah's verses.|Juz Amma only (37 Surahs); selected `Surah` and `Verse` content.|None specified.|FR-04 to FR-06; learner user-flow; learner activity; sequence; `QuranCatalogService`, `Surah`, `Verse`, `VerseWord`.|🟢|
|3|Selects Al-Mujawwid or Al-Mushajji, then starts a session.|Configures an active session with the selected Surah and mode.|`RecitationSession`; selected `AIMode`.|Detailed mode behaviour is not defined here.|FR-07 to FR-11; learner user-flow and activity; sequence; `RecitationService`.|🟢 Session selection; 🔴 detailed AI-mode behaviour.|
|4|Grants microphone access and recites the displayed verse(s).|Captures recitation audio for analysis.|Audio exists transiently in memory only; per-verse processing is the architecture direction.|If microphone access is unavailable, the existing user flow presents permission guidance; its exact recovery UX is not specified.|FR-12; learner user-flow and activity; sequence; `AudioCapturePort`; architecture §§2, 4.|🟢 Audio capture and transient policy; 🟡 exact permission/recovery UX.|
|5|Continues reciting while the system processes the active segment.|Sends the audio and verse identifier for analysis, compares the result to the expected verse, and maps relevant issues to word locations. It discards the raw audio after analysis.|Transient audio; analysis result; phoneme/articulation attributes; `RecitationSegment`, `RecitationAnalysis`, `RecitationError`, and word location.|If analysis is unavailable or fails, the architecture keeps reading/review available but does not prescribe a retry screen or message.|FR-13 to FR-15; learner activity; sequence; architecture §§3-4; `AnalysisService`, `AIAnalysisPort`.|🟢 Analysis and discard; 🔴 final real-time/failure interaction (OQ-10, OQ-11).|
|6|Reviews feedback and, when offered, listens to corrective help.|Highlights the affected word(s), presents feedback, and may play bundled reference audio when appropriate.|Error type, word index, feedback; optional `AudioAssistance`.|Error detected? Audio assistance appropriate? Smart Prompting is an approved functional requirement (FR-26) with Should Have priority.|FR-16, FR-17; learner user-flow and activity; sequence; `FeedbackService`, `ErrorFeedback`, `AudioAssistance`.|🟢 Feedback and optional audio assistance; 🔴 Smart Prompting (FR-26) is confirmed; detailed trigger wording remains to be defined.|
|7|Continues reciting or ends the session.|Continues the active session or closes it and calculates/displays the mastery result and detected words.|Session lifecycle; result and score out of 100.|Continue/end is a learner decision. The score follows FR-20 when `total\\\\\\\_words > 0`.|FR-18 to FR-20; learner user-flow and activity; sequence; `RecitationSession`, `MasteryScoreHistory`.|🟢 Control, result display, and defined formula.|
|8|Reviews progress after the session.|Stores only permitted result data (for example, Surah/verse-word error results, score, timestamp, and progress summaries) and updates progress where supported. Raw audio is already discarded and is not stored or shared.|`RecitationSession`, `RecitationError`, progress and mastery records; no raw-audio field or object is persisted.|Progress/streak behaviour and the final schema remain subject to approval.|FR-21, FR-22; learner activity; sequence; architecture §§4.1, 4.4; ERD traceability; class-diagram notes.|🟢 Result-only persistence and no teacher audio access; 🔴 final requirements/schema (OQ-01, OQ-15).|

## Journey 2: Teacher Class Monitoring

|Step|Teacher action|System response|Information / state involved|Exception or decision point|Traceability|Status|
|-:|-|-|-|-|-|-|
|1|Signs in and opens teacher features / Al-Mu'allim context.|Displays the teacher dashboard and available teacher action.|Teacher account/role context.|The final authentication flow and exact dashboard design are not defined.|FR-02, FR-10, FR-23; use-case diagram; teacher activity; `TeacherProfile`.|🟢 Teacher functions exist; 🔴 authentication (OQ-14) and dashboard detail (OQ-06).|
|2|Chooses class management or monitoring.|For class management, validates and persists class changes; for monitoring, presents classes/learners available to the teacher.|`LearningClass`, `ClassEnrollment`; teacher ownership.|Readers join a teacher class using the teacher-provided join code; there is no invitation-link/acceptance flow.|FR-24; teacher activity; `ClassService`, `LearningClass`, `ClassEnrollment`.|🟢 Class management and join-code enrollment boundary; no invitation workflow.|
|3|Selects a class and learner to monitor.|Verifies that the teacher owns the class and that the learner has active enrolment before reading data.|Class ownership, learner enrolment status and period.|If the relationship is absent or inactive, the request is refused.|FR-23; architecture §4.3 and §8.3; class-diagram notes; `TeacherMonitoringService`.|🟢|
|4|Reviews learner activity, completion, mastery, and progress.|Retrieves authorised stored results and prepares the monitoring view.|Session/progress summaries, mastery figures, error types and word locations; no audio.|The exact dashboard metrics and any empty-state presentation are not specified.|FR-23; teacher activity; use-case diagram; ERD traceability; `LearnerSurahProgress`, `MasteryScoreHistory`, `RecitationError`.|🟢 Authorised result scope; 🔴 dashboard/empty-state detail (OQ-06).|
|5|Reviews another authorised record or exits.|Returns to the available class/learner selection or ends the monitoring interaction.|Authorised stored learning data only.|Teachers cannot access raw recitation audio, contact details, or activity outside the enrolment period.|Teacher activity; architecture §§4.2-4.4, §8.3; class-diagram notes.|🟢|

## Alternate and Failure Paths

|Path|Evidence-supported behaviour|Status / source|
|-|-|-|
|Microphone unavailable or permission denied|Show permission guidance before recitation can proceed. The diagrams do not specify retry wording, settings navigation, or a fallback input method.|🟢 Guidance shown in learner user-flow; 🟡 recovery UX.|
|Analysis processing unavailable or failed|Analysis-dependent feedback cannot be produced. Reading and review remain available because Quran content is bundled and the analysis service is isolated. A final retry/error UI is not specified.|🟢 Architecture §§3.3, 4.5, 6.2; 🔴 exact failure/retry behaviour (OQ-11).|
|Teacher access denied|Refuse the read when the teacher does not own the class or the learner lacks active enrolment.|🟢 Architecture §4.3; class-diagram notes.|
|No available class, learner, or results|No evidence defines an empty-state screen or message. This journey does not invent one.|🔴 OQ-05, OQ-06.|
|Learner ends a session|End the active session and show a result where analysis/result data is available; raw audio is discarded, regardless of whether a result is persisted.|🟢 FR-19, FR-20; architecture §§4.1-4.4.|

## Cross-Artifact Consistency

|Journey|Use case / activity / sequence|Class and ERD concepts|Requirements and open questions|
|-|-|-|-|
|Learner recitation and feedback|Use cases: Browse Juz Amma through View Session Results; activity: `Itqan\\\\\\\_Activity\\\\\\\_01\\\\\\\_Learner\\\\\\\_Recitation\\\\\\\_Session.svg`; sequence: `Itqan\\\\\\\_Sequence\\\\\\\_01\\\\\\\_Recitation\\\\\\\_Session\\\\\\\_FINAL.svg`; user flow: `Itqan\\\\\\\_User\\\\\\\_Flow\\\\\\\_01\\\\\\\_Learner\\\\\\\_Recitation.svg`.|`RecitationService`, `AudioCapturePort`, `AnalysisService`, `FeedbackService`, `ProgressService`; `RecitationSession`, `RecitationSegment`, `RecitationAnalysis`, `RecitationError`, `ErrorFeedback`, `AudioAssistance`, progress records. The ERD/class design expressly forbids persisted learner audio.|FR-01 to FR-09, FR-11 to FR-22; OQ-01, OQ-07 to OQ-11, OQ-14, OQ-15.|
|Teacher class monitoring|Use cases: Teacher Dashboard, Student Recitation Activity/Completion/Score, Manage Class; activity: `Itqan\\\\\\\_Activity\\\\\\\_02\\\\\\\_Teacher\\\\\\\_Class\\\\\\\_and\\\\\\\_Monitoring.svg`. No teacher sequence diagram is present.|`ClassService`, `TeacherMonitoringService`; `LearningClass`, `ClassEnrollment`, `LearnerSurahProgress`, `MasteryScoreHistory`, `RecitationError`. Every teacher read is scoped by class ownership and active enrolment.|FR-10, FR-23, FR-24; OQ-01, OQ-05, OQ-06, OQ-14, OQ-15.|

## Open Questions and Assumptions

* **OQ-01 / OQ-03 / OQ-04:** Functional requirements, priority method, and traceability remain subject to approval; this journey traces the current draft rather than finalising it.
* **Enrollment:** The approved design uses a class join code. Teachers do not directly add readers and there is no invitation-link/acceptance flow.
* **OQ-06:** Teacher dashboard fields, filters, empty states, and presentation remain unresolved. This document includes only activity, completion, mastery/progress, error types, and word locations already evidenced.
* **OQ-07: Exact behaviours of Al-Mujawwid, Al-Mushajji, and Al-Mu'allim remain to be detailed. Smart Prompting is confirmed as FR-26.**
* **OQ-08:** The Mastery Score formula is defined in FR-20; evaluating its interpretation remains open.
* **OQ-09 to OQ-11:** The selected Muaalem model and real-time/near-real-time design are recorded in the current decision log and architecture; integrated evaluation remains an IS499 activity. The architecture's transient-processing policy remains mandatory regardless.
* **OQ-14:** Registration/login mechanism and role establishment are unresolved beyond FR-01 and FR-02.
* **OQ-15:** The database schema is pending approval. The current ERD/class artifacts are used for consistency only and must not be read as implementation completion.
* **Assumption (🟡):** The exact screens and wording are intentionally deferred to Abdulaziz's later wireframes/prototype work; they must preserve the confirmed states and boundaries above.

## Review Checklist

* \[x] Learner journey is traced to the existing requirements, use case, user-flow, activity, sequence, class, ERD, and architecture artifacts.
* \[x] Teacher journey enforces class ownership and active learner-enrolment boundaries on every read.
* \[x] No learner recitation audio storage, backup, file retention, object storage, or teacher exposure is introduced.
* \[x] Confirmed, proposed, and unresolved information are explicitly separated.
* \[x] Ibrahim review is needed for final FR approval, teacher-relationship requirements, traceability, and ERD status.
* \[x] Saud review is needed only to confirm that the journey preserves the current architecture's transient-audio, analysis-availability, and authorisation policies; this document does not alter architecture.

