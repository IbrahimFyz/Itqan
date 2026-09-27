# Itqan ERD Deliverables Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a large, specific, report-ready ERD, relational schema, and functional-requirements traceability package for Itqan.

**Architecture:** Use one Mermaid crow's-foot source as the canonical diagram, render it to SVG for report use, and keep detailed relational constraints in a companion Markdown schema. A separate traceability matrix maps FR-01 through FR-25 to the data model while distinguishing behavior-only requirements and proposed entities.

**Tech Stack:** Mermaid ER diagram syntax, SVG, Markdown, Git, and the ephemeral `@mermaid-js/mermaid-cli` renderer invoked through `npx`.

**Spec:** `docs/superpowers/specs/2026-09-19-erd-design.md`

## Global Constraints

- Model the standalone Itqan application and Juz Amma only.
- Include learner and teacher roles; do not introduce an Admin role.
- Use all entity, attribute, type, key, and constraint names defined in the approved spec.
- Store audio metadata and a storage URI, not audio bytes.
- Store mastery outputs and formula versions without inventing mastery weights.
- Mark assignments, performance snapshots, and Al-Mushajji gamification as proposed.
- Keep exact AI technology choices outside the ERD; model traceability fields only.
- Use logical account deletion and explicit audio-retention metadata.

---

### Task 1: Canonical Mermaid ERD

**Files:**
- Create: `docs/database/itqan-erd.mmd`

**Interfaces:**
- Consumes: all 29 entity definitions and cardinalities from `docs/superpowers/specs/2026-09-19-erd-design.md`
- Produces: a valid Mermaid `erDiagram` source consumed by the SVG renderer and relational-schema documentation

- [ ] **Step 1: Create the Mermaid ERD header and entity groups**

Use Mermaid front matter and comments to separate the seven domains while retaining one valid `erDiagram`:

```mermaid
---
title: Itqan Complete Entity Relationship Diagram
config:
  theme: neutral
  layout: elk
---
erDiagram
    %% CONFIRMED: Identity and access
    %% CONFIRMED: Quran content and Tajweed reference data
    %% CONFIRMED: AI modes and recitation sessions
    %% CONFIRMED: Error detection and feedback
    %% CONFIRMED: Progress and practice history
    %% CONFIRMED: Teacher, class, and communication functions
    %% PROPOSED: Assignments, dashboard cache, and Al-Mushajji gamification
```

- [ ] **Step 2: Add every entity with exact key annotations**

Add these 29 entities and no Admin entity:

```text
USER, ROLE, USER_ROLE, LEARNER_PROFILE, TEACHER_PROFILE,
JUZ, SURAH, VERSE, VERSE_WORD, TAJWEED_RULE,
AI_MODE, RECITATION_SESSION, AUDIO_RECORDING, RECITATION_SEGMENT,
RECITATION_ANALYSIS, PAUSE_EVENT, ERROR_TYPE, RECITATION_ERROR,
ERROR_FEEDBACK, AUDIO_ASSISTANCE, LEARNER_SURAH_PROGRESS,
MASTERY_SCORE_HISTORY, DAILY_PRACTICE, PRACTICE_STREAK,
CLASS, CLASS_ENROLLMENT, CLASS_ASSIGNMENT, ASSIGNMENT_PROGRESS,
TEACHER_MESSAGE, STUDENT_PERFORMANCE_SNAPSHOT, CHALLENGE,
LEARNER_CHALLENGE, REWARD, LEARNER_REWARD
```

The approved spec actually defines 34 named tables; use all 34. Correct the spec's “29 entities” summary wording during Task 4 rather than dropping any table. For each Mermaid attribute, append `PK`, `FK`, or `UK` where applicable and add a concise quoted note only when it explains a non-obvious constraint.

- [ ] **Step 3: Add all crow's-foot relationships**

Encode these exact relationships:

```text
USER ||--o{ USER_ROLE : has
ROLE ||--o{ USER_ROLE : assigns
USER ||--o| LEARNER_PROFILE : extends
USER ||--o| TEACHER_PROFILE : extends
JUZ ||--|{ SURAH : contains
SURAH ||--|{ VERSE : contains
VERSE ||--|{ VERSE_WORD : contains
TAJWEED_RULE o|--o{ ERROR_TYPE : classifies
LEARNER_PROFILE ||--o{ RECITATION_SESSION : performs
SURAH ||--o{ RECITATION_SESSION : selected_for
AI_MODE ||--o{ RECITATION_SESSION : configures
RECITATION_SESSION ||--o| AUDIO_RECORDING : records
RECITATION_SESSION ||--o{ RECITATION_SEGMENT : contains
VERSE ||--o{ RECITATION_SEGMENT : recited_as
RECITATION_SEGMENT ||--o| RECITATION_ANALYSIS : analyzed_by
RECITATION_SESSION ||--o{ PAUSE_EVENT : detects
RECITATION_SEGMENT o|--o{ PAUSE_EVENT : locates
RECITATION_ANALYSIS ||--o{ RECITATION_ERROR : identifies
ERROR_TYPE ||--o{ RECITATION_ERROR : categorizes
VERSE_WORD o|--o{ RECITATION_ERROR : locates
RECITATION_ERROR ||--o{ ERROR_FEEDBACK : receives
RECITATION_ERROR o|--o{ AUDIO_ASSISTANCE : triggers
PAUSE_EVENT o|--o{ AUDIO_ASSISTANCE : triggers
VERSE ||--o{ AUDIO_ASSISTANCE : supplies
LEARNER_PROFILE ||--o{ LEARNER_SURAH_PROGRESS : tracks
SURAH ||--o{ LEARNER_SURAH_PROGRESS : summarizes
LEARNER_PROFILE ||--o{ MASTERY_SCORE_HISTORY : earns
SURAH ||--o{ MASTERY_SCORE_HISTORY : measures
RECITATION_SESSION ||--o| MASTERY_SCORE_HISTORY : produces
LEARNER_PROFILE ||--o{ DAILY_PRACTICE : logs
LEARNER_PROFILE ||--o| PRACTICE_STREAK : maintains
TEACHER_PROFILE ||--o{ CLASS : owns
CLASS ||--o{ CLASS_ENROLLMENT : has
LEARNER_PROFILE ||--o{ CLASS_ENROLLMENT : joins
CLASS ||--o{ CLASS_ASSIGNMENT : receives
SURAH ||--o{ CLASS_ASSIGNMENT : targets
TEACHER_PROFILE ||--o{ CLASS_ASSIGNMENT : creates
CLASS_ASSIGNMENT ||--o{ ASSIGNMENT_PROGRESS : tracks
LEARNER_PROFILE ||--o{ ASSIGNMENT_PROGRESS : completes
RECITATION_SESSION o|--o{ ASSIGNMENT_PROGRESS : evidences
TEACHER_PROFILE ||--o{ TEACHER_MESSAGE : sends
LEARNER_PROFILE ||--o{ TEACHER_MESSAGE : receives
CLASS o|--o{ TEACHER_MESSAGE : contextualizes
RECITATION_SESSION o|--o{ TEACHER_MESSAGE : references
CLASS ||--o{ STUDENT_PERFORMANCE_SNAPSHOT : summarizes
LEARNER_PROFILE ||--o{ STUDENT_PERFORMANCE_SNAPSHOT : measured_in
LEARNER_PROFILE ||--o{ LEARNER_CHALLENGE : joins
CHALLENGE ||--o{ LEARNER_CHALLENGE : enrolls
LEARNER_PROFILE ||--o{ LEARNER_REWARD : earns
REWARD ||--o{ LEARNER_REWARD : awards
CHALLENGE o|--o{ LEARNER_REWARD : produces
```

- [ ] **Step 4: Run structural checks**

Run:

```bash
test "$(rg -c '^    [A-Z_]+ \{' docs/database/itqan-erd.mmd)" -eq 34
! rg -n '\bADMIN\b' docs/database/itqan-erd.mmd
for id in USER RECITATION_SESSION RECITATION_ERROR LEARNER_SURAH_PROGRESS CLASS CHALLENGE; do rg -q "^    ${id} \{" docs/database/itqan-erd.mmd; done
git diff --check
```

Expected: every command exits successfully and the entity count is 34.

- [ ] **Step 5: Commit the canonical ERD source**

```bash
git add docs/database/itqan-erd.mmd
git commit -m "docs: add complete Itqan ERD source"
```

---

### Task 2: Relational Schema and Integrity Rules

**Files:**
- Create: `docs/database/RELATIONAL_SCHEMA.md`

**Interfaces:**
- Consumes: table and relationship names from `docs/database/itqan-erd.mmd`
- Produces: implementation-neutral PostgreSQL-oriented definitions for all 34 tables

- [ ] **Step 1: Document notation and cross-cutting rules**

State that `PK` means primary key, `FK` means foreign key, `UK` means unique key, nullable columns are explicitly labeled, timestamps use UTC-aware `TIMESTAMPTZ`, scores use 0–100, confidence uses 0–1, and generated/user records use UUIDs.

- [ ] **Step 2: Add the 34 table definitions**

For each table, copy the approved attributes and types from spec sections 3.1–3.7. Use this exact format:

```markdown
### RECITATION_SESSION

`RECITATION_SESSION(session_id PK, learner_id FK→LEARNER_PROFILE.learner_id, surah_id FK→SURAH.surah_id, ai_mode_id FK→AI_MODE.ai_mode_id, started_at, ended_at NULL, session_status, completion_percentage, mastery_score NULL, total_duration_seconds NULL, total_pause_count, error_count, failure_reason NULL)`

Purpose: Stores one learner attempt for one Surah in one selected AI mode.

Constraints:
- `completion_percentage` and `mastery_score` are between 0 and 100.
- `total_duration_seconds`, `total_pause_count`, and `error_count` are non-negative.
- Completed sessions require `ended_at`; active sessions do not have `ended_at`.
```

Do not shorten a definition by referring to another table's section.

- [ ] **Step 3: Add deletion, privacy, and authorization rules**

Document restrictive deletion for Quran reference data, logical deletion for users, audio URI clearing on retention expiry, conditional cascade for privacy purges, and class-enrollment authorization for teacher access.

- [ ] **Step 4: Check schema coverage**

Run:

```bash
for table in $(sed -n 's/^    \([A-Z_]*\) {$/\1/p' docs/database/itqan-erd.mmd); do rg -q "^### ${table}$" docs/database/RELATIONAL_SCHEMA.md || { echo "Missing ${table}"; exit 1; }; done
git diff --check
```

Expected: no missing-table output and exit status 0.

- [ ] **Step 5: Commit the relational schema**

```bash
git add docs/database/RELATIONAL_SCHEMA.md
git commit -m "docs: add detailed relational schema"
```

---

### Task 3: Requirements Traceability

**Files:**
- Create: `docs/database/ERD_REQUIREMENTS_TRACEABILITY.md`

**Interfaces:**
- Consumes: FR-01–FR-25 from `docs/project/REQUIREMENTS.md` and all 34 ERD entities
- Produces: a complete mapping showing what the database supports and what remains application behavior

- [ ] **Step 1: Create one mapping row for every functional requirement**

Use columns `Requirement`, `Requirement name`, `Supporting entities`, `Stored evidence`, and `Notes/status`. At minimum, map:

```text
FR-01–FR-03 → USER, ROLE, USER_ROLE, LEARNER_PROFILE, TEACHER_PROFILE
FR-04–FR-06 → JUZ, SURAH, VERSE, VERSE_WORD
FR-07–FR-10 → AI_MODE, RECITATION_SESSION, CLASS, CLASS_ENROLLMENT
FR-11–FR-19 → RECITATION_SESSION, AUDIO_RECORDING, RECITATION_SEGMENT,
               RECITATION_ANALYSIS, PAUSE_EVENT, RECITATION_ERROR,
               ERROR_TYPE, ERROR_FEEDBACK, AUDIO_ASSISTANCE
FR-20–FR-22 → RECITATION_SESSION, LEARNER_SURAH_PROGRESS,
               MASTERY_SCORE_HISTORY, DAILY_PRACTICE, PRACTICE_STREAK
FR-23 → CLASS, CLASS_ENROLLMENT, LEARNER_SURAH_PROGRESS,
        STUDENT_PERFORMANCE_SNAPSHOT
FR-24 → CLASS, CLASS_ENROLLMENT, CLASS_ASSIGNMENT, ASSIGNMENT_PROGRESS
FR-25 → TEACHER_MESSAGE
```

Mark browsing, display, session control, analysis execution, and sending messages as behaviors supported by stored data—not behaviors implemented by the database itself.

- [ ] **Step 2: Add an entity-to-requirement reverse index**

List all 34 entities and their related FR identifiers. Mark Quran reference and analysis-detail tables as enabling/supporting entities when no requirement names the storage structure directly.

- [ ] **Step 3: Verify all FR identifiers and all entities appear**

Run:

```bash
for n in $(seq -w 1 25); do rg -q "FR-${n}" docs/database/ERD_REQUIREMENTS_TRACEABILITY.md || { echo "Missing FR-${n}"; exit 1; }; done
for table in $(sed -n 's/^    \([A-Z_]*\) {$/\1/p' docs/database/itqan-erd.mmd); do rg -q "\b${table}\b" docs/database/ERD_REQUIREMENTS_TRACEABILITY.md || { echo "Missing ${table}"; exit 1; }; done
git diff --check
```

Expected: no missing-requirement or missing-entity output and exit status 0.

- [ ] **Step 4: Commit the traceability document**

```bash
git add docs/database/ERD_REQUIREMENTS_TRACEABILITY.md
git commit -m "docs: trace requirements to ERD entities"
```

---

### Task 4: Render, Visually Verify, and Correct the Design Summary

**Files:**
- Create: `docs/database/itqan-erd.svg`
- Modify: `docs/superpowers/specs/2026-09-19-erd-design.md`

**Interfaces:**
- Consumes: `docs/database/itqan-erd.mmd`
- Produces: report-ready SVG and a corrected spec summary

- [ ] **Step 1: Correct the entity-count wording in the approved spec**

Replace “29 entities” with “34 entities.” Do not alter the approved entity definitions or scope.

- [ ] **Step 2: Render the Mermaid ERD**

Run:

```bash
npx -y @mermaid-js/mermaid-cli -i docs/database/itqan-erd.mmd -o docs/database/itqan-erd.svg -b white -w 4800 -H 3200
```

Expected: exit status 0 and a non-empty SVG containing the title `Itqan Complete Entity Relationship Diagram`.

- [ ] **Step 3: Verify the rendered artifact structurally**

Run:

```bash
test -s docs/database/itqan-erd.svg
rg -q 'Itqan Complete Entity Relationship Diagram' docs/database/itqan-erd.svg
test "$(rg -c '^    [A-Z_]+ \{' docs/database/itqan-erd.mmd)" -eq 34
git diff --check
```

Expected: all commands exit successfully.

- [ ] **Step 4: Visually inspect the SVG**

Open `docs/database/itqan-erd.svg` and confirm:

- all entity boxes render without clipped fields;
- relationship labels and cardinalities are legible;
- confirmed and proposed sections can be identified from comments/documentation;
- the diagram has no overlapping boxes or disconnected relationship lines;
- the canvas remains readable when inserted as a landscape report figure.

If one full diagram is too dense at report scale, retain it as the canonical ERD and additionally render domain-level crops without changing the source model.

- [ ] **Step 5: Run final repository checks**

```bash
git status --short
git log --oneline -5
for n in $(seq -w 1 25); do rg -q "FR-${n}" docs/database/ERD_REQUIREMENTS_TRACEABILITY.md || exit 1; done
for table in $(sed -n 's/^    \([A-Z_]*\) {$/\1/p' docs/database/itqan-erd.mmd); do rg -q "^### ${table}$" docs/database/RELATIONAL_SCHEMA.md || exit 1; done
```

Expected: only the SVG and corrected spec are uncommitted before the final commit; all coverage checks exit successfully.

- [ ] **Step 6: Commit the rendered deliverable and correction**

```bash
git add docs/database/itqan-erd.svg docs/superpowers/specs/2026-09-19-erd-design.md
git commit -m "docs: render and verify complete Itqan ERD"
```
