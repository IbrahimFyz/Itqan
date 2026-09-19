# Itqan Decision Log

Use this file to record significant project decisions.

## Decision Format

### [DATE] — [Decision Title]
- **Status:** 🟢 Confirmed / 🟡 Proposed / 🔴 Unresolved
- **Decision:**
- **Reason:**
- **Source/Evidence:**
- **Affected artifacts:**
- **Notes:**

---

### 2026-09-13 — Standalone Application
- **Status:** 🟢 Confirmed
- **Decision:** The current graduation-project version of Itqan is a standalone application.
- **Reason:** Current team decision.
- **Source/Evidence:** Latest team-approved project direction.
- **Affected artifacts:** Scope, architecture, requirements, UI, report.

### 2026-09-13 — Future Integrations
- **Status:** 🟢 Confirmed as Future Vision
- **Decision:** Future vision includes integration with other Quran applications and integration with AI agents.
- **Reason:** Long-term product direction.
- **Affected artifacts:** Future vision only; not current IS498 scope.

### 2026-09-13 — Target Audience
- **Status:** 🟢 Confirmed
- **Decision:** The general target audience is anyone who reads the Quran. Children are an additional target group, particularly for Al-Mushajji. Student/Learner and Teacher remain the main system roles.
- **Affected artifacts:** Stakeholder analysis, user research, requirements, use cases, UI.

### 2026-09-13 — AI Modes
- **Status:** 🟢 Confirmed
- **Decision:** Adopt Al-Mujawwid, Al-Mushajji, and Al-Mu'allim.
- **Affected artifacts:** Requirements, use cases, UI, architecture, testing.

### 2026-09-13 — Accuracy Goal
- **Status:** 🟢 Confirmed as Goal
- **Decision:** Aim for the highest practical accuracy, with 100% as an aspirational target.
- **Important:** This is not a guarantee.
- **Affected artifacts:** NFRs, testing, report limitations.

### 2026-09-13 — Flexible Scope Evolution
- **Status:** 🟢 Confirmed Principle
- **Decision:** Features may be added, modified, or removed as the project evolves, provided changes are justified and documented.
- **Affected artifacts:** Requirements, diagrams, implementation, testing, report.

### 2026-09-16 — Development Methodology
- **Status:** 🟡 Proposed
- **Decision:** Use an iterative Agile software development life cycle with academic phase gates. The approach supports small, reviewable iterations while preventing downstream artifacts from being finalized before their required inputs are sufficiently stable.
- **Reason:** Itqan has evolving requirements, AI feasibility uncertainty, UI prototyping needs, cross-artifact dependencies, and formal IS498 deliverables that require documented review points.
- **Source/Evidence:** Official IS498/IS499 Graduation Project Handbook; current project context, open questions, dependency rules, and GitHub workflow.
- **Affected artifacts:** Project plan, Gantt chart, resource schedule, risk register, requirements, diagrams, UI/UX, architecture, test plan, IS498 report, and IS499 implementation workflow.
- **Notes:** This is not a claim of strict Scrum. Iteration duration, review frequency, formal roles, and gate approval criteria require team and advisor review before confirmation.
