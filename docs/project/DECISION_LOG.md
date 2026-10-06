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
- **Status:** 🟢 Confirmed
- **Decision:** Use an Iterative Agile Software Development Life Cycle with Academic Phase Gates. Requirements may evolve during the project, especially due to AI feasibility and validation. An iterative approach supports continuous refinement and validation, while academic phase gates provide clear boundaries between IS498 analysis/design and IS499 implementation.
- **Reason:** Itqan has evolving requirements, AI feasibility uncertainty, UI prototyping needs, cross-artifact dependencies, and formal IS498 deliverables that require documented review points.
- **Source/Evidence:** Official IS498/IS499 Graduation Project Handbook; current project context, open questions, dependency rules, and GitHub workflow.
- **Affected artifacts:** Project plan, Gantt chart, resource schedule, risk register, requirements, diagrams, UI/UX, architecture, test plan, IS498 report, and IS499 implementation workflow.
- **Notes:** This is not a claim of strict Scrum. Iteration duration, review frequency, formal roles, and gate approval criteria require team and advisor review before confirmation.

### 2026-09-22 — Class Enrollment Mechanism (Join Code)
- **Status:** 🟢 Confirmed
- **Decision:** Learners join a class by entering a teacher-provided class join code. Teachers do not directly add students to a class. "Add Students to Class" is removed as a Teacher use case and replaced with "Join Class via Code" (UC-26) as a Quran Reader use case.
- **Reason:** Aligns the approved Use Case Diagram and FR-24 with the already-implemented architecture/ERD decision (no invitation-link path; join-code based enrollment). Resolves a prior inconsistency between FR-24's wording, the Use Case Diagram, and the ERD/relational schema.
- **Source/Evidence:** docs/report/architecture-artifact-corrections.md; docs/database/RELATIONAL_SCHEMA.md (LEARNING_CLASS.join_code); team decision, 2026-09-22.
- **Affected artifacts:**
  1. docs/project/REQUIREMENTS.md — FR-24 wording + RTM row for FR-24 (updated)
  2. Itqan_Use_Case_Diagram_v2.svg — "Add Students to Class" bubble removed from Teacher side; "Join Class via Code" added under Quran Reader (updated)
  3. Use Case Scenario UC-26 — Join Class via Code, Actor: Quran Reader (drafted)
- **Notes:** This also resolves the previously-flagged contradiction in Activity Diagram 02's footnote ("does not assume invitations, messages, or adding students") — that footnote is now consistent with the confirmed design and requires no further correction.

### 2026-09-22 — Use Case Diagram Naming Cleanup
- **Status:** 🟢 Confirmed
- **Decision:** Renamed four Teacher-side use case labels on the diagram to match RTM/scenario wording: "Teacher Dashboard" → "View Teacher Dashboard", "Student Recitation Activity" → "View Student Recitation Activity", "Student Completion" → "View Student Completion", "Student Score" → "View Student Score". Also standardized the Quran Reader actor's use case scenarios to use "Quran Reader" (matching the diagram's actor label) instead of "Reader".
- **Reason:** Appendix R requires identical terminology across requirements, diagrams, and scenarios; these were the only remaining naming mismatches found during the Use Case Scenario cross-check.
- **Source/Evidence:** Use Case Scenario cross-check, 2026-09-22.
- **Affected artifacts:** Itqan_Use_Case_Diagram_v2.svg (updated); Use Case Scenarios UC-02 through UC-27 (actor line only).

### 2026-09-22 — Smart Prompting Confirmed as Scope (FR-26)
- **Status:** 🟢 Confirmed
- **Decision:** Smart Prompting is confirmed as an approved feature of Itqan. Added FR-26 — Receive Smart Prompting: "The system shall provide smart prompting when the user pauses, hesitates, or appears to forget during Quran recitation." Priority: Should Have.
- **Reason:** Resolves OQ-22. "Receive Smart Prompting" and "Generate Smart Prompt" already existed on the approved Use Case Diagram and the ERD's PAUSE_EVENT design already assumed this behavior, but no FR backed them. FR-26 is kept distinct from FR-17 (Provide Audio Assistance), which is scoped to detected recitation errors only — Smart Prompting covers pause/hesitation/forgotten-recitation, matching the original problem statement.
- **Source/Evidence:** OQ-22; team decision, 2026-09-22.
- **Affected artifacts:**
  1. docs/project/REQUIREMENTS.md — FR-26 added (§10 new "G. Recitation Assistance" category); Prioritization table and summary updated (Should Have: 6→7); RTM row added
  2. docs/database/ERD_REQUIREMENTS_TRACEABILITY.md — FR-26 row added, linked to PAUSE_EVENT, RECITATION_SESSION, RECITATION_SEGMENT; PAUSE_EVENT reverse-index updated; coverage statement updated to FR-01–FR-26
  3. docs/project/OPEN_QUESTIONS.md — OQ-22 marked 🟢 Resolved
  4. Use Case Scenario UC-28 — Receive Smart Prompting, Actor: Quran Reader (drafted)
- **Notes:** No changes needed to the Use Case Diagram itself — "Receive Smart Prompting" and "Generate Smart Prompt" were already present and correctly related (`<<extend>>` from Receive Recitation Feedback); they now have a backing FR.


### 2026-09-27 — Recitation Analysis Model Selection
- **Status:** 🟢 Confirmed
- **Decision:** The phase-one recitation analysis model is `obadx/muaalem-model-v3_2`, based on `facebook/w2v-bert-2.0`, under the MIT license. It is used as the speech-analysis component for Quranic phoneme and articulation analysis.
- **Reason:** The model is directly associated with Quranic pronunciation-error detection, is openly licensed under MIT, and already matches the selected server-side analysis architecture. The associated paper describes a Quran-specific phonetic representation and reports 0.16% average phoneme error rate on its reported test set. These published results are model evidence, not a guarantee of Itqan performance; Itqan must evaluate the integrated system on its own test data in IS499.
- **Source/Evidence:** Hugging Face model card and arXiv paper: https://huggingface.co/obadx/muaalem-model-v3_2 ; https://arxiv.org/abs/2509.00094 (verified 2026-09-27).
- **Affected artifacts:** System Architecture and Technology Stack, Open Questions OQ-09, Requirements/RTM references where model identification is stated, IS499 evaluation/test plan, report references.
- **Notes:** The model choice does not authorize claims of perfect Tajweed detection or 100% accuracy. Published evaluation scope and limitations must be reported accurately.

### 2026-09-27 — Architecture Consistency Correction v2
- **Status:** 🟢 Confirmed
- **Decision:** The final architecture correction explicitly supersedes conflicting wording in the retained architecture PDF. Teacher enrollment uses a join code, not an invitation/acceptance flow; FR-23 to FR-26 are included in architecture traceability; IS499 evaluation data is described as evaluation activity rather than user research; production hosting remains deferred; and the selected Muaalem model is the authoritative recitation-analysis model.
- **Reason:** The architecture PDF was structurally sound but contained several stale phrases that conflicted with the approved requirements, join-code decision, or current implementation boundary.
- **Affected artifacts:** system-architecture.pdf, system-architecture-correction.pdf, OPEN_QUESTIONS.md, report architecture section.
