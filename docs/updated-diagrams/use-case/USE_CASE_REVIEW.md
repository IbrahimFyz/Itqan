# Use Case Diagram: final version

**Built from:** [`Itqan_Requirements.md`](../../../Itqan_Requirements.md) §2 (actors), §7.1 (use cases), §7.2 (relationships) and §13 (checklist). It replaces Use Case Diagram v2 (report Figure 2). Ibrahim owns the use case artifacts, so the team should approve the swap.

**Files:**
- `itqan-use-case.puml`: editable source.
- `itqan-use-case.svg` and `itqan-use-case.png`: rendered with PlantUML 1.2026.9.

**Size:** 794 × 1245 px. Scaled to fit an A4 portrait page, the text is about 8 pt and no lines cross.

## Purpose

The diagram shows what each actor can achieve with Itqan, as user goals only. Internal processing (capture, analysis, detection, location, scoring, progress update) is in UC-10's flow (§7.3) and in the activity and sequence diagrams.

## Contents

| Group | Use cases | Actor |
|---|---|---|
| Practice | UC-07 Browse and Read Surah, UC-10 Recite Surah, UC-13 View Session History, UC-14 View User Progress, UC-15 View Practice Streak | Quran Reader |
| Reached through relationships | UC-08 Select Surah, UC-09 Select AI Mode, UC-12 View Session Results (included); UC-11 Receive Audio Assistance, UC-28 Receive Smart Prompting (extend) | Quran Reader |
| Classes and messages | UC-26 Join Class via Code, UC-27 Leave Class, UC-16 View Teacher Messages | Quran Reader |
| Account (shared) | UC-01 Register, UC-02 Login, UC-03 Logout, UC-04 Manage Profile, UC-05 Manage Consent and Privacy, UC-06 Delete Account | Both |
| Teaching (Al-Mu'allim) | UC-17 Manage Class, UC-18 View Teacher Dashboard, UC-19 Send Student Messages | Teacher |

**Relationships** (exactly as in §7.2):
- **«include»:** Recite Surah → Select Surah, Select AI Mode and View Session Results; View Session History → View Session Results.
- **«extend»:** Receive Audio Assistance → Recite Surah at *word highlighted*; Receive Smart Prompting → Recite Surah at *pause detected*.

## §13 checklist

- [x] Only the actors Quran Reader and Teacher.
- [x] All 22 use cases, with the names and IDs from §7.1. UC-20 to UC-25 are unused; UC-26 and UC-28 are the report's official IDs.
- [x] «include» and «extend» exactly as in §7.2, with no others.
- [x] Every use case traces to FRs: §7.1 maps all FR-01 to FR-29.
- [x] No internal processing steps drawn as use cases.

## Changes from v2 (report Figure 2)

- **Removed as use cases** (internal steps, kept in the flows): Capture Recitation Audio, Analyze Recitation, Detect Recitation Errors, Identify Error Location, Provide Feedback, Receive Recitation Feedback, Generate Audio Help, Generate Smart Prompt, Calculate Mastery Score, Update Progress, Recite Quran, Continue Recitation, End Recitation Session.
- **Removed:** Al-Mujawwid and Al-Mushajji as use cases. They are options of Select AI Mode.
- **Merged into one use case:** the dashboard's sub-views go into View Teacher Dashboard; Create Class into Manage Class; Browse Juz Amma and View Surah Verses into Browse and Read Surah.
- **Added:** Logout, Manage Consent and Privacy, Delete Account, View Session History, Leave Class and View Teacher Messages, from FR-24 to FR-29.
- **Fixed:**
  - Login and Manage Profile are drawn once each, linked to both actors.
  - Register is now linked to the Teacher too.
  - The dangling arrow and the overlapping ellipses are gone.
  - Start Recitation Session is renamed **Recite Surah**, because it is the goal.

The report's §7.1, Table 9 and Appendix G Table 28 must be updated to this list.

## Rendering note

PlantUML 1.2026.9 applies a `title { … }` style to use cases, which removes their outlines and makes some labels bold. The source therefore has no title; the report's figure caption replaces it. The `---` edges and `[hidden]` links only control the layout. To re-render:

```bash
java -jar C:\Users\SAUDK\plantuml.jar -tsvg itqan-use-case.puml
```
