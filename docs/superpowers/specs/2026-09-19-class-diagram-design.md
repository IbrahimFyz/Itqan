# Itqan Class Diagram Design Specification

**Date:** 2026-09-19  
**Phase:** IS498 — analysis and system design  
**Status:** Approved conversational design, awaiting written-spec review  
**Source artifacts:** `docs/project/REQUIREMENTS.md`, `docs/database/itqan-erd.mmd`, `docs/database/RELATIONAL_SCHEMA.md`, use-case, activity, sequence, and architecture diagrams.

## 1. Purpose

Create a complete, implementation-neutral UML class model for Itqan. The model must explain how domain objects, application services, persistence boundaries, and external audio/AI components collaborate without committing the project to Flutter, FastAPI, PostgreSQL libraries, or a specific AI model.

The class model must remain consistent with the merged ERD while adding behavior that an ERD does not express.

## 2. Deliverables

The class-diagram package will contain:

1. `docs/diagrams/class/itqan-class-diagram.mmd` — canonical complete Mermaid UML source.
2. `docs/diagrams/class/itqan-class-diagram.svg` — complete report-ready rendering.
3. `docs/diagrams/class/identity-quran-classes.mmd` and `.svg` — detailed identity and Quran reference view.
4. `docs/diagrams/class/recitation-feedback-classes.mmd` and `.svg` — detailed recitation, AI analysis, and feedback view.
5. `docs/diagrams/class/progress-teacher-classes.mmd` and `.svg` — detailed progress, teacher, class, and messaging view.
6. `docs/diagrams/class/gamification-classes-proposed.mmd` and `.svg` — proposed Al-Mushajji view.
7. `docs/diagrams/class/CLASS_DIAGRAM_NOTES.md` — class responsibilities, relationship rationale, confirmed/proposed scope, and ERD consistency notes.

The complete diagram is authoritative. Domain views repeat selected classes only to improve report readability; they do not define separate models.

## 3. UML conventions

- Use Mermaid `classDiagram` syntax.
- `+` means public, `-` means private, and `#` means protected.
- Use `<<entity>>`, `<<value object>>`, `<<enumeration>>`, `<<service>>`, `<<repository>>`, and `<<external>>` stereotypes.
- Use composition (`*--`) when the child has no independent lifecycle, aggregation (`o--`) for ownership without strict lifecycle dependence, association (`--`) for domain links, inheritance (`<|--`) only for true subtype relationships, and dependency (`..>`) for service use.
- Show multiplicities on every domain relationship.
- Methods express domain/application responsibilities, not framework endpoints.
- Nullable references use a `?` suffix. Collections use `List~T~`.
- Async/framework syntax is excluded because the final technology stack is unresolved.
- Proposed classes and methods include the `<<proposed>>` annotation in their class body or name label.
- No Admin actor, class, service, or repository is allowed.

## 4. Architectural layers

### 4.1 Domain entities and value objects

Domain classes hold identity, state, invariants, and behavior. They do not call repositories, microphones, storage providers, or AI engines directly.

### 4.2 Application services

Services coordinate use cases. They validate permissions and lifecycle transitions, call repositories and external ports, and return domain objects or results. They do not contain presentation logic.

### 4.3 Repository interfaces

Repositories define persistence operations for aggregate roots. The diagram models interfaces only and does not invent database implementation classes.

### 4.4 External ports

External interfaces isolate microphone capture, audio storage, and AI recitation analysis. Concrete providers remain unresolved.

## 5. Identity and access classes

### User `<<entity>>`

Attributes:

- `userId: UUID`
- `email: String`
- `passwordHash: String`
- `displayName: String`
- `preferredLanguage: LanguageCode`
- `accountStatus: AccountStatus`
- `createdAt: DateTime`
- `updatedAt: DateTime`
- `lastLoginAt: DateTime?`

Methods:

- `+changeDisplayName(name: String): void`
- `+changePreferredLanguage(language: LanguageCode): void`
- `+activate(): void`
- `+suspend(): void`
- `+markDeleted(): void`
- `+hasRole(roleCode: String): Boolean`

### Role `<<entity>>`

Attributes: `roleId`, `roleCode`, `nameAr`, `nameEn`.

Methods: `+matches(code: String): Boolean`.

### UserRole `<<entity>>`

Attributes: `userId`, `roleId`, `assignedAt`.

This association class permits one user to hold learner and teacher roles simultaneously.

### LearnerProfile `<<entity>>`

Attributes: `learnerId`, `learningGoal?`, `experienceLevel?`, `remindersEnabled`.

Methods:

- `+updateLearningGoal(goal: String): void`
- `+setExperienceLevel(level: String): void`
- `+setReminders(enabled: Boolean): void`

### TeacherProfile `<<entity>>`

Attributes: `teacherId`, `biography?`, `qualification?`.

Methods: `+updateBiography(text: String): void`, `+updateQualification(text: String): void`.

### Identity enumerations

- `LanguageCode`: `AR`, `EN`
- `AccountStatus`: `ACTIVE`, `SUSPENDED`, `DELETED`

There is no `Learner extends User` or `Teacher extends User` inheritance. Optional profiles preserve the approved ability for one account to hold both roles.

## 6. Quran and Tajweed classes

### Juz `<<entity>>`

Attributes: `juzId`, `juzNumber`, `nameAr`, `nameEn`, `surahs: List<Surah>`.

Methods: `+getOrderedSurahs(): List<Surah>`.

### Surah `<<entity>>`

Attributes: `surahId`, `juzId`, `nameAr`, `nameEn`, `revelationOrder?`, `revelationType?`, `verseCount`, `displayOrder`, `verses: List<Verse>`.

Methods: `+getVerse(number: Integer): Verse`, `+containsVerse(number: Integer): Boolean`.

### Verse `<<entity>>`

Attributes: `verseId`, `surahId`, `verseNumber`, `uthmaniText`, `normalizedText`, `pageNumber?`, `hizbNumber?`, `words: List<VerseWord>`.

Methods: `+getWord(position: Integer): VerseWord`, `+getDisplayText(): String`.

### VerseWord `<<value object>>`

Attributes: `wordId`, `verseId`, `wordPosition`, `uthmaniText`, `normalizedText`.

Methods: `+matchesNormalized(text: String): Boolean`.

### TajweedRule `<<entity>>`

Attributes: `tajweedRuleId`, `ruleCode`, bilingual names/descriptions, `supported`.

Methods: `+isAvailableForAnalysis(): Boolean`.

## 7. Recitation and analysis classes

### AIMode `<<entity>>`

Attributes: `aiModeId`, `modeCode`, bilingual names, `description`, `active`.

Methods: `+isSelectable(): Boolean`.

Approved mode values: `AL_MUJAWWID`, `AL_MUSHAJJI`, `AL_MUALLIM`.

### RecitationSession `<<entity, aggregate root>>`

Attributes: `sessionId`, `learnerId`, `surahId`, `aiModeId`, timestamps, `status`, `completionPercentage`, `masteryScore?`, duration, pause count, error count, failure reason, `segments`, and `pauseEvents`.

Methods:

- `+start(startedAt: DateTime): void`
- `+addSegment(segment: RecitationSegment): void`
- `+recordPause(event: PauseEvent): void`
- `+complete(endedAt: DateTime, masteryScore: Decimal): void`
- `+abandon(endedAt: DateTime): void`
- `+fail(reason: String, endedAt: DateTime): void`
- `+calculateCompletion(): Decimal`
- `+canAcceptAudio(): Boolean`

Lifecycle invariant: only an active session accepts segments, pauses, or completion.

### AudioRecording `<<entity>>`

Attributes: recording identity, session identity, storage URI, format, duration, sample rate, file size, consent, recording time, retention expiry, deletion time.

Methods:

- `+registerStorage(uri: String): void`
- `+scheduleRetention(expiry: DateTime): void`
- `+markDeleted(at: DateTime): void`
- `+isRetained(at: DateTime): Boolean`

### RecitationSegment `<<entity>>`

Attributes: segment identity, session/verse identity, order, audio offsets, recognized text, confidence, fluency, status, and optional analysis.

Methods:

- `+attachRecognizedText(text: String, confidence: Decimal): void`
- `+markProcessing(): void`
- `+attachAnalysis(analysis: RecitationAnalysis): void`
- `+fail(): void`
- `+durationMs(): Integer`

### RecitationAnalysis `<<entity>>`

Attributes: analysis/segment identity, status, model name/version, processing time, analysis timestamp, confidence, failure reason, and detected errors.

Methods:

- `+start(): void`
- `+addError(error: RecitationError): void`
- `+complete(confidence: Decimal): void`
- `+fail(reason: String): void`
- `+acceptedErrors(): List<RecitationError>`

### PauseEvent `<<entity>>`

Attributes: pause/session/optional segment identity, start, duration, type, prompt state, and prompt delay.

Methods: `+requiresPrompt(thresholdMs: Integer): Boolean`, `+markPromptTriggered(delayMs: Integer): void`.

### Recitation enumerations

- `SessionStatus`: `ACTIVE`, `COMPLETED`, `ABANDONED`, `FAILED`
- `SegmentStatus`: `CAPTURED`, `PROCESSING`, `ANALYZED`, `FAILED`
- `AnalysisStatus`: `PENDING`, `PROCESSING`, `COMPLETED`, `FAILED`
- `PauseType`: `NATURAL`, `HESITATION`, `FORGOTTEN`, `TECHNICAL`

## 8. Error and feedback classes

### ErrorType `<<entity>>`

Attributes: identity, optional Tajweed rule, code, category, bilingual names, severity, and description.

Methods: `+isTajweedError(): Boolean`.

### RecitationError `<<entity>>`

Attributes: identity, analysis/error type, optional word, detected/expected text, audio offsets, confidence, review status, detection time, and feedback collection.

Methods:

- `+addFeedback(feedback: ErrorFeedback): void`
- `+accept(): void`
- `+reject(): void`
- `+correct(): void`
- `+hasExactWordLocation(): Boolean`

### ErrorFeedback `<<entity>>`

Attributes: identity, error identity, type, language, feedback text, optional correction, and creation time.

Methods: `+isForLanguage(language: LanguageCode): Boolean`.

### AudioAssistance `<<entity>>`

Attributes: identity, exactly one of error/pause identity, verse identity, audio URI, assistance type, and playback time.

Methods: `+markPlayed(at: DateTime): void`, `+validateSingleTrigger(): Boolean`.

### Feedback enumerations

- `ErrorCategory`: `PRONUNCIATION`, `TAJWEED`, `OMISSION`, `INSERTION`, `SUBSTITUTION`, `FLUENCY`
- `ReviewStatus`: `UNREVIEWED`, `ACCEPTED`, `REJECTED`, `CORRECTED`
- `FeedbackType`: `TEXT`, `VISUAL`, `INSTRUCTION`
- `AssistanceType`: `CORRECTION`, `CONTINUATION`, `EXAMPLE`

## 9. Progress classes

### LearnerSurahProgress `<<entity>>`

Attributes: learner/Surah composite identity, attempt counts, best/average/latest mastery, full-mastery flag, and practice/mastery timestamps.

Methods:

- `+recordAttempt(session: RecitationSession): void`
- `+recalculateAverage(history: List<MasteryScoreHistory>): void`
- `+markMastered(at: DateTime): void`
- `+isMasteryImproving(history: List<MasteryScoreHistory>): Boolean`

### MasteryScoreHistory `<<entity>>`

Attributes: history, learner, Surah, and session identity; Tajweed, pronunciation, fluency, pause, and final scores; calculation time; formula version.

Methods: `+validateScoreRange(): Boolean`.

The class stores formula results but does not calculate unapproved weights.

### DailyPractice `<<entity>>`

Attributes: learner/date composite identity, session counts, practice seconds, and verses practiced.

Methods: `+recordSession(session: RecitationSession): void`.

### PracticeStreak `<<entity>>`

Attributes: learner identity, current/longest streak, start date, last-practice date, and update time.

Methods: `+recordPractice(date: Date): void`, `+resetIfBroken(date: Date): void`.

## 10. Teacher and class classes

### LearningClass `<<entity, aggregate root>>`

Attributes: class/teacher identity, name, description, join code, status, timestamps, enrollments, and assignments.

Methods:

- `+inviteLearner(learnerId: UUID): ClassEnrollment`
- `+activateEnrollment(learnerId: UUID): void`
- `+removeLearner(learnerId: UUID): void`
- `+archive(): void`
- `+hasActiveLearner(learnerId: UUID): Boolean`
- `+addAssignment(assignment: ClassAssignment): void`

### ClassEnrollment `<<entity>>`

Attributes: enrollment/class/learner identity, status, enrollment time, and end time.

Methods: `+accept(at: DateTime): void`, `+leave(at: DateTime): void`, `+remove(at: DateTime): void`, `+isActive(): Boolean`.

### ClassAssignment `<<entity, proposed>>`

Attributes: assignment/class/Surah/teacher identity, title, instructions, target mastery, due time, and creation time.

Methods: `+isDue(at: DateTime): Boolean`, `+meetsTarget(score: Decimal): Boolean`.

### AssignmentProgress `<<entity, proposed>>`

Attributes: assignment/learner identity, optional best session, status, best mastery, completion time, and update time.

Methods: `+recordAttempt(session: RecitationSession): void`, `+markCompleted(at: DateTime): void`.

### TeacherMessage `<<entity>>`

Attributes: message, teacher, learner, optional class/session identity, message text, sent time, and read time.

Methods: `+markRead(at: DateTime): void`, `+referencesSession(): Boolean`.

### StudentPerformanceSnapshot `<<entity, proposed>>`

Attributes: snapshot/class/learner identity, generation time, mastered Surah count, average mastery, sessions, practice time, and streak.

Methods: `+isCurrent(asOf: DateTime, maxAgeMinutes: Integer): Boolean`.

### Teacher enumerations

- `ClassStatus`: `ACTIVE`, `ARCHIVED`, `CLOSED`
- `EnrollmentStatus`: `INVITED`, `ACTIVE`, `LEFT`, `REMOVED`
- `AssignmentStatus`: `NOT_STARTED`, `IN_PROGRESS`, `COMPLETED`, `OVERDUE`

## 11. Proposed Al-Mushajji classes

All classes in this section are marked `<<proposed>>` because the mode is approved but its mechanics are unresolved.

### Challenge

Attributes: identity, bilingual titles/descriptions, type, target, schedule, and active flag.

Methods: `+isAvailable(at: DateTime): Boolean`, `+isCompletedBy(value: Integer): Boolean`.

### LearnerChallenge

Attributes: learner/challenge identity, progress, status, join time, and completion time.

Methods: `+incrementProgress(amount: Integer): void`, `+complete(at: DateTime): void`.

### Reward

Attributes: identity, code, bilingual names, description, and type.

Methods: `+matches(code: String): Boolean`.

### LearnerReward

Attributes: learner/reward identity, optional challenge identity, and award time.

Methods: `+wasAwardedByChallenge(): Boolean`.

## 12. Application services

### AuthenticationService `<<service>>`

- `+register(email, password, displayName, roles): User`
- `+authenticate(email, password): User`
- `+changeProfile(userId, profileData): User`
- Dependencies: `UserRepository`, password-hashing mechanism (not modeled as a technology).

### QuranCatalogService `<<service>>`

- `+browseJuzAmma(): List<Surah>`
- `+getSurah(surahId): Surah`
- `+getVerse(verseId): Verse`
- Dependency: `QuranRepository`.

### RecitationService `<<service>>`

- `+startSession(learnerId, surahId, modeId): RecitationSession`
- `+captureSegment(sessionId, verseId): RecitationSegment`
- `+recordPause(sessionId, pause): PauseEvent`
- `+endSession(sessionId): RecitationSession`
- `+abandonSession(sessionId): RecitationSession`
- Dependencies: `RecitationRepository`, `QuranRepository`, `AudioCapturePort`, `AudioStoragePort`.

### AnalysisService `<<service>>`

- `+analyzeSegment(segmentId): RecitationAnalysis`
- `+reanalyzeSegment(segmentId): RecitationAnalysis`
- `+getSupportedTajweedRules(): List<TajweedRule>`
- Dependencies: `RecitationRepository`, `QuranRepository`, `AIAnalysisPort`.

### FeedbackService `<<service>>`

- `+buildFeedback(errorId, language): List<ErrorFeedback>`
- `+provideAudioAssistance(triggerId): AudioAssistance`
- Dependencies: `RecitationRepository`, `QuranRepository`, `AudioStoragePort`.

### ProgressService `<<service>>`

- `+updateFromCompletedSession(sessionId): LearnerSurahProgress`
- `+getLearnerProgress(learnerId): List<LearnerSurahProgress>`
- `+updateDailyPractice(sessionId): DailyPractice`
- `+updateStreak(learnerId, date): PracticeStreak`
- Dependencies: `RecitationRepository`, `ProgressRepository`.

### ClassService `<<service>>`

- `+createClass(teacherId, name): LearningClass`
- `+inviteLearner(classId, learnerId): ClassEnrollment`
- `+acceptInvitation(classId, learnerId): ClassEnrollment`
- `+removeLearner(classId, learnerId): void`
- `+createAssignment(classId, assignmentData): ClassAssignment` (proposed)
- Dependencies: `UserRepository`, `ClassRepository`.

### TeacherMonitoringService `<<service>>`

- `+getClassProgress(teacherId, classId): List<LearnerSurahProgress>`
- `+getLearnerPerformance(teacherId, classId, learnerId): StudentPerformanceSnapshot`
- Dependencies: `ClassRepository`, `ProgressRepository`, `RecitationRepository`.

### MessagingService `<<service>>`

- `+sendMessage(teacherId, learnerId, classId, text, sessionId?): TeacherMessage`
- `+markRead(messageId, learnerId): TeacherMessage`
- Dependencies: `ClassRepository`; active enrollment is mandatory.

### GamificationService `<<service, proposed>>`

- `+joinChallenge(learnerId, challengeId): LearnerChallenge`
- `+recordProgress(learnerId, challengeId, amount): LearnerChallenge`
- `+awardReward(learnerId, rewardId, challengeId?): LearnerReward`
- Dependency: `GamificationRepository`.

## 13. Repository interfaces

### UserRepository `<<repository>>`

- `+findById(userId): User?`
- `+findByEmail(email): User?`
- `+save(user): User`
- `+saveLearnerProfile(profile): LearnerProfile`
- `+saveTeacherProfile(profile): TeacherProfile`

### QuranRepository `<<repository>>`

- `+findJuz(number): Juz?`
- `+findSurah(surahId): Surah?`
- `+findVerse(verseId): Verse?`
- `+listJuzAmmaSurahs(): List<Surah>`
- `+listSupportedTajweedRules(): List<TajweedRule>`

### RecitationRepository `<<repository>>`

- `+findSession(sessionId): RecitationSession?`
- `+saveSession(session): RecitationSession`
- `+saveRecording(recording): AudioRecording`
- `+saveSegment(segment): RecitationSegment`
- `+saveAnalysis(analysis): RecitationAnalysis`

### ProgressRepository `<<repository>>`

- `+findSurahProgress(learnerId, surahId): LearnerSurahProgress?`
- `+saveSurahProgress(progress): LearnerSurahProgress`
- `+listMasteryHistory(learnerId, surahId): List<MasteryScoreHistory>`
- `+saveMasteryHistory(history): MasteryScoreHistory`
- `+saveDailyPractice(practice): DailyPractice`
- `+saveStreak(streak): PracticeStreak`

### ClassRepository `<<repository>>`

- `+findClass(classId): LearningClass?`
- `+saveClass(class): LearningClass`
- `+findActiveEnrollment(classId, learnerId): ClassEnrollment?`
- `+saveEnrollment(enrollment): ClassEnrollment`
- `+saveMessage(message): TeacherMessage`

### GamificationRepository `<<repository, proposed>>`

- `+findChallenge(challengeId): Challenge?`
- `+saveLearnerChallenge(progress): LearnerChallenge`
- `+findReward(rewardId): Reward?`
- `+saveLearnerReward(reward): LearnerReward`

## 14. External ports

### AudioCapturePort `<<external>>`

- `+startCapture(sessionId): void`
- `+readSegment(): AudioData`
- `+stopCapture(): AudioData`

### AudioStoragePort `<<external>>`

- `+store(audio: AudioData, consent: Boolean): AudioRecording`
- `+load(recordingId): AudioData`
- `+delete(recordingId): void`

### AIAnalysisPort `<<external>>`

- `+analyze(audio: AudioData, expectedVerse: Verse): AnalysisResult`
- `+supportedRules(): List<TajweedRule>`

`AudioData` and `AnalysisResult` are transport value objects, not persisted domain entities.

## 15. Principal relationships

- `User 1 *-- 0..1 LearnerProfile` and `User 1 *-- 0..1 TeacherProfile`.
- `User 1 -- 0..* UserRole -- 1 Role`.
- `Juz 1 *-- 1..* Surah`; `Surah 1 *-- 1..* Verse`; `Verse 1 *-- 1..* VerseWord`.
- `LearnerProfile 1 -- 0..* RecitationSession`.
- `RecitationSession 1 *-- 0..1 AudioRecording`, `1 *-- 0..* RecitationSegment`, and `1 *-- 0..* PauseEvent`.
- `RecitationSegment 1 *-- 0..1 RecitationAnalysis`; `RecitationAnalysis 1 *-- 0..* RecitationError`; `RecitationError 1 *-- 0..* ErrorFeedback`.
- `RecitationError 0..1 -- 0..* AudioAssistance`; `PauseEvent 0..1 -- 0..* AudioAssistance` with exactly one trigger per assistance record.
- `LearnerProfile` and `Surah` connect through `LearnerSurahProgress` and `MasteryScoreHistory`.
- `TeacherProfile 1 -- 0..* LearningClass`; `LearningClass 1 *-- 0..* ClassEnrollment`; each enrollment refers to one learner.
- `LearningClass 1 *-- 0..* ClassAssignment` and `ClassAssignment 1 *-- 0..* AssignmentProgress` are proposed.
- `TeacherProfile 1 -- 0..* TeacherMessage`; each message targets one learner and may reference one class/session.
- Challenge/reward relationships remain proposed and visually separated.
- Services depend on repositories and external ports; entities never depend on services.

## 16. Main interaction flows

### Learner recitation

1. `RecitationService` validates learner, Surah, and AI mode.
2. It creates an active `RecitationSession` and invokes `AudioCapturePort`.
3. Captured audio becomes `RecitationSegment` objects and is stored through `AudioStoragePort` according to consent.
4. `AnalysisService` invokes `AIAnalysisPort` and attaches `RecitationAnalysis`, `RecitationError`, and feedback data.
5. `FeedbackService` selects localized text/audio guidance.
6. Completing the session triggers `ProgressService` to update mastery, daily practice, and streak records.

### Teacher monitoring

1. `ClassService` manages class ownership and enrollment.
2. `TeacherMonitoringService` verifies the teacher owns the class and the learner has active enrollment.
3. It reads progress and session summaries through repositories.
4. `MessagingService` applies the same authorization before creating a `TeacherMessage`.

## 17. Errors and invariants

The design must make these invalid states visible in notes or method responsibilities:

- duplicate email or class join code;
- missing learner/teacher role for a requested operation;
- inactive, closed, or unauthorized class relationship;
- session transition from a non-active state;
- analysis requested before audio/segment capture;
- confidence or score outside its valid range;
- assistance linked to both an error and a pause, or neither;
- audio storage without consent where consent is required;
- use of an unsupported Tajweed rule;
- progress update from an incomplete session.

Framework exceptions, HTTP status codes, retries, and UI error messages are outside the class diagram because the implementation architecture is unresolved.

## 18. ERD consistency rules

- Every persisted entity maps to one merged ERD entity using the same name, except naming style changes from uppercase snake case to PascalCase.
- Primary and foreign-key attributes remain represented in detailed diagrams.
- ERD composite identities remain composite identities in the class model.
- The class diagram may add behavior, enumerations, services, repositories, and external ports but may not silently add persisted tables.
- Proposed ERD tables remain proposed UML classes.
- `LearningClass` is used instead of the reserved name `Class`.
- The absence of an Admin role is preserved.

## 19. Visual organization

- Complete diagram: left-to-right flow from identity/Quran → recitation/analysis → feedback/progress → teacher/gamification, with services above domain classes and repositories/external ports below.
- Identity/Quran view: compact reference model emphasizing composition and lookups.
- Recitation/feedback view: central session aggregate with lifecycle methods and external ports.
- Progress/teacher view: learner progress and teacher authorization relationships.
- Proposed gamification view: visually and textually labeled as proposed.
- Render complete diagram at a large landscape size; render domain views at report-page-friendly landscape sizes.

## 20. Validation criteria

1. All Mermaid sources parse and render without errors.
2. The complete diagram includes every persisted ERD entity, all services, repository interfaces, external ports, and enumerations described here.
3. Every persisted class has a matching ERD entity and consistent key attributes.
4. No Admin class or implementation-specific framework class appears.
5. Proposed classes are visibly marked.
6. All relationships show multiplicity and use appropriate UML relationship types.
7. Rendered SVG text remains readable and boxes do not clip attributes or methods.
8. Domain views contain no relationship that contradicts the complete diagram.
