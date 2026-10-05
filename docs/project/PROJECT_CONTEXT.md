# Itqan — Project Context

## 1. Project Identity

**Project:** Itqan (إتقان) — AI-Powered Quran Recitation Coaching
**University:** King Saud University
**Department:** Information Systems
**Courses:** IS498 Graduation Project I / IS499 Graduation Project II
**Team:** Ibrahim, Abdulaziz, Saud

Itqan is a standalone application for Quran recitation coaching. IS498 focuses on problem definition, requirements, analysis, and system design. Implementation and further testing are planned for IS499.

---

## 2. Problem

Quran readers and learners may have difficulty accessing continuous and immediate guidance while practicing. Pronunciation and Tajweed mistakes may remain uncorrected, and a reader may pause, hesitate, or forget without immediate assistance.

Itqan aims to provide AI-assisted recitation analysis and timely feedback to support Quran readers during practice.

---

## 3. Target Audience and Roles

### General Target Audience

Itqan is intended for anyone who reads the Quran and seeks to improve recitation, pronunciation, Tajweed, reading, or memorization.

### Main System Roles

- Quran Reader / Learner
- Teacher

### Additional Target Group

Children are particularly relevant to the Al-Mushajji mode, which focuses on encouragement and motivation.

No Admin role is currently approved.

### Teacher Enrollment

Teachers create and manage classes. Quran Readers join a teacher's class using a teacher-provided class join code.

Teachers do not directly add readers, and no invitation-link or invitation-acceptance flow is part of the approved design.

Teacher registration additionally requires the school name.

---

## 4. Current Scope

The current IS498 project scope includes:

- Standalone Itqan application.
- Juz Amma only: 37 Surahs, 564 verses, and 2,308 words.
- Browsing and selecting Surahs.
- Displaying Quranic verses for recitation.
- Microphone-based recitation sessions.
- AI-assisted recitation analysis.
- Pronunciation and Tajweed error detection as a target capability.
- Error-location identification.
- Recitation feedback.
- Audio-based assistance where applicable.
- Smart Prompting when the reader pauses, hesitates, forgets, or needs assistance.
- Session results and Mastery Score.
- User progress tracking.
- Practice streaks.
- Teacher classes and student progress monitoring.
- Teacher messaging.
- Three approved AI modes:
  - Al-Mujawwid
  - Al-Mushajji
  - Al-Mu'allim

The authoritative functional requirement list is FR-01 through FR-26 in `docs/project/REQUIREMENTS.md`.

---

## 5. AI Modes

### Al-Mujawwid

Focuses on recitation analysis, pronunciation/Tajweed error detection, and feedback during recitation.

### Al-Mushajji

Focuses on motivation, encouragement, challenges, and rewards. It is particularly relevant to children and users who benefit from motivational support.

### Al-Mu'allim

Supports teacher-oriented learning and progress functionality, including teacher visibility into enrolled Quran Readers' recitation activity and progress.

AI modes are system functionality, not external actors in the Use Case Diagram.

---

## 6. Smart Prompting

Smart Prompting is an approved project capability and is represented by FR-26.

It is intended to assist the Quran Reader when the system detects that assistance may be needed, such as after a pause, hesitation, or apparent forgetting.

Smart Prompting is modeled as an extension of the normal recitation-feedback flow and is not treated as a separate external actor.

---

## 7. Mastery Score

The system calculates a Mastery Score on a 0–100 scale.

The approved formula is:

`Mastery Score = (Total Words − Effective Errors) / Total Words × 100`

Error weighting:

- Complete word-pronunciation error = 1 effective error.
- Tajweed-only error = 0.5 effective error.
- Maximum contribution per word = 1 effective error.

The score is used to summarize the user's performance for a completed recitation session.

---

## 8. Current Architecture and Technical Direction

The current architecture direction is:

- Flutter mobile application for Android and iOS.
- FastAPI/Python backend.
- PostgreSQL database.
- Managed identity provider for authentication.
- Separate stateless Python recitation-analysis service.
- Recitation analysis using `obadx/muaalem-model-v3_2`, based on `facebook/w2v-bert-2.0`.
- Quranic content bundled from the King Fahd Glorious Quran Printing Complex source selected by the architecture.
- Audio is processed in memory and is not retained.
- Teacher access is scoped according to class ownership and active enrollment.
- Production hosting/deployment remains an IS499 implementation decision.

The Recitation Service acts as the main orchestrator for the recitation session flow. The intended flow is:

`Itqan App → Recitation Service → AI Analysis Engine → Recitation Service → Itqan App`

Services should not bypass the Recitation Service to communicate directly with the application for the main recitation-session flow.

Detailed implementation choices and deployment decisions may be refined during IS499.

---

## 9. IS498 / IS499 Boundaries

### IS498

IS498 focuses on:

- Problem definition.
- Stakeholder and target-user analysis.
- Existing solution review and gap analysis.
- Functional and non-functional requirements.
- Requirements prioritization and traceability.
- Use cases and scenarios.
- System analysis and design.
- Database design.
- Architecture and technology justification.
- Relevant system diagrams.
- UI/UX design and prototype artifacts.
- Test planning.
- Social, ethical, legal, global, and security impact analysis.
- Project planning and supporting documentation.

### IS499

IS499 is intended to cover:

- System implementation.
- Integration.
- Detailed testing and evaluation.
- Deployment/hosting decisions.
- Final documentation and evidence of implementation.
- Further validation of AI performance and system behavior.

IS498 does not claim production implementation or completed implementation-level evaluation.

---

## 10. Current Non-Goals and Explicit Exclusions

The following are not part of the current approved IS498 scope:

- Production implementation.
- A claim of 100% AI accuracy.
- Invented user-research findings.
- Ayat integration as part of the current project.
- Whisper as part of the final approved architecture.
- Invitation-based class enrollment.
- Direct teacher addition of Quran Readers to classes.

Future ideas must not be presented as current requirements.

---

## 11. Future Vision

The following are future directions and are not current IS498 requirements:

1. Integration with other Quran applications or platforms.
2. Integration with AI agents.
3. Expansion beyond Juz Amma to the full Quran.
4. Additional future capabilities based on research, feasibility, testing, and user needs.

Future vision must remain separate from the current approved scope unless a future project decision explicitly changes the scope.

---

## 12. Competitive Analysis

Relevant existing solutions identified for comparison include:

- Tarteel
- Tilawa.ai
- QariAI
- Tajweed.chat

Competitive claims must be based on reliable and current sources.

Itqan must not be described as the first, only, or unique AI Quran application, Tajweed detector, or voice-enabled Quran solution without reliable evidence.

---

## 13. Artifact Consistency

The project artifacts must remain consistent and traceable.

Important relationships include:

- Stakeholders ↔ Use Case Actors
- Requirements ↔ Use Cases
- Use Cases ↔ Scenarios
- Significant Scenarios ↔ Sequence Diagrams
- ERD ↔ Relational Schema
- ERD / Schema ↔ Class and Architecture decisions where applicable
- NFRs ↔ Test Plan
- Use Cases ↔ UI Screens / User Flows
- Requirements ↔ Architecture
- Terminology across all project artifacts

Changes to one major artifact should be checked against related artifacts before being treated as final.

---

## 14. Team Responsibilities

### Ibrahim

Primary responsibility includes:

- Problem
- Objectives
- Scope
- Stakeholders
- Target Users
- Gap Analysis
- Functional Requirements
- Non-Functional Requirements
- Requirements Prioritization
- Requirements Traceability
- Use Case Diagram
- Sequence Diagram
- Social Impact
- Global Impact
- Report Coordination
- Abstract
- Introduction
- Conclusion and IS499 Plan
- Reference List
- Formatting and Report Compilation
- Weekly Progress Log
- AI Use Declaration
- GitHub Follow-up

### Saud

Primary responsibility includes:

- Existing Solutions
- System Analysis
- Database
- ER Diagram
- Relational Schema
- System Architecture
- Architecture Diagram
- Technology Stack
- Technology Justification
- Data Flow

### Abdulaziz

Primary responsibility includes:

- UI/UX
- Design
- Activity Diagram
- Class Diagram
- User Flow
- Wireframes
- Clickable Prototype
- Heuristic Evaluation
- Development Methodology
- Gantt Chart
- Resource Schedule
- Risk Register
- Risk Mitigation
- Test Plan
- Ethical Impact
- Legal Impact

Responsibilities may be shared or reassigned when a team member completes their primary work and takes additional work from another member.

---

## 15. Evidence and Decision Status Rules

Project information should be distinguished according to its status:

### Confirmed

Explicitly approved by the team or supported by an authoritative source.

### Proposed

Suggested or discussed but not yet finalized.

### Unresolved

Missing, contradictory, deferred, or awaiting a decision, research, or implementation validation.

AI tools and team members must not silently convert proposed or unresolved information into confirmed project decisions.

---

## 16. AI Tool Rules

Any AI tool working with the Itqan repository must:

1. Never invent requirements, features, research findings, technologies, datasets, architecture decisions, competitor capabilities, or academic requirements.
2. Distinguish confirmed, proposed, and unresolved information.
3. Use the official IS498/IS499 handbook as the academic authority.
4. Preserve consistency between requirements, use cases, scenarios, diagrams, database, architecture, UI, testing, and the report.
5. Never fabricate surveys, interviews, participants, statistics, or user-research findings.
6. Never claim guaranteed 100% AI accuracy or perfect Tajweed detection without evidence.
7. Keep future vision separate from current scope.
8. Identify conflicts instead of guessing.
9. Propose project changes explicitly and explain their impact.
10. Treat AI-generated content as assistance that requires team review and approval.
11. Do not describe unimplemented or unevaluated functionality as completed functionality.
12. Flag critical missing project information instead of making unsupported assumptions.

---

## 17. Source Priority

When project sources conflict, use the following priority:

1. Official IS498/IS499 Handbook — academic requirements.
2. Latest team-approved project decisions — current project scope and decisions.
3. Latest approved project artifacts and documentation — current project definition.
4. Verified external research — competitors, technologies, and supporting information.
5. AI suggestions — ideas only.

Conflicts must be explicitly identified and resolved rather than silently overwritten.

---

## 18. User Research and BMC Status

### User Research

User research is not required for the current project according to the advisor's direction.

No user-research findings, survey results, interviews, participants, or statistics should be invented or presented as completed research.

### Business Model Canvas

A Business Model Canvas is not required for the current project according to the advisor's direction.

If project requirements change, its applicability can be reconsidered.

---

## 19. Authoritative Project Sources

The following artifacts should be treated as the primary project sources of truth for their respective areas:

- `docs/project/REQUIREMENTS.md`
- `docs/project/DECISION_LOG.md`
- `docs/project/OPEN_QUESTIONS.md`
- `docs/project/SYSTEM_ARCHITECTURE_FINAL.md`
- ERD artifacts
- Relational schema
- Latest approved project documentation

The README should also be consulted for current repository context and team workflow.

When sources conflict, apply the Source Priority rules above and explicitly resolve the conflict.

---

## 20. Current Principle

> Build what we can justify, test what we claim, and document what we actually do.
