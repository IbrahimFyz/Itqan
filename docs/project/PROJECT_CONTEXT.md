# Itqan Project Context

## 1. Project Identity
- Name: Itqan / إتقان
- University: King Saud University
- Department: Information Systems
- Project courses: IS498 / IS499
- Current platform decision: standalone Itqan application.

## 2. Problem
Quran readers and learners may have difficulty accessing continuous and immediate guidance while practicing. Pronunciation/Tajweed mistakes may remain uncorrected, and a reader may pause or forget without immediate assistance.

## 3. Target Audience and Roles
### General audience
Anyone who reads the Quran and seeks to improve recitation, pronunciation, Tajweed, reading, or memorization.

### Main system roles
- Student / Learner
- Teacher

### Additional target group
Children are specifically relevant to the Al-Mushajji mode.

No Admin role is currently approved.

## 4. Current Scope
- Standalone application.
- Juz Amma only: 37 Surahs, from An-Naba (78) to An-Nas (114).
- Surah selection.
- Microphone-based recitation.
- AI recitation analysis.
- Pronunciation/Tajweed error detection as a target capability.
- Feedback.
- Audio-based assistance where applicable.
- Smart Prompting after a pause or when assistance is needed.
- Session/progress tracking.
- Mastery Score.
- Al-Mujawwid, Al-Mushajji, and Al-Mu'allim.

## 5. Future Vision
These are future directions, not current IS498 requirements:
1. Integration with other Quran applications/platforms.
2. Integration with AI agents.
3. Expansion to the full Quran.
4. Additional future capabilities.

The product is intentionally allowed to evolve. Features may be added, modified, or removed when justified by research, feasibility, testing, user feedback, or project decisions.

## 6. Accuracy and Performance
The team aims for the highest practical accuracy possible, with 100% accuracy as an aspirational target.

The team also aims for real-time and comprehensive Tajweed-error detection as far as technically feasible.

Do NOT state that the system guarantees 100% accuracy or detects every Tajweed error perfectly unless testing provides evidence.

## 7. Mastery Score
The project includes a 0–100 Mastery Score.

For a completed session with `total_words > 0`, the formula is `(Total Words − Effective Errors) / Total Words × 100`. A complete word-pronunciation error contributes 1 effective error, a Tajweed-only error contributes 0.5, and each word contributes at most 1. A session with `total_words = 0` has no mastery score. Evaluation of the score's interpretation remains open.

## 8. Technical Direction
The project presentation proposed:
- Python
- Whisper
- Flutter
- FastAPI
- PostgreSQL
- Hugging Face
- RAG
- Google Colab
- Quran API
- Firebase

These are proposed directions unless separately approved. Technology choices must be justified and documented.

## 9. Core User Flow
1. Select Surah.
2. Start reciting.
3. AI analyzes recitation.
4. AI provides feedback.
5. AI provides Smart Prompting when needed.
6. Session/progress information is updated.

This flow can evolve during analysis, prototyping, implementation, and testing.

## 10. Competitive Analysis
Relevant solutions identified for research include:
- Tarteel
- Tilawa.ai
- QariAI
- Tajweed.chat

Never claim Itqan is the first or only AI Quran application, Tajweed detector, or voice-enabled solution without reliable evidence.

Competitive capabilities must be verified using current sources.

## 11. IS498 / IS499
The official Graduation Project Handbook is the academic authority.

IS498 Track A includes areas such as:
- Problem/stakeholder analysis.
- User research.
- Existing solution review.
- BMC when applicable.
- Functional and non-functional requirements.
- Prioritization and traceability.
- Development methodology.
- Use cases and scenarios.
- Activity/BPMN modeling where applicable.
- ERD and relational schema.
- Sequence and class diagrams.
- Architecture and technology justification.
- Clickable UI prototype.
- Test plan.
- Social, ethical, legal, global, and security impacts.
- Report and supporting documentation.

IS499 continues with implementation, testing, deployment/hosted build, documentation, and evidence of genuine individual contribution.

## 12. Artifact Consistency
The following must remain connected:
- Stakeholders ↔ Use Case Actors
- Use Cases ↔ Scenarios
- Significant Scenarios ↔ Sequence Diagrams
- ERD ↔ Relational Schema / Classes
- NFRs ↔ Tests
- Use Cases ↔ UI Screens
- Requirements ↔ Architecture
- Terminology across all artifacts

## 13. Team Responsibilities
### Ibrahim
Problem, objectives, scope, stakeholders, target users, user research, gap analysis, requirements, prioritization, traceability, BMC if applicable, Use Case Diagram, Sequence Diagram, ERD, Relational Schema, Use Cases ↔ System mapping, social/global impact, report coordination, abstract/introduction/conclusion, references, weekly progress compilation, AI Use Declaration, GitHub follow-up.

### Saud
Existing solutions, system analysis, system architecture, technology stack and justification, data flow within architecture, Requirements ↔ Architecture, security impact.

### Abdulaziz
UI/UX, Activity Diagram, Class Diagram, user flow, wireframes, clickable prototype, main user journeys, heuristic evaluation, development methodology, methodology justification, Gantt, resource schedule, risk register/mitigation, test plan, ethical/legal impact.

### Team principle
Responsibilities are flexible. A team member may take additional work from another member after completing their own tasks.

## 14. GitHub Structure
```text
Itqan/
├── README.md
├── .gitignore
├── docs/
│   ├── requirements/
│   ├── diagrams/
│   ├── database/
│   ├── architecture/
│   ├── ui-ux/
│   └── report/
├── src/
└── tests/
```

Recommended task branches:
- feature/problem-users
- feature/requirements
- feature/use-case-diagram
- feature/erd
- feature/ui-wireframes
- feature/architecture
- feature/test-plan

Workflow:
Task → branch → commit → push → PR → review → merge.

## 15. Evidence Status Rules
### 🟢 Confirmed
Explicitly approved or verified from an authoritative source.

### 🟡 Proposed
Suggested or mentioned but not finalized.

### 🔴 Unresolved
Missing, contradictory, or awaiting a decision/research.

Never silently convert 🟡 or 🔴 information into 🟢 information.

## 16. AI Tool Rules
Any AI tool working on this repository must:

1. Never invent requirements, features, research results, technologies, datasets, architecture decisions, competitor capabilities, or academic requirements.
2. Distinguish confirmed, proposed, and unresolved information.
3. Use the official IS498/IS499 handbook for academic requirements.
4. Preserve consistency between requirements, use cases, scenarios, diagrams, database, architecture, UI, testing, and report.
5. Never fabricate survey responses, interviews, participants, statistics, or user-research findings.
6. Never claim guaranteed 100% AI accuracy or perfect Tajweed detection without evidence.
7. Keep future vision separate from current scope.
8. Identify conflicts instead of guessing.
9. Propose project changes explicitly and explain their impact.
10. Treat AI-generated content as assistance that requires team review and approval.
11. Do not describe unimplemented or unevaluated functionality as completed functionality.
12. Prefer asking/flagging when a critical project fact is missing.

## 17. Source Priority
When sources conflict:
1. Official IS498/IS499 Handbook — academic requirements.
2. Latest team-approved project decisions — current project scope/decisions.
3. Latest approved project presentation/documentation — project concept.
4. Verified external research — competitors, technologies, market information.
5. AI suggestions — ideas only.

Conflicts must be explicitly flagged.

## 18. Open Questions
Still requiring analysis, research, or approval:
- Final FR/NFR list and IDs.
- Prioritization and traceability method.
- Teacher-student relationship workflow.
- Exact Teacher Dashboard.
- Exact behavior of the three AI modes.
- AI model/dataset/training strategy.
- Tajweed detection approach.
- Real-time processing approach.
- Quran text source.
- Final technology stack.
- Authentication.
- Database schema.
- API design.
- Hosting/deployment.
- User Research results.
- Final Existing Solutions and Gap Analysis.
- BMC applicability.
- Detailed impact analyses.

## 19. Current Principle
> Build what we can justify, test what we claim, and document what we actually do.
