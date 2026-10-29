# Activity Diagrams: final version

**Built from:** [`Itqan_Requirements.md`](../../../Itqan_Requirements.md), using the §7.3 flows and exceptions, the §6 business rules and the §13 checklist. These are built from the Task 1 scenarios ([`USE_CASE_SCENARIOS.md`](../scenarios/USE_CASE_SCENARIOS.md)). They replace Activity Diagram 01 (learner recitation session) and Activity Diagram 02 (teacher class and monitoring), report Figures 11 and 12. Abdulaziz owns the activity diagrams, so the team should approve the swap.

## Purpose and inputs

An activity diagram shows how work flows between the actors and the system: the order of steps, the decisions, the exceptions and where each flow ends. Inputs: the use case flows in §7.3, the use case IDs in §7.1, the business rules in §6, and the use case diagram (for the include and extend points).

## Diagrams

| File | Covers | Lanes | Size (px) | Text on A4 |
|---|---|---|---|---|
| `itqan-act-01a-session-start` | UC-10 steps 1–3: Select Surah (UC-08), Select AI Mode (UC-09), recitation consent (UC-05), microphone check, session start. Ends at connector **A**. | Quran Reader, Itqan System | 771 × 689 | 9.0 pt |
| `itqan-act-01b-recite-and-results` | UC-10 steps 4–14 from connector **A**: per-verse loop, Smart Prompting (UC-28), analysis failure, Audio Assistance (UC-11), all end reasons including logout, scoring, store and discard, View Session Results (UC-12). | Quran Reader, Itqan System | 968 × 1053 | 7.4 pt |
| `itqan-act-02-class-enrolment` | UC-17 Manage Class (**create or rename**, with the empty-name loop) → share join code → UC-26 Join Class via Code, with consent and every exception. | Teacher, Itqan System, Quran Reader | 946 × 1367 | 7.4 pt |
| `itqan-act-03-teacher-monitoring` | UC-18 View Teacher Dashboard: class → reader → session, with "no classes", "no readers" and "enrolment ended". | Teacher, Itqan System | 592 × 1134 | 8.9 pt |
| `itqan-act-04-messaging` | UC-19 Send Student Messages (one reader or whole class, empty message, empty class) → UC-16 View Teacher Messages with read status. | Teacher, Itqan System, Quran Reader | 818 × 1149 | 8.7 pt |

**Why five diagrams:**
- **01a and 01b:** as one diagram, the recitation session was too tall to print readably, so it is split at the session start and joined by the UML connector **(A)**.
- **02, 03 and 04:** enrolment, monitoring and messaging are independent processes, so each gets its own view, as Task 3 allows.

## Changes after the Task 1 scenario review

| Diagram | Change | Source |
|---|---|---|
| 01b | Logout added to the interruption reasons. | FR-19, UC-10 6c |
| 02 | Rename path added. One shared "name empty?" loop refuses and returns to the name step instead of stopping. | Task 3 item 5, UC-17 1a, 2a |
| 02 | "Code matches an active class?" became "Code matches a class?", because classes no longer have states. | BR-11, UC-26 2a |
| 02 | Note added that class names need not be unique. | FR-24 |
| 03 | "No enrolled readers → show the join code" branch and an empty-list note added. Messaging moved to 04. | UC-18 4a, 6b |
| 04 | New view: empty-message loop, and the "class has no readers yet" refusal. | UC-19 2a, 3b |

## Consistency checks

- [x] Only the actors from §2, with the "Itqan System" lane for system behaviour (§10 parts are for sequence diagrams).
- [x] Use case references (UC-xx) match §7.1 and the use case diagram.
- [x] Include and extend points match §7.2: Smart Prompting at *pause detected* and Audio Assistance at *word highlighted*, both optional inside the loop.
- [x] Every exception in the Task 1 scenarios for UC-10, UC-17, UC-18, UC-19, UC-26 and UC-16 has a branch or note.
- [x] Session end covers all three end reasons (FR-19, §9). Scoring follows BR-01 and BR-02, and storing and discarding follows BR-05.
- [x] Teacher visibility is limited to sessions from the join date (BR-08). Messages go only to enrolled readers and show read status (BR-12, BR-13).
- [x] Nothing contradicts the requirements, and no requirement had to be added.

## Not drawn as activity diagrams

These use cases have short linear flows that §7.3 already describes completely: UC-01 to UC-06 (account, consent screen, deletion), UC-07, UC-13 to UC-15 and UC-27. 

## Changes from the report's activity diagrams

- **Added:** consent steps, the microphone check, the analysis-failure branch, interruption as an end reason, the join-date rule, read status, and the "already enrolled" and "no classes" exceptions.
- **Removed:**
  - Configure Session, which no requirement covers.
  - Record pause event and Save session record, replaced by the BR-05 store-and-discard step.
  - The invitation-free note, now implied by the flow.
- **Changed:**
  - Smart Prompting shows the next word as a hint (FR-26).
  - Audio Assistance happens when the reader taps a word (FR-17).
  - Feedback is per verse while the reader continues (FR-13, FR-16, NFR-03).

## Rendering notes

- In PlantUML 1.2026.9, a white `root` background also turns the fork and join bars white. The `activityBar` style keeps them black.
- No title, for the same reason as the use case diagram: the report's figure caption replaces it.
- To re-render:

```bash
java -jar C:\Users\SAUDK\plantuml.jar -tsvg *.puml
```
