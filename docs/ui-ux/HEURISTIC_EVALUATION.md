# Itqan Phase One Heuristic Evaluation

## Scope and method

- **Owner:** Abdulaziz.
- **Date:** 2026-09-20.
- **Artifact reviewed:** [Itqan — Phase One Clickable Prototype](https://www.figma.com/make/VvQmndtn3jCGSVMu04LciU/Itqan-%25E2%2580%2594-Phase-One-Clickable-Prototype).
- **Method:** Expert review against Nielsen's usability heuristics, using the learner route and authorised teacher-monitoring route in `CLICKABLE_PROTOTYPE.md` and the current requirements.
- **Scope:** Interface and interaction design only. This does not validate production microphone capture, AI analysis, authorisation enforcement, or Quran-text sourcing.
- **Severity scale:** 0 = not a problem; 1 = cosmetic; 2 = minor; 3 = major; 4 = blocker.

## Findings and actions

| ID | Heuristic | Issue and evidence | Severity | Recommended / final change | Status |
|---|---|---|---:|---|---|
| HE-01 | Visibility of system status | At the 2026-09-20 review, the mastery formula was unresolved. FR-20 now defines the approved formula; empirical validation of the integrated scoring behavior remains an IS499 evaluation activity. | 3 | Update the prototype label to explain the defined formula, while avoiding claims of a validated assessment until evaluation is complete. | **Formula defined; integrated validation remains an IS499 evaluation activity.** |
| HE-02 | Help users recognise, diagnose, and recover from errors | A learner denied microphone permission needs clear recovery guidance. The prototype shows a microphone-permission explanation and Retry, but the exact failure/retry behaviour is not approved (OQ-11). | 3 | After the team decides the technical recovery path, specify whether Retry re-requests permission, directs the learner to device settings, or both. Test the wording with learners. | **Deferred pending OQ-11.** |
| HE-03 | Match between system and the real world | AI-mode names alone may be unfamiliar to a first-time learner. The mode screen uses descriptive choice cards: Al-Mujawwid for Tajweed/recitation feedback and Al-Mushajji for encouragement. | 2 | Keep the plain-language descriptions beside the Arabic mode names; confirm final detailed behaviours once OQ-07 is resolved. | **Implemented safeguard; deferred decision.** |
| HE-04 | Error prevention | Search must not leave a learner without an understandable outcome when no Surah matches. The Juz Amma browser includes a live search and no-results state; the browser covers all 37 Surahs from An-Naba to An-Nas. | 2 | Keep a short no-results explanation and an obvious way to clear the query. Confirm the final wording during learner testing. | **Implemented safeguard; proposed wording.** |
| HE-05 | Recognition rather than recall | The selected-Surah overview preserves the chosen Surah, number, verse count, and preview before mode selection, so users do not need to remember their earlier choice. | 1 | Retain this proposed confirmation screen because it supports FR-05/FR-06. It may be removed only if testing shows it adds unnecessary delay. | **Implemented safeguard; proposed screen.** |
| HE-06 | User control and freedom | The learner path has Back navigation and a persistent bottom navigation area. This gives a recovery route during browse, overview, mode selection, and results. | 2 | Test whether leaving an active recitation needs an explicit confirmation before a prototype becomes a production design. | **Deferred: requires session-loss policy.** |
| HE-07 | Consistency and standards | The prototype consistently uses Arabic-first Quran content, a visible English toggle, the same light-beige palette, and repeated primary-action placement. | 1 | Keep the language control visible on each key learner screen; validate RTL layout and final English wording during accessibility/usability testing. | **Implemented safeguard.** |
| HE-08 | Aesthetic and minimalist design | The original AI pass added Surah difficulty badges, although no approved requirement defines Surah difficulty. | 2 | Remove the badges to avoid inventing learner classification. | **Fixed on 2026-09-20.** All 37 entries now retain only number, Arabic/English name, and verse count. |
| HE-09 | Privacy and trust | A learner may reasonably worry that recitation audio is retained or reviewed by teachers. The recitation screen states that audio is processed in memory, discarded after analysis, and never shared with teachers. The teacher area states “No raw recitation audio” and scopes monitoring to owned classes and active enrolments. | 4 | Preserve these statements in every future version. Validate technical enforcement separately with architecture/security tests. | **Implemented safeguard.** |
| HE-10 | Help and documentation | Users and evaluators need to distinguish product requirements from interface proposals. The prototype includes a Prototype Notes area with Confirmed, Proposed, and Unresolved categories. | 1 | Keep this area for evaluation; do not present unresolved features as committed functionality in the final report. | **Implemented safeguard.** |

## Prioritised follow-up

1. Resolve the microphone-denied and analysis-failure recovery behaviour before implementation or formal usability testing (HE-02; OQ-11).
2. Update the mastery-score label and evaluate its interpretation before presenting scores as validated results (HE-01; OQ-08).
3. Define the detailed AI-mode behaviours and teacher dashboard fields before expanding those prototype areas (HE-03; OQ-07 and OQ-06).
4. Run task-based learner and teacher usability testing after those decisions, then update this log with participant evidence and final changes.

## Requirement and artifact links

- Learner selection, mode, recitation, feedback, result, and progress: FR-04 to FR-22.
- Teacher dashboard and class management: FR-23 and FR-24.
- Clear, user-friendly flow and language support: NFR-04 and NFR-11.
- Privacy and transient-audio policy: NFR-07, `USER_JOURNEYS.md`, and `system-architecture.pdf`.
- Unresolved decisions: `OPEN_QUESTIONS.md` (OQ-05 to OQ-07 and OQ-11); OQ-08 records the defined formula.
