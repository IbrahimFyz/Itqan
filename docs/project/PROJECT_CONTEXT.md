# Itqan — Project Context

## Identity
**Project:** Itqan (إتقان) — AI-Powered Quran Recitation Coaching
**Course:** IS498 Graduation Project I
**Team:** Ibrahim, Abdulaziz, Saud

## Scope
Itqan is a standalone application for anyone who reads the Quran. IS498 covers analysis and design; implementation is planned for IS499.

The initial Quran scope is Juz Amma: 37 Surahs, 564 verses, and 2,308 words.

## Users
- Quran Reader
- Teacher

Teacher registration additionally requires school name. Readers can join teacher classes using a class join code. Teachers do not directly add readers and no invitation-link/acceptance flow is part of the approved design.

## AI Modes
- Al-Mujawwid — pronunciation/Tajweed correction and feedback.
- Al-Mushajji — motivational support, challenges, and rewards.
- Al-Mu'allim — teacher-facing learning/progress support.

## Functional Requirements
The authoritative list is FR-01 through FR-26 in `REQUIREMENTS.md`. FR-26 covers Smart Prompting when a reader pauses, hesitates, or appears to forget.

## Mastery Score
`Mastery Score = (Total Words − Effective Errors) / Total Words × 100`

Complete word pronunciation error = 1; Tajweed-only error = 0.5; per-word contribution is capped at 1.

## Architecture
- Flutter mobile application.
- FastAPI/Python backend.
- PostgreSQL database.
- Managed identity provider.
- Separate stateless Python recitation-analysis service using `obadx/muaalem-model-v3_2` based on `facebook/w2v-bert-2.0`.
- Quranic content bundled from the King Fahd Glorious Quran Printing Complex source selected by the architecture.
- Audio is processed in memory and not retained.
- Teacher reads are scoped to class ownership and active enrollment.
- Production hosting is deferred to IS499.

## IS498 Non-Goals
- No production implementation.
- No claim of 100% AI accuracy.
- No invented user research.
- No Ayat integration as part of the current project scope.
- No Whisper-based final architecture.
- No invitation-based class enrollment.

## Authoritative Sources
Use `REQUIREMENTS.md`, `DECISION_LOG.md`, `OPEN_QUESTIONS.md`, `SYSTEM_ARCHITECTURE_FINAL.md`, the ERD, and relational schema as the current project sources of truth.
