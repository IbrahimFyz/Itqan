# Itqan Class Diagram Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a complete, implementation-neutral UML class-diagram package that adds behavior and architectural boundaries to the merged Itqan ERD.

**Architecture:** One canonical Mermaid `classDiagram` defines all domain classes, services, repositories, external ports, enumerations, methods, multiplicities, and dependencies. Four smaller diagrams repeat subsets of that model for report readability; a permanent shell verification checks rendering, required classes, forbidden Admin/framework classes, proposed labels, and ERD consistency.

**Tech Stack:** Mermaid class-diagram syntax, SVG, Markdown, POSIX shell, Git, and ephemeral `@mermaid-js/mermaid-cli` through `npx`.

**Spec:** `docs/superpowers/specs/2026-09-19-class-diagram-design.md`

## Global Constraints

- Remain implementation-neutral: no Flutter, FastAPI, ORM, HTTP controller, PostgreSQL driver, or named AI-model classes.
- Preserve all 34 persisted ERD entities using PascalCase names; `LEARNING_CLASS` maps to `LearningClass`.
- Include the 10 services, 6 repository interfaces, 3 external ports, value objects, and enumerations defined in the specification.
- Model one user with optional learner and teacher profiles; do not use learner/teacher inheritance.
- Do not add an Admin class, actor, service, repository, or enumeration value.
- Mark assignments, performance snapshots, challenges, rewards, and their related service/repository elements as proposed.
- Show multiplicities for domain relationships and distinguish composition, aggregation, association, inheritance, and dependency.
- Store no new persisted class that is absent from the merged ERD.
- Render SVGs from committed Mermaid sources; do not hand-edit generated SVGs.

## Review Focus

- A user holding both learner and teacher roles must remain valid; verification rejects `User <|-- Learner` and `User <|-- Teacher` inheritance.
- Proposed functionality must not appear confirmed; verification requires `proposed` markers for assignment, snapshot, challenge, and reward classes.
- The UML must not drift from the ERD; verification checks every ERD entity has a PascalCase class in the complete diagram.
- Framework choices must remain unresolved; verification rejects Flutter, FastAPI, SQLAlchemy, ORM, and HTTP controller names.
- The diagram must be usable as an artifact; verification renders all five Mermaid sources and checks every SVG is non-empty.

---

### Task 1: Canonical Complete Class Diagram

**Files:**
- Create: `docs/diagrams/class/itqan-class-diagram.mmd`
- Create: `tests/verify_class_diagrams.sh`

**Interfaces:**
- Consumes: exact class definitions and relationships in the approved specification and persisted entity names from `docs/database/itqan-erd.mmd`
- Produces: authoritative UML source used by every detailed view and all consistency checks

- [ ] **Step 1: Write the failing verification script**

Create an executable POSIX shell script with these checks:

```sh
#!/bin/sh
set -eu

diagram_dir="docs/diagrams/class"
complete="$diagram_dir/itqan-class-diagram.mmd"

test -f "$complete"

for name in User Role UserRole LearnerProfile TeacherProfile Juz Surah Verse VerseWord TajweedRule AIMode RecitationSession AudioRecording RecitationSegment RecitationAnalysis PauseEvent ErrorType RecitationError ErrorFeedback AudioAssistance LearnerSurahProgress MasteryScoreHistory DailyPractice PracticeStreak LearningClass ClassEnrollment ClassAssignment AssignmentProgress TeacherMessage StudentPerformanceSnapshot Challenge LearnerChallenge Reward LearnerReward; do
  rg -q "class $name([ {]|$)" "$complete" || { echo "Missing class: $name"; exit 1; }
done

for name in AuthenticationService QuranCatalogService RecitationService AnalysisService FeedbackService ProgressService ClassService TeacherMonitoringService MessagingService GamificationService UserRepository QuranRepository RecitationRepository ProgressRepository ClassRepository GamificationRepository AudioCapturePort AudioStoragePort AIAnalysisPort; do
  rg -q "class $name([ {]|$)" "$complete" || { echo "Missing boundary: $name"; exit 1; }
done

! rg -ni '\bAdmin\b|Flutter|FastAPI|SQLAlchemy|ORM|HttpController' "$diagram_dir"/*.mmd
! rg -n 'User[[:space:]]+<\|--[[:space:]]+(Learner|Teacher)' "$complete"

for name in ClassAssignment AssignmentProgress StudentPerformanceSnapshot Challenge LearnerChallenge Reward LearnerReward GamificationService GamificationRepository; do
  rg -A4 "class $name" "$complete" | rg -qi 'proposed' || { echo "Missing proposed marker: $name"; exit 1; }
done

for source in "$diagram_dir"/*.mmd; do
  output="/tmp/$(basename "${source%.mmd}").svg"
  npx -y @mermaid-js/mermaid-cli -i "$source" -o "$output" -b white
  test -s "$output"
done
```

- [ ] **Step 2: Run verification and confirm the expected failure**

Run: `sh tests/verify_class_diagrams.sh`

Expected: failure at `test -f docs/diagrams/class/itqan-class-diagram.mmd`.

- [ ] **Step 3: Create the canonical Mermaid source**

Create `classDiagram` declarations for these exact groups:

```text
Entities (34): User, Role, UserRole, LearnerProfile, TeacherProfile,
Juz, Surah, Verse, VerseWord, TajweedRule, AIMode, RecitationSession,
AudioRecording, RecitationSegment, RecitationAnalysis, PauseEvent,
ErrorType, RecitationError, ErrorFeedback, AudioAssistance,
LearnerSurahProgress, MasteryScoreHistory, DailyPractice, PracticeStreak,
LearningClass, ClassEnrollment, ClassAssignment, AssignmentProgress,
TeacherMessage, StudentPerformanceSnapshot, Challenge, LearnerChallenge,
Reward, LearnerReward.

Services (10): AuthenticationService, QuranCatalogService,
RecitationService, AnalysisService, FeedbackService, ProgressService,
ClassService, TeacherMonitoringService, MessagingService,
GamificationService.

Repositories (6): UserRepository, QuranRepository, RecitationRepository,
ProgressRepository, ClassRepository, GamificationRepository.

External ports (3): AudioCapturePort, AudioStoragePort, AIAnalysisPort.

Transport values: AudioData, AnalysisResult.
```

For every class, copy the exact attributes and methods from spec sections 5–14. Mark service, repository, external, value-object, entity, enumeration, and proposed stereotypes in the class body.

- [ ] **Step 4: Add the exact domain relationships**

Use the relationships from spec section 15, including:

```mermaid
User "1" *-- "0..1" LearnerProfile
User "1" *-- "0..1" TeacherProfile
User "1" -- "0..*" UserRole
Role "1" -- "0..*" UserRole
Juz "1" *-- "1..*" Surah
Surah "1" *-- "1..*" Verse
Verse "1" *-- "1..*" VerseWord
LearnerProfile "1" -- "0..*" RecitationSession
RecitationSession "1" *-- "0..1" AudioRecording
RecitationSession "1" *-- "0..*" RecitationSegment
RecitationSession "1" *-- "0..*" PauseEvent
RecitationSegment "1" *-- "0..1" RecitationAnalysis
RecitationAnalysis "1" *-- "0..*" RecitationError
RecitationError "1" *-- "0..*" ErrorFeedback
TeacherProfile "1" -- "0..*" LearningClass
LearningClass "1" *-- "0..*" ClassEnrollment
LearningClass "1" *-- "0..*" ClassAssignment
ClassAssignment "1" *-- "0..*" AssignmentProgress
```

Add every remaining association in spec section 15 with multiplicities.

- [ ] **Step 5: Add service dependencies**

Use dependency arrows (`..>`) from each service to the repositories, external ports, and aggregate roots named in spec section 12. Entities must never depend on services.

- [ ] **Step 6: Run focused canonical checks**

Run:

```bash
rg -c '^class ' docs/diagrams/class/itqan-class-diagram.mmd
npx -y @mermaid-js/mermaid-cli -i docs/diagrams/class/itqan-class-diagram.mmd -o /tmp/itqan-class-diagram.svg -b white -w 5600 -H 3600
test -s /tmp/itqan-class-diagram.svg
git diff --check
```

Expected: at least 55 class declarations, successful render, non-empty SVG, and no whitespace errors.

- [ ] **Step 7: Commit the canonical source and verification**

```bash
chmod +x tests/verify_class_diagrams.sh
git add docs/diagrams/class/itqan-class-diagram.mmd tests/verify_class_diagrams.sh
git commit -m "docs: add complete Itqan class diagram source"
```

---

### Task 2: Readable Domain Views

**Files:**
- Create: `docs/diagrams/class/identity-quran-classes.mmd`
- Create: `docs/diagrams/class/recitation-feedback-classes.mmd`
- Create: `docs/diagrams/class/progress-teacher-classes.mmd`
- Create: `docs/diagrams/class/gamification-classes-proposed.mmd`
- Modify: `tests/verify_class_diagrams.sh`

**Interfaces:**
- Consumes: class names, attributes, methods, stereotypes, and relationships from the canonical source
- Produces: four report-readable subsets that cannot contradict the authoritative diagram

- [ ] **Step 1: Extend verification with per-view ownership checks**

Add checks requiring:

```text
identity-quran: User, Role, UserRole, LearnerProfile, TeacherProfile,
                Juz, Surah, Verse, VerseWord, TajweedRule,
                AuthenticationService, QuranCatalogService
recitation-feedback: RecitationSession, AudioRecording, RecitationSegment,
                     RecitationAnalysis, PauseEvent, RecitationError,
                     ErrorFeedback, AudioAssistance, RecitationService,
                     AnalysisService, FeedbackService
progress-teacher: LearnerSurahProgress, MasteryScoreHistory, DailyPractice,
                  PracticeStreak, LearningClass, ClassEnrollment,
                  ClassAssignment, AssignmentProgress, TeacherMessage,
                  StudentPerformanceSnapshot, ProgressService, ClassService,
                  TeacherMonitoringService, MessagingService
gamification: Challenge, LearnerChallenge, Reward, LearnerReward,
              GamificationService, GamificationRepository
```

- [ ] **Step 2: Run verification and confirm missing-view failure**

Run: `sh tests/verify_class_diagrams.sh`

Expected: failure because the four view sources do not exist.

- [ ] **Step 3: Create the four view sources**

Copy the exact selected declarations and relationships from the canonical source. Include dependencies only when both endpoints appear in the view. Add a title front matter block to each source and do not invent view-only methods or relationships.

- [ ] **Step 4: Run complete source verification**

Run: `sh tests/verify_class_diagrams.sh`

Expected: all five Mermaid sources render and every required view class is found.

- [ ] **Step 5: Commit the detailed views**

```bash
git add docs/diagrams/class/*.mmd tests/verify_class_diagrams.sh
git commit -m "docs: add readable class diagram domain views"
```

---

### Task 3: Diagram Notes and ERD Consistency

**Files:**
- Create: `docs/diagrams/class/CLASS_DIAGRAM_NOTES.md`
- Modify: `tests/verify_class_diagrams.sh`

**Interfaces:**
- Consumes: canonical class model, merged ERD, and approved class-diagram specification
- Produces: reviewer guidance plus an automated ERD-to-UML entity check

- [ ] **Step 1: Add an ERD consistency check**

Extend the verification script to extract ERD entity names, convert the known snake-case names to PascalCase, and check them against the canonical diagram. Use an explicit mapping file inside the script for all 34 names so conversion is deterministic, including `AI_MODE → AIMode` and `LEARNING_CLASS → LearningClass`.

- [ ] **Step 2: Confirm the check detects a missing mapped class**

Temporarily run the mapping loop with `LearningClass` replaced by `MissingLearningClass` through standard input or a temporary copy.

Expected: `Missing UML class for ERD entity: LEARNING_CLASS` and non-zero exit. Do not edit the canonical source for this negative test.

- [ ] **Step 3: Write the diagram notes**

Document:

- how the class diagram differs from the ERD;
- why profiles replace learner/teacher inheritance;
- service, repository, and external-port responsibilities;
- confirmed versus proposed classes;
- how to read multiplicities and UML arrows;
- the two principal interaction flows from spec section 16;
- invalid states from spec section 17;
- the canonical-versus-domain-view rule;
- exact render and verification commands.

- [ ] **Step 4: Run verification**

Run: `sh tests/verify_class_diagrams.sh && git diff --check`

Expected: successful exit with five rendered temporary SVGs and no ERD mapping gaps.

- [ ] **Step 5: Commit notes and consistency checks**

```bash
git add docs/diagrams/class/CLASS_DIAGRAM_NOTES.md tests/verify_class_diagrams.sh
git commit -m "docs: document and verify class diagram consistency"
```

---

### Task 4: Rendered SVG Artifacts and Visual QA

**Files:**
- Create: `docs/diagrams/class/itqan-class-diagram.svg`
- Create: `docs/diagrams/class/identity-quran-classes.svg`
- Create: `docs/diagrams/class/recitation-feedback-classes.svg`
- Create: `docs/diagrams/class/progress-teacher-classes.svg`
- Create: `docs/diagrams/class/gamification-classes-proposed.svg`

**Interfaces:**
- Consumes: the five verified Mermaid sources
- Produces: GitHub- and report-ready SVGs

- [ ] **Step 1: Render all SVGs**

Run:

```bash
npx -y @mermaid-js/mermaid-cli -i docs/diagrams/class/itqan-class-diagram.mmd -o docs/diagrams/class/itqan-class-diagram.svg -b white -w 5600 -H 3600
npx -y @mermaid-js/mermaid-cli -i docs/diagrams/class/identity-quran-classes.mmd -o docs/diagrams/class/identity-quran-classes.svg -b white -w 3200 -H 2200
npx -y @mermaid-js/mermaid-cli -i docs/diagrams/class/recitation-feedback-classes.mmd -o docs/diagrams/class/recitation-feedback-classes.svg -b white -w 3600 -H 2600
npx -y @mermaid-js/mermaid-cli -i docs/diagrams/class/progress-teacher-classes.mmd -o docs/diagrams/class/progress-teacher-classes.svg -b white -w 3800 -H 2600
npx -y @mermaid-js/mermaid-cli -i docs/diagrams/class/gamification-classes-proposed.mmd -o docs/diagrams/class/gamification-classes-proposed.svg -b white -w 2400 -H 1800
```

- [ ] **Step 2: Verify rendered files**

Run:

```bash
for svg in docs/diagrams/class/*.svg; do test -s "$svg"; rg -q '<svg' "$svg"; done
sh tests/verify_class_diagrams.sh
git diff --check
```

Expected: five non-empty SVGs, valid SVG roots, five successful temporary renders, and no whitespace errors.

- [ ] **Step 3: Visually inspect every SVG**

Confirm that attributes and methods are not clipped, multiplicities are readable, dependency lines have distinguishable endpoints, proposed classes visibly include the proposed stereotype, and the detailed views fit landscape report pages. If the complete diagram is too dense at normal zoom, retain it as the authoritative poster-size artifact because the four domain views provide report readability.

- [ ] **Step 4: Commit rendered artifacts**

```bash
git add docs/diagrams/class/*.svg
git commit -m "docs: render and verify Itqan class diagrams"
```

- [ ] **Step 5: Final branch verification**

Run:

```bash
sh tests/verify_class_diagrams.sh
test -z "$(git status --porcelain -uall)"
git log --oneline -5
```

Expected: verification succeeds, worktree is clean, and the four implementation commits follow the specification commit.
