# Itqan class diagram — Task 8 review notes

**Diagram:** [open SVG](itqan-class-diagram.svg) · [editable Mermaid source](itqan-class-diagram.mmd). This is **one class diagram** at the repository root.

**Sources:** [final requirements](Itqan_Requirements.md), [reviewed Task 1 scenarios](docs/updated-diagrams/scenarios/USE_CASE_SCENARIOS.md), [Task 4 architecture](docs/updated-diagrams/architecture/ARCHITECTURE.md), [approved ERD](docs/updated-diagrams/erd/itqan-erd.mmd), and [Task 7 relational schema](itqan-relational-schema.md). The older `docs/diagrams/class/` model predates the final requirements and was not reused.

## How to read it

The diagram shows the main domain classes and the services that act on them. Solid lines show associations and multiplicities. Dashed arrows show service dependencies. The filled diamond means `ComparisonEngine` is contained in `RecitationService`, as in Task 4. `?` means nullable. Class names use UML camel case; the schema uses PostgreSQL snake case. A class diagram shows essential attributes and responsibilities, so the [schema](itqan-relational-schema.md) remains the complete list of stored fields, keys, constraints and deletion effects.

`Account.accountType` is exactly one immutable value: Reader or Teacher. There is no Reader/Teacher inheritance. Reader or Teacher labels on association lines state which account type may participate. Only Teachers have a school name; it is stored in `TEACHER_DETAIL` and managed through `AccountService`.

## Responsibilities and boundaries

- `AccountService` creates and updates accounts, manages the two dated Reader consents and the stored-data summary, and deletes accounts. Credentials, sign-in, sign-out and identity removal belong to the managed Identity Provider. Itqan stores no password. The app routes users by account type and suppresses inactivity logout during an active session (FR-01–FR-03, FR-27–FR-29).
- The phone app browses bundled Juz Amma text offline, shows verses, captures verse audio only in memory, displays per-verse feedback while recitation continues, detects pauses, shows the next-word hint and plays bundled reference word audio only when tapped. It asks for microphone permission before recitation. These app actions are not stored classes (FR-04–FR-06, FR-11–FR-12, FR-16–FR-18, FR-26).
- `RecitationService` checks Reader role and recitation consent, starts a session for a selected Surah and mode, sends each verse to the separate stateless Analysis Service, and uses its `ComparisonEngine` to classify and locate errors against read-only Word references. Analysis failure gives no invented mistakes or counted words. The service ends and scores sessions on completion, early stop or interruption, including logout (FR-07–FR-20). Audio, phonemes, feedback and hints remain transient.
- `ProgressService` derives history, results, best score per Surah, full mastery, average mastery and practice streak from ended sessions. It creates no required progress table (FR-20–FR-22).
- `ClassService` handles Teacher-owned classes, immutable unique join codes, Reader enrolment and leave, authorized dashboard reads, one-way messages, recipients and read dates. It checks active enrolment and Teacher ownership on each dashboard read (FR-23–FR-25).

These operations name responsibilities, not a proposed API. `RecitationSession` represents the ended summary that is stored; Started and Active are transient runtime states. A zero-word session has a NULL score. Every `Mistake` refers to one expected `Word` from its session's Surah; an added-word error points to the following expected Word. Tajweed-only errors use one of Ghunnah, Qalqalah or Madd and a 0.5 penalty; whole-word errors use penalty 1. A Word contributes at most 1 effective error. These and the score formula are specified in the [schema](itqan-relational-schema.md) and requirements.

A Reader can have several class enrolments, but only one active enrolment per Reader/Class. Rejoining creates a new enrolment with a new join date. Teacher-sharing consent is required to join; withdrawing it ends all active enrolments. Dashboard access shows only sessions ended on or after the earliest active join date across that Teacher's classes. A whole-class message snapshots its active recipients at send time; Readers cannot reply, and delivered messages remain after leaving. Reader and Teacher deletion follow FR-28.

## ERD entity mapping

Eleven of the 14 persistent ERD entities are shown as classes. The other three remain required in the ERD and schema; omitting their boxes keeps this single diagram readable.

| ERD entity | In this diagram | Reason or relationship |
|---|---|---|
| ACCOUNT | `Account` | Reader owns consents, sessions, enrolments and received messages; Teacher owns classes and sent messages. |
| TEACHER_DETAIL | Data-only, omitted | Required school name for Teachers; 1:1 Teacher detail in schema, managed by `AccountService`. |
| CONSENT_RECORD | `ConsentRecord` | Reader can grant, withdraw and regrant each purpose. |
| SURAH | `Surah` | Contains Verses; selected for a Session. |
| VERSE | `Verse` | Contains Words. |
| WORD | `Word` | Expected Word for each Mistake. |
| TAJWEED_RULE | Reference-only, omitted | `Mistake.ruleId?` refers to the required Ghunnah, Qalqalah or Madd reference row. |
| RECITATION_SESSION | `RecitationSession` | Ended summary owned by Reader, with Mistakes. |
| MISTAKE | `Mistake` | Belongs to one Session and expected Word; optional Tajweed rule reference. |
| QURAN_CLASS | `QuranClass` | Owned by Teacher; has Enrolments and Messages. |
| ENROLMENT | `Enrolment` | Connects Reader and Class, including joined and left dates. |
| MESSAGE | `Message` | Sent by Teacher in a Class. |
| MESSAGE_RECIPIENT | `MessageRecipient` | Connects each delivered Message to a Reader and read date. |
| DELETION_LOG | Audit-only, omitted | Anonymous account type and deletion date; deliberately has no Account link. |

The Identity Provider, phone app and stateless Analysis Service are architecture components described above, not persistent domain classes. The Database is also a component. There are no persisted audio, phoneme, feedback, prompt, assignment, challenge, reward or performance-snapshot classes (§8.3).

## Functional-requirement coverage

| Requirement | Responsibility shown or explained |
|---|---|
| FR-01 Create Account | `AccountService`, `Account`; Teacher school name in required `TEACHER_DETAIL`; managed Identity Provider. |
| FR-02 Login | Identity Provider authenticates; immutable `Account.accountType` selects Reader or Teacher area. |
| FR-03 Manage Profile | `AccountService` updates display name, language and Teacher school name; provider owns email. |
| FR-04 Browse Juz Amma | App browses bundled content; `Surah` represents read-only reference. |
| FR-05 Select Surah | `RecitationService.startSession` requires a selected `Surah`. |
| FR-06 Display Verses | App displays bundled Uthmani text; `Verse` represents it. |
| FR-07 Select AI Mode | App selects Mujawwid or Mushajji; `RecitationSession.mode` records it. |
| FR-08 Al-Mujawwid | `RecitationService` and `ComparisonEngine` analyse; app gives direct feedback. |
| FR-09 Al-Mushajji | Same analysis and score; app gives encouraging feedback and praise. |
| FR-10 Al-Mu'allim | Teacher `Account.accountType` grants `ClassService` features without a selected mode. |
| FR-11 Start Session | `RecitationService.startSession` checks consent; app checks microphone permission. |
| FR-12 Capture Audio | App captures verse audio in memory; no audio class or record. |
| FR-13 Analyze Recitation | `RecitationService.analyseVerse` uses stateless Analysis Service; failed verses excluded. |
| FR-14 Detect Errors | `ComparisonEngine`, `Mistake`, optional `ruleId` to `TAJWEED_RULE`. |
| FR-15 Locate Error | Every `Mistake` associates with one expected `Word`; added-word position rule in schema. |
| FR-16 Provide Feedback | App highlights mistaken Words and shows mode-specific feedback during the next verse. |
| FR-17 Audio Assistance | App plays bundled reference audio on highlighted or prompted Word tap. |
| FR-18 Continue Recitation | App and `RecitationService` continue per verse without a restart. |
| FR-19 End Session | `RecitationService.endAndScoreSession` handles completed, early and interrupted endings. |
| FR-20 Results/History | `RecitationSession`, `Mistake`, `ProgressService.getResultsAndHistory`. |
| FR-21 Progress | `ProgressService.getMasteryAndStreak` derives best scores, full mastery and average mastery. |
| FR-22 Streak | `ProgressService.getMasteryAndStreak` derives consecutive practice days. |
| FR-23 Teacher Dashboard | `ClassService.getVisibleSessions` checks enrolment, ownership and join date at each read. |
| FR-24 Manage Class | `QuranClass`, `Enrolment`, `ClassService` create, rename, join and leave. |
| FR-25 Student Messages | `Message`, `MessageRecipient`, `ClassService.sendAndReadMessages`. |
| FR-26 Smart Prompting | App detects pause and shows transient next-Word hint. |
| FR-27 Consent/Privacy | `ConsentRecord`, `AccountService.grantOrWithdrawConsent`, stored-data summary. |
| FR-28 Delete Account | `AccountService.deleteAccount`; anonymous `DELETION_LOG` and cascades in schema. |
| FR-29 Logout | Identity Provider signs out; active `RecitationSession` ends interrupted. |

## Review status

The single SVG is rendered from its Mermaid source. Task 5 sequence diagrams are still Open; their eventual message names should be checked against these operations. The device-local practice-day ambiguity flagged in the schema remains: §8.1 stores no historical device time zone. No extra field or product decision is introduced here.
