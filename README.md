# Itqan — AI-Powered Quran Recitation Coaching

## Project Overview
Itqan (إتقان) is a standalone Quran recitation coaching application for anyone who reads the Quran. The IS498 phase focuses on problem definition, requirements, analysis, and system design; implementation is planned for IS499.

### Current Scope
- Quran scope: Juz Amma (37 Surahs, 564 verses, 2,308 words).
- Primary Quran content: bundled from the King Fahd Glorious Quran Printing Complex source selected by the architecture.
- Primary UI languages: Arabic and English.
- Recitation analysis: server-side, stateless processing using `obadx/muaalem-model-v3_2` based on `facebook/w2v-bert-2.0`.
- Audio policy: recitation audio is processed in memory and is not retained as a stored user artifact or teacher-accessible recording.
- IS498 does not claim perfect AI accuracy; integrated accuracy and rule-level performance are to be evaluated in IS499.

## Users and Roles
- **Quran Reader:** registers, selects a Surah and AI mode, recites, receives feedback, reviews results/progress, practices streaks, and may join a teacher class using a join code.
- **Teacher:** registers with school name, creates/manages classes, provides a join code, monitors enrolled readers' stored learning results, and sends student messages.

## AI Modes
1. **Al-Mujawwid** — recitation pronunciation/Tajweed correction and feedback.
2. **Al-Mushajji** — motivational support, challenges, and rewards.
3. **Al-Mu'allim** — teacher-facing learning/progress support.

## Current Functional Requirements
The authoritative requirements are `docs/project/REQUIREMENTS.md` and cover FR-01 through FR-26, including:
- account creation with Reader/Teacher registration paths;
- Quran browsing and Surah selection;
- AI mode selection;
- recitation analysis and error location;
- feedback and optional audio assistance;
- continued/end session flows;
- mastery score and progress tracking;
- teacher dashboard, class management, and messages;
- **FR-26 Smart Prompting** when the reader pauses, hesitates, or appears to forget.

### Mastery Score
The approved IS498 formula is:

`Mastery Score = (Total Words − Effective Errors) / Total Words × 100`

- Complete word pronunciation error = 1 effective error.
- Tajweed-only error = 0.5 effective error.
- Effective error contribution per word is capped at 1.

The score is displayed as a percentage from 0–100, followed by the words where errors occurred.

## Architecture and Technology Stack
- **Mobile:** Flutter (Android/iOS target platforms for implementation).
- **Backend:** FastAPI / Python.
- **Database:** PostgreSQL.
- **Authentication:** managed identity provider; local password hashes are not stored by Itqan.
- **Recitation analysis:** separate Python analysis service using Muaalem v3_2; processing is stateless.
- **Quran content:** bundled locally for the Juz Amma scope.
- **Teacher access:** every teacher read is scoped to class ownership and active enrollment.
- **Production hosting:** deferred to IS499 after deployment/vendor and PDPL transfer considerations are evaluated.

## Enrollment Decision
Teachers do not directly add readers to a class and there is no invitation-link/acceptance flow in the approved phase-one design.

The reader joins a class using the teacher-provided **class join code** (`Join Class via Code`).

## Key Design Decisions
- AI is an internal system component, not an external actor.
- Al-Mujawwid, Al-Mushajji, and Al-Mu'allim are modes, not actors.
- Recitation Service is the orchestration point for the recitation-session flow.
- Smart Prompting is an approved FR-26 `Should Have` behavior and is modeled as an extension of the active feedback/recitation flow.
- Quran Reader and Teacher registration are separate paths; Teacher registration additionally requires school name.
- Audio is not retained after analysis and is never exposed to teachers.

## Authoritative Project Documents
| Area | Source |
|---|---|
| Requirements / RTM | `docs/project/REQUIREMENTS.md` |
| Decisions | `docs/project/DECISION_LOG.md` |
| Open Questions | `docs/project/OPEN_QUESTIONS.md` |
| Architecture | `docs/project/SYSTEM_ARCHITECTURE_FINAL.md` and `docs/system-architecture.pdf` |
| ERD | `docs/database/itqan-erd.mmd` |
| Relational Schema | `docs/database/RELATIONAL_SCHEMA.md` |
| Use Case | `docs/diagrams/Itqan_Use_Case_Diagram_v2.svg` |
| Sequence | `docs/diagrams/Itqan_Sequence_01_Recitation_Session_FINAL.svg` |

## IS498 Boundary
IS498 defines the problem, users, requirements, analysis, design, architecture, data model, UI/prototype, impacts, planning, risks, and test plan. Actual implementation, integrated model evaluation, deployment decisions, and production validation are planned for IS499.

## Important Rules for Contributors and AI Tools
- Read this README and the authoritative project documents before making project changes.
- Do not reintroduce Ayat integration, Whisper, unapproved RAG architecture, invitation-based enrollment, `Add Students to Class`, or unsupported perfect-accuracy claims.
- Do not invent user research, interviews, survey statistics, or user quotes.
- Keep diagrams, requirements, schema, architecture, and decision records consistent with the latest approved decisions.
