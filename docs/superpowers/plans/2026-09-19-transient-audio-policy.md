# Transient Audio Policy Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make every persisted-model artifact conform to the architecture policy that learner recitation audio is transient and discarded after analysis.

**Architecture:** Remove the persisted recording entity and its storage boundary from the ERD, relational schema, canonical UML model, and recitation view. Keep transient capture and analysis input through `AudioCapturePort`, `AIAnalysisPort`, and `AudioData`; persist only session and analysis results. Extend the existing shell verifier to prevent storage/retention concepts from returning.

**Tech Stack:** Mermaid class and ER diagrams, POSIX shell, ripgrep, Mermaid CLI.

**Spec:** `docs/superpowers/specs/2026-09-19-transient-audio-policy-design.md`

## Global Constraints

- Learner recitation audio is never written to a database, object store, file system, backup, or teacher-facing service.
- Persist only session metadata and analysis results; `RECITATION_SEGMENT` audio offsets remain valid result-location metadata.
- `AudioCapturePort`, `AIAnalysisPort`, and transient `AudioData` remain; `AudioRecording` and `AudioStoragePort` do not.
- The separate consented IS499 evaluation dataset and bundled corrective reference audio are out of scope.
- All five Mermaid sources must still render successfully.

## Review Focus

- Ordinary session persistence must keep result data after audio is discarded; the model must retain `RECITATION_SESSION`, `RECITATION_SEGMENT`, `RECITATION_ANALYSIS`, and `RECITATION_ERROR`.
- A storage-oriented name must fail validation even if it is added only to a detailed class view.
- `AUDIO_RECORDING` must be absent from both the ERD declaration and its ERD-to-UML mapping.
- The detailed recitation view must not retain a dependency on a removed storage port or recording class.
- Existing SVG artifacts must be regenerated rather than left showing removed storage concepts.

---

### Task 1: Remove persisted learner-audio storage from the database model

**Files:**
- Modify: `docs/database/itqan-erd.mmd`
- Modify: `docs/database/RELATIONAL_SCHEMA.md`
- Modify: `docs/database/ERD_REQUIREMENTS_TRACEABILITY.md`
- Modify: `tests/verify_class_diagrams.sh`

**Interfaces:**
- Consumes: the approved transient-audio policy and the existing 34-entity ERD.
- Produces: a 33-entity ERD/schema with no stored learner-audio record; Task 2 consumes the removed name when updating UML validation.

- [ ] **Step 1: Add a failing source-policy check to the existing verifier**

Add this before the Mermaid rendering loop in `tests/verify_class_diagrams.sh`:

```sh
for source in docs/database/itqan-erd.mmd docs/database/RELATIONAL_SCHEMA.md "$diagram_dir"/*.mmd; do
  if rg -qi 'AUDIO_RECORDING|AudioRecording|AudioStoragePort|storageUri|retentionExpiresAt|deletedAt' "$source"; then
    echo "Persisted learner-audio storage is forbidden: $source"
    exit 1
  fi
done
```

- [ ] **Step 2: Run the verifier to prove the check fails**

Run: `sh tests/verify_class_diagrams.sh`

Expected: non-zero exit with `Persisted learner-audio storage is forbidden` because the current ERD/schema/UML still contain stored-recording names.

- [ ] **Step 3: Remove the persisted recording entity and references**

Delete the complete `AUDIO_RECORDING` declaration from `docs/database/itqan-erd.mmd` and delete its relationship to `RECITATION_SESSION`. Delete the `AUDIO_RECORDING` section from `RELATIONAL_SCHEMA.md`, including its URI, consent, retention, and deletion explanation. Remove the expired/withdrawn-audio deletion rule.

In `ERD_REQUIREMENTS_TRACEABILITY.md`, change FR-12 to list only `RECITATION_SESSION` and describe in-memory capture with no stored audio. Remove the `AUDIO_RECORDING` reverse-index row. Change FR-17 from an assistance URI to bundled corrective reference playback; it must not describe learner recording storage.

- [ ] **Step 4: Verify database source removal**

Run: `rg -n 'AUDIO_RECORDING|storage_uri|retention_expires_at|deleted_at' docs/database/itqan-erd.mmd docs/database/RELATIONAL_SCHEMA.md docs/database/ERD_REQUIREMENTS_TRACEABILITY.md`

Expected: no matches.

- [ ] **Step 5: Commit the database-model change**

```bash
git add docs/database/itqan-erd.mmd docs/database/RELATIONAL_SCHEMA.md docs/database/ERD_REQUIREMENTS_TRACEABILITY.md tests/verify_class_diagrams.sh
git commit -m "docs: remove persisted learner audio model"
```

### Task 2: Align the UML sources and permanent validation

**Files:**
- Modify: `docs/diagrams/class/itqan-class-diagram.mmd`
- Modify: `docs/diagrams/class/recitation-feedback-classes.mmd`
- Modify: `docs/diagrams/class/CLASS_DIAGRAM_NOTES.md`
- Modify: `tests/verify_class_diagrams.sh`

**Interfaces:**
- Consumes: Task 1's 33-entity ERD and its no-storage constraint.
- Produces: canonical and detailed UML sources without persisted learner-audio storage; Task 3 renders these sources.

- [ ] **Step 1: Extend required-entity checks before removing the UML declarations**

Remove `AudioRecording` from the persisted class list, `AudioStoragePort` from the boundary list, and `AUDIO_RECORDING AudioRecording` from `ENTITY_MAP` in `tests/verify_class_diagrams.sh`. Add these positive checks after the forbidden-storage loop:

```sh
for name in RecitationSession RecitationSegment RecitationAnalysis RecitationError AudioCapturePort AIAnalysisPort AudioData; do
  rg -q "class $name([ {]|$)" "$complete" || { echo "Missing transient-audio model element: $name"; exit 1; }
done
```

- [ ] **Step 2: Run the verifier to prove it still fails on current UML storage declarations**

Run: `sh tests/verify_class_diagrams.sh`

Expected: non-zero exit with `Persisted learner-audio storage is forbidden` for a class-diagram source.

- [ ] **Step 3: Remove storage classes, members, methods, and relationships**

From `itqan-class-diagram.mmd`, delete `class AudioRecording`, `class AudioStoragePort`, `RecitationRepository.saveRecording`, the `RecitationSession *-- AudioRecording` relationship, and all `AudioStoragePort` dependencies. From `recitation-feedback-classes.mmd`, delete the same selected declarations and relationships. Retain `AudioData`, `AudioCapturePort`, and `AIAnalysisPort` because they carry in-memory data during capture and inference.

Update `CLASS_DIAGRAM_NOTES.md` to state that learner audio is transient and discarded after analysis; retained records are session, segment, analysis, error, feedback, and progress results. Remove any claim that the class model defines storage, retention, or deletion for learner recordings.

- [ ] **Step 4: Run the full verifier and whitespace check**

Run: `sh tests/verify_class_diagrams.sh && git diff --check`

Expected: successful exit; five temporary SVGs render; every one of the remaining 33 ERD entities maps to the canonical UML source.

- [ ] **Step 5: Commit the UML alignment**

```bash
git add docs/diagrams/class/itqan-class-diagram.mmd docs/diagrams/class/recitation-feedback-classes.mmd docs/diagrams/class/CLASS_DIAGRAM_NOTES.md tests/verify_class_diagrams.sh
git commit -m "docs: align UML with transient audio policy"
```

### Task 3: Regenerate artifacts and verify the policy end to end

**Files:**
- Modify: `docs/database/itqan-erd.svg`
- Modify: `docs/diagrams/class/itqan-class-diagram.svg`
- Modify: `docs/diagrams/class/recitation-feedback-classes.svg`

**Interfaces:**
- Consumes: Task 1 ERD source and Task 2 class-diagram sources.
- Produces: permanent rendered artifacts that match the source policy.

- [ ] **Step 1: Render updated ERD and class artifacts**

```bash
npx -y @mermaid-js/mermaid-cli -i docs/database/itqan-erd.mmd -o docs/database/itqan-erd.svg -b white -w 5600 -H 3600
npx -y @mermaid-js/mermaid-cli -i docs/diagrams/class/itqan-class-diagram.mmd -o docs/diagrams/class/itqan-class-diagram.svg -b white -w 5600 -H 3600
npx -y @mermaid-js/mermaid-cli -i docs/diagrams/class/recitation-feedback-classes.mmd -o docs/diagrams/class/recitation-feedback-classes.svg -b white -w 3600 -H 2600
```

- [ ] **Step 2: Check the permanent SVGs contain no removed storage names**

Run:

```bash
for svg in docs/database/itqan-erd.svg docs/diagrams/class/itqan-class-diagram.svg docs/diagrams/class/recitation-feedback-classes.svg; do
  test -s "$svg"
  rg -q '<svg' "$svg"
  ! rg -qi 'AUDIO_RECORDING|AudioRecording|AudioStoragePort|storageUri|retentionExpiresAt|deletedAt' "$svg"
done
```

Expected: successful exit for all three SVGs.

- [ ] **Step 3: Run final policy verification**

Run: `sh tests/verify_class_diagrams.sh && git diff --check`

Expected: successful exit with five class-diagram renders and no whitespace errors.

- [ ] **Step 4: Commit regenerated artifacts**

```bash
git add docs/database/itqan-erd.svg docs/diagrams/class/itqan-class-diagram.svg docs/diagrams/class/recitation-feedback-classes.svg
git commit -m "docs: render transient audio policy artifacts"
```
