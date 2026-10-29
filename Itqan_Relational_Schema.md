# Itqan relational schema and data dictionary

This is the PostgreSQL translation of the [approved ERD](docs/updated-diagrams/erd/itqan-erd.mmd) and [final requirements](Itqan_Requirements.md), especially §8. It describes the logical schema and required transactional checks; it is not an executed migration. Constraint expressions are illustrative and have not been executed against PostgreSQL. There are 14 tables and no stored progress cache.

## Notation and type choices

`PK`, `FK` and `UQ` mean primary key, foreign key and unique constraint/index; `—` means none. Every `PK` is implicitly `NOT NULL` and unique. `NULL?` is explicit for every column. `UUID` is a non-sequential service-generated UUIDv4; there is no implicit database ID default. `TIMESTAMPTZ` preserves an instant in time; the application displays it in the device's local calendar. `NUMERIC(10,1)` represents half-error increments without floating-point drift; `NUMERIC(4,1)` represents a 0–100 score. `TEXT` value lists below are exact stored strings. Unless shown, there is no default or additional column-level check. Foreign keys are immediate unless a rule below explicitly calls for a deferred check. Reference rows must be seeded and kept read-only by application permissions.

The `Rule` column traces each field to a functional requirement (`FR`), business rule (`BR`), or requirements §8.1. Composite keys and supporting `UQ` constraints are stated below the tables. `ON DELETE RESTRICT` on reference data prevents accidental loss of Quran content; `ON DELETE CASCADE` implements account deletion. Update of identity/relationship keys is disallowed by the service; no `ON UPDATE CASCADE` is intended.

## Data dictionary

### 1. `account`

| Column | PostgreSQL type | Key | NULL? | Default / allowed values / check | FK target; delete | Rule |
|---|---|---|---|---|---|---|
| `account_id` | `UUID` | PK | No | Service-generated UUIDv4 | — | §8.1, NFR-06 |
| `identity_subject` | `TEXT` | UQ | No | Nonblank; fixed after registration | — | FR-01, FR-02, §8.1 |
| `account_type` | `TEXT` | — | No | `CHECK (account_type IN ('Reader', 'Teacher'))`; immutable | — | FR-01, BR-15 |
| `display_name` | `TEXT` | — | No | Nonblank after trimming | — | FR-01, FR-03 |
| `email` | `TEXT` | UQ* | No | Nonblank; identity-provider-managed value | — | FR-01, FR-03, UC-01 |
| `language` | `TEXT` | — | No | Default `'ar'`; `CHECK (language IN ('ar', 'en'))` | — | FR-03, NFR-11 |
| `created_at` | `TIMESTAMPTZ` | — | No | Default `CURRENT_TIMESTAMP` | — | §8.1 |

*Use a unique expression index on `lower(email)` so case-only duplicates cannot be registered locally. Keep its comparison policy aligned with the chosen identity provider. The service must synchronize a provider-managed email change. The database rejects updates to `account_type` and `identity_subject` (trigger or restricted write path); an account never changes role. Store no password.

### 2. `teacher_detail`

| Column | PostgreSQL type | Key | NULL? | Default / allowed values / check | FK target; delete | Rule |
|---|---|---|---|---|---|---|
| `teacher_id` | `UUID` | PK, FK | No | — | `account(account_id)`; CASCADE | FR-01, BR-15, §8.1–8.2 |
| `school_name` | `TEXT` | — | No | Nonblank after trimming | — | FR-01, FR-03 |

The shared PK permits at most one detail row per account. A deferred constraint trigger at transaction end must require exactly one detail row for every surviving Teacher account and none for a Reader. Create Teacher and detail in one transaction. A plain FK cannot require the child row or test the parent's role.

### 3. `consent_record`

| Column | PostgreSQL type | Key | NULL? | Default / allowed values / check | FK target; delete | Rule |
|---|---|---|---|---|---|---|
| `consent_id` | `UUID` | PK | No | Service-generated UUIDv4 | — | FR-27, §8.1 |
| `reader_id` | `UUID` | FK | No | Reader role required | `account(account_id)`; CASCADE | FR-27, BR-16 |
| `purpose` | `TEXT` | — | No | `CHECK (purpose IN ('recitation', 'teacher sharing'))` | — | FR-27, BR-16 |
| `granted_at` | `TIMESTAMPTZ` | — | No | Default `CURRENT_TIMESTAMP`; immutable | — | BR-16, §8.1 |
| `withdrawn_at` | `TIMESTAMPTZ` | — | Yes | NULL means active; when set, `withdrawn_at >= granted_at`; immutable once set | — | FR-27, BR-16 |

Add a **partial unique index** on `(reader_id, purpose) WHERE withdrawn_at IS NULL`. Thus history remains and a later grant inserts a new row. A role-check trigger or the trusted service must reject non-Readers. Grant/withdraw under a transaction lock on the Reader account. Withdrawal of `teacher sharing` must set `withdrawn_at` and end **all** active enrolments for that Reader in the same transaction; withdrawal of `recitation` blocks new starts but keeps historical results. The service checks an active grant before a session starts or a class is joined.

### 4. `surah` — read-only reference data

| Column | PostgreSQL type | Key | NULL? | Default / allowed values / check | FK target; delete | Rule |
|---|---|---|---|---|---|---|
| `surah_number` | `SMALLINT` | PK | No | `CHECK (surah_number BETWEEN 78 AND 114)` | — | FR-04, §8.1 |
| `arabic_name` | `TEXT` | — | No | Nonblank | — | FR-04, §8.1 |
| `english_name` | `TEXT` | — | No | Nonblank | — | FR-04, §8.1 |
| `verse_count` | `SMALLINT` | — | No | `CHECK (verse_count > 0)` | — | FR-04, §8.1 |

Seed exactly the 37 Juz Amma surahs. `verse_count` must equal the number of seeded verses; verify during reference-data loading, since a row check cannot count children.

### 5. `verse` — read-only reference data

| Column | PostgreSQL type | Key | NULL? | Default / allowed values / check | FK target; delete | Rule |
|---|---|---|---|---|---|---|
| `surah_number` | `SMALLINT` | PK, FK | No | — | `surah(surah_number)`; RESTRICT | FR-06, §8.1–8.2 |
| `verse_number` | `SMALLINT` | PK | No | `CHECK (verse_number > 0)` | — | FR-06, §8.1 |
| `uthmani_text` | `TEXT` | — | No | Nonblank | — | FR-06, §8.1 |
| `imlaei_text` | `TEXT` | — | No | Nonblank | — | FR-13, §8.1 |

PK `(surah_number, verse_number)`. Seed 564 verses; validate continuous verse numbering from 1 through each `surah.verse_count` during loading.

### 6. `word` — read-only reference data

| Column | PostgreSQL type | Key | NULL? | Default / allowed values / check | FK target; delete | Rule |
|---|---|---|---|---|---|---|
| `surah_number` | `SMALLINT` | PK, FK† | No | — | With `verse_number` → `verse(surah_number, verse_number)`; RESTRICT | FR-15, §8.1–8.2 |
| `verse_number` | `SMALLINT` | PK, FK† | No | — | With `surah_number` → `verse(surah_number, verse_number)`; RESTRICT | FR-15, §8.1–8.2 |
| `word_position` | `SMALLINT` | PK | No | `CHECK (word_position > 0)` | — | FR-15, §8.1 |
| `word_text` | `TEXT` | — | No | Nonblank | — | FR-15, §8.1 |
| `audio_start_ms` | `INTEGER` | — | No | `CHECK (audio_start_ms >= 0)` | — | FR-17, §8.1 |
| `audio_end_ms` | `INTEGER` | — | No | `CHECK (audio_end_ms > audio_start_ms)` | — | FR-17, §8.1 |

PK `(surah_number, verse_number, word_position)`. †One composite FK, not two independent FKs. Seed 2,308 words and validate continuous positions per verse. Timing values are millisecond offsets identifying the word's interval in the app's corresponding bundled reference audio; the app bundle resolves the Word key to its audio asset. No audio, audio path or reciter metadata is stored in PostgreSQL. The audio source and timing calibration remain IS499 item O-4.

### 7. `tajweed_rule` — read-only reference data

| Column | PostgreSQL type | Key | NULL? | Default / allowed values / check | FK target; delete | Rule |
|---|---|---|---|---|---|---|
| `rule_id` | `SMALLINT` | PK | No | Positive; seed IDs 1, 2, 3 only in phase one | — | FR-14, §8.1 |
| `name` | `TEXT` | UQ | No | Seed `Ghunnah`, `Qalqalah`, `Madd` | — | FR-14, §8.1 |

Schema seed mapping: `1 = Ghunnah`, `2 = Qalqalah`, `3 = Madd`. This numeric mapping is an implementation choice, not a new product rule. Do not insert other rules in phase one. The FK below checks existence; service/reference-data permissions restrict the available IDs to these three.

### 8. `recitation_session`

| Column | PostgreSQL type | Key | NULL? | Default / allowed values / check | FK target; delete | Rule |
|---|---|---|---|---|---|---|
| `session_id` | `UUID` | PK, UQ* | No | Service-generated UUIDv4 | — | FR-19, §8.1 |
| `reader_id` | `UUID` | FK | No | Reader role required | `account(account_id)`; CASCADE | FR-11, FR-28 |
| `surah_number` | `SMALLINT` | FK, UQ* | No | — | `surah(surah_number)`; RESTRICT | FR-05, BR-07 |
| `mode` | `TEXT` | — | No | `CHECK (mode IN ('Mujawwid', 'Mushajji'))` | — | FR-07–FR-09 |
| `started_at` | `TIMESTAMPTZ` | — | No | Original start instant; `started_at <= ended_at` | — | FR-19, §8.1 |
| `ended_at` | `TIMESTAMPTZ` | — | No | End instant; `ended_at >= started_at` | — | FR-19, BR-06, BR-08 |
| `end_reason` | `TEXT` | — | No | `CHECK (end_reason IN ('completed', 'ended early', 'interrupted'))` | — | FR-19, §9 |
| `counted_words` | `INTEGER` | — | No | `CHECK (counted_words >= 0)` | — | BR-02 |
| `effective_errors` | `NUMERIC(10,1)` | — | No | `CHECK (effective_errors >= 0 AND effective_errors <= counted_words)` | — | BR-01, BR-02 |
| `mastery_score` | `NUMERIC(4,1)` | — | Yes | `CHECK (mastery_score BETWEEN 0 AND 100)` when non-NULL | — | BR-01, BR-02 |
| `whole_surah_analysed` | `BOOLEAN` | — | No | True only if every verse was reliably analysed | — | BR-03, BR-18 |

*Add supporting `UNIQUE (session_id, surah_number)` for the composite Mistake FK. It does not change the identity of a session. Add a table check: `(counted_words = 0 AND effective_errors = 0 AND mastery_score IS NULL AND whole_surah_analysed = FALSE) OR (counted_words > 0 AND mastery_score IS NOT NULL)`. Persist **only ended** summaries; `ended_at` and `end_reason` are mandatory. Finalize a session and its mistakes atomically, including interruption. The service derives counted words from reached, reliably analysed words, caps effective errors per Word at 1, then sets `mastery_score = round((counted_words - effective_errors) * 100 / counted_words, 1)` when the denominator is positive. A database row check cannot prove the score agrees with the child Mistakes, that `whole_surah_analysed` matches the transient analysis, or that a Mistake was on a counted word; the finalization transaction must do so. A zero-word or interrupted session remains a valid stored row.

### 9. `mistake`

| Column | PostgreSQL type | Key | NULL? | Default / allowed values / check | FK target; delete | Rule |
|---|---|---|---|---|---|---|
| `mistake_id` | `UUID` | PK | No | Service-generated UUIDv4 | — | FR-14, §8.1 |
| `session_id` | `UUID` | FK† | No | — | With `surah_number` → `recitation_session(session_id, surah_number)`; CASCADE | FR-15, BR-05 |
| `surah_number` | `SMALLINT` | FK†, FK‡ | No | Must equal the session's Surah | Both composite FKs shown here; CASCADE for session, RESTRICT for Word | FR-15, §8.2 |
| `verse_number` | `SMALLINT` | FK‡ | No | — | With Word key → `word(surah_number, verse_number, word_position)`; RESTRICT | FR-15, §8.2 |
| `word_position` | `SMALLINT` | FK‡ | No | — | With Word key → `word(surah_number, verse_number, word_position)`; RESTRICT | FR-15, §8.2 |
| `error_type` | `TEXT` | — | No | One of `wrong word`, `skipped word`, `added word`, `mispronounced letter`, `Tajweed` | — | FR-14, BR-01 |
| `rule_id` | `SMALLINT` | FK | Yes | Present exactly for `Tajweed` | `tajweed_rule(rule_id)`; RESTRICT | FR-14, BR-01 |
| `penalty` | `NUMERIC(2,1)` | — | No | `0.5` for `Tajweed`; `1.0` otherwise | — | BR-01, §8.1 |

†Composite session FK and ‡composite Word FK enforce that every Mistake references exactly one existing Word **in that session's Surah**. The `error_type`/`rule_id`/`penalty` condition is one table `CHECK`: `error_type = 'Tajweed' AND rule_id IS NOT NULL AND penalty = 0.5`, or `error_type IN ('wrong word', 'skipped word', 'added word', 'mispronounced letter') AND rule_id IS NULL AND penalty = 1.0`. An added word points to the **following expected Word**, not to a nonexistent extra word. Multiple detected errors may reference one Word; the finalizer groups by `(session_id, surah_number, verse_number, word_position)` and adds `LEAST(1, SUM(penalty))` once per Word. It rejects mistakes on unanalysed words and ensures aggregate effective errors do not exceed counted words. These are cross-row/session checks, not per-row `CHECK` constraints.

### 10. `quran_class`

| Column | PostgreSQL type | Key | NULL? | Default / allowed values / check | FK target; delete | Rule |
|---|---|---|---|---|---|---|
| `class_id` | `UUID` | PK, UQ* | No | Service-generated UUIDv4 | — | FR-24, §8.1 |
| `teacher_id` | `UUID` | FK, UQ* | No | Teacher role required | `account(account_id)`; CASCADE | FR-24, FR-28 |
| `name` | `TEXT` | — | No | Nonblank after trimming; **not unique** | — | FR-24 |
| `join_code` | `TEXT` | UQ | No | Nonblank; generated at creation; immutable | — | BR-10, §8.1 |
| `created_at` | `TIMESTAMPTZ` | — | No | Default `CURRENT_TIMESTAMP` | — | §8.1 |

*Add supporting `UNIQUE (class_id, teacher_id)` for Message ownership. The service creates codes with retry on the unique violation; the exact format is IS499 item O-7. Reject updates to `join_code` and `teacher_id` in the database or restrict writes to an immutable path. A Teacher can rename `name`; cannot delete one class or close it. Teacher account deletion cascades through the class, releasing its code.

### 11. `enrolment`

| Column | PostgreSQL type | Key | NULL? | Default / allowed values / check | FK target; delete | Rule |
|---|---|---|---|---|---|---|
| `enrolment_id` | `UUID` | PK | No | Service-generated UUIDv4 | — | BR-09, §8.1 |
| `class_id` | `UUID` | FK | No | — | `quran_class(class_id)`; CASCADE | FR-24, FR-28 |
| `reader_id` | `UUID` | FK | No | Reader role required | `account(account_id)`; CASCADE | FR-24, FR-28 |
| `joined_at` | `TIMESTAMPTZ` | — | No | Default `CURRENT_TIMESTAMP`; immutable | — | BR-08, BR-09 |
| `left_at` | `TIMESTAMPTZ` | — | Yes | NULL while active; if set, `left_at >= joined_at` | — | BR-09, §8.1 |
| `status` | `TEXT` | — | No | `active` or `ended`; no default, set on insert | — | BR-09, §9 |
| `end_reason` | `TEXT` | — | Yes | NULL while active; `left` or `consent withdrawn` when ended | — | FR-27, BR-09 |

Add a table check: `(status = 'active' AND left_at IS NULL AND end_reason IS NULL) OR (status = 'ended' AND left_at IS NOT NULL AND end_reason IS NOT NULL AND end_reason IN ('left', 'consent withdrawn') AND left_at >= joined_at)`. Add a **partial unique index** on `(class_id, reader_id) WHERE status = 'active'`. Historical ended rows remain, and rejoining inserts a new row with a new `joined_at`. Only transition active → ended; never reactivate or alter history. Joining checks a valid code and active teacher-sharing consent in one transaction; the unique index also protects concurrent joins. The service, not the Teacher, initiates join/leave. Teacher-sharing withdrawal ends all active enrolments atomically.

### 12. `message`

| Column | PostgreSQL type | Key | NULL? | Default / allowed values / check | FK target; delete | Rule |
|---|---|---|---|---|---|---|
| `message_id` | `UUID` | PK | No | Service-generated UUIDv4 | — | FR-25, §8.1 |
| `teacher_id` | `UUID` | FK† | No | Teacher role required | With `class_id` → `quran_class(class_id, teacher_id)`; CASCADE | FR-25, BR-12 |
| `class_id` | `UUID` | FK† | No | Must be owned by `teacher_id` | With `teacher_id` → `quran_class(class_id, teacher_id)`; CASCADE | FR-25, BR-12 |
| `audience` | `TEXT` | — | No | `CHECK (audience IN ('one reader', 'whole class'))` | — | FR-25, §8.1 |
| `message_text` | `TEXT` | — | No | Nonblank after trimming | — | FR-25, §8.1 |
| `sent_at` | `TIMESTAMPTZ` | — | No | Set to the send transaction's timestamp | — | BR-12, §8.1 |

†One composite FK proves Teacher ownership of Class; the Class FK's cascade also deletes sent messages on Teacher deletion. There is no reply table or reverse sender role. Each committed Message needs at least one `message_recipient`; enforce with a deferred constraint trigger or make all Message writes go through a transaction that verifies recipient count before commit. A single-recipient send requires exactly one recipient; a whole-class send requires every Reader actively enrolled in that Class at send time, and at least one. Lock the relevant Class/enrolment rows or serialize send against join/leave so the snapshot and `sent_at` agree; refuse empty class and invalid single recipient without storing a Message. After delivery, recipients remain even if they leave the class.

### 13. `message_recipient`

| Column | PostgreSQL type | Key | NULL? | Default / allowed values / check | FK target; delete | Rule |
|---|---|---|---|---|---|---|
| `message_id` | `UUID` | PK, FK | No | — | `message(message_id)`; CASCADE | FR-25, BR-12–BR-13 |
| `reader_id` | `UUID` | PK, FK | No | Reader role required | `account(account_id)`; CASCADE | FR-25, BR-12–BR-13 |
| `read_at` | `TIMESTAMPTZ` | — | Yes | Default NULL = unread; when set, `read_at >= message.sent_at`; set once | — | FR-25, BR-13 |

PK `(message_id, reader_id)` prevents duplicate delivery. Check Reader role and active enrolment in the Message's Class **at delivery**, not on later reads; a trigger or the trusted sending transaction is needed because FKs cannot test this temporal condition. Opening a message sets `read_at` once; that transaction also checks it is not before `message.sent_at`. Both inbox and sent views read the same recipient row; unread badge counts rows with `read_at IS NULL`. On Reader deletion, cascade removes their recipient rows; delete a Message in the same deletion transaction if it now has **zero** recipients, so the minimum-one-recipient invariant survives. Other recipients keep their delivered copies. A message from a deleted Teacher disappears because its Class and Message are deleted.

### 14. `deletion_log`

| Column | PostgreSQL type | Key | NULL? | Default / allowed values / check | FK target; delete | Rule |
|---|---|---|---|---|---|---|
| `log_id` | `UUID` | PK | No | Fresh random UUIDv4, unrelated to deleted account | — | FR-28, §8.1 |
| `account_type` | `TEXT` | — | No | `CHECK (account_type IN ('Reader', 'Teacher'))` | — | FR-28, BR-17 |
| `deleted_at` | `TIMESTAMPTZ` | — | No | Default `CURRENT_TIMESTAMP` | — | FR-28, BR-17 |

There is **no FK to `account`** and no account ID, identity subject, name, email, join code or other recoverable identifier. Restrict access to this log; its random ID is only the log entry's own key.

## Transaction and access rules

**Role integrity.** `account_type` is fixed. PostgreSQL directly enforces its two allowed values and FKs; it cannot make an FK conditional on a parent's role without extra columns. Use role-check triggers on `teacher_detail`, `consent_record`, `recitation_session`, `quran_class`, `enrolment`, `message_recipient`, and the Message's teacher through its Class. Keep Teacher/detail creation together and validate the mandatory detail with a deferred trigger. If the implementation chooses service checks instead, revoke direct table writes from all other roles and keep the same checks inside serialized transactions. Role rules are not implied by FK existence alone.

**Teacher visibility (FR-23, BR-08).** For the authenticated Teacher, select their Classes joined to **active** Enrolments; group by Reader and take `MIN(joined_at)` across all of that Teacher's currently active classes. Show that Reader's sessions only where `session.reader_id = reader_id AND session.ended_at >= min_joined_at`. Drill-down starts with a Class currently owned by that Teacher and a Reader currently active in that Class, then applies the teacher-wide minimum join date. Recheck this predicate in the data layer on **every** class, reader, session and mistake read, ideally in one database statement/snapshot; revoke access immediately when the last active enrolment ends. Do not expose earlier sessions or other Teachers' data. FKs do not provide authorization.

**Session finalization (FR-19–FR-20, BR-01–BR-05, BR-18).** Keep capture/analysis transient. On every ending, including interruption, write the ended session and its Mistakes in one transaction. Count only reached words in reliably analysed verses; do not turn analysis failures into Mistakes. For each distinct expected Word, cap the sum of penalties at 1 before summing effective errors. Check all Mistakes target counted words, compute the one-decimal score, and set `whole_surah_analysed` only when every verse was analysed. Persist no active-state row. Zero counted words gives zero effective errors and NULL score. Readers may open their own ended history; teachers see only the filtered subset above.

**Deletion (FR-28, BR-17).** Reader deletion in one database transaction removes `account` and cascades its consent records, sessions and their Mistakes, enrolments and received `message_recipient` rows; remove any now-recipientless Messages and insert exactly one anonymous `deletion_log` row. Teacher deletion cascades its `teacher_detail`, Classes and join codes, all those Classes' enrolments and Messages/recipient rows; Readers' own sessions stay. Delete the corresponding identity-provider account as part of the account-deletion workflow, handling provider/database failure so a supposedly deleted account cannot still sign in or leave protected data visible. The external identity provider is outside PostgreSQL; the database transaction alone cannot make that cross-system action atomic. Do not retain an account identifier in the deletion log.

## Derived values and storage boundary

| Derived value | Source and exact rule |
|---|---|
| Best score per Surah | Maximum non-NULL `mastery_score` over a Reader's ended sessions for that Surah (FR-21, BR-04). |
| Full mastery count | Count distinct Surahs having **one** ended session with `whole_surah_analysed = TRUE` and `mastery_score >= 90.0`; do not combine partial sessions (BR-03). |
| Average mastery | Arithmetic mean of the best non-NULL score for each practised Surah; no scored Surahs gives no average (BR-04). |
| Practice streak | Distinct device-local calendar dates of ended sessions with non-NULL score, any end reason; count consecutive days ending today or yesterday, otherwise 0 (BR-06). |
| Teacher dashboard | For active Readers in the Teacher's Classes, apply the BR-08 visibility threshold **before** session count, last practice date, full-mastery count and average; then show the filtered sessions and their Mistakes (FR-23, BR-08). |

These are queries over stored sessions and active enrolments, not new tables or persisted snapshots. Surah, Verse, Word and Tajweed rule are read-only database reference data; Quran text is also bundled in the app for offline reading, and reference audio is **only** bundled in the app.

**Open interpretation limit.** BR-06 says practice days use the device's local calendar, but §8.1 stores only `ended_at`, no device time zone or offset. A current device time zone can be applied at query time; if a Reader changes time zones, that can shift a past session to a different day. Reproducing the device-local date **as it was when each session ended** would require a new stored time-zone/offset field or an explicit product decision. This schema does not invent one. This does not affect the stored Mastery Score.

## Coverage and consistency checks

### Requirements §8.1 — stored fields

| Group | Required fields covered | Result |
|---|---|---|
| Account | ID, subject, type, display name, email, language, creation | `account` ✓ |
| Teacher detail | account link, school name | `teacher_detail` ✓ |
| Consent | ID, Reader, purpose, grant, optional withdrawal | `consent_record` ✓ |
| Surah | number, Arabic/English names, verse count | `surah` ✓ |
| Verse | Surah, number, two text forms | `verse` ✓ |
| Word | Verse, position, text, audio start/end | `word` ✓ |
| Tajweed rule | ID, name | `tajweed_rule` ✓ |
| Session | ID, Reader, Surah, mode, times, reason, counts, score, whole Surah | `recitation_session` ✓ |
| Mistake | ID, session, exact expected Word FK, type, rule, penalty | `mistake` ✓ |
| Class | ID, Teacher, name, join code, created | `quran_class` ✓ |
| Enrolment | ID, Class, Reader, dates, status, reason | `enrolment` ✓ |
| Message | ID, Teacher, Class, audience, text, sent | `message` ✓ |
| Recipient | Message + Reader composite identity, read date | `message_recipient` ✓ |
| Deletion log | ID, account type, deletion date only | `deletion_log` ✓ |

### Requirements §8.2 — relationships

| Relationship | Implemented by | Result |
|---|---|---|
| Teacher account 1–1 detail | Shared PK/FK + deferred role/completeness check | ✓ |
| Reader 1–0..* consent and sessions | Reader FKs + role checks | ✓ |
| Surah 1–1..* Verse 1–1..* Word | Composite keys/FKs + complete reference-data seed validation | ✓ |
| Surah 1–0..* sessions | Session Surah FK | ✓ |
| Session 1–0..* Mistakes; Word 1–0..* Mistakes | Composite FKs tying Mistake to session Surah and Word | ✓ |
| Rule 0..1–0..* Mistakes | Nullable rule FK + conditional check | ✓ |
| Teacher 1–0..* Classes | Class Teacher FK + role check | ✓ |
| Class/Reader 1–0..* Enrolments | Both FKs + partial active uniqueness | ✓ |
| Teacher/Class 1–0..* Messages | Composite ownership FK | ✓ |
| Message 1–1..* recipients; Reader 1–0..* recipients | Composite recipient PK/FKs + send/deletion transaction check | ✓ |

### Conditional and lifecycle audit

| Case | Constraint / transaction outcome |
|---|---|
| Interrupted or zero-word session | Required ended reason, nonnegative counts, NULL score exactly when zero; history retained. |
| Repeated enrolment | Only one active Reader/Class row; ended history and fresh join timestamp retained. |
| Consent withdrawal/regrant | Partial unique active grant; old row is dated and new row is inserted; teacher-sharing withdrawal ends all enrolments. |
| Class and read status | Ownership FK, enrolled recipient snapshot, nonempty delivery, immutable delivered recipients, nullable read date. |
| Both deletion paths | Cascades plus recipientless-message cleanup; only anonymous log remains; identity-provider removal required. |
| FR-23–FR-28 and BR-01–BR-17 | Mapped in column `Rule` cells and transaction/access rules above; BR-06 historical time-zone ambiguity is flagged. |
| §8.3 exclusions | No recorded audio/segments, phonemes/raw analysis, feedback/praise text, audio-assistance requests, prompting/pause events, voiceprints, location, unnecessary device IDs, age, gender, phone; no assignments, challenges, rewards or performance snapshots. |

The ERD and finalized requirements have no conflicting stored fields or relationships. The ERD's `ACCOUNT ||--o| TEACHER_DETAIL` notation needs its stated conditional interpretation: **exactly one for Teachers, zero for Readers**. PostgreSQL's FK alone cannot enforce that minimum. The historical schema and ERD are not sources for this design.
