# Itqan ERD Design Specification

**Date:** 2026-09-19  
**Phase:** IS498 — analysis and system design  
**Scope:** Standalone Itqan application covering Juz Amma, learner recitation, AI feedback, progress tracking, teacher classes, and the three approved AI modes.

## 1. Design goals

The ERD must:

1. Trace back to the functional and non-functional requirements in `docs/project/REQUIREMENTS.md`.
2. support both learner and teacher workflows without introducing an Admin role;
3. model all 37 Surahs and their verses without duplicating Quran text in session records;
4. preserve detailed recitation-analysis evidence at verse, word, and Tajweed-rule level;
5. support progress, mastery history, streaks, classes, assignments, and teacher communication;
6. separate confirmed scope from proposed details that still require team approval;
7. avoid embedding the AI model, deployment stack, or mastery formula into the database design.

## 2. Modeling approach

Use a normalized relational model suitable for PostgreSQL. Stable reference data, operational records, and derived progress records remain separate. UUIDs identify user-generated records; small integer identifiers are appropriate for fixed Quran and lookup data.

The diagram will use crow's-foot cardinality and show primary keys, foreign keys, required fields, unique constraints, and major status/type fields. The matching relational schema will explain constraints that cannot be expressed clearly in a visual ERD.

## 3. Domain groups

### 3.1 Identity and access

#### USER

Represents every authenticated learner or teacher.

| Attribute | Type | Constraint |
|---|---|---|
| user_id | UUID | PK |
| email | VARCHAR(254) | required, unique |
| password_hash | TEXT | required |
| display_name | VARCHAR(100) | required |
| preferred_language | VARCHAR(5) | required; `ar` or `en` |
| account_status | VARCHAR(20) | required; active, suspended, or deleted |
| created_at | TIMESTAMPTZ | required |
| updated_at | TIMESTAMPTZ | required |
| last_login_at | TIMESTAMPTZ | nullable |

#### ROLE

Fixed role lookup. Initial rows are `learner` and `teacher`; there is no Admin role.

| Attribute | Type | Constraint |
|---|---|---|
| role_id | SMALLINT | PK |
| role_code | VARCHAR(30) | required, unique |
| role_name_ar | VARCHAR(50) | required |
| role_name_en | VARCHAR(50) | required |

#### USER_ROLE

Allows one account to be both a learner and a teacher.

| Attribute | Type | Constraint |
|---|---|---|
| user_id | UUID | PK, FK → USER.user_id |
| role_id | SMALLINT | PK, FK → ROLE.role_id |
| assigned_at | TIMESTAMPTZ | required |

#### LEARNER_PROFILE

| Attribute | Type | Constraint |
|---|---|---|
| learner_id | UUID | PK, FK → USER.user_id |
| learning_goal | TEXT | nullable |
| experience_level | VARCHAR(20) | nullable |
| reminders_enabled | BOOLEAN | required, default false |

#### TEACHER_PROFILE

| Attribute | Type | Constraint |
|---|---|---|
| teacher_id | UUID | PK, FK → USER.user_id |
| biography | TEXT | nullable |
| qualification | TEXT | nullable; team must decide whether verification is required |

### 3.2 Quran content and Tajweed reference data

#### JUZ

| Attribute | Type | Constraint |
|---|---|---|
| juz_id | SMALLINT | PK; current scope uses 30 |
| juz_number | SMALLINT | required, unique |
| name_ar | VARCHAR(100) | required |
| name_en | VARCHAR(100) | required |

#### SURAH

| Attribute | Type | Constraint |
|---|---|---|
| surah_id | SMALLINT | PK; Quran Surah number |
| juz_id | SMALLINT | required, FK → JUZ.juz_id |
| name_ar | VARCHAR(100) | required |
| name_en | VARCHAR(100) | required |
| revelation_order | SMALLINT | nullable |
| revelation_type | VARCHAR(10) | nullable; Makki or Madani |
| verse_count | SMALLINT | required |
| display_order | SMALLINT | required, unique |

#### VERSE

| Attribute | Type | Constraint |
|---|---|---|
| verse_id | INTEGER | PK |
| surah_id | SMALLINT | required, FK → SURAH.surah_id |
| verse_number | SMALLINT | required |
| uthmani_text | TEXT | required |
| normalized_text | TEXT | required |
| page_number | SMALLINT | nullable |
| hizb_number | SMALLINT | nullable |

Unique constraint: `(surah_id, verse_number)`.

#### VERSE_WORD

Supports exact error location instead of storing an ambiguous text position.

| Attribute | Type | Constraint |
|---|---|---|
| word_id | BIGINT | PK |
| verse_id | INTEGER | required, FK → VERSE.verse_id |
| word_position | SMALLINT | required |
| uthmani_text | VARCHAR(255) | required |
| normalized_text | VARCHAR(255) | required |

Unique constraint: `(verse_id, word_position)`.

#### TAJWEED_RULE

Reference catalog; the final supported rule set remains subject to AI feasibility testing.

| Attribute | Type | Constraint |
|---|---|---|
| tajweed_rule_id | SMALLINT | PK |
| rule_code | VARCHAR(50) | required, unique |
| name_ar | VARCHAR(100) | required |
| name_en | VARCHAR(100) | required |
| description_ar | TEXT | required |
| description_en | TEXT | required |
| is_supported | BOOLEAN | required, default false |

### 3.3 AI modes and recitation sessions

#### AI_MODE

Fixed rows: `al_mujawwid`, `al_mushajji`, and `al_muallim`.

| Attribute | Type | Constraint |
|---|---|---|
| ai_mode_id | SMALLINT | PK |
| mode_code | VARCHAR(30) | required, unique |
| name_ar | VARCHAR(50) | required |
| name_en | VARCHAR(50) | required |
| description | TEXT | required |
| is_active | BOOLEAN | required, default true |

#### RECITATION_SESSION

One learner attempt for one Surah and one selected AI mode.

| Attribute | Type | Constraint |
|---|---|---|
| session_id | UUID | PK |
| learner_id | UUID | required, FK → LEARNER_PROFILE.learner_id |
| surah_id | SMALLINT | required, FK → SURAH.surah_id |
| ai_mode_id | SMALLINT | required, FK → AI_MODE.ai_mode_id |
| started_at | TIMESTAMPTZ | required |
| ended_at | TIMESTAMPTZ | nullable |
| session_status | VARCHAR(20) | required; active, completed, abandoned, or failed |
| completion_percentage | NUMERIC(5,2) | required, default 0; range 0–100 |
| mastery_score | NUMERIC(5,2) | nullable; range 0–100 |
| total_duration_seconds | INTEGER | nullable, non-negative |
| total_pause_count | INTEGER | required, default 0 |
| error_count | INTEGER | required, default 0 |
| failure_reason | TEXT | nullable |

The mastery score is stored as an output, but its formula is deliberately outside this schema until approved.

#### AUDIO_RECORDING

Stores metadata, consent, and retention state rather than embedding audio bytes in the database.

| Attribute | Type | Constraint |
|---|---|---|
| recording_id | UUID | PK |
| session_id | UUID | required, unique, FK → RECITATION_SESSION.session_id |
| storage_uri | TEXT | nullable |
| format | VARCHAR(20) | required |
| duration_seconds | INTEGER | nullable, non-negative |
| sample_rate_hz | INTEGER | nullable |
| file_size_bytes | BIGINT | nullable, non-negative |
| consent_granted | BOOLEAN | required |
| recorded_at | TIMESTAMPTZ | required |
| retention_expires_at | TIMESTAMPTZ | nullable |
| deleted_at | TIMESTAMPTZ | nullable |

#### RECITATION_SEGMENT

Splits a session into ordered verse-level processing units.

| Attribute | Type | Constraint |
|---|---|---|
| segment_id | UUID | PK |
| session_id | UUID | required, FK → RECITATION_SESSION.session_id |
| verse_id | INTEGER | required, FK → VERSE.verse_id |
| segment_order | SMALLINT | required |
| audio_start_ms | INTEGER | required, non-negative |
| audio_end_ms | INTEGER | required and greater than audio_start_ms |
| recognized_text | TEXT | nullable |
| confidence_score | NUMERIC(5,4) | nullable; range 0–1 |
| fluency_score | NUMERIC(5,2) | nullable; range 0–100 |
| segment_status | VARCHAR(20) | required |

Unique constraint: `(session_id, segment_order)`.

#### RECITATION_ANALYSIS

Records the processing result and model traceability for each segment.

| Attribute | Type | Constraint |
|---|---|---|
| analysis_id | UUID | PK |
| segment_id | UUID | required, unique, FK → RECITATION_SEGMENT.segment_id |
| analysis_status | VARCHAR(20) | required; pending, processing, completed, or failed |
| model_name | VARCHAR(100) | nullable |
| model_version | VARCHAR(50) | nullable |
| processing_time_ms | INTEGER | nullable, non-negative |
| analyzed_at | TIMESTAMPTZ | nullable |
| overall_confidence | NUMERIC(5,4) | nullable; range 0–1 |
| failure_reason | TEXT | nullable |

#### PAUSE_EVENT

Supports smart prompting and the pause component of mastery analysis.

| Attribute | Type | Constraint |
|---|---|---|
| pause_event_id | UUID | PK |
| session_id | UUID | required, FK → RECITATION_SESSION.session_id |
| segment_id | UUID | nullable, FK → RECITATION_SEGMENT.segment_id |
| started_at_ms | INTEGER | required, non-negative |
| duration_ms | INTEGER | required, positive |
| pause_type | VARCHAR(20) | required; natural, hesitation, forgotten, or technical |
| prompt_triggered | BOOLEAN | required, default false |
| prompt_delay_ms | INTEGER | nullable |

### 3.4 Error detection and feedback

#### ERROR_TYPE

| Attribute | Type | Constraint |
|---|---|---|
| error_type_id | SMALLINT | PK |
| tajweed_rule_id | SMALLINT | nullable, FK → TAJWEED_RULE.tajweed_rule_id |
| error_code | VARCHAR(50) | required, unique |
| category | VARCHAR(30) | required; pronunciation, Tajweed, omission, insertion, substitution, or fluency |
| name_ar | VARCHAR(100) | required |
| name_en | VARCHAR(100) | required |
| severity | VARCHAR(20) | required |
| description | TEXT | required |

#### RECITATION_ERROR

| Attribute | Type | Constraint |
|---|---|---|
| recitation_error_id | UUID | PK |
| analysis_id | UUID | required, FK → RECITATION_ANALYSIS.analysis_id |
| error_type_id | SMALLINT | required, FK → ERROR_TYPE.error_type_id |
| word_id | BIGINT | nullable, FK → VERSE_WORD.word_id |
| detected_text | TEXT | nullable |
| expected_text | TEXT | nullable |
| audio_start_ms | INTEGER | nullable, non-negative |
| audio_end_ms | INTEGER | nullable |
| confidence_score | NUMERIC(5,4) | required; range 0–1 |
| review_status | VARCHAR(20) | required; unreviewed, accepted, rejected, or corrected |
| detected_at | TIMESTAMPTZ | required |

#### ERROR_FEEDBACK

Allows localized feedback and multiple feedback forms for one detected error.

| Attribute | Type | Constraint |
|---|---|---|
| feedback_id | UUID | PK |
| recitation_error_id | UUID | required, FK → RECITATION_ERROR.recitation_error_id |
| feedback_type | VARCHAR(20) | required; text, visual, or instruction |
| language_code | VARCHAR(5) | required; `ar` or `en` |
| feedback_text | TEXT | required |
| correction_text | TEXT | nullable |
| created_at | TIMESTAMPTZ | required |

#### AUDIO_ASSISTANCE

| Attribute | Type | Constraint |
|---|---|---|
| assistance_id | UUID | PK |
| recitation_error_id | UUID | nullable, FK → RECITATION_ERROR.recitation_error_id |
| pause_event_id | UUID | nullable, FK → PAUSE_EVENT.pause_event_id |
| verse_id | INTEGER | required, FK → VERSE.verse_id |
| audio_uri | TEXT | required |
| assistance_type | VARCHAR(20) | required; correction, continuation, or example |
| played_at | TIMESTAMPTZ | nullable |

Constraint: exactly one of `recitation_error_id` and `pause_event_id` must be present.

### 3.5 Progress and practice history

#### LEARNER_SURAH_PROGRESS

One current summary per learner and Surah.

| Attribute | Type | Constraint |
|---|---|---|
| learner_id | UUID | PK, FK → LEARNER_PROFILE.learner_id |
| surah_id | SMALLINT | PK, FK → SURAH.surah_id |
| attempt_count | INTEGER | required, default 0 |
| completed_session_count | INTEGER | required, default 0 |
| best_mastery_score | NUMERIC(5,2) | nullable; range 0–100 |
| average_mastery_score | NUMERIC(5,2) | nullable; range 0–100 |
| latest_mastery_score | NUMERIC(5,2) | nullable; range 0–100 |
| is_fully_mastered | BOOLEAN | required, default false |
| first_practiced_at | TIMESTAMPTZ | nullable |
| last_practiced_at | TIMESTAMPTZ | nullable |
| mastered_at | TIMESTAMPTZ | nullable |

#### MASTERY_SCORE_HISTORY

Preserves how each completed session affected progress.

| Attribute | Type | Constraint |
|---|---|---|
| mastery_history_id | UUID | PK |
| learner_id | UUID | required, FK → LEARNER_PROFILE.learner_id |
| surah_id | SMALLINT | required, FK → SURAH.surah_id |
| session_id | UUID | required, unique, FK → RECITATION_SESSION.session_id |
| tajweed_score | NUMERIC(5,2) | nullable |
| pronunciation_score | NUMERIC(5,2) | nullable |
| fluency_score | NUMERIC(5,2) | nullable |
| pause_score | NUMERIC(5,2) | nullable |
| final_mastery_score | NUMERIC(5,2) | required; range 0–100 |
| calculated_at | TIMESTAMPTZ | required |
| formula_version | VARCHAR(30) | nullable |

#### DAILY_PRACTICE

| Attribute | Type | Constraint |
|---|---|---|
| learner_id | UUID | PK, FK → LEARNER_PROFILE.learner_id |
| practice_date | DATE | PK |
| session_count | INTEGER | required, positive |
| completed_session_count | INTEGER | required, non-negative |
| total_practice_seconds | INTEGER | required, non-negative |
| verses_practiced | INTEGER | required, non-negative |

#### PRACTICE_STREAK

| Attribute | Type | Constraint |
|---|---|---|
| learner_id | UUID | PK, FK → LEARNER_PROFILE.learner_id |
| current_streak_days | INTEGER | required, default 0 |
| longest_streak_days | INTEGER | required, default 0 |
| current_streak_started_on | DATE | nullable |
| last_practice_date | DATE | nullable |
| updated_at | TIMESTAMPTZ | required |

### 3.6 Teacher, class, and communication functions

#### CLASS

| Attribute | Type | Constraint |
|---|---|---|
| class_id | UUID | PK |
| teacher_id | UUID | required, FK → TEACHER_PROFILE.teacher_id |
| class_name | VARCHAR(100) | required |
| description | TEXT | nullable |
| join_code | VARCHAR(20) | required, unique |
| class_status | VARCHAR(20) | required; active, archived, or closed |
| created_at | TIMESTAMPTZ | required |
| updated_at | TIMESTAMPTZ | required |

#### CLASS_ENROLLMENT

| Attribute | Type | Constraint |
|---|---|---|
| enrollment_id | UUID | PK |
| class_id | UUID | required, FK → CLASS.class_id |
| learner_id | UUID | required, FK → LEARNER_PROFILE.learner_id |
| enrollment_status | VARCHAR(20) | required; invited, active, left, or removed |
| enrolled_at | TIMESTAMPTZ | nullable |
| ended_at | TIMESTAMPTZ | nullable |

Unique constraint: `(class_id, learner_id)`.

#### CLASS_ASSIGNMENT

Proposed detail supporting class management; it must be approved before being treated as a final requirement.

| Attribute | Type | Constraint |
|---|---|---|
| assignment_id | UUID | PK |
| class_id | UUID | required, FK → CLASS.class_id |
| surah_id | SMALLINT | required, FK → SURAH.surah_id |
| created_by | UUID | required, FK → TEACHER_PROFILE.teacher_id |
| title | VARCHAR(150) | required |
| instructions | TEXT | nullable |
| target_mastery_score | NUMERIC(5,2) | nullable; range 0–100 |
| due_at | TIMESTAMPTZ | nullable |
| created_at | TIMESTAMPTZ | required |

#### ASSIGNMENT_PROGRESS

| Attribute | Type | Constraint |
|---|---|---|
| assignment_id | UUID | PK, FK → CLASS_ASSIGNMENT.assignment_id |
| learner_id | UUID | PK, FK → LEARNER_PROFILE.learner_id |
| best_session_id | UUID | nullable, FK → RECITATION_SESSION.session_id |
| assignment_status | VARCHAR(20) | required; not_started, in_progress, completed, or overdue |
| best_mastery_score | NUMERIC(5,2) | nullable |
| completed_at | TIMESTAMPTZ | nullable |
| updated_at | TIMESTAMPTZ | required |

#### TEACHER_MESSAGE

| Attribute | Type | Constraint |
|---|---|---|
| message_id | UUID | PK |
| teacher_id | UUID | required, FK → TEACHER_PROFILE.teacher_id |
| learner_id | UUID | required, FK → LEARNER_PROFILE.learner_id |
| class_id | UUID | nullable, FK → CLASS.class_id |
| session_id | UUID | nullable, FK → RECITATION_SESSION.session_id |
| message_text | TEXT | required |
| sent_at | TIMESTAMPTZ | required |
| read_at | TIMESTAMPTZ | nullable |

Application authorization must ensure that the learner belongs to the teacher's class when the message is sent.

#### STUDENT_PERFORMANCE_SNAPSHOT

Optional reporting cache for teacher dashboards. It is derived from session and progress data and may be omitted from the initial implementation if live queries perform adequately.

| Attribute | Type | Constraint |
|---|---|---|
| snapshot_id | UUID | PK |
| class_id | UUID | required, FK → CLASS.class_id |
| learner_id | UUID | required, FK → LEARNER_PROFILE.learner_id |
| generated_at | TIMESTAMPTZ | required |
| completed_surah_count | SMALLINT | required |
| average_mastery_score | NUMERIC(5,2) | nullable |
| total_sessions | INTEGER | required |
| total_practice_seconds | INTEGER | required |
| current_streak_days | INTEGER | required |

Unique constraint: `(class_id, learner_id, generated_at)`.

### 3.7 Al-Mushajji gamification — proposed

The requirements approve motivational interactions, challenges, and rewards conceptually, but their mechanics remain unresolved. These tables will appear in a visually marked **PROPOSED** area of the ERD.

#### CHALLENGE

| Attribute | Type | Constraint |
|---|---|---|
| challenge_id | UUID | PK |
| title_ar | VARCHAR(150) | required |
| title_en | VARCHAR(150) | required |
| description_ar | TEXT | required |
| description_en | TEXT | required |
| challenge_type | VARCHAR(30) | required |
| target_value | INTEGER | required, positive |
| starts_at | TIMESTAMPTZ | nullable |
| ends_at | TIMESTAMPTZ | nullable |
| is_active | BOOLEAN | required, default true |

#### LEARNER_CHALLENGE

| Attribute | Type | Constraint |
|---|---|---|
| learner_id | UUID | PK, FK → LEARNER_PROFILE.learner_id |
| challenge_id | UUID | PK, FK → CHALLENGE.challenge_id |
| progress_value | INTEGER | required, default 0 |
| challenge_status | VARCHAR(20) | required |
| joined_at | TIMESTAMPTZ | required |
| completed_at | TIMESTAMPTZ | nullable |

#### REWARD

| Attribute | Type | Constraint |
|---|---|---|
| reward_id | UUID | PK |
| reward_code | VARCHAR(50) | required, unique |
| name_ar | VARCHAR(100) | required |
| name_en | VARCHAR(100) | required |
| description | TEXT | required |
| reward_type | VARCHAR(30) | required |

#### LEARNER_REWARD

| Attribute | Type | Constraint |
|---|---|---|
| learner_id | UUID | PK, FK → LEARNER_PROFILE.learner_id |
| reward_id | UUID | PK, FK → REWARD.reward_id |
| challenge_id | UUID | nullable, FK → CHALLENGE.challenge_id |
| awarded_at | TIMESTAMPTZ | required |

## 4. Cardinality summary

- USER has zero or more USER_ROLE rows; each USER_ROLE belongs to one USER and one ROLE.
- USER has zero or one LEARNER_PROFILE and zero or one TEACHER_PROFILE.
- JUZ has one or more SURAH rows; SURAH belongs to one JUZ.
- SURAH has one or more VERSE rows; VERSE belongs to one SURAH.
- VERSE has one or more VERSE_WORD rows; VERSE_WORD belongs to one VERSE.
- LEARNER_PROFILE has zero or more RECITATION_SESSION rows.
- SURAH and AI_MODE each classify zero or more RECITATION_SESSION rows.
- RECITATION_SESSION has zero or one AUDIO_RECORDING and one or more RECITATION_SEGMENT rows after processing begins.
- RECITATION_SEGMENT has zero or one RECITATION_ANALYSIS; an analysis has zero or more RECITATION_ERROR rows.
- RECITATION_ERROR belongs to one ERROR_TYPE and may identify one VERSE_WORD.
- RECITATION_ERROR has zero or more ERROR_FEEDBACK rows.
- RECITATION_SESSION has zero or more PAUSE_EVENT rows.
- AUDIO_ASSISTANCE belongs to either one RECITATION_ERROR or one PAUSE_EVENT.
- LEARNER_PROFILE and SURAH have a many-to-many history resolved by LEARNER_SURAH_PROGRESS and MASTERY_SCORE_HISTORY.
- TEACHER_PROFILE has zero or more CLASS rows; CLASS and LEARNER_PROFILE are many-to-many through CLASS_ENROLLMENT.
- CLASS has zero or more CLASS_ASSIGNMENT rows; assignments and learners are many-to-many through ASSIGNMENT_PROGRESS.
- TEACHER_PROFILE sends zero or more TEACHER_MESSAGE rows to LEARNER_PROFILE.
- CHALLENGE and LEARNER_PROFILE are many-to-many through LEARNER_CHALLENGE.
- REWARD and LEARNER_PROFILE are many-to-many through LEARNER_REWARD.

## 5. Data integrity and deletion behavior

- Quran reference data uses restrictive deletion; Surahs and verses cannot be removed while referenced.
- Deleting an account is logical (`account_status = deleted`) so academic progress and audit evidence are not accidentally lost.
- Deleting retained audio clears `storage_uri` and sets `deleted_at`; session results remain available.
- Session-owned detail rows may use cascading deletion only when a session is deliberately purged under the final privacy policy.
- Scores and percentages are constrained to 0–100; confidence values are constrained to 0–1.
- Time ranges require end values greater than start values.
- A completed session requires `ended_at`; an active session must not have an end time.
- Teacher access to learner data is permitted only through active class enrollment.

## 6. Confirmed versus proposed scope

### Confirmed foundation

Identity, learner and teacher roles, Juz Amma content, AI modes, microphone recitation sessions, analysis, error location, feedback, audio assistance, session results, mastery percentage, progress tracking, streaks, teacher dashboards, classes, and teacher messages derive from the current requirements.

### Proposed details requiring explicit team approval

- teacher qualifications;
- exact Tajweed-rule catalog and supported-rule flags;
- audio-retention duration and storage provider;
- class assignments and assignment progress;
- performance snapshots as stored reporting data;
- gamification tables and mechanics;
- mastery component weights and formula;
- AI model metadata retained for each analysis;
- the exact conditions under which audio assistance is stored or generated.

These elements will be visually distinguished in the ERD and documented as proposed rather than presented as finalized requirements.

## 7. Deliverables after approval

1. `docs/database/itqan-erd.mmd` — editable Mermaid ERD source.
2. `docs/database/itqan-erd.svg` — rendered diagram for the report.
3. `docs/database/RELATIONAL_SCHEMA.md` — table-by-table relational schema and constraints.
4. `docs/database/ERD_REQUIREMENTS_TRACEABILITY.md` — mapping from FRs to entities.

## 8. Validation

The finished artifacts will be checked by:

1. rendering the Mermaid source without syntax errors;
2. verifying that every foreign key targets an existing primary or unique key;
3. tracing FR-01 through FR-25 to at least one entity or explicitly marking a requirement as behavior-only;
4. checking that no Admin role or full-Quran scope was added;
5. checking that proposed features are visually and textually separated from confirmed scope.
