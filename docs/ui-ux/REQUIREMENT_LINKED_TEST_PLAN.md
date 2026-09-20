# Itqan Requirement-Linked Test Plan

**Phase:** One  
**Scope owner:** Abdulaziz  
**Status:** Draft test plan based on the current project requirements

## Purpose and scope

This plan defines how Itqan will be tested against the current functional and non-functional requirements. It covers the learner recitation flow, teacher monitoring, privacy and authorization, error handling, prototype usability, and measurable performance observations.

It does **not** claim that the clickable prototype performs microphone capture or AI analysis. The prototype is evaluated as an interactive representation of the approved flow; implementation tests apply when those features exist.

### Fixed architecture policy

Learner recitation audio is processed in memory during analysis and then discarded. It must never be stored in databases, object storage, files, logs, backups, or exposed to teachers. Teachers may access only authorized stored learning-result data for learners actively enrolled in their own class.

## Test approach

- Record each test as **Pass**, **Fail**, **Blocked**, or **Not run** with evidence (screen recording, request/response capture, audit output, or defect record).
- Run functional tests on representative learner and teacher accounts.
- Use simulated analysis outputs until a validated Quran-recitation evaluation dataset and acceptance criteria are approved.
- Treat unresolved decisions as blockers, not assumptions.

### Test accounts and data

| ID | Test data |
| --- | --- |
| L1 | Learner with an active enrollment in T1's class |
| L2 | Learner not enrolled in T1's class |
| T1 | Teacher for the class containing L1 |
| T2 | Unrelated teacher |
| S1 | A Juz Amma Surah, for example An-Naba or Al-Masad |
| A1 | Simulated correct-recitation and detected-error outputs, including word locations |

Any real learner audio used during testing requires the applicable consent decision and must follow the transient-audio policy above.

## Functional test cases

| ID | Requirement(s) | Test and expected result |
| --- | --- | --- |
| FT-01 | FR-01 | Create a learner account with valid required details. The account is created; invalid or incomplete input is explained without exposing sensitive data. |
| FT-02 | FR-02 | Sign in with valid and invalid credentials. Valid credentials open the permitted role experience; invalid credentials do not. |
| FT-03 | FR-03 | View and update the learner profile. Only the authenticated learner can view or change their own permitted profile fields. |
| FT-04 | FR-04 | Open Juz Amma content. The learner can browse and select the supported Juz Amma Surahs. |
| FT-05 | FR-05, FR-07 | Start practice. The learner must select a Surah before selecting Al-Mujawwid or Al-Mushajji; the mode choice is then available for that Surah. |
| FT-06 | FR-06 | Enter a session for S1. The session displays its Quran verses in the approved Arabic-first presentation. |
| FT-07 | FR-08, FR-13, FR-14, FR-15, FR-16 | With A1, run Al-Mujawwid analysis. Feedback identifies the simulated relevant errors and their word locations, then presents actionable feedback. |
| FT-08 | FR-09 | With A1, run Al-Mushajji. The response provides encouragement consistent with the selected mode; detailed mode boundaries remain subject to OQ-07. |
| FT-09 | FR-11, FR-12 | Start a session and grant microphone permission. Audio capture begins only for the active session. |
| FT-10 | FR-17, FR-18 | Request appropriate audio assistance, then continue recitation. Assistance is available where supported and the learner can resume the same session. |
| FT-11 | FR-19, FR-20 | End a session. The learner receives a result containing a mastery value on the 0–100 scale and detected-word information. The score formula is subject to OQ-08. |
| FT-12 | FR-21, FR-22 | Complete sessions with varied results. Progress shows completed Surahs at full mastery and average mastery; streak behaviour is tested once its definition is confirmed. |
| FT-13 | FR-10, FR-23 | Sign in as T1. The teacher dashboard presents only the authorized stored learning results for L1. |
| FT-14 | FR-24 | Perform the approved class-management actions. Exact actions are blocked until the class-management scope is confirmed. |
| FT-15 | FR-25 | Send and receive learner messages only if this optional feature is approved for Phase One. Otherwise mark Not run. |

## Privacy, consent, and authorization tests

| ID | Requirement(s) | Test and expected result |
| --- | --- | --- |
| PT-01 | NFR-07; architecture policy | Inspect application storage, object storage, files, logs, backups, telemetry, and API payloads after a recitation. No raw learner audio is retained. |
| PT-02 | NFR-07; architecture policy | Observe the analysis lifecycle. Audio exists only in memory for active analysis and is discarded after analysis completes or fails. |
| PT-03 | FR-23, NFR-06, NFR-07 | As T1, open L1's monitoring data. Authorized result-only data is available; raw audio is unavailable. |
| PT-04 | FR-23, NFR-06 | As T1, request L2's data and as T2 request L1's data. Both requests are denied without leaking data. |
| PT-05 | FR-23, NFR-07 | Inspect teacher screens and API responses. They contain no raw audio, audio URLs, transcripts, or learner contact details. |
| PT-06 | FR-12, NFR-07 | Decline microphone or applicable consent. Capture does not begin and the learner receives a clear next step. Consent wording and retention record are pending the privacy decision. |
| PT-07 | FR-01, FR-02, NFR-06 | Attempt learner-only and teacher-only routes with the wrong role or no authenticated session. Access is denied. The authentication mechanism is pending OQ-14. |

## Error and recovery tests

| ID | Requirement(s) | Test and expected result |
| --- | --- | --- |
| ET-01 | FR-12, NFR-10, NFR-04 | Deny or remove microphone permission. The learner sees a clear explanation and can retry after enabling permission; no capture starts. |
| ET-02 | FR-13, FR-16, NFR-02 | Simulate analysis-service failure. The app does not present invented feedback and offers the approved recovery path. Retry and fallback rules are pending OQ-11. |
| ET-03 | FR-19, NFR-05 | Interrupt an active session. Relevant permitted session/result data is preserved according to the approved recovery policy; raw audio is discarded. |
| ET-04 | FR-04, NFR-04 | Search for unavailable Surah text or clear the search. The UI communicates the result and retains a usable way back to the list. |
| ET-05 | FR-23, NFR-06 | Attempt a stale or invalid class/enrollment link. Monitoring access is denied and no learner data is shown. |

## Non-functional and usability tests

| ID | Requirement(s) | Measurement and expected result |
| --- | --- | --- |
| NFT-01 | NFR-01 | Compare analysis output with an expert-labelled evaluation set. Report precision, recall, and error-location accuracy. Acceptance criteria are **TBD** after OQ-09 and OQ-10. |
| NFT-02 | NFR-02 | Measure end-to-end feedback latency across representative sessions and report median and 95th percentile. The maximum acceptable delay is **TBD**; do not label a delay acceptable without an approved target. |
| NFT-03 | NFR-03 | Observe active recitation sessions. Feedback is delivered during active recitation without requiring a pause after every word; define the observable timing rule after OQ-11. |
| NFT-04 | NFR-04 | Ask representative learners to complete: choose S1, choose a mode, start a session, interpret feedback, and find progress. Record completion, time, errors, and assistance needed. Acceptance threshold is **TBD**. |
| NFT-05 | NFR-05 | Repeat ET-03 under network/app interruption. Record whether the approved permitted state is retained and whether audio is discarded. |
| NFT-06 | NFR-08 | Add or configure a representative content expansion in a test environment. Record whether the system supports the planned expansion without breaking existing Juz Amma access. Expansion scope is **TBD**. |
| NFT-07 | NFR-09 | Review implementation modules against the architecture and trace tests to requirements. Record coupling, undocumented dependencies, and maintainability defects. |
| NFT-08 | NFR-10 | Execute FT-09 and ET-01 on the approved mobile/browser and microphone compatibility matrix. Devices, operating systems, and browsers are **TBD**. |
| NFT-09 | NFR-11 | Verify Arabic is primary for Quran content and UI supports Arabic and English. Check RTL layout, readable Arabic text, and language consistency on learner and teacher screens. |

## Prototype usability checks

The clickable prototype is used to validate navigation and comprehension, not microphone or AI quality.

| Check | Evidence to collect | Linked requirement(s) |
| --- | --- | --- |
| Learner selects Surah before mode | Completion/error observations | FR-04, FR-05, FR-07 |
| Learner identifies the selected Surah and continues to mode selection | Completion/error observations | FR-05, FR-06, NFR-04 |
| Learner understands that recitation audio is transient | Participant explanation and screen review | NFR-07 |
| Teacher understands result-only monitoring and class limits | Participant explanation and screen review | FR-23, NFR-06, NFR-07 |
| Arabic/English and RTL presentation remain understandable | Screen review and participant observations | NFR-11 |

The current heuristic evaluation is the initial expert review. Its privacy, navigation, recovery, and language findings should be retested when the prototype or implementation changes.

## Open decisions that block final acceptance

| Open question | Effect on testing |
| --- | --- |
| OQ-05, OQ-06 | Defines teacher–learner relationship, dashboard fields, and class-management acceptance tests. |
| OQ-07 | Defines the testable difference between Al-Mujawwid and Al-Mushajji. |
| OQ-08 | Defines the mastery-score calculation and scoring test oracle. |
| OQ-09, OQ-10 | Defines error taxonomy, expert benchmark, and NFR-01 accuracy targets. |
| OQ-11 | Defines real-time timing, failure handling, retry, and fallback acceptance criteria. |
| OQ-12 | Requires a verified Quran-content source before content-verification testing. |
| OQ-14 | Defines authentication flow details and related security test cases. |

## Exit criteria

Before a Phase One feature is accepted:

1. Every applicable Must requirement has a passing test with recorded evidence.
2. Privacy and authorization tests PT-01 through PT-07 pass; a raw-audio exposure or retention finding is a release blocker.
3. Any approved Should/Could requirement is either tested and passed or explicitly deferred in the project record.
4. Tests blocked by an open decision remain blocked until the team/advisor approves the corresponding rule; no placeholder becomes an assumed requirement.

## Sources

- `docs/project/REQUIREMENTS.md`
- `docs/project/OPEN_QUESTIONS.md`
- `docs/project/PROJECT_CONTEXT.md`
- `docs/system-architecture.pdf`
- `docs/ui-ux/USER_JOURNEYS.md`
- `docs/ui-ux/HEURISTIC_EVALUATION.md`
