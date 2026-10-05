# Itqan Relational Schema

This schema accompanies the complete Itqan ERD. It is implementation-neutral but uses PostgreSQL-compatible data types.

## Notation and shared rules

- `PK`: primary key; `FK`: foreign key; `UK`: unique key.
- Columns are required unless marked `NULL`.
- User-generated records use UUID identifiers. Fixed Quran and lookup data use integer identifiers.
- All timestamps are UTC-aware `TIMESTAMPTZ` values.
- Percentages and scores use `NUMERIC(5,2)` and must remain between 0 and 100.
- AI confidence values use `NUMERIC(5,4)` and must remain between 0 and 1.
- Durations, counts, positions, and file sizes cannot be negative.
- Proposed tables are clearly labeled and must not be treated as approved requirements until the team confirms them.

## Identity and access

### USER

`USER(user_id UUID PK, identity_subject VARCHAR(255) UK, email VARCHAR(254) UK, display_name VARCHAR(100), preferred_language VARCHAR(5), account_status VARCHAR(20), created_at TIMESTAMPTZ, updated_at TIMESTAMPTZ, last_login_at TIMESTAMPTZ NULL)`

Stores every authenticated learner or teacher account. `identity_subject` is issued by the managed identity provider; the application never stores or verifies a password. `preferred_language` is `ar` or `en`; `account_status` is `active`, `suspended`, or `deleted`. Account deletion is logical.

### ROLE

`ROLE(role_id SMALLINT PK, role_code VARCHAR(30) UK, role_name_ar VARCHAR(50), role_name_en VARCHAR(50))`

Fixed rows are `learner` and `teacher`. No Admin role is approved.

### USER_ROLE

`USER_ROLE(user_id UUID PK FK→USER.user_id, role_id SMALLINT PK FK→ROLE.role_id, assigned_at TIMESTAMPTZ)`

Composite primary key `(user_id, role_id)`. Supports an account holding both approved roles.

### LEARNER_PROFILE

`LEARNER_PROFILE(learner_id UUID PK FK→USER.user_id, learning_goal TEXT NULL, experience_level VARCHAR(20) NULL, reminders_enabled BOOLEAN DEFAULT FALSE)`

Extends a user account with learner-specific preferences.

### TEACHER_PROFILE

`TEACHER_PROFILE(teacher_id UUID PK FK→USER.user_id, school_name VARCHAR(150), biography TEXT NULL, qualification TEXT NULL)`

Extends a user account with teacher-specific information. Qualification verification remains unresolved.

### CONSENT_RECORD

`CONSENT_RECORD(consent_id UUID PK, user_id UUID FK→USER.user_id, purpose_code VARCHAR(50), policy_version VARCHAR(30), collection_method VARCHAR(30), granted_at TIMESTAMPTZ, withdrawn_at TIMESTAMPTZ NULL)`

Immutable per-purpose consent history. A record is active when `withdrawn_at` is null; only one active record may exist for a `(user_id, purpose_code)` pair.

## Quran content and Tajweed references

### JUZ

`JUZ(juz_id SMALLINT PK, juz_number SMALLINT UK, name_ar VARCHAR(100), name_en VARCHAR(100))`

Current scope uses Juz 30 only.

### SURAH

`SURAH(surah_id SMALLINT PK, juz_id SMALLINT FK→JUZ.juz_id, name_ar VARCHAR(100), name_en VARCHAR(100), revelation_order SMALLINT NULL, revelation_type VARCHAR(10) NULL, verse_count SMALLINT, display_order SMALLINT UK)`

Contains the 37 Surahs of Juz Amma. `revelation_type`, when known, is `Makki` or `Madani`.

### VERSE

`VERSE(verse_id INTEGER PK, surah_id SMALLINT FK→SURAH.surah_id, verse_number SMALLINT, uthmani_text TEXT, normalized_text TEXT, page_number SMALLINT NULL, hizb_number SMALLINT NULL)`

Unique key `(surah_id, verse_number)`. Quran reference rows use restrictive deletion.

### VERSE_WORD

`VERSE_WORD(word_id BIGINT PK, verse_id INTEGER FK→VERSE.verse_id, word_position SMALLINT, uthmani_text VARCHAR(255), normalized_text VARCHAR(255))`

Unique key `(verse_id, word_position)`. Provides an exact location for detected errors.

### TAJWEED_RULE

`TAJWEED_RULE(tajweed_rule_id SMALLINT PK, rule_code VARCHAR(50) UK, name_ar VARCHAR(100), name_en VARCHAR(100), description_ar TEXT, description_en TEXT, is_supported BOOLEAN DEFAULT FALSE)`

The complete rule catalog and supported subset depend on AI feasibility testing.

## AI modes and recitation sessions

### AI_MODE

`AI_MODE(ai_mode_id SMALLINT PK, mode_code VARCHAR(30) UK, name_ar VARCHAR(50), name_en VARCHAR(50), description TEXT, is_active BOOLEAN DEFAULT TRUE)`

Fixed modes are `al_mujawwid`, `al_mushajji`, and `al_muallim`.

### RECITATION_SESSION

`RECITATION_SESSION(session_id UUID PK, learner_id UUID FK→LEARNER_PROFILE.learner_id, surah_id SMALLINT FK→SURAH.surah_id, ai_mode_id SMALLINT FK→AI_MODE.ai_mode_id, started_at TIMESTAMPTZ, ended_at TIMESTAMPTZ NULL, session_status VARCHAR(20), completion_percentage NUMERIC(5,2) DEFAULT 0, mastery_score NUMERIC(5,2) NULL, total_duration_seconds INTEGER NULL, total_pause_count INTEGER DEFAULT 0, error_count INTEGER DEFAULT 0, failure_reason TEXT NULL)`

Stores one learner attempt for one Surah and selected AI mode. Status is `active`, `completed`, `abandoned`, or `failed`. Completed sessions require `ended_at`; active sessions must not have it. The schema stores the session mastery result; the calculation is defined by the approved mastery formula in the requirements.

### RECITATION_SEGMENT

`RECITATION_SEGMENT(segment_id UUID PK, session_id UUID FK→RECITATION_SESSION.session_id, verse_id INTEGER FK→VERSE.verse_id, segment_order SMALLINT, audio_start_ms INTEGER, audio_end_ms INTEGER, recognized_text TEXT NULL, confidence_score NUMERIC(5,4) NULL, fluency_score NUMERIC(5,2) NULL, segment_status VARCHAR(20))`

Unique key `(session_id, segment_order)`. `audio_end_ms` must be greater than `audio_start_ms`.

### RECITATION_ANALYSIS

`RECITATION_ANALYSIS(analysis_id UUID PK, segment_id UUID UK FK→RECITATION_SEGMENT.segment_id, analysis_status VARCHAR(20), model_name VARCHAR(100) NULL, model_version VARCHAR(50) NULL, processing_time_ms INTEGER NULL, analyzed_at TIMESTAMPTZ NULL, overall_confidence NUMERIC(5,4) NULL, failure_reason TEXT NULL)`

Status is `pending`, `processing`, `completed`, or `failed`. Model fields support evaluation traceability without fixing the technology stack.

### PAUSE_EVENT

`PAUSE_EVENT(pause_event_id UUID PK, session_id UUID FK→RECITATION_SESSION.session_id, segment_id UUID NULL FK→RECITATION_SEGMENT.segment_id, started_at_ms INTEGER, duration_ms INTEGER, pause_type VARCHAR(20), prompt_triggered BOOLEAN DEFAULT FALSE, prompt_delay_ms INTEGER NULL)`

`duration_ms` must be positive. Pause type is `natural`, `hesitation`, `forgotten`, or `technical`.

## Error detection and feedback

### ERROR_TYPE

`ERROR_TYPE(error_type_id SMALLINT PK, tajweed_rule_id SMALLINT NULL FK→TAJWEED_RULE.tajweed_rule_id, error_code VARCHAR(50) UK, category VARCHAR(30), name_ar VARCHAR(100), name_en VARCHAR(100), severity VARCHAR(20), description TEXT)`

Category is `pronunciation`, `tajweed`, `omission`, `insertion`, `substitution`, or `fluency`.

### RECITATION_ERROR

`RECITATION_ERROR(recitation_error_id UUID PK, analysis_id UUID FK→RECITATION_ANALYSIS.analysis_id, error_type_id SMALLINT FK→ERROR_TYPE.error_type_id, word_id BIGINT NULL FK→VERSE_WORD.word_id, detected_text TEXT NULL, expected_text TEXT NULL, audio_start_ms INTEGER NULL, audio_end_ms INTEGER NULL, confidence_score NUMERIC(5,4), review_status VARCHAR(20), detected_at TIMESTAMPTZ)`

Review status is `unreviewed`, `accepted`, `rejected`, or `corrected`. Audio end, when present, must exceed audio start.

### ERROR_FEEDBACK

`ERROR_FEEDBACK(feedback_id UUID PK, recitation_error_id UUID FK→RECITATION_ERROR.recitation_error_id, feedback_type VARCHAR(20), language_code VARCHAR(5), feedback_text TEXT, correction_text TEXT NULL, created_at TIMESTAMPTZ)`

Feedback type is `text`, `visual`, or `instruction`; language is `ar` or `en`.

### AUDIO_ASSISTANCE

`AUDIO_ASSISTANCE(assistance_id UUID PK, recitation_error_id UUID NULL FK→RECITATION_ERROR.recitation_error_id, pause_event_id UUID NULL FK→PAUSE_EVENT.pause_event_id, verse_id INTEGER FK→VERSE.verse_id, audio_uri TEXT, assistance_type VARCHAR(20), played_at TIMESTAMPTZ NULL)`

Exactly one of `recitation_error_id` and `pause_event_id` must be present. Type is `correction`, `continuation`, or `example`.

## Progress and practice history

### LEARNER_SURAH_PROGRESS

`LEARNER_SURAH_PROGRESS(learner_id UUID PK FK→LEARNER_PROFILE.learner_id, surah_id SMALLINT PK FK→SURAH.surah_id, attempt_count INTEGER DEFAULT 0, completed_session_count INTEGER DEFAULT 0, best_mastery_score NUMERIC(5,2) NULL, average_mastery_score NUMERIC(5,2) NULL, latest_mastery_score NUMERIC(5,2) NULL, is_fully_mastered BOOLEAN DEFAULT FALSE, first_practiced_at TIMESTAMPTZ NULL, last_practiced_at TIMESTAMPTZ NULL, mastered_at TIMESTAMPTZ NULL)`

Composite primary key `(learner_id, surah_id)`. Contains the current progress summary; history remains in sessions and mastery history.

### MASTERY_SCORE_HISTORY

`MASTERY_SCORE_HISTORY(mastery_history_id UUID PK, learner_id UUID FK→LEARNER_PROFILE.learner_id, surah_id SMALLINT FK→SURAH.surah_id, session_id UUID UK FK→RECITATION_SESSION.session_id, total_words INTEGER, effective_errors NUMERIC(6,2), final_mastery_score NUMERIC(5,2), calculated_at TIMESTAMPTZ, formula_version VARCHAR(30) NULL)`

Stores the values used for the approved mastery calculation: `Mastery Score = (Total Words − Effective Errors) / Total Words × 100`. A complete word pronunciation error contributes 1 effective error, while a Tajweed-only error contributes 0.5; the effective error contribution per word is capped at 1.

### DAILY_PRACTICE

`DAILY_PRACTICE(learner_id UUID PK FK→LEARNER_PROFILE.learner_id, practice_date DATE PK, session_count INTEGER, completed_session_count INTEGER, total_practice_seconds INTEGER, verses_practiced INTEGER)`

Composite primary key `(learner_id, practice_date)`. `session_count` is positive; other counts are non-negative.

### PRACTICE_STREAK

`PRACTICE_STREAK(learner_id UUID PK FK→LEARNER_PROFILE.learner_id, current_streak_days INTEGER DEFAULT 0, longest_streak_days INTEGER DEFAULT 0, current_streak_started_on DATE NULL, last_practice_date DATE NULL, updated_at TIMESTAMPTZ)`

Maintains one current streak summary per learner; daily evidence remains in `DAILY_PRACTICE`.

## Teacher, class, and communication functions

### LEARNING_CLASS

`LEARNING_CLASS(class_id UUID PK, teacher_id UUID FK→TEACHER_PROFILE.teacher_id, class_name VARCHAR(100), description TEXT NULL, join_code VARCHAR(20) UK, class_status VARCHAR(20), created_at TIMESTAMPTZ, updated_at TIMESTAMPTZ)`

Status is `active`, `archived`, or `closed`. A learner joins by entering the unique class code; an active enrollment grants the teacher scoped access.

### CLASS_ENROLLMENT

`CLASS_ENROLLMENT(enrollment_id UUID PK, class_id UUID FK→LEARNING_CLASS.class_id, learner_id UUID FK→LEARNER_PROFILE.learner_id, enrollment_status VARCHAR(20), enrolled_at TIMESTAMPTZ NULL, ended_at TIMESTAMPTZ NULL)`

Unique key `(class_id, learner_id)`. Status is `active`, `left`, or `removed`.

### CLASS_ASSIGNMENT — proposed

`CLASS_ASSIGNMENT(assignment_id UUID PK, class_id UUID FK→LEARNING_CLASS.class_id, surah_id SMALLINT FK→SURAH.surah_id, created_by UUID FK→TEACHER_PROFILE.teacher_id, title VARCHAR(150), instructions TEXT NULL, target_mastery_score NUMERIC(5,2) NULL, due_at TIMESTAMPTZ NULL, created_at TIMESTAMPTZ)`

Supports assigning Surah practice to a class. Assignment behavior requires team approval.

### ASSIGNMENT_PROGRESS — proposed

`ASSIGNMENT_PROGRESS(assignment_id UUID PK FK→CLASS_ASSIGNMENT.assignment_id, learner_id UUID PK FK→LEARNER_PROFILE.learner_id, best_session_id UUID NULL FK→RECITATION_SESSION.session_id, assignment_status VARCHAR(20), best_mastery_score NUMERIC(5,2) NULL, completed_at TIMESTAMPTZ NULL, updated_at TIMESTAMPTZ)`

Composite primary key `(assignment_id, learner_id)`. Status is `not_started`, `in_progress`, `completed`, or `overdue`.

### TEACHER_MESSAGE

`TEACHER_MESSAGE(message_id UUID PK, teacher_id UUID FK→TEACHER_PROFILE.teacher_id, learner_id UUID FK→LEARNER_PROFILE.learner_id, class_id UUID NULL FK→LEARNING_CLASS.class_id, session_id UUID NULL FK→RECITATION_SESSION.session_id, message_text TEXT, sent_at TIMESTAMPTZ, read_at TIMESTAMPTZ NULL)`

The application must verify an active class enrollment before a teacher accesses learner data or sends a message.

### LEARNER_PERFORMANCE_SNAPSHOT — proposed reporting cache

`LEARNER_PERFORMANCE_SNAPSHOT(snapshot_id UUID PK, class_id UUID FK→LEARNING_CLASS.class_id, learner_id UUID FK→LEARNER_PROFILE.learner_id, generated_at TIMESTAMPTZ, completed_surah_count SMALLINT, average_mastery_score NUMERIC(5,2) NULL, total_sessions INTEGER, total_practice_seconds INTEGER, current_streak_days INTEGER)`

Unique key `(class_id, learner_id, generated_at)`. This derived cache can be omitted if live dashboard queries perform adequately.

## Al-Mushajji gamification — proposed

The mode is approved, but challenge and reward mechanics remain unresolved. These four tables are design proposals.

### CHALLENGE

`CHALLENGE(challenge_id UUID PK, title_ar VARCHAR(150), title_en VARCHAR(150), description_ar TEXT, description_en TEXT, challenge_type VARCHAR(30), target_value INTEGER, starts_at TIMESTAMPTZ NULL, ends_at TIMESTAMPTZ NULL, is_active BOOLEAN DEFAULT TRUE)`

`target_value` is positive; `ends_at`, when present, must be later than `starts_at`.

### LEARNER_CHALLENGE

`LEARNER_CHALLENGE(learner_id UUID PK FK→LEARNER_PROFILE.learner_id, challenge_id UUID PK FK→CHALLENGE.challenge_id, progress_value INTEGER DEFAULT 0, challenge_status VARCHAR(20), joined_at TIMESTAMPTZ, completed_at TIMESTAMPTZ NULL)`

Composite primary key `(learner_id, challenge_id)`.

### REWARD

`REWARD(reward_id UUID PK, reward_code VARCHAR(50) UK, name_ar VARCHAR(100), name_en VARCHAR(100), description TEXT, reward_type VARCHAR(30))`

Defines a reusable motivational reward.

### LEARNER_REWARD

`LEARNER_REWARD(learner_id UUID PK FK→LEARNER_PROFILE.learner_id, reward_id UUID PK FK→REWARD.reward_id, challenge_id UUID NULL FK→CHALLENGE.challenge_id, awarded_at TIMESTAMPTZ)`

Composite primary key `(learner_id, reward_id)`. `challenge_id` records the source when a challenge awarded the reward.

## Deletion, privacy, and authorization

- Quran reference rows and lookup rows use restrictive deletion while referenced.
- User accounts use logical deletion through `USER.account_status`; historical academic evidence is retained according to the final privacy policy.
- Session-owned detail may cascade only during an authorized privacy purge; normal account deactivation must not destroy progress evidence.
- Teachers may access learner progress, sessions, snapshots, and messages only through an active `CLASS_ENROLLMENT` associated with a class they own.
- Sensitive fields and account credentials require authorization and encryption controls outside this logical schema.
