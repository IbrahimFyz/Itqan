# Itqan Open Questions

This file tracks unresolved or deferred decisions. Confirmed items are retained as a record of closure and must remain consistent with the approved project artifacts.

| ID | Topic | Status | Notes |
|---|---|---|---|
| OQ-01 | Final Functional Requirements | 🟢 | FR-01 to FR-26 reviewed and approved. |
| OQ-02 | Final Non-Functional Requirements | 🟢 | NFR-01 to NFR-11 reviewed and approved; implementation-specific thresholds/platform details are deferred where explicitly stated. |
| OQ-03 | Requirements Prioritization | 🟢 | Final distribution: 17 Must Have, 7 Should Have, 2 Could Have, 0 Won't Have. |
| OQ-04 | Requirements Traceability | 🟢 | RTM updated for FR-01 to FR-26 and aligned with current Use Cases. |
| OQ-05 | Teacher-student relationship | 🟢 | Teachers create/manage classes; Quran Readers join using a teacher-provided join code. |
| OQ-06 | Teacher Dashboard | 🟢 | Dashboard covers recitation activity, completion status, mastery scores, and overall progress. |
| OQ-07 | AI Mode behavior | 🟢 | Al-Mujawwid: recitation analysis/feedback; Al-Mushajji: motivation; Al-Mu'allim: teacher-oriented functionality. |
| OQ-08 | Mastery Score formula | 🟢 | Mastery Score = (Total Words − Effective Errors) / Total Words × 100. Complete-word pronunciation error = 1; Tajweed-only error = 0.5; maximum penalty per word = 1. |
| OQ-09 | AI model and dataset | 🟢 | Selected recitation-analysis model: `obadx/muaalem-model-v3_2` (MIT), based on `facebook/w2v-bert-2.0`. The associated paper reports a Quran-specific pronunciation-error detection approach and 0.16% average PER on its test set. Project-specific evaluation data and rule-level validation remain part of IS499 testing. |
| OQ-10 | Tajweed detection approach | 🟢 | Phoneme-level speech analysis combined with rule-based Tajweed validation and alignment against expected Quranic pronunciation. |
| OQ-11 | Real-time processing | 🟢 | Real-time/near-real-time feedback is a system requirement; implementation details are deferred to IS499. |
| OQ-12 | Quran text source | 🟢 | Quranic content is selected to be bundled locally from the King Fahd Glorious Quran Printing Complex source used by the architecture; Juz Amma is limited to 37 surahs, 564 verses, and 2,308 words. |
| OQ-13 | Final technology stack | 🟢 | Architecture selects Flutter (mobile), FastAPI/Python (backend), PostgreSQL (database), and a managed identity provider. Recitation analysis uses the selected Muaalem model in a separate Python analysis service. |
| OQ-14 | Authentication | 🟢 | Authentication is delegated to a managed identity provider. `USER` stores the provider-issued `identity_subject`; no local password hash is stored. Exact vendor selection remains an IS499 implementation/deployment detail. |
| OQ-15 | Database schema | 🟢 | ERD and relational schema are defined and the architecture selects PostgreSQL for implementation. |
| OQ-16 | API design | 🟢 | RESTful API communication is the approved direction; detailed endpoints, request/response structures, and implementation are deferred to IS499. |
| OQ-17 | Hosting/deployment | 🟡 | Final production hosting remains deferred to IS499. The phase-one architecture allows server-side analysis for development/demo, but external processing is not a deployment assumption and requires vendor/privacy/PDPL transfer review before use. |
| OQ-18 | User Research | 🟢 | Not required for this project according to the advisor's direction; no user-research findings should be invented. |
| OQ-19 | Existing Solutions / Gap Analysis | 🟢 | Current-source comparison and gap analysis are completed for Tarteel, Tilawa.ai, QariAI, and Tajweed.chat. Report claims must remain limited to the cited official sources. |
| OQ-20 | BMC applicability | 🟢 | Business Model Canvas is not required according to the advisor's direction. |
| OQ-21 | Impact analyses | 🟢 | Social, ethical, legal, global, and security impacts have defined project-specific content; final report citation audit remains required. |
| OQ-22 | Smart Prompting scope | 🟢 | Confirmed as FR-26. Receive Smart Prompting is supported by the Use Case, scenario, RTM, and ERD traceability. |
| OQ-23 | Teacher Registration Path and School Name | 🟢 | Teacher registration requires school name; the registration flow and ERD/diagram updates are aligned. |

## Remaining Items Requiring Closure

OQ-17 remains 🟡 intentionally because production hosting/deployment is an IS499 implementation decision. This does not block the IS498 architecture: the phase-one architecture defines the analysis boundary, data flow, storage behavior, access control, and technology direction while explicitly avoiding an unapproved production deployment assumption. All other tracked open questions are closed.
