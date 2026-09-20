# Artifact Consistency Design

**Date:** 2026-09-20  
**Scope:** Align the managed-identity, consent, enrollment, and terminology decisions across the current Itqan design artifacts.

## Decisions

1. Authentication is delegated to a managed identity provider. The application stores the provider subject identifier and account profile data; it never stores a password hash or verifies a password.
2. A learner joins a teacher's class only through an invitation accepted by the learner or guardian. There is no self-enrollment join-code path.
3. Consent is represented by an immutable `CONSENT_RECORD` history. Each record stores the user, purpose, policy version, collection method, grant time, and optional withdrawal time. A withdrawal ends the applicable consent without deleting the audit history.
4. Internal artifacts use `learner` and `enrollment`. `student` is reserved only for teacher-facing prose where it reads naturally.

## Data model

`USER` replaces `password_hash` with `identity_subject`, a unique value issued by the managed identity provider.

`LEARNING_CLASS` removes `join_code`.

`CONSENT_RECORD` contains:

- `consent_id UUID PK`
- `user_id UUID FK -> USER.user_id`
- `purpose_code VARCHAR(50)`
- `policy_version VARCHAR(30)`
- `collection_method VARCHAR(30)`
- `granted_at TIMESTAMPTZ`
- `withdrawn_at TIMESTAMPTZ NULL`

The schema requires a single active consent record per `(user_id, purpose_code)` and treats a non-null `withdrawn_at` as inactive.

## UML model

`User` exposes `identitySubject` instead of `passwordHash`.
`AuthenticationService` receives an identity-provider subject after provider authentication; it does not accept or verify passwords.
`ConsentRecord` is a persisted entity related to `User` and has `withdraw(at)` and `isActive()` operations.
`LearningClass` has invitation and enrollment operations only.

## Artifact boundaries

The Mermaid ERD, relational schema, complete UML diagram, applicable UML detail views, traceability, and verification script are authoritative editable sources and must be changed together.

`docs/system-architecture.pdf` and `docs/security-impact.pdf` are rendered artifacts with no tracked authoring source. Their current content contradicts the ERD on managed identity, consent, and terminology. The implementation creates a source-controlled correction note rather than attempting an unsafe visual reconstruction of those PDFs. The PDFs must be regenerated from their original authoring sources before submission.

## Verification

The consistency script must fail if a password-hash field, join-code field, or password-based authentication signature returns. It must require the `ConsentRecord`/`CONSENT_RECORD` mapping and render all Mermaid diagrams.

## Non-goals

- Selecting a specific identity-provider vendor.
- Adding guardian accounts or a guardian data model.
- Rebuilding the architecture or security PDFs without their source files.
- Changing the transient learner-audio policy.
