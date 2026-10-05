# Itqan — System Architecture and Technology Stack (Final v2)

> **Authority:** This document records the final phase-one architecture boundary. The v2 correction supersedes any earlier wording in the retained architecture PDF that conflicts with approved requirements, ERD/schema, use cases, or the decision log.

## 1. Architecture

- **Mobile application:** Flutter for Android/iOS.
- **Application backend:** FastAPI (Python).
- **Recitation analysis:** separate Python/GPU service using `obadx/muaalem-model-v3_2`, based on `facebook/w2v-bert-2.0`, MIT licensed.
- **Database:** PostgreSQL.
- **Authentication:** managed identity provider; `USER.identity_subject` stores the provider-issued identity subject; no local password hash.
- **Quran content:** bundled locally from the selected King Fahd Glorious Quran Printing Complex source for Juz Amma (37 surahs, 564 verses, 2,308 words).

## 2. Recitation data flow

1. Reader selects a Surah and starts a session.
2. The mobile app captures recitation audio at 16 kHz mono, segmented by verse.
3. Audio and verse identifier are sent over HTTPS to the backend.
4. The analysis service returns phoneme/articulation observations.
5. The backend comparison logic aligns observations with the expected verse and maps detected differences to word locations.
6. Feedback is returned to the app.
7. Only result/progress data is persisted; recitation audio is discarded after analysis.

## 3. Teacher path

- Teacher creates/manages a class.
- Quran Reader joins using the teacher-provided **join code**.
- There is **no invitation-link/acceptance workflow** in phase one.
- Teacher reads are restricted to active class enrollment.
- Teacher receives stored activity/completion/mastery information and messages as defined by FR-23–FR-25; teacher never receives retained recitation audio.

## 4. Requirement coverage

- **FR-01–FR-22:** covered by the original architecture mapping.
- **FR-23:** Teacher Dashboard → Class Service, Progress Service, learner/session/progress data.
- **FR-24:** Manage Class → Class Service, `LEARNING_CLASS`, `CLASS_ENROLLMENT`, join-code behavior.
- **FR-25:** Send Student Messages → Class Service and `TEACHER_MESSAGE`, scoped by enrollment.
- **FR-26:** Smart Prompting → Session Service/Recitation UI and `PAUSE_EVENT`, triggered by pause/hesitation/forgetting.

## 5. Non-functional boundaries

- Accuracy is evaluated during IS499 using a project-specific evaluation/test-data activity; it is not asserted from the architecture alone.
- Real-time/near-real-time feedback is a requirement; exact performance thresholds are validated during implementation/testing.
- Privacy is strengthened by not retaining recitation audio.
- External analysis is not a production deployment assumption; vendor and PDPL transfer review are required before external processing is used.
- Production hosting/deployment remains an IS499 implementation decision.

## 6. Model evidence

The current Muaalem model card identifies `obadx/muaalem-model-v3_2` as an ASR/Transformers model with MIT licensing and a base model of `facebook/w2v-bert-2.0`. The associated paper describes a Quran-specific pronunciation-error detection approach and reports 0.16% average phoneme error rate on its reported test set. These published results are not a guarantee of Itqan performance; the integrated system must be evaluated on project-specific data.

Sources:
- https://huggingface.co/obadx/muaalem-model-v3_2
- https://arxiv.org/abs/2509.00094
