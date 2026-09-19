# Itqan Class Diagram Notes

## Purpose

The class diagram describes the static software design of Itqan: domain state, behavior, application services, persistence boundaries, and external audio/AI integrations. It is implementation-neutral because the final technology stack remains unresolved.

## Class diagram versus ERD

The ERD answers **what data is stored**. It shows tables, keys, attributes, and relational cardinalities. The class diagram answers **which objects collaborate and what they do**. It preserves all 34 persisted ERD entities and adds:

- domain methods and lifecycle rules;
- enumerations and value objects;
- application services that coordinate use cases;
- repository interfaces that isolate persistence;
- external ports for microphone capture, audio storage, and AI analysis.

Services, repositories, external ports, enumerations, and transport value objects are not additional database tables.

## Identity model

`LearnerProfile` and `TeacherProfile` are composed under `User`; they do not inherit from it. This matches the requirements and ERD because one account may hold both learner and teacher roles through `UserRole`. An inheritance model would incorrectly force those roles to be mutually exclusive.

No Admin role or class is included because the project has not approved one.

## Architectural responsibilities

### Domain classes

Entities contain state and enforce local invariants. Examples include session state transitions in `RecitationSession`, enrollment status in `ClassEnrollment`, and review state in `RecitationError`. Domain classes do not call storage, microphones, or AI providers directly.

### Application services

Services coordinate complete use cases:

- `AuthenticationService`: registration, login, and profile changes.
- `QuranCatalogService`: browsing Juz Amma and retrieving Quran content.
- `RecitationService`: recitation-session and audio-capture lifecycle.
- `AnalysisService`: AI analysis and supported Tajweed rules.
- `FeedbackService`: localized text and audio assistance.
- `ProgressService`: mastery, daily practice, and streak updates.
- `ClassService`: classes, enrollment, and proposed assignments.
- `TeacherMonitoringService`: authorized class and learner progress views.
- `MessagingService`: authorized teacher-to-learner messages.
- `GamificationService`: proposed challenge and reward workflows.

### Repository interfaces

Repositories define persistence operations for aggregate groups without selecting an ORM or database library: `UserRepository`, `QuranRepository`, `RecitationRepository`, `ProgressRepository`, `ClassRepository`, and the proposed `GamificationRepository`.

### External ports

- `AudioCapturePort` isolates the device microphone.
- `AudioStoragePort` isolates retained recording storage and deletion.
- `AIAnalysisPort` isolates speech/Tajweed analysis.

Concrete implementations are intentionally absent until the team approves the technology stack.

## Confirmed and proposed scope

The core identity, Quran, recitation, analysis, feedback, progress, class, enrollment, and messaging classes come from current requirements.

These elements remain **proposed** and are marked `<<proposed>>`:

- `ClassAssignment` and `AssignmentProgress`;
- `AssignmentData`, `AssignmentStatus`, and assignment-creating operations;
- `StudentPerformanceSnapshot` as a stored dashboard cache;
- `Challenge`, `LearnerChallenge`, `Reward`, and `LearnerReward`;
- `GamificationService` and `GamificationRepository`.

Their presence shows a possible design without converting unresolved mechanics into approved requirements.

## UML notation

| Notation | Meaning |
|---|---|
| `A *-- B` | Composition: B belongs to A's lifecycle. |
| `A o-- B` | Aggregation: A groups B without owning its lifecycle. |
| `A -- B` | Association: domain objects are related. |
| `A <|-- B` | Inheritance: B is a subtype of A. It is deliberately not used for learner/teacher roles. |
| `A ..> B` | Dependency: A temporarily uses B, primarily for services and ports. |
| `"1"`, `"0..1"`, `"0..*"`, `"1..*"` | UML multiplicity at each relationship end. |
| `+`, `-`, `#` | Public, private, and protected class members. |

## Main interaction flows

### Learner recitation

1. `RecitationService` validates the learner, selected `Surah`, and `AIMode`.
2. It creates an active `RecitationSession` and starts `AudioCapturePort`.
3. Audio becomes ordered `RecitationSegment` instances and may be retained through `AudioStoragePort` according to consent.
4. `AnalysisService` sends a segment and expected `Verse` to `AIAnalysisPort`.
5. The result becomes `RecitationAnalysis`, `RecitationError`, `ErrorFeedback`, and optional `AudioAssistance` objects.
6. When the session completes, `ProgressService` updates `LearnerSurahProgress`, `MasteryScoreHistory`, `DailyPractice`, and `PracticeStreak`.

### Teacher monitoring

1. `ClassService` manages `LearningClass` ownership and `ClassEnrollment`.
2. `TeacherMonitoringService` verifies the teacher owns the class and the learner has an active enrollment.
3. It reads progress and session information through `ClassRepository`, `ProgressRepository`, and `RecitationRepository`.
4. `MessagingService` applies the same authorization before creating a `TeacherMessage`.

## Invalid states the implementation must reject

- duplicate account email or class join code;
- learner operations without a learner role or teacher operations without a teacher role;
- teacher access without class ownership and active learner enrollment;
- recording, analysis, or completion against a non-active session;
- analysis before audio and segment capture;
- confidence values outside 0–1 or scores outside 0–100;
- `AudioAssistance` linked to both an error and pause, or to neither;
- retained audio without required consent;
- analysis using an unsupported Tajweed rule;
- progress updates from incomplete sessions.

HTTP status codes, framework exceptions, retry strategies, and UI messages belong to later implementation design.

## Canonical model and report views

`itqan-class-diagram.mmd` is authoritative. The four smaller files repeat selected declarations and relationships only for readability:

- `identity-quran-classes.mmd`
- `recitation-feedback-classes.mmd`
- `progress-teacher-classes.mmd`
- `gamification-classes-proposed.mmd`

If a detail view and the complete diagram ever differ, correct the detail view to match the complete model.

The SVGs preserve every specified member and are intended for zoomable digital use or tiled/large-format printing. Do not shrink a whole detailed view onto one A4 page; crop or tile it across landscape pages so the class text remains readable.

## Verification and rendering

Run all consistency and parse checks:

```bash
sh tests/verify_class_diagrams.sh
```

Render the complete diagram:

```bash
npx -y @mermaid-js/mermaid-cli \
  -i docs/diagrams/class/itqan-class-diagram.mmd \
  -o docs/diagrams/class/itqan-class-diagram.svg \
  -b white -w 5600 -H 3600
```

The verification script checks required classes, proposed labels, forbidden implementation-specific classes, learner/teacher profile modeling, all five Mermaid renders, and the explicit 34-entity ERD-to-UML mapping.
