# Development Methodology and Justification

**Status:** 🟡 Proposed

**Owner:** Abdulaziz Alfarhood

**Last updated:** 2026-09-16

## Purpose

This section proposes how the Itqan team will organize analysis, design, development, review, and testing across IS498 and IS499. It is based on the official IS498/IS499 Graduation Project Handbook and the current project context recorded in this repository. The methodology remains proposed until it is reviewed by the team and, where required, the project advisor.

## Selected Methodology

Itqan will use an **iterative Agile software development life cycle with academic phase gates**. The team will work in small, reviewable iterations instead of attempting to finalize the complete system in one pass. Each iteration will select justified work, produce or revise an artifact, review it against its dependencies and evidence, and record significant decisions before approved work is merged.

This is an Agile approach rather than a claim that the team follows strict Scrum. The project has not assigned formal Scrum roles or fixed sprint durations, so those details will not be stated unless the team approves them.

Academic phase gates will ensure that iteration does not bypass required IS498 outputs. Downstream artifacts will be finalized only when their required inputs are sufficiently stable. Draft work may begin earlier when it is clearly labeled as a draft.

## Justification

### Evolving requirements

Several project decisions remain unresolved, including the final functional and non-functional requirements, detailed behavior of the AI modes, teacher workflow, technology stack, database schema, and AI feasibility. The defined Mastery Score formula still requires evaluation. An iterative approach allows the team to refine these decisions as research, prototyping, technical investigation, and advisor feedback provide better evidence.

### AI and technical uncertainty

Itqan depends on capabilities such as Arabic speech processing, Tajweed-error detection, feedback, and Smart Prompting. Their accuracy and real-time performance must be tested rather than assumed. Iteration allows technical findings to influence scope, architecture, requirements, and test criteria without presenting unverified capabilities as completed features.

### UI and user-flow validation

The user journeys, interface, and clickable prototype must remain consistent with approved actors, requirements, and use cases. An iterative process supports early drafts, team review, and revision before the interface is treated as final.

### Parallel teamwork with dependencies

The project responsibilities are distributed among Ibrahim, Saud, and Abdulaziz, but many outputs depend on one another. Iterative planning allows independent work to proceed in parallel while academic phase gates protect consistency between requirements, use cases, diagrams, architecture, UI screens, database design, and testing.

### Academic traceability

The handbook requires planning, analysis and design artifacts, a development methodology, a test plan, impact analyses, a report, and regular advisor follow-up. The proposed approach combines flexible iteration with explicit review points so that changes remain documented and required deliverables are not omitted.

## Iteration Workflow

Each iteration will use the following workflow:

1. **Select justified work:** Choose a task whose required inputs are available, or label the output as a draft when an input is still unresolved.
2. **Confirm dependencies:** Check the project context, decision log, open questions, requirements, and related artifacts before starting.
3. **Produce the smallest reviewable output:** Create or revise one focused artifact, feature, diagram, research result, or test definition.
4. **Review and verify:** Check the output for accuracy, evidence, consistency with connected artifacts, and compliance with the handbook.
5. **Collect feedback:** Obtain team and advisor feedback when the output affects project scope, academic requirements, or another member's work.
6. **Record changes:** Update affected artifacts and record significant approved or proposed decisions.
7. **Merge approved work:** Commit the work on a task branch, open a pull request, review it, and merge it into the main branch after approval.

## Proposed Academic Phase Gates

The following gates define when major downstream work can be finalized. They do not prevent clearly labeled drafts.

### Requirements Gate

Actors, scope, functional requirements, and non-functional requirements are reviewed before finalizing use cases, detailed UI flows, architecture, database design, or the test plan.

### Analysis and Design Gate

Use cases and significant scenarios are reviewed before finalizing activity and sequence diagrams. Data requirements and the ERD are reviewed before finalizing the relational schema and class diagram.

### Prototype Gate

Main user journeys and their related use cases are reviewed before finalizing wireframes and the clickable prototype. The prototype is then checked for consistency and usability before heuristic evaluation.

### Test Planning Gate

Requirements and measurable non-functional requirements are reviewed before finalizing the test plan. Each planned test must trace to an approved requirement or a justified quality objective.

### IS498 Submission Gate

The team reviews the required report sections, diagrams, prototype, planning artifacts, impact analyses, references, and contribution evidence before the IS498 submission and presentation.

## Team Coordination

Team members may work in parallel where dependencies allow. Ownership identifies primary responsibility but does not prevent collaboration or reassignment. Work that affects another member's artifact must be reviewed with that member before it is treated as final.

The team will use its regular meetings and the required advisor follow-up to review progress, blockers, risks, proposed changes, and upcoming dependencies. Exact meeting schedules and iteration durations will be documented only after team approval.

## GitHub Workflow

GitHub provides version control and evidence of individual contribution. The working sequence is:

```text
Task selection → task branch → focused changes → self-review → commit → push → pull request → team review → merge
```

Branches should represent tasks or deliverables rather than permanent ownership. Commit messages should state the completed change, and pull requests should identify dependencies, evidence status, and any unresolved decisions.

## Change and Evidence Control

The team will classify information as confirmed, proposed, or unresolved. Proposed or unresolved information will not be silently presented as confirmed. When a change affects scope, requirements, diagrams, architecture, UI, database design, testing, schedule, or risks, the connected artifacts must be reviewed and updated together.

Claims about AI accuracy, Tajweed detection, real-time performance, competitor capabilities, or user-research results require evidence. The team will document limitations and will not claim that unimplemented or unevaluated functionality is complete.

## Quality Controls

Quality will be supported through:

- dependency and consistency checks between related artifacts;
- team review through pull requests;
- advisor feedback at appropriate review points;
- requirement traceability for tests and system artifacts;
- prototype review and heuristic evaluation;
- documented decisions, risks, changes, and limitations; and
- testing of implemented capabilities during IS499.

## Application Across IS498 and IS499

During IS498, iteration focuses on research, requirements, analysis, design, planning, prototype development, test planning, impact analysis, and report preparation. During IS499, the same workflow continues through implementation, integration, testing, deployment, evaluation, and final documentation. Findings from IS499 may require justified updates to earlier artifacts, with those changes recorded through the same decision and review process.

## Approval Required

Before this methodology is marked as confirmed, the team should approve:

- the iterative Agile approach with academic phase gates;
- how often iterations and internal reviews occur;
- how advisor feedback is incorporated;
- whether any formal Agile roles are needed; and
- the point at which each phase gate is considered satisfied.

## Source Basis

- Official IS498/IS499 Graduation Project Handbook.
- `README.md`.
- `docs/project/PROJECT_CONTEXT.md`.
- `docs/project/DECISION_LOG.md`.
- `docs/project/OPEN_QUESTIONS.md`.
