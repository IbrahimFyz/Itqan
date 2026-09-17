# Learner Use Case Scenarios

**Status:** Proposed — team review required

**Actor:** Learner

**Diagram source:** `docs/diagrams/learner-use-case-diagram.mmd`

## Requirement Mapping

| Use case | Requirements |
|---|---|
| Register and log in | FR-01, FR-02 |
| Manage profile | FR-03 |
| Select Surah and view verses | FR-04, FR-05, FR-06 |
| Select AI mode | FR-07, FR-08, FR-09 |
| Complete recitation session | FR-11 to FR-19 |
| View session result | FR-20 |
| View progress and streak | FR-21, FR-22 |

## UC-01 Complete Recitation Session

| Field | Description |
|---|---|
| Primary actor | Learner |
| Trigger | The learner chooses to practise a Surah. |
| Preconditions | The learner is logged in and Juz Amma content is available. |
| Requirements | FR-04 to FR-09, FR-11 to FR-19 |
| Success outcome | The learner completes or ends a recitation session after receiving applicable feedback. |

### Main flow

1. The learner browses Juz Amma and selects a Surah.
2. The system displays the selected Surah verses.
3. The learner selects an AI mode and starts the session.
4. The learner grants microphone access when requested.
5. The system captures and analyses the recitation.
6. When the system detects a relevant error, it identifies the location and provides feedback; audio assistance is provided when applicable.
7. The learner continues reciting or ends the session.
8. The system stores the session outcome for results and progress tracking.

### Alternatives

- If microphone access is unavailable, the system explains that audio capture is required before the session can start.
- If no relevant error is detected, the learner continues or ends the session without correction feedback.

## UC-02 View Results and Progress

| Field | Description |
|---|---|
| Primary actor | Learner |
| Trigger | The learner ends a recitation session or opens progress. |
| Preconditions | The learner is logged in. |
| Requirements | FR-20 to FR-22 |
| Success outcome | The learner sees the session mastery result, error words, available progress, and current streak. |

### Main flow

1. The learner ends a recitation session or opens the progress area.
2. The system displays the mastery percentage and words with detected errors for a completed session.
3. The system displays completed Surahs, average mastery percentage, and the current practice streak.

## Open Decisions

- The mastery-score formula is unresolved; the scenarios display the percentage required by FR-20 without defining its calculation.
- Smart Prompting after a pause is described in the project context but is not a functional requirement. It is not included as a separate use case until the team approves it.
