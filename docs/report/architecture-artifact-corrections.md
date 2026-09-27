# Architecture Artifact Corrections

The editable ERD, relational schema, UML diagrams, and traceability were aligned on 2026-09-20 with the architecture decisions already stated in `docs/system-architecture.pdf` and `docs/security-impact.pdf`:

- authentication uses a managed identity provider; the application stores an identity subject, never a password hash;
- consent is retained as per-purpose history in `CONSENT_RECORD`;
- learners create enrollments by entering a class join code; no invitation-link path is modeled;
- internal model terminology uses `learner` and `enrollment`.

The two PDFs have no tracked authoring sources, so they were not reconstructed or edited. Regenerate them from their original sources before submission, preserving these decisions and using `learner`/`enrollment` outside teacher-facing prose.
