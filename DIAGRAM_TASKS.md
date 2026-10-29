# Itqan required diagram and design tasks

Rebuild every drawing from scratch using [Itqan_Requirements.md](Itqan_Requirements.md). Old drawings are historical references only.

This list covers the diagram and design deliverables explicitly required for Track A by the Graduation Project Handbook §§13.1–13.2 (pages 18–19), with scenario coverage from Appendix R (page 76). It is not the complete checklist for the report or course.

## How to use

- Add your name to claim a task.
- Status: Open → In progress → Review → Done. Use Blocked when necessary.
- “Needs first” means those inputs must be reviewed before finalizing. Drafts can start earlier.
- Save editable drawing sources and SVG exports in `docs/updated-diagrams/`, except the Task 6 ERD SVG at the repository root. Put output links in the last column.

## Required tasks

| Task | Deliverable | What to produce | Needs first | Owner | Status | Output / notes |
|---|---|---|---|---|---|---|
| 1 | Written use-case scenarios | Review the flows already in requirements §7.3. Cover every catalogue use case with its conditions, steps, exceptions and outcome. | New requirements | saud | Review | [USE_CASE_SCENARIOS.md](docs/updated-diagrams/scenarios/USE_CASE_SCENARIOS.md): all 22 use cases; 5 gaps decided and added to the requirements |
| 2 | Use Case Diagram | Quran Reader and Teacher; exact use-case names, IDs and include/extend relationships from §7.1–7.2. | New requirements | saud | closed | [itqan-use-case.puml](docs/updated-diagrams/use-case/itqan-use-case.puml) · [SVG](docs/updated-diagrams/use-case/itqan-use-case.svg) · [review notes](docs/updated-diagrams/use-case/USE_CASE_REVIEW.md) |
| 3 | Activity Diagrams | Main learner and teacher workflows, including decisions and exceptions. Use readable separate views for independent processes. BPMN or an equivalent notation is also accepted by the handbook. | 1 | saud | Review | [activity/](docs/updated-diagrams/activity/): ACT-01a, 01b, 02, 03, 04 · [review notes](docs/updated-diagrams/activity/ACTIVITY_REVIEW.md) |
| 4 | System architecture and technology justification | Parts, responsibilities and connections from §10; processing and storage boundaries; reasons for the technology choices. | New requirements | saud | Review | [itqan-architecture.puml](docs/updated-diagrams/architecture/itqan-architecture.puml) · [SVG](docs/updated-diagrams/architecture/itqan-architecture.svg) · [architecture + justification](docs/updated-diagrams/architecture/ARCHITECTURE.md) |
| 5 | Sequence Diagrams | Interactions for every significant scenario. Cover recitation and its endings/failures; assess class access, enrolment, messaging, consent and deletion for separate sequences. Record the scenario coverage. | 1, 4 | — | Open | |
| 6 | ERD | Required stored data, keys, relationships and cardinalities from §8. Exclude prohibited stored data. | New requirements | Abdulaziz Alfarhood | Done | [editable ERD](docs/updated-diagrams/erd/itqan-erd.mmd) · [open SVG full size](https://raw.githubusercontent.com/IbrahimFyz/Itqan/feature/project-rework/itqan-erd.svg). All §8.1 stored fields and §8.2 relationships are shown; derived progress has no cache. Reviewed by Abdulaziz on 2026-10-29; report placement remains. |
| 7 | Relational schema | Tables, fields, primary/foreign keys, nullability and constraints matching the ERD. | 6 | Abdulaziz Alfarhood | Review | [Itqan_Relational_Schema.md](Itqan_Relational_Schema.md) |
| 8 | Class Diagram | Essential classes, attributes, operations, responsibilities and relationships. Use multiple views only when needed for readability. | 1, 4 | — | Open | |
| 9 | Clickable wireframes / UI prototype | Principal journeys for both roles, including consent, recitation/results, class access, messaging and account controls. Include relevant error and empty states. | 1, 3 | — | Open | |
| 10 | Time and resource schedule | Work packages, owners, durations, dependencies and milestones using a project-management tool. A Gantt chart is an accepted format. | Team-agreed work packages and timing | — | Open | |

## Starting order

1. Start **1, 2, 4 and 6** together. Task **10** can start when the team agrees its schedule.
2. After **1**, start **3**. After **1 and 4**, start **5 and 8**.
3. After **6**, start **7**. After **1 and 3**, start **9**.

Tasks **5, 6 and 8** develop together: review sequence messages, data and class responsibilities for consistency. A finished Activity Diagram or ERD is not a universal prerequisite for a Sequence Diagram.

## Before marking a task Done

- [ ] Matches the new requirements and requirements §13 checklist.
- [ ] Agrees with related diagrams, scenarios, schema and prototype.
- [ ] Uses correct notation and remains readable at report size. Split crowded views instead of shrinking text.
- [ ] Editable source and readable export are linked above.
- [ ] Another team member has reviewed it.
- [ ] Its report figure, explanation and references are updated where applicable.

The handbook also requires a test plan and other report/course deliverables; those are outside this diagram and design task list. Separate DFDs, User Flow Diagrams, state machines and API contracts are not included here.

## Task instructions

### Task 1 — Written use-case scenarios

**Purpose:** explain what happens when a user tries to achieve each goal. This is written documentation, not a drawing.

**Read first:** requirements §7, plus the FRs and business rules referenced by each use case.

**What to do:**
1. Make a list of every use case in §7.1 using its exact ID and name.
2. Review the existing flows in §7.3 rather than inventing new flows.
3. For each use case, document the actor, trigger, preconditions, numbered main steps, alternative/error paths, and final outcome.
4. Link it to the relevant FR and BR IDs. Flag missing or conflicting behavior for resolution in the requirements.

**Example:** Recite Surah needs a Reader account and consent; it selects a surah and mode, checks microphone permission, analyses verses, and ends with saved results. Denied permission, failed verse analysis, interruption and zero counted words need their own paths.

**Deliver:** an editable Markdown file with one compact scenario table or section per use case.

**Done when:** every catalogue use case is covered, and another person can build its activity/sequence diagram without guessing its behavior.

### Task 2 — Use Case Diagram

**Purpose:** show who uses Itqan and which goals each role can achieve. It does not show the chronological steps of recitation.

**Read first:** requirements §2 and §7.1–7.2.

**What to do:**
1. Draw a system boundary labelled Itqan.
2. Put Quran Reader and Teacher outside the boundary and the catalogue use cases inside it.
3. Connect each role to its permitted use cases.
4. Add only the include/extend relationships specified in §7.2. Include points toward the included use case; extend points toward the base use case.
5. Keep processing steps such as capture, analysis, scoring and saving out of the use-case list. AI modes are not actors.

**Deliver:** editable source and an SVG; use separate readable views if needed without changing the underlying model.

**Done when:** IDs, names, role associations and relationships match the requirements exactly.

### Task 3 — Activity Diagrams

**Purpose:** show the order of actions, decisions, repetition and exceptions in a workflow.

**Read first:** reviewed Task 1 and requirements §7.3.

**What to do:**
1. Start with two workflow groups: Reader recitation and Teacher class/monitoring. Separate independent flows when necessary.
2. Draw the start, main actions, decisions with labelled conditions, loops, and end points.
3. Use swimlanes if they help distinguish user actions from system actions.
4. For recitation, cover selection, consent/permission, per-verse processing, feedback while reading continues, requested audio, automatic prompting, and all session endings.
5. For teacher workflows, cover class creation/renaming, reader enrolment/consent, permitted monitoring and messaging. Show access denial when enrolment ends.
6. Put long secondary flows in a separate view instead of filling one page with every detail.

**Deliver:** editable sources and SVGs, each labelled with the use cases it covers.

**Done when:** every decision has clear outcomes and each path ends or returns to a valid step. No path implies that the Reader must stop after every verse for feedback.

### Task 4 — System architecture and technology justification

**Purpose:** show the major parts of Itqan, where they run, and how they communicate.

**Read first:** requirements §10, §8 and the non-functional requirements.

**What to do:**
1. Group the parts by phone, backend, managed identity provider, analysis service and database.
2. Use the exact names and responsibilities in §10. Place Comparison Engine inside Recitation Service.
3. Draw and label major connections. All session traffic passes through Recitation Service.
4. Show bundled Quran text and reference audio, including offline reading and word-audio assistance.
5. Distinguish temporary audio/phoneme processing from stored summaries and mistakes. Never draw an audio-storage path to the database.
6. Add a short explanation of why the stated Flutter, FastAPI, PostgreSQL and analysis-service choices fit the requirements. Compare relevant alternatives without presenting assumptions as facts.
7. Keep hosting and identity-provider vendor generic where §11 leaves them open.

**Deliver:** editable architecture source, SVG and a short technology-justification section.

**Done when:** the diagram accounts for every §10 part and its connections support the specified workflows and privacy rules.

### Task 5 — Sequence Diagrams

**Purpose:** show how participants exchange messages to deliver a particular scenario.

**Read first:** Tasks 1 and 4; requirements §10. Coordinate with Tasks 6 and 8.

**What to do:**
1. Make a scenario-coverage list. Identify the significant scenarios that need sequence diagrams; record why a scenario is covered in another view or does not need a separate one.
2. Begin with Recite Surah, then cover significant enrolment/access, messaging, consent and deletion scenarios in separate diagrams as needed.
3. Put the user and relevant §10 system parts across the top. Place messages from top to bottom in execution order.
4. For recitation, use App → Recitation Service → Analysis Service → Recitation Service/Comparison Engine → App; show final storage and progress recalculation.
5. Use loop fragments for per-verse repetition and alt/opt fragments for supported alternatives. Show interrupted sessions, failed analysis and no-score results without inventing recovery rules.
6. Keep message names consistent with component responsibilities and Class Diagram operations.

**Deliver:** one source and SVG per diagram, plus the scenario-coverage list.

**Done when:** every significant scenario has coverage, messages follow the agreed architecture, and temporary data is not shown as persisted.

### Task 6 — Entity-Relationship Diagram

**Purpose:** describe the data the system keeps and how records relate. It is not a processing-flow diagram.

**Read first:** requirements §8, relevant business rules, and §9 lifecycle rules.

**What to do:**
1. Turn the required stored-data groups in §8.1 into an appropriate entity model.
2. Show identifiers, key fields, relationships, cardinalities and optionality using one consistent ERD notation.
3. Include accounts/Teacher detail, consent, Quran reference data, sessions, mistakes, classes, enrolments, messages/recipients and the anonymous deletion log.
4. Support repeated enrolments with new join dates, one active enrolment per reader/class, and per-recipient read dates.
5. Label derived progress separately from source data; identify any cache as a cache. Distinguish bundled content from server database storage.
6. Exclude everything prohibited by §8.3. Do not copy obsolete entities from the old ERD.
7. Coordinate deletion behavior and account/class relationships with FR-28; flag any ambiguity before finalizing.

**Deliver:** editable ERD source and SVG, with readable detail views if necessary.

**Done when:** every required stored item is accounted for and relationships support the required access, history, messaging and deletion behavior.

### Task 7 — Relational schema

**Purpose:** translate the ERD into precise database table definitions. This is usually a set of tables in Markdown, not another UML diagram.

**Read first:** reviewed Task 6, requirements §8 and applicable business rules.

**What to do:**
1. Define each table and its fields, data types, primary key and foreign keys.
2. Specify required/optional fields, uniqueness, allowed values and other constraints.
3. Explain how relationships, active-enrolment uniqueness and conditional Tajweed-rule fields are enforced.
4. Document deletion effects and ensure the anonymous deletion log cannot identify an account.
5. List bundled reference structures and optional derived caches separately.

**Deliver:** an editable Markdown schema/data dictionary matching the ERD.

**Done when:** every ERD entity/relationship has a matching definition and a developer can implement it without guessing the basic constraints.

### Task 8 — Class Diagram

**Purpose:** show the software’s main classes, their responsibilities and relationships. Classes are not automatically database tables.

**Read first:** Tasks 1 and 4; requirements §8–§10. Coordinate with Tasks 5 and 6.

**What to do:**
1. Identify the main domain classes and the service responsibilities needed to deliver the scenarios.
2. Add essential attributes and operations only. Avoid listing every getter, setter or implementation helper.
3. Draw supported associations, multiplicities and dependencies using correct UML notation. Use inheritance/composition only where their meaning is justified.
4. Align service operations with sequence messages and persistent fields with the ERD.
5. Explain any ERD entity without a corresponding class, as Appendix R requests.
6. Split into readable views if needed; repeated classes must refer to the same definitions. Do not introduce prohibited persisted data as new classes.

**Deliver:** editable source and SVG views describing one consistent model.

**Done when:** classes explain the scenario responsibilities, agree with the data model and sequence diagrams, and contain no speculative features.

### Task 9 — Clickable wireframes / UI prototype

**Purpose:** demonstrate how both roles operate the system through screens. A prototype demonstrates the design, not working AI analysis.

**Read first:** Tasks 1 and 3; relevant interface, language and usability requirements.

**What to do:**
1. Build fresh wireframes for the principal Reader and Teacher journeys.
2. Connect screens so the team can click through registration/login, reading, surah → mode → recitation → results, history/progress, classes and messages.
3. Include profile, privacy/consent, account deletion and logout routes, plus relevant refusal/error/empty states.
4. Preserve Teacher access limits, one-way messaging, and the separation between requested audio and automatic prompting.
5. Support the Arabic-first RTL design and show how English is accommodated. Use labelled demonstration data.
6. Export readable screenshots for the report and map each screen to its use case. Ensure each use case is represented by an appropriate screen or interaction.

**Deliver:** editable wireframes, a working clickable prototype link/file, report screenshots and a brief screen-to-use-case mapping.

**Done when:** another team member can complete the principal journeys without explanation, and the screens agree with the requirements and workflow diagrams.

### Task 10 — Time and resource schedule

**Purpose:** show when work happens, who is responsible, and which work must finish before other work can finish. A Gantt chart is an accepted format.

**Read first:** the team’s agreed work packages, available resources, academic deadlines and dependencies in this board.

**What to do:**
1. List the IS498 work packages, including work outside the drawing tasks, and assign owners.
2. Agree durations, available resources, start/end timing and milestones.
3. Show dependencies and realistic overlaps in a project-management tool.
4. Use relative weeks if calendar dates are not agreed; do not invent deadlines or completion claims.
5. Keep the schedule editable and update actual progress during the project.

**Deliver:** editable project schedule and a readable report export, with owners and resource allocation.

**Done when:** timing and resources are agreed by the team and the chart matches the underlying work-package list and dependencies.
