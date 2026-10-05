# Phase One Project Plan

**Status:** 🟡 Proposed

**Phase:** IS498

**Planning basis:** 15 relative weeks

**Last updated:** 2026-09-16

## Purpose

This document provides the initial work breakdown, week-based Gantt schedule, resource schedule, dependencies, and review points for Itqan Phase One. Week numbers are temporary and will be replaced with calendar dates when the current academic calendar and project deadlines are confirmed.

Phase One covers IS498 analysis, requirements, design, planning, prototype work, test planning, impact analysis, report preparation, and presentation preparation. Detailed IS499 implementation scheduling is outside this plan.

## Planning Assumptions

- Phase One is planned across 15 relative weeks, following the duration proposed in the project presentation.
- The official handbook controls the submission timing: the report is due by Tuesday of the week before the preparatory week, and the presentation occurs during the preparatory exam week.
- The team meets the project advisor weekly.
- Dates, durations, and overlaps remain proposed until reviewed by the team and advisor.
- Draft downstream work may begin early, but it is not finalized before its required inputs are stable.
- Ownership identifies the primary contributor; team members may collaborate or reassign work when needed.

## Work Breakdown

| ID | Work package | Primary owner | Planned weeks | Main output | Depends on |
|---|---|---|---|---|---|
| P1 | Project setup, methodology, initial planning, and risk identification | Abdulaziz | 1-3 | Methodology, planning baseline, initial risks | Confirmed project scope |
| P2 | Stakeholders, target users, and user research planning | Ibrahim | 1-4 | Stakeholder and target-user analysis | Project problem and scope |
| P3 | Existing-solutions research and comparison | Saud | 1-5 | Verified comparison of existing solutions | Research sources |
| P4 | Problem statement, objectives, scope, and gap analysis | Ibrahim | 3-6 | Formal problem, objectives, scope, and gap | P2, P3 |
| P5 | Functional and non-functional requirements | Ibrahim | 4-7 | Reviewed FRs and NFRs | P2, P4 |
| P6 | Prioritization and traceability | Ibrahim | 6-8 | Prioritized requirements and traceability | P5 |
| P7 | Use cases, scenarios, and use-case diagram | Ibrahim | 6-9 | Reviewed use cases and scenarios | P5, P6 |
| P8 | Architecture, technology assessment, and data flow | Saud | 6-10 | Proposed architecture and justified technology direction | P5 |
| P9 | Main user journeys and user flow | Abdulaziz | 7-9 | Reviewed journeys and user flow | P2, P7 |
| P10 | Activity and sequence diagrams | Abdulaziz / Ibrahim | 8-10 | Activity and sequence diagrams | P7 |
| P11 | ERD, relational schema, and class diagram | Ibrahim / Abdulaziz | 9-11 | Consistent data and class models | P5, P7, P8 |
| P12 | Wireframes and clickable prototype | Abdulaziz | 9-12 | Clickable UI prototype | P7, P9 |
| P13 | Test plan | Abdulaziz | 11-13 | Requirement-linked test plan | P5, P6, P8, P12 |
| P14 | Heuristic evaluation | Abdulaziz | 12-13 | Heuristic findings and recommended revisions | P12 |
| P15 | Social, ethical, legal, global, and security impacts | Team by assigned area | 11-13 | Impact-analysis sections | P5, P8 |
| P16 | Report integration and consistency review | Ibrahim with team | 3-15 | Complete IS498 report | All available approved outputs |
| P17 | Final review and presentation preparation | Team | 14-15 | Submission-ready report and presentation | P13-P16 |
| P18 | Advisor review and progress follow-up | Team | 1-15 | Weekly feedback and documented actions | Ongoing work |

## Week-Based Gantt Schedule

`●` indicates planned activity. The schedule shows relative effort, not completion status.

| Work package | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| P1 Methodology and planning | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  |
| P2 Stakeholders and users | ● | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |
| P3 Existing solutions | ● | ● | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |
| P4 Problem, objectives, scope, and gap |  |  | ● | ● | ● | ● |  |  |  |  |  |  |  |  |  |
| P5 Requirements |  |  |  | ● | ● | ● | ● |  |  |  |  |  |  |  |  |
| P6 Prioritization and traceability |  |  |  |  |  | ● | ● | ● |  |  |  |  |  |  |  |
| P7 Use cases and scenarios |  |  |  |  |  | ● | ● | ● | ● |  |  |  |  |  |  |
| P8 Architecture and technology |  |  |  |  |  | ● | ● | ● | ● | ● |  |  |  |  |  |
| P9 User journeys and user flow |  |  |  |  |  |  | ● | ● | ● |  |  |  |  |  |  |
| P10 Activity and sequence diagrams |  |  |  |  |  |  |  | ● | ● | ● |  |  |  |  |  |
| P11 ERD, schema, and class diagram |  |  |  |  |  |  |  |  | ● | ● | ● |  |  |  |  |
| P12 Wireframes and prototype |  |  |  |  |  |  |  |  | ● | ● | ● | ● |  |  |  |
| P13 Test plan |  |  |  |  |  |  |  |  |  |  | ● | ● | ● |  |  |
| P14 Heuristic evaluation |  |  |  |  |  |  |  |  |  |  |  | ● | ● |  |  |
| P15 Impact analyses |  |  |  |  |  |  |  |  |  |  | ● | ● | ● |  |  |
| P16 Report integration |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| P17 Final review and presentation |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● |
| P18 Advisor review | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |

## Resource Schedule

| Member | Weeks 1-5 | Weeks 6-10 | Weeks 11-13 | Weeks 14-15 |
|---|---|---|---|---|
| Ibrahim | Stakeholders, target users, research planning, problem and scope | Requirements, prioritization, traceability, use cases, sequence diagram, ERD | Schema completion, social/global impact, report integration | Final report coordination and presentation preparation |
| Saud | Existing-solutions research and comparison | Architecture, technology assessment, justification, and data flow | Architecture completion and security impact | Technical review and presentation preparation |
| Abdulaziz | Methodology, planning baseline, resource planning, and initial risks | User journeys, user flow, Activity Diagram, Class Diagram preparation, and initial wireframes | Prototype, Test Plan, heuristic evaluation, ethical/legal impact, and planning updates | Final consistency review and presentation preparation |
| Team | Weekly advisor follow-up and evidence collection | Reviews across requirements, design, UI, architecture, and data | Cross-artifact consistency review | Submission and presentation readiness review |

## Dependency and Review Gates

| Gate | Required before finalizing | Inputs required |
|---|---|---|
| Requirements Gate | Use cases, detailed UI flows, architecture, database design, Test Plan | Actors, scope, FRs, NFRs |
| Analysis and Design Gate | Activity/sequence diagrams, schema, Class Diagram | Reviewed use cases, scenarios, data requirements, ERD |
| Prototype Gate | Wireframes, clickable prototype, heuristic evaluation | Main journeys and related use cases |
| Test Planning Gate | Final Test Plan | Reviewed requirements, measurable NFRs, proposed architecture |
| Submission Gate | Report and presentation | Reviewed required artifacts, evidence, references, and contribution records |

## Calendar Conversion

When official dates become available, Week 1 will be mapped to the official Phase One start week. The report deadline will be set to the Tuesday before the preparatory week, and the presentation milestone will be placed in the preparatory exam week. If these dates conflict with the proposed Week 14-15 activities, the schedule will be compressed or moved earlier rather than changing the handbook deadline.

## Approval Required

The team and advisor should review:

- whether 15 relative weeks match the current semester;
- the proposed task durations and overlaps;
- whether dependencies are placed early enough;
- each member's workload and availability; and
- the final report and presentation milestone weeks.

## Source Basis

- Official IS498/IS499 Graduation Project Handbook.
- `README.md`.
- `docs/project/PROJECT_CONTEXT.md`.
- `docs/project/DECISION_LOG.md`.
- `docs/project/OPEN_QUESTIONS.md`.
- Current project presentation, used only for the proposed 15-week duration.
