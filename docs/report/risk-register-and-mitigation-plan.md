# Itqan Risk Register and Mitigation Plan

**Status:** Proposed - team and advisor review required

**Primary owner:** Abdulaziz Alfarhood

**Last updated:** 2026-09-17

## Purpose

This register identifies risks that could affect Itqan's IS498 analysis and design deliverables or its IS499 implementation, testing, and evaluation. It is based on the approved project scope, the current functional and non-functional requirements, the proposed architecture, and the Phase One project plan.

The register is reviewed in the weekly team/advisor meeting. A risk owner reports changes in likelihood, impact, mitigation progress, and any triggered contingency action. New risks are added with evidence; closed risks remain recorded with their outcome.

## Assessment Method

Likelihood and impact use a 1-5 scale. The risk score is `likelihood x impact`.

| Score | Rating | Required response |
|---:|---|---|
| 1-4 | Low | Monitor during normal project reviews. |
| 5-9 | Medium | Assign an owner and complete mitigation before the related deliverable is finalized. |
| 10-15 | High | Discuss in the next team/advisor meeting and track mitigation weekly. |
| 16-25 | Critical | Escalate immediately; do not proceed with the affected scope without a documented decision. |

## Risk Register

| ID | Risk | L | I | Score | Owner | Early warning / trigger | Mitigation | Contingency | Related scope |
|---|---|:---:|:---:|:---:|---|---|---|---|---|
| R-01 | Recitation analysis does not identify pronunciation or Tajweed errors with sufficient accuracy. | 4 | 5 | 20 Critical | Saud with team | Prototype results are inconsistent, or evaluation data shows unreliable error detection. | Define a measurable evaluation protocol; test a narrow set of supported errors first; state limitations rather than claiming complete Tajweed coverage. | Reduce the supported error set, change the feedback to confidence-aware guidance, and document the limitation in the report. | FR-08, FR-13 to FR-16, NFR-01 |
| R-02 | Audio analysis and feedback are too slow for a usable active recitation session. | 4 | 4 | 16 Critical | Saud | Measured processing delay interrupts the learner's recitation or requires repeated waiting. | Prototype end-to-end audio flow early; measure latency by stage; keep Juz Amma as the initial scope; evaluate near-real-time feedback if strict real time is not feasible. | Change to short audio segments or end-of-verse feedback and update the NFR claim accordingly. | FR-12 to FR-18, NFR-02, NFR-03 |
| R-03 | The AI model, dataset, or Tajweed-detection approach proves unsuitable, unavailable, or insufficiently documented. | 4 | 5 | 20 Critical | Saud | No validated model/dataset is found, licensing is unclear, or a proof of concept cannot meet the selected capability. | Compare feasible approaches using verified sources; record selection criteria, dataset licence, language coverage, and limitations before committing to the architecture. | Use a smaller justified prototype capability, substitute a documented alternative, or defer unsupported detection to future work. | FR-08, FR-13 to FR-16, NFR-01, NFR-08 |
| R-04 | Recitation audio or personal data is collected, stored, or retained without adequate privacy controls or consent. | 3 | 5 | 15 High | Abdulaziz with Saud | The design has no consent step, retention rule, access control, or documented data flow for audio. | Define the minimum data collected; document consent, retention, access, deletion, and secure transport/storage requirements before implementation. | Disable persistent audio storage and retain only the minimum session metadata until controls are approved. | FR-01 to FR-03, FR-12, NFR-06, NFR-07 |
| R-05 | Teacher monitoring exposes learner performance to an unauthorized teacher or class. | 3 | 5 | 15 High | Ibrahim with team | The teacher-learner relationship, class membership, or authorization rule is still undefined. | Obtain a team decision on teacher-class-learner association; model authorization in the use cases, ERD, UI, and test plan. | Limit teacher mode to demonstration data until a defensible access model is approved. | FR-10, NFR-06, NFR-07 |
| R-06 | Requirements and diagrams become inconsistent because key decisions remain unresolved. | 4 | 4 | 16 Critical | Ibrahim with team | A requirement conflicts with a diagram, UI screen, architecture decision, or test case; unresolved items are presented as final. | Use the decision log and traceability table; review affected artifacts together whenever scope changes; label proposed and unresolved items clearly. | Freeze the affected artifact as a draft and correct dependent artifacts before the next submission review. | All FRs/NFRs; IS498 report |
| R-07 | Scope expands beyond a feasible graduation-project implementation. | 4 | 4 | 16 Critical | Team | Requests add full-Quran coverage, external-app integration, AI agents, or unplanned dashboard/gamification features. | Keep the initial release to Juz Amma; prioritize Must Have requirements; treat integrations and unapproved features as future vision. | Remove lower-priority features and preserve the required learner recitation path as the MVP. | Scope boundaries; prioritization |
| R-08 | The Mastery Score is presented as meaningful without validation evidence. | 3 | 4 | 12 High | Ibrahim with Saud | The FR-20 formula is defined, but its interpretation and performance have not been evaluated. | Evaluate the formula and document its limitations before presenting scores as validated assessments. | Label the score as an experimental prototype metric until evaluation is complete. | FR-20, FR-21, NFR-01 |
| R-09 | User research and competitive claims lack evidence or use fabricated findings. | 3 | 4 | 12 High | Ibrahim | Report sections contain unverified interview results, survey statistics, competitor claims, or unsupported user needs. | Use an approved research plan; retain sources and research evidence; distinguish planned research from completed research. | Remove unsupported claims and describe them as assumptions or open questions until evidence exists. | User research, gap analysis, report |
| R-10 | The team misses IS498 deliverables because dependent work starts before inputs are approved. | 3 | 4 | 12 High | Abdulaziz with team | UI, ERD, test plan, or diagrams need repeated rework after requirements/architecture changes. | Follow the Phase One dependency gates; maintain a weekly workboard; review blockers with the advisor. | Re-sequence work, reduce lower-priority scope, and focus on submission-critical artifacts first. | Phase One plan, all deliverables |
| R-11 | Device microphone, Arabic language support, or network conditions prevent reliable use on target mobile devices. | 3 | 4 | 12 High | Saud | Audio capture fails on a target device, Arabic transcription is weak, or network-dependent analysis is unavailable. | Define target devices and minimum microphone/network assumptions; test Arabic audio capture and failures early; provide clear user-facing error handling. | Support the tested device set only for the prototype and document compatibility limits. | FR-12, NFR-05, NFR-10, NFR-11 |
| R-12 | Quran text, recitation content, or external services are used without a verified source or permitted usage. | 2 | 5 | 10 High | Saud with Ibrahim | The chosen Quran source/API has unclear provenance, licence, accuracy, or availability. | Select and document an authoritative source; verify terms, attribution, versioning, and fallback availability before integration. | Replace the source with a verified alternative and delay dependent features until the content is validated. | FR-04 to FR-06, NFR-05, NFR-07 |
| R-13 | The final prototype is difficult for learners to understand or use during recitation. | 3 | 4 | 12 High | Abdulaziz | Users cannot find the Surah/mode/session controls, or feedback disrupts practice. | Build user flows and wireframes from approved use cases; run heuristic evaluation; test the critical learner journey before finalizing the prototype. | Simplify the session screen and defer nonessential controls. | NFR-04, learner UI/UX |
| R-14 | Individual contribution and decision evidence are insufficient for assessment. | 2 | 4 | 8 Medium | Team | Work is not committed, ownership is unclear, or meetings/feedback are not recorded. | Use task branches, focused commits, pull requests, decision log entries, and weekly progress notes. | Reconstruct evidence from Git history and advisor/team records before submission. | IS498 assessment and report |

## Immediate Actions

| Priority | Action | Owner | Due before |
|---|---|---|---|
| Critical | Validate a feasible Arabic recitation-analysis approach and define supported error scope. | Saud with team | Architecture and NFR approval |
| Critical | Decide whether near-real-time feedback is technically feasible and measurable. | Saud | Prototype/architecture review |
| Critical | Approve the teacher-learner authorization and class relationship. | Ibrahim with team | ERD, teacher UI, and test-plan work |
| High | Define consent, audio retention, and deletion expectations. | Abdulaziz with Saud | Architecture and privacy review |
| High | Evaluate the defined Mastery Score formula and its interpretation. | Ibrahim with Saud | Results UI and test-plan work |
| High | Confirm the learner journey through a wireframe and heuristic review. | Abdulaziz | Prototype completion |

## Review Log

| Date | Reviewed by | Changes / decision | Next review |
|---|---|---|---|
| 2026-09-17 | Abdulaziz | Initial proposed register created from current repository artifacts. | Next team/advisor meeting |

## Source Basis

- Official IS498/IS499 Graduation Project Handbook.
- `docs/project/REQUIREMENTS.md`.
- `docs/project/PROJECT_CONTEXT.md`.
- `docs/project/OPEN_QUESTIONS.md`.
- `docs/report/development-methodology.md`.
- `docs/report/phase-one-project-plan.md`.
- `docs/system-architecture.pdf`.
