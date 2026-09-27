# Itqan Phase One Clickable Prototype

## Access

- **Prototype:** [Itqan — Phase One Clickable Prototype](https://www.figma.com/make/VvQmndtn3jCGSVMu04LciU/Itqan-%25E2%2580%2594-Phase-One-Clickable-Prototype)
- **Tool:** Figma Make.
- **Owner:** Abdulaziz.
- **Status:** Phase One UX prototype. It demonstrates intended interactions; it is not a production implementation or evidence of live microphone or AI-analysis capability.

## Confirmed learner route

1. Start practice.
2. Browse or search the 37 Surahs in Juz Amma and select a Surah.
3. Review the selected-Surah overview and verse preview.
4. Select Al-Mujawwid or Al-Mushajji.
5. Enter the recitation experience.
6. Review feedback, optional audio help, illustrative session result, and learner progress.

This route implements the current ordering in FR-04 to FR-08 and FR-11 to FR-21: a learner selects a Surah before choosing an AI mode and beginning a recitation session.

## Teacher area

The Al-Mu'allim area demonstrates teacher monitoring of authorised stored learning results. It represents activity, completion, mastery, and progress only. A teacher view is limited to the teacher's own class and actively enrolled learners.

## Privacy boundary

Learner recitation audio is processed transiently in memory and discarded after analysis. It is never stored or exposed to teachers. The prototype does not perform real recording or analysis; its microphone, feedback, and error states demonstrate the intended interface only.

## Prototype status key

| Status | Represented details |
|---|---|
| **Confirmed** | Juz Amma browse/select, Surah verses, mode selection, recitation session, feedback, session result, progress, teacher dashboard, and class management boundaries. |
| **Proposed** | Selected-Surah overview, exact screen wording, search presentation, navigation layout, streak presentation, and retry/empty-state wording. |
| **Unresolved** | Detailed AI-mode behaviour (OQ-07), teacher-learner workflow and detailed dashboard fields (OQ-05/OQ-06), and final processing-failure behaviour (OQ-11). The prototype's old “formula pending” label needs updating to match FR-20. |

## Traceability

- Requirements: `docs/project/REQUIREMENTS.md` (FR-04 to FR-24; NFR-04, NFR-07, NFR-11).
- Journeys: `docs/ui-ux/USER_JOURNEYS.md`.
- Supporting flow and activities: `docs/diagrams/Itqan_User_Flow_01_Learner_Recitation.svg`, `docs/diagrams/Itqan_Activity_01_Learner_Recitation_Session.svg`, and `docs/diagrams/Itqan_Activity_02_Teacher_Class_and_Monitoring.svg`.
- Architecture policy: `docs/system-architecture.pdf`.
