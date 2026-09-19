# ERD–Requirements Traceability

This matrix connects the functional requirements in `docs/project/REQUIREMENTS.md` to the data model. An entity stores evidence or state needed by a requirement; it does not by itself implement application behavior.

## Functional requirements to entities

| Requirement | Requirement name | Supporting entities | Stored evidence | Notes/status |
|---|---|---|---|---|
| FR-01 | Create Account | `USER`, `ROLE`, `USER_ROLE`, `LEARNER_PROFILE`, `TEACHER_PROFILE` | Account identity, credentials, role, and profile | Registration validation and password hashing are application behavior. |
| FR-02 | User Login | `USER` | Credential hash, account status, and last-login timestamp | Authentication execution is application behavior. |
| FR-03 | Manage User Profile | `USER`, `LEARNER_PROFILE`, `TEACHER_PROFILE` | Shared and role-specific profile values | Profile authorization is application behavior. |
| FR-04 | Browse Juz Amma | `JUZ`, `SURAH` | Juz and ordered Surah catalog | UI browsing is application behavior. |
| FR-05 | Select Surah | `SURAH`, `RECITATION_SESSION` | Selected Surah for each session | Selection interaction is application behavior. |
| FR-06 | Display Surah Verses | `SURAH`, `VERSE`, `VERSE_WORD` | Verified verse and word content | Rendering and fonts are UI behavior. |
| FR-07 | Select AI Mode | `AI_MODE`, `RECITATION_SESSION` | Selected mode for each session | Mode-selection interaction is application behavior. |
| FR-08 | Al-Mujawwid Mode | `AI_MODE`, `RECITATION_ANALYSIS`, `RECITATION_ERROR`, `ERROR_TYPE`, `TAJWEED_RULE`, `ERROR_FEEDBACK` | Analysis, detected errors, Tajweed classification, and feedback | AI inference is application/service behavior. |
| FR-09 | Al-Mushajji Mode | `AI_MODE`, `CHALLENGE`, `LEARNER_CHALLENGE`, `REWARD`, `LEARNER_REWARD` | Mode selection and proposed motivation state | Gamification entities are proposed because mechanics remain unresolved. |
| FR-10 | Al-Mu'allim Mode | `AI_MODE`, `LEARNING_CLASS`, `CLASS_ENROLLMENT`, `LEARNER_SURAH_PROGRESS`, `TEACHER_MESSAGE` | Teacher context, learners, progress, and communication | Dashboard behavior is detailed in FR-23–FR-25. |
| FR-11 | Start Recitation Session | `RECITATION_SESSION` | Start time, selected Surah/mode, and active status | Microphone activation is device behavior. |
| FR-12 | Capture Recitation Audio | `AUDIO_RECORDING`, `RECITATION_SESSION` | Consent, format, duration, storage URI, and retention metadata | Audio bytes remain outside the relational database. |
| FR-13 | Analyze Recitation | `RECITATION_SEGMENT`, `RECITATION_ANALYSIS` | Segment boundaries, recognized text, model traceability, status, and confidence | Analysis execution is AI-service behavior. |
| FR-14 | Detect Recitation Errors | `RECITATION_ANALYSIS`, `RECITATION_ERROR`, `ERROR_TYPE`, `TAJWEED_RULE` | Detected error, category, rule, confidence, and review state | Detection algorithms remain outside the schema. |
| FR-15 | Identify Error Location | `VERSE`, `VERSE_WORD`, `RECITATION_SEGMENT`, `RECITATION_ERROR` | Verse, word, and audio-offset location | Supports exact Quran and recording positions. |
| FR-16 | Provide Recitation Feedback | `RECITATION_ERROR`, `ERROR_FEEDBACK` | Localized explanation and correction text | Feedback presentation is application behavior. |
| FR-17 | Provide Audio Assistance | `AUDIO_ASSISTANCE`, `RECITATION_ERROR`, `PAUSE_EVENT`, `VERSE` | Assistance source, type, URI, and playback time | Audio generation/playback is service and device behavior. |
| FR-18 | Continue Recitation | `RECITATION_SESSION`, `RECITATION_SEGMENT`, `PAUSE_EVENT` | Ordered segments and prompt/pause history | Resume control is application behavior. |
| FR-19 | End Recitation Session | `RECITATION_SESSION` | End time, final status, duration, completion, and counts | Session finalization is application behavior. |
| FR-20 | Display Session Results | `RECITATION_SESSION`, `RECITATION_ERROR`, `VERSE_WORD`, `MASTERY_SCORE_HISTORY` | Mastery result and words containing errors | Result rendering is UI behavior. |
| FR-21 | Track User Progress | `LEARNER_SURAH_PROGRESS`, `MASTERY_SCORE_HISTORY`, `RECITATION_SESSION`, `SURAH` | Attempts, mastered Surahs, latest/best/average mastery, and history | Summary updates are application/database-service behavior. |
| FR-22 | Track Practice Streaks | `DAILY_PRACTICE`, `PRACTICE_STREAK` | Daily practice evidence and current/longest streak | Requirement priority is Could Have. |
| FR-23 | Teacher Dashboard | `LEARNING_CLASS`, `CLASS_ENROLLMENT`, `LEARNER_SURAH_PROGRESS`, `MASTERY_SCORE_HISTORY`, `DAILY_PRACTICE`, `PRACTICE_STREAK`, `STUDENT_PERFORMANCE_SNAPSHOT` | Class membership, completion, mastery, activity, and streak information | Snapshot table is proposed and may be replaced by live queries. |
| FR-24 | Manage Class | `LEARNING_CLASS`, `CLASS_ENROLLMENT`, `CLASS_ASSIGNMENT`, `ASSIGNMENT_PROGRESS` | Class details, membership, and proposed assignment state | Assignment tables are proposed; class and enrollment are confirmed. |
| FR-25 | Send Student Messages | `TEACHER_MESSAGE`, `LEARNING_CLASS`, `CLASS_ENROLLMENT`, `RECITATION_SESSION` | Message, sender, recipient, class/session context, and read time | Sending and notifications are application behavior; enrollment controls access. |

## Entity-to-requirement reverse index

| Entity | Related requirements | Status and purpose |
|---|---|---|
| `USER` | FR-01, FR-02, FR-03 | Confirmed account identity and authentication state. |
| `ROLE` | FR-01 | Confirmed learner/teacher role catalog. |
| `USER_ROLE` | FR-01 | Confirmed many-to-many user-role assignment. |
| `LEARNER_PROFILE` | FR-01, FR-03, FR-11, FR-21, FR-22 | Confirmed learner extension and parent for learning records. |
| `TEACHER_PROFILE` | FR-01, FR-03, FR-23, FR-24, FR-25 | Confirmed teacher extension and ownership. |
| `JUZ` | FR-04 | Confirmed Quran navigation reference. |
| `SURAH` | FR-04, FR-05, FR-06, FR-11, FR-21, FR-24 | Confirmed Surah catalog and session target. |
| `VERSE` | FR-06, FR-13, FR-15, FR-17 | Confirmed verse content and analysis location. |
| `VERSE_WORD` | FR-06, FR-15, FR-20 | Supporting exact word-level location. |
| `TAJWEED_RULE` | FR-08, FR-14 | Supporting reference catalog; supported subset unresolved. |
| `AI_MODE` | FR-07, FR-08, FR-09, FR-10, FR-11 | Confirmed three-mode catalog and session selection. |
| `RECITATION_SESSION` | FR-05, FR-07, FR-11, FR-12, FR-18, FR-19, FR-20, FR-21 | Confirmed attempt lifecycle and summary results. |
| `AUDIO_RECORDING` | FR-12 | Confirmed audio metadata, consent, and retention record. |
| `RECITATION_SEGMENT` | FR-13, FR-15, FR-18 | Supporting ordered verse/audio processing unit. |
| `RECITATION_ANALYSIS` | FR-08, FR-13, FR-14 | Confirmed analysis result and evaluation traceability. |
| `PAUSE_EVENT` | FR-17, FR-18 | Confirmed smart-prompting and pause evidence. |
| `ERROR_TYPE` | FR-08, FR-14 | Supporting error classification catalog. |
| `RECITATION_ERROR` | FR-08, FR-14, FR-15, FR-16, FR-17, FR-20 | Confirmed detected-error record. |
| `ERROR_FEEDBACK` | FR-08, FR-16 | Confirmed localized feedback content. |
| `AUDIO_ASSISTANCE` | FR-17 | Confirmed assistance reference and playback evidence. |
| `LEARNER_SURAH_PROGRESS` | FR-10, FR-21, FR-23 | Confirmed current per-Surah progress summary. |
| `MASTERY_SCORE_HISTORY` | FR-20, FR-21, FR-23 | Confirmed session-level mastery history; formula unresolved. |
| `DAILY_PRACTICE` | FR-22, FR-23 | Supporting daily activity evidence. |
| `PRACTICE_STREAK` | FR-22, FR-23 | Confirmed current and longest streak summary. |
| `LEARNING_CLASS` | FR-10, FR-23, FR-24, FR-25 | Confirmed teacher-owned class. |
| `CLASS_ENROLLMENT` | FR-10, FR-23, FR-24, FR-25 | Confirmed teacher–learner access relationship. |
| `CLASS_ASSIGNMENT` | FR-24 | Proposed class assignment detail. |
| `ASSIGNMENT_PROGRESS` | FR-24 | Proposed learner assignment state. |
| `TEACHER_MESSAGE` | FR-10, FR-25 | Confirmed teacher-to-learner message record. |
| `STUDENT_PERFORMANCE_SNAPSHOT` | FR-23 | Proposed dashboard reporting cache. |
| `CHALLENGE` | FR-09 | Proposed Al-Mushajji challenge definition. |
| `LEARNER_CHALLENGE` | FR-09 | Proposed learner challenge progress. |
| `REWARD` | FR-09 | Proposed Al-Mushajji reward definition. |
| `LEARNER_REWARD` | FR-09 | Proposed awarded-reward record. |

## Coverage result

- FR-01 through FR-25 are represented.
- All 34 ERD entities map to at least one requirement.
- Behavior-only responsibilities are explicitly distinguished from stored data.
- Proposed entities are not presented as confirmed project requirements.
- No Admin actor, Admin table, or full-Quran expansion is introduced.
