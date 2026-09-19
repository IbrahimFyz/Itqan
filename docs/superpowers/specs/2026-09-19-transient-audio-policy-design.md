# Transient Audio Policy Alignment

**Date:** 2026-09-19  
**Status:** Approved design

## Decision

Itqan processes recitation audio in memory only. Audio is discarded immediately after analysis and is never written to a database, object store, file system, backup, or teacher-facing service. The system persists only session metadata and analysis results such as detected errors, locations, feedback, and mastery/progress values.

## Required model changes

- Remove `AUDIO_RECORDING` from the ERD, relational schema, ERD traceability, canonical class diagram, and recitation-feedback class view.
- Remove `AudioRecording` and `AudioStoragePort` from the canonical class model and its rendered SVG artifacts.
- Remove recording-storage methods and dependencies, including `saveRecording`, `store`, `load`, and `delete`.
- Keep `AudioCapturePort` and `AIAnalysisPort`; their `AudioData` is transient request data, not a persisted entity.
- Keep `RECITATION_SEGMENT` audio offsets because they identify positions within a session result, not stored audio.
- Update the class-diagram verifier so the 33 remaining ERD entities are required and persisted-storage names cannot return.
- Update notes and traceability so FR-12 records in-memory capture only, and FR-17 describes reference playback without storing a learner recording.

## Verification

The verifier must fail if `AUDIO_RECORDING`, `AudioRecording`, `AudioStoragePort`, `storageUri`, or retention/deletion fields appear in the database or class-diagram sources. It must still render all class diagrams successfully and preserve the ERD-to-UML mapping for every remaining persisted entity.

## Out of scope

This decision does not change consent for the separate, explicitly approved IS499 evaluation dataset. It also does not change the bundled reference audio used for corrective playback; that is application content, not a learner recording.
