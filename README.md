# Itqan (إتقان) — Project README / AI Context

> **Purpose:** This README is the main onboarding and context document for the Itqan project.
> It is written so that a teammate or an AI coding/documentation assistant can understand the
> current project before proposing, documenting, designing, or implementing anything.
>
> **Important:** Do not assume every item below is final. Each item is marked as:
> - 🟢 CONFIRMED — currently agreed/verified and can be treated as project context.
> - 🟡 PROPOSED — suggested/current concept, but may still change.
> - 🔴 UNRESOLVED — do not invent an answer; ask/check before using it as a final requirement.

---

# 1. Project Identity

- **Project Name:** Itqan / إتقان
- **Course:** IS498 — Graduation Project I
- **Track:** Track A — System/Product Development
- **University:** King Saud University
- **Department:** Information Systems
- **Project Type:** Graduation Project
- **Current Phase:** IS498 (analysis, design, planning, research, and prototype)
- **Future Phase:** IS499 (implementation, testing, evaluation, deployment)

---

# 2. One-Sentence Project Description

🟢 **Itqan is a standalone application that helps Quran readers practice and improve their recitation using AI by listening to recitation, analyzing it, providing feedback, helping the user when they pause, and tracking progress.**

The current project scope is **Juz Amma (37 surahs)**.

---

# 3. Core Problem

🟢 The project presentation identifies the following problem areas:

1. Some Quran learners may have difficulty accessing a qualified Quran teacher who can correct their recitation during practice.
2. During self-study, pronunciation/Tajweed mistakes may remain uncorrected.
3. A learner may pause or forget during recitation and need assistance to continue.

These points are the starting point for the academic problem definition.

⚠️ **Important academic rule:** These statements are the project's current problem basis, but formal User Research has not yet been completed. Do not invent interviews, survey results, percentages, or user quotes. User Research must be conducted and documented later.

---

# 4. Proposed Solution

🟢 The current concept is an AI-powered Quran recitation coach.

Basic flow:

```text
User
  ↓
Select Surah
  ↓
Start Recitation
  ↓
Microphone captures voice
  ↓
AI analyzes recitation
  ↓
Attempt to detect pronunciation/Tajweed issues
  ↓
Feedback / correction
  ↓
Smart Prompting if the user pauses
  ↓
Session is recorded
  ↓
Progress is updated
```

The goal is to make Quran practice more interactive and provide feedback instead of leaving the learner with only self-practice.

---

# 5. Current Platform Decision

🟢 **Itqan is currently a standalone application.**

This is the current project decision.

There are older presentation materials that describe Itqan as being integrated with the Ayat app. Do not treat that older wording as the current implementation decision.

### Future vision

🟡 Integration with other Quran applications/platforms may be considered in the future.

🟡 An API for other applications may be considered in the future.

🟡 AI-agent integration is part of the future vision and should not be treated as a current IS498 implementation requirement.

---

# 6. Current Scope

🟢 Current scope:

> **Juz Amma — 37 Surahs**

The scope covers the surahs from An-Naba to An-Nas.

Current intended capabilities include:

- Quran recitation practice
- Microphone-based recitation input
- AI listening/analysis
- Pronunciation/Tajweed analysis as a target capability
- Feedback
- Smart Prompting
- User account
- Progress Tracking
- Streak
- Memorized Surahs tracking
- Progress percentage
- Mastery Score
- Student/Learner functionality
- Teacher functionality
- Three AI modes

### Out of current scope

🔵 Full Quran coverage
🔵 Paid API
🔵 Integration with external Quran apps
🔵 Any feature not yet agreed or justified

These may be future work or may change as the project evolves.

---

# 7. Target Audience

🟢 General target audience:

> **Anyone who reads the Quran.**

There is currently no approved restriction by:

- Gender
- Specific age group
- Student status
- Teacher status

However, the system currently has two main roles:

## 7.1 Student / Learner

A user who wants to practice recitation, improve performance, identify mistakes, and track progress.

Current intended needs:

- Practice recitation
- Receive feedback
- Get assistance when pausing
- Track progress
- Track memorized surahs
- Maintain a streak
- View Mastery Score

## 7.2 Teacher

A Quran teacher who uses the system to follow students and review their performance/progress.

Current intended needs:

- View students
- Follow student progress
- Review performance
- Identify strengths
- Identify areas that need improvement

⚠️ Exact teacher workflows and dashboard details are not final.

---

# 8. AI Modes

The project currently has three approved AI modes.

## 8.1 Al-Mujawwid — المجوّد

Purpose:

> Improve Quran recitation.

Current intended capabilities:

- Detect pronunciation issues
- Detect Tajweed issues
- Provide direct feedback

⚠️ Exact Tajweed rules, detection methodology, model, confidence thresholds, and feedback format are unresolved.

---

## 8.2 Al-Mushajji — المشجّع

Purpose:

> Encourage users, especially children, to continue learning and reviewing Quran.

Current concept includes:

- Encouragement
- Challenges
- Rewards
- Motivation

⚠️ Exact gamification mechanics are unresolved.

---

## 8.3 Al-Mu'allim — المعلّم

Purpose:

> Provide teacher-oriented student monitoring.

Current intended capabilities:

- Student tracking
- Performance review
- Progress review
- Strengths
- Areas requiring improvement

⚠️ Exact dashboard screens, metrics, reports, and teacher/student linking process are unresolved.

---

# 9. Admin Role

🔴 There is currently **no approved Admin role**.

Do not add an Admin actor, Admin dashboard, or Admin requirements unless the team explicitly decides that one is necessary.

---

# 10. Core Student Journey

Current conceptual journey:

```text
Open App
   ↓
Login / Account
   ↓
Select Surah
   ↓
Start Recitation
   ↓
AI Listening
   ↓
Recitation Analysis
   ↓
Tajweed / Pronunciation Feedback
   ↓
Smart Prompting if needed
   ↓
End Session
   ↓
Update Progress
   ↓
View Results / Mastery Score
```

This is a conceptual flow and must later be converted into formal Use Cases, scenarios, UI flows, and testable requirements.

---

# 11. Core Teacher Journey

Current conceptual journey:

```text
Teacher
   ↓
Login
   ↓
Teacher Dashboard
   ↓
View Students
   ↓
Select Student
   ↓
View Performance / Progress
   ↓
Review Strengths / Areas for Improvement
```

🔴 Unresolved:

- How students are connected to teachers
- Whether teacher invites students
- Whether students request teacher connection
- What exact dashboard pages exist
- What exact metrics are displayed
- What reports can be generated

Do not invent these details.

---

# 12. Core Functional Concepts

The following are current agreed functions/concepts that will later be converted into formal Functional Requirements.

## Account

A personal account associated with user data and progress.

## Select Surah

The learner selects a surah from Juz Amma.

## Recitation

The user recites Quran aloud using a microphone.

## AI Listening

The system receives and analyzes the user's recitation.

## Tajweed / Pronunciation Correction

The system attempts to detect relevant recitation/pronunciation/Tajweed issues and provide feedback.

⚠️ This is a core project goal, not a guaranteed technical capability.

## Smart Prompting

When the learner pauses, the system provides assistance to help continue.

⚠️ Exact implementation is unresolved.

## Progress Tracking

Tracks user development over time.

Potential/current concepts include:

- Sessions
- Performance
- Memorized Surahs
- Progress percentage
- Streak
- Mastery Score

## Streak

Tracks consecutive days of Quran practice.

## Mastery Score

Current concept:

> **0–100%**

Initial conceptual components:

- Tajweed Accuracy
- Reading Fluency
- Number of Pauses

⚠️ The exact formula and weights are unresolved.

## Teacher Dashboard

Teacher-oriented view for monitoring students.

## Student Tracking

Teacher can follow student progress/performance.

---

# 13. AI Accuracy Rule

The team wants to achieve the highest practical accuracy possible.

However:

❌ Do not claim that the system guarantees 100% accuracy.

❌ Do not write “100% accurate” in academic documentation unless it is actually demonstrated through a valid evaluation.

Use wording such as:

- “aims to achieve high accuracy”
- “designed to maximize practical accuracy”
- “target performance”
- “evaluated using defined metrics”

Actual accuracy claims must come from testing.

---

# 14. AI / Technical Architecture

Current conceptual architecture:

```text
Voice Input
    ↓
Speech Recognition
    ↓
Quran Reference / Content
    ↓
Recitation Analysis
    ↓
Tajweed / Pronunciation Analysis
    ↓
Feedback / Smart Prompt
    ↓
Session & Progress Data
```

The exact architecture is not final.

Potential components mentioned in project materials include:

- Speech Recognition / ASR
- Quran content/reference
- Tajweed analysis
- Feedback engine
- Prompting engine
- Session logging
- Progress tracking

These are architectural concepts, not necessarily final implementation components.

---

# 15. Technology Stack Status

The project presentation proposed technologies such as:

- Python
- Flutter
- FastAPI
- PostgreSQL
- Whisper
- Hugging Face
- RAG
- Quran API
- Firebase
- Google Colab

🟡 **These are proposals, not final technology decisions.**

Before documenting them as final architecture/stack, the team must evaluate and justify the choices.

Do not state:

> “Itqan uses Flutter/FastAPI/PostgreSQL/Whisper”

as a final fact until the team has made and documented the decision.

Instead, while unresolved, use:

> “The current proposal includes…”

---

# 16. Quran Data

The system needs reliable Quran content for functions involving verses and comparison/reference.

🟢 Required concept:

> A trusted Quran text/reference source.

🔴 Unresolved:

- Final Quran data source
- API
- Local database vs external API
- Exact storage structure
- Licensing/usage conditions
- Audio source, if required

Do not invent the final source.

---

# 17. User Data

Current conceptual data includes:

- Account
- Progress
- Memorized Surahs
- Sessions
- Performance/error-related data
- Streak
- Mastery Score

🔴 Final user fields are unresolved.

Do not automatically add:

- Age
- Gender
- Phone number
- Date of birth
- Address
- Any unnecessary personal data

unless there is a documented requirement.

---

# 18. Database Status

The final database schema has not been approved yet.

Potential conceptual areas:

```text
User
Student
Teacher
Surah
Recitation Session
Progress
Memorized Surah
Streak
Mastery Score
Recitation Performance / Errors
Teacher-Student relationship
```

⚠️ These are conceptual areas, not a final ERD.

The final ERD must be derived from actual approved requirements.

The relational schema must match the ERD.

The class diagram must be reasonably consistent with the data/model design.

---

# 19. Teacher–Student Relationship

🔴 Unresolved.

Possible approaches may include:

- Teacher adds student
- Student requests teacher
- Teacher sends invitation
- Code-based linking
- Class/group model

Do not select one without an explicit decision.

---

# 20. Existing Solutions / Competitor Research

Existing-solution research must be evidence-based.

Potential competitors/related systems that have been identified for research include:

- Tarteel
- Tilawa.ai
- QariAI
- Tajweed.chat

Important rule:

❌ Do not claim Itqan is the first AI Quran application.

❌ Do not claim Itqan is the only Tajweed AI system.

❌ Do not claim competitors lack a capability without checking current evidence.

The final Gap Analysis must be based on documented research.

---

# 21. User Research

🔴 User Research has not yet been completed.

Do not fabricate:

- Interview results
- Survey results
- Participant numbers
- User percentages
- Quotes
- Pain points supposedly discovered from users

The team needs actual research evidence for the IS498 report.

Possible research methods may include:

- Questionnaire
- Interviews
- Observation

The exact method, sample, questions, and analysis must be decided and documented.

---

# 22. Formal Requirements Status

🔴 There is currently no final approved FR/NFR list.

The following concepts are candidates to become formal Functional Requirements:

- Account
- Select Surah
- Recitation
- AI Listening
- Recitation Analysis
- Tajweed/Pronunciation Feedback
- Smart Prompting
- Progress Tracking
- Streak
- Memorized Surahs
- Progress Percentage
- Mastery Score
- Teacher Dashboard
- Student Tracking
- AI Modes

But these must be converted into proper requirement statements with IDs and acceptance/test criteria.

Example structure:

```text
FR-XX
The system shall ...
```

Do not create arbitrary final FR numbers without coordinating the requirements set.

---

# 23. Non-Functional Requirements

🔴 No final NFR list has been approved yet.

Potential NFR categories that may need investigation include:

- Performance
- Usability
- Reliability
- Security
- Privacy
- Availability
- Scalability
- Maintainability
- Accessibility

Do not assign exact numbers such as “response within 2 seconds” unless the team has a justified requirement or target.

---

# 24. Requirements Prioritization

🔴 Prioritization method is not final.

A prioritization framework must eventually be selected and applied consistently.

Do not randomly label requirements as High/Medium/Low without an agreed method.

---

# 25. Requirements Traceability

The requirements must eventually connect to other project artifacts.

Expected relationships include:

```text
Requirement
   ↓
Use Case
   ↓
Scenario
   ↓
Design
   ↓
UI / System Component
   ↓
Test Case
```

Every requirement should be traceable.

---

# 26. IS498 Deliverables

The project is Track A — System/Product Development.

Major IS498 work includes:

- Problem definition
- Stakeholder analysis
- User research
- Existing solutions
- Gap analysis
- BMC if applicable
- Functional requirements
- Non-functional requirements
- Requirements prioritization
- Requirements traceability
- Use Case Diagram
- Use Case Scenarios
- Activity Diagram / BPMN
- Sequence Diagram
- ERD
- Relational Schema
- Class Diagram
- System Architecture
- Technology Stack and justification
- UI/UX prototype
- Test Plan
- Project methodology
- Schedule
- Resource planning
- Risk register
- Impact analysis
- Final report
- Presentation/defense

---

# 27. IS499

IS499 is expected to focus on:

- Implementation
- Actual system development
- Unit testing
- Integration testing
- User Acceptance Testing
- Evaluation
- Deployment/hosting
- User/install documentation
- Final project delivery

The Test Plan is prepared in IS498 and then executed in IS499.

---

# 28. BMC Status

🔴 BMC is not yet confirmed as required.

The handbook requires BMC when the project has a relevant:

- Commercial dimension
- Entrepreneurial dimension
- Service-delivery dimension

The future paid API/subscription idea alone should not automatically be treated as current project scope.

If the advisor determines BMC is applicable, it must be completed.

---

# 29. Impact Analysis

The project documentation needs appropriate impact analysis.

Current team responsibilities include:

- Social Impact
- Global Impact
- Ethical Impact
- Legal Impact
- Security Impact

These should be based on the actual system and data practices, not generic statements.

---

# 30. Important Consistency Rules

The project artifacts must agree with one another.

Examples:

### Stakeholders ↔ Actors

Every relevant system actor should be supported by stakeholder analysis.

### Use Cases ↔ Scenarios

Every important use case should have a scenario.

### Use Cases ↔ Sequence Diagrams

Significant scenarios should be represented in sequence diagrams where required.

### ERD ↔ Schema

Every ERD entity must have a corresponding relational representation.

### Requirements ↔ Tests

NFRs and testable requirements must have a way to verify them.

### Prototype ↔ Use Cases

Prototype screens should support actual use cases.

### Terminology

Use consistent names across:

- Requirements
- Diagrams
- Database
- UI
- Report
- Code

Do not call the same thing “Learner” in one document, “Student” in another, and “User” in a third without a reason.

---

# 31. Team

Current team:

- Ibrahim
- Saud
- Abdulaziz

The task distribution is flexible.

A member can take work from another member when they finish their own tasks.

---

# 32. Current Team Responsibilities

## Ibrahim

Primary:

- Problem
- Users
- Requirements
- Report Coordination

Also currently responsible for:

- ER Diagram
- Relational Schema
- Use Cases ↔ System Mapping
- Stakeholder Analysis
- Target Users
- User Research
- Gap Analysis
- Functional Requirements
- Non-Functional Requirements
- Prioritization
- Traceability
- Use Cases
- Use Case Diagram
- Sequence Diagram
- Social Impact
- Global Impact
- Abstract
- References
- Report compilation/formatting
- Weekly Progress Log compilation
- AI Use Declaration
- Conclusion + IS499 plan

## Saud

Primary:

- Existing Solutions
- System Analysis
- Database
- Architecture

Current areas:

- Existing Solutions Comparison
- Gap-related analysis support
- System Architecture
- Architecture Diagram
- Technology Stack
- Technology Justification
- Data Flow
- Requirements ↔ Architecture
- Security Impact

## Abdulaziz

Primary:

- UI/UX
- Design
- Planning
- Testing

Current areas:

- Activity Diagram
- Class Diagram
- User Flow
- Wireframes
- Clickable Prototype
- Main User Journeys
- Heuristic Evaluation
- Development Methodology
- Methodology Justification
- Gantt
- Resource Schedule
- Risk Register
- Risk Mitigation
- Test Plan
- Ethical Impact
- Legal Impact

### Important

This split is **not a hard ownership barrier**.

Tasks can move between team members.

---

# 33. GitHub Repository

Repository:

> `Itqan`

Current workflow:

```text
main
  ↑
Pull Request
  ↑
feature/task-branch
```

Recommended branch naming:

```text
feature/problem-users
feature/requirements
feature/use-cases
feature/erd
feature/architecture
feature/ui
feature/testing
```

Branches should represent **tasks/features**, not permanently represent individual people.

---

# 34. Git Workflow

For a task:

```text
Create / switch to task branch
        ↓
Work
        ↓
Review your changes
        ↓
git add
        ↓
git commit
        ↓
git push
        ↓
Pull Request
        ↓
Review
        ↓
Merge into main
```

Do not directly make large unreviewed changes to `main`.

---

# 35. Current Repository Structure

```text
Itqan/
├── README.md
├── .gitignore
│
├── docs/
│   ├── project/
│   │   ├── PROJECT_CONTEXT.md
│   │   ├── DECISION_LOG.md
│   │   └── OPEN_QUESTIONS.md
│   │
│   ├── requirements/
│   ├── diagrams/
│   ├── database/
│   ├── architecture/
│   ├── ui-ux/
│   └── report/
│
├── src/
└── tests/
```

---

# 36. Documentation Files

## README.md

This file should provide project onboarding/context.

## PROJECT_CONTEXT.md

Contains the more detailed project context and working assumptions.

## DECISION_LOG.md

Contains decisions that have been explicitly made.

## OPEN_QUESTIONS.md

Contains unresolved decisions that must not be silently assumed.

---

# 37. AI Assistant Rules

Any AI tool used by a team member should first read:

1. `README.md`
2. `docs/project/PROJECT_CONTEXT.md`
3. `docs/project/DECISION_LOG.md`
4. `docs/project/OPEN_QUESTIONS.md`

Then, if the task relates to the academic requirements, also consult the IS498/IS499 handbook and relevant project source material.

### AI must not:

- Invent project requirements
- Invent user research
- Invent competitor capabilities
- Treat proposed technologies as final
- Add an Admin role without approval
- Treat future vision as current scope
- Claim 100% AI accuracy
- Assume teacher workflow
- Assume database fields
- Assume final APIs/models
- Rewrite project decisions silently
- Delete or change an approved decision without documenting it

### AI should:

- Identify assumptions
- Mark uncertainty
- Ask for clarification when a decision is needed
- Keep terminology consistent
- Check dependencies between artifacts
- Explain why a proposed change is needed
- Update documentation when a decision changes

---

# 38. Source Priority

When information conflicts, use this priority:

### 1. Current explicit team decision
Highest priority for project decisions.

### 2. Official IS498/IS499 handbook
Highest authority for academic requirements.

### 3. Latest approved project documentation
Current project context/decision log.

### 4. Latest project presentation
Useful project source, but older slides may contain outdated decisions.

### 5. Older presentations/documents
Use only if still consistent with current decisions.

### 6. AI assumptions/general knowledge
Never override project decisions.

---

# 39. Status Labels

Use these labels when documenting decisions:

### 🟢 CONFIRMED

The team has explicitly agreed on it or it is clearly verified.

### 🟡 PROPOSED

A reasonable suggestion or current concept that still needs confirmation.

### 🔴 UNRESOLVED

No decision has been made.

Do not silently convert 🟡 or 🔴 into 🟢.

---

# 40. Current Confirmed Decisions

At the current project state:

🟢 Standalone application

🟢 Juz Amma / 37 Surahs

🟢 General target audience: anyone who reads Quran

🟢 Main roles: Student/Learner + Teacher

🟢 Three AI modes:
- Al-Mujawwid
- Al-Mushajji
- Al-Mu'allim

🟢 Smart Prompting is part of the concept

🟢 Progress Tracking is part of the concept

🟢 Streak is part of the concept

🟢 Memorized Surahs tracking is part of the concept

🟢 Mastery Score 0–100% is part of the concept

🟢 Future integrations are not current scope

🟢 No Admin role currently approved

🟢 AI accuracy is a target, not a guaranteed 100%

🟢 User Research has not yet been completed

🟢 Technology stack is not final

🟢 Teacher dashboard details are not final

---

# 41. Current Unresolved Decisions

The following require explicit investigation/decision:

## Project

- Exact final feature list
- Exact Smart Prompt behavior
- Exact Teacher Dashboard
- Teacher ↔ Student relationship

## Users

- Detailed user personas
- User research sample
- User research method
- Exact user needs from research

## Requirements

- Formal FR list
- Formal NFR list
- Requirement IDs
- Prioritization method
- Traceability matrix

## AI

- Final model
- Dataset
- Fine-tuning
- Tajweed detection methodology
- Pronunciation detection methodology
- Accuracy metrics
- Evaluation dataset
- Real-time processing method

## Technology

- Frontend
- Backend
- Database
- Authentication
- Hosting
- APIs
- AI infrastructure

## Quran Data

- Final source
- API
- Storage
- Licensing/usage considerations

## Database

- Final entities
- Attributes
- Relationships
- Session structure
- Progress structure
- Teacher/student relationship

## Existing Solutions

- Final competitor list
- Evidence
- Comparison criteria
- Gap Analysis

## BMC

- Whether it is required

---

# 42. Current Work Status

### Already established

🟢 Project idea
🟢 Basic problem
🟢 Basic solution
🟢 Standalone decision
🟢 Juz Amma scope
🟢 User roles
🟢 AI modes
🟢 Initial user journey
🟢 Initial architecture concept
🟢 Initial technology proposals
🟢 Team task distribution
🟢 GitHub repository
🟢 Project documentation structure

### Not completed yet

🔴 Final Stakeholder Analysis
🔴 Formal User Research
🔴 Final academic Problem Statement
🔴 Existing Solutions research
🔴 Final Gap Analysis
🔴 Formal Functional Requirements
🔴 Formal Non-Functional Requirements
🔴 Prioritization
🔴 Traceability
🔴 Formal Use Cases + Scenarios
🔴 Final diagrams
🔴 Final architecture
🔴 Final technology selection
🔴 Final ERD/schema
🔴 UI/UX prototype
🔴 Test Plan
🔴 Full report

---

# 43. Recommended Work Order

The current recommended order for the Ibrahim workstream is:

```text
Stakeholder Analysis
        ↓
Target Users
        ↓
User Research
        ↓
Problem Statement
        ↓
Objectives + Scope
        ↓
Existing Solutions / Gap Analysis
        ↓
Functional Requirements
        ↓
Non-Functional Requirements
        ↓
Prioritization
        ↓
Traceability
        ↓
Use Cases
        ↓
Use Case Scenarios
        ↓
Use Case Diagram
        ↓
Sequence Diagram
        ↓
ERD
        ↓
Relational Schema
        ↓
Use Cases ↔ System Mapping
```

Other team members can work in parallel where dependencies allow.

---

# 44. Dependency Rule

Before creating an artifact, check what it depends on.

Examples:

- Use Cases depend on requirements and actors.
- Sequence Diagrams depend on selected scenarios.
- ERD depends on actual data requirements.
- Relational Schema depends on ERD.
- UI screens depend on actual user journeys/use cases.
- Architecture depends on requirements and selected technology.
- Test Plan depends on requirements and NFRs.

Do not finalize downstream artifacts while upstream decisions are still unknown unless the artifact is explicitly labeled as a draft.

---

# 45. Final Instruction to Any AI Working on Itqan

Before doing any task:

1. Read this README.
2. Read the project context files.
3. Check the decision log.
4. Check open questions.
5. Identify dependencies.
6. Separate confirmed information from proposals.
7. Do not invent missing project information.
8. If an important decision is missing, flag it.
9. Keep all project artifacts consistent.
10. Prefer evidence and the official handbook over assumptions.

> **The goal is not simply to produce documents. The goal is to build one consistent, academically defensible project where the problem, users, requirements, diagrams, architecture, UI, database, tests, and final implementation all describe the same system.**
