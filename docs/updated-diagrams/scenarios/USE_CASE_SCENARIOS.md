# Itqan — Use Case Scenarios

**Task 1** in [`DIAGRAM_TASKS.md`](../../../DIAGRAM_TASKS.md).
**Source:** [`Itqan_Requirements.md`](../../../Itqan_Requirements.md), using §7.3 (flows), §4 (FRs), §6 (BRs), §9 (states) and §10 (parts).

Each scenario reviews the §7.3 flow and adds no new behaviour. The gaps found during the review were decided by Saud on 2026-10-29 and added to the requirements first; they are listed at the end.

**How to read a scenario:**
- Main steps are numbered 1, 2, 3, ….
- An exception or alternative is numbered after the step where it happens. For example, **4a** branches from step 4, then either rejoins the main flow ("→ step n") or ends ("ends").
- "System" means Itqan as a whole. Sequence diagrams split it into the §10 parts.
- Each scenario ends with its traces to FR, BR and UC IDs.

## Coverage

All 22 use cases in §7.1 are covered.

| ID | Use case | Primary actor | Section |
|---|---|---|---|
| UC-01 | Register | Quran Reader, Teacher | [→](#uc-01-register) |
| UC-02 | Login | Quran Reader, Teacher | [→](#uc-02-login) |
| UC-03 | Logout | Quran Reader, Teacher | [→](#uc-03-logout) |
| UC-04 | Manage Profile | Quran Reader, Teacher | [→](#uc-04-manage-profile) |
| UC-05 | Manage Consent and Privacy | Quran Reader, Teacher | [→](#uc-05-manage-consent-and-privacy) |
| UC-06 | Delete Account | Quran Reader, Teacher | [→](#uc-06-delete-account) |
| UC-07 | Browse and Read Surah | Quran Reader | [→](#uc-07-browse-and-read-surah) |
| UC-08 | Select Surah | Quran Reader (included by UC-10) | [→](#uc-08-select-surah) |
| UC-09 | Select AI Mode | Quran Reader (included by UC-10) | [→](#uc-09-select-ai-mode) |
| UC-10 | Recite Surah | Quran Reader | [→](#uc-10-recite-surah) |
| UC-11 | Receive Audio Assistance | Quran Reader (extends UC-10) | [→](#uc-11-receive-audio-assistance) |
| UC-12 | View Session Results | Quran Reader (included by UC-10, UC-13) | [→](#uc-12-view-session-results) |
| UC-13 | View Session History | Quran Reader | [→](#uc-13-view-session-history) |
| UC-14 | View User Progress | Quran Reader | [→](#uc-14-view-user-progress) |
| UC-15 | View Practice Streak | Quran Reader | [→](#uc-15-view-practice-streak) |
| UC-16 | View Teacher Messages | Quran Reader | [→](#uc-16-view-teacher-messages) |
| UC-17 | Manage Class | Teacher | [→](#uc-17-manage-class) |
| UC-18 | View Teacher Dashboard | Teacher | [→](#uc-18-view-teacher-dashboard) |
| UC-19 | Send Student Messages | Teacher | [→](#uc-19-send-student-messages) |
| UC-26 | Join Class via Code | Quran Reader | [→](#uc-26-join-class-via-code) |
| UC-27 | Leave Class | Quran Reader | [→](#uc-27-leave-class) |
| UC-28 | Receive Smart Prompting | Quran Reader (extends UC-10) | [→](#uc-28-receive-smart-prompting) |

---

## Account

### UC-01 Register

| | |
|---|---|
| **Actor** | New user, who becomes a Quran Reader or a Teacher |
| **Trigger** | The user chooses to create an account. |
| **Preconditions** | No account exists for the user's email. |
| **Outcome (success)** | One account of the chosen type exists, with Arabic as its language. A Teacher account has the school name and the Al-Mu'allim mode. Itqan stores no password. |
| **Outcome (failure)** | No account is created. |

**Main flow**
1. The user chooses the account type: Quran Reader or Teacher.
2. The user enters a display name and an email. A Teacher also enters the school name.
3. The system checks that every required field is filled.
4. The identity provider creates the credentials and returns the identity subject.
5. The system creates the account with the chosen type and language Arabic. A Teacher account gets Al-Mu'allim.

**Exceptions**
- **3a** A required field is empty (a Teacher's school name included) → the system refuses and marks the field → step 2.
- **4a** The email is already registered → the system refuses → ends.
- **4b** The identity provider is unavailable → "try again later" → ends; no account.

**Traces:** FR-01, FR-10 · BR-15

### UC-02 Login

| | |
|---|---|
| **Actor** | Quran Reader or Teacher |
| **Trigger** | The user opens Itqan while logged out. |
| **Preconditions** | The user has an account. |
| **Outcome (success)** | The user is in the area for their account type. |
| **Outcome (failure)** | The user stays logged out. |

**Main flow**
1. The user signs in through the identity provider.
2. The identity provider verifies the credentials and returns the identity subject.
3. The system finds the matching account.
4. The system opens the Reader area or the Teacher area.

**Exceptions**
- **2a** Wrong credentials → the identity provider rejects them → step 1.
- **2b** Identity provider unavailable → "try again later" → ends.
- **4a** The user tries to open a screen or data of the other account type → denied.

**Traces:** FR-02 · BR-15

### UC-03 Logout

| | |
|---|---|
| **Actor** | Quran Reader or Teacher |
| **Trigger** | The user chooses Logout, or the inactivity timeout expires. |
| **Preconditions** | The user is logged in. |
| **Outcome** | The login session has ended, and no protected screen or data can be reached until the next login. |

**Main flow**
1. The user chooses Logout.
2. The system ends the login session with the identity provider.
3. The system shows the login screen.

**Alternatives**
- **1a** The inactivity timeout expires → step 2. The timeout never runs during an active recitation session (FR-29).
- **1b** The user logs out during an active recitation session → the session ends as **interrupted** and is scored (UC-10, exception 6c) → step 2.

**Traces:** FR-29, FR-19 · O-6 (timeout length)

### UC-04 Manage Profile

| | |
|---|---|
| **Actor** | Quran Reader or Teacher |
| **Trigger** | The user opens their profile. |
| **Preconditions** | The user is logged in. |
| **Outcome** | The changed values are saved with the account and shown on every device. |

**Main flow**
1. The user opens the profile.
2. The system shows the display name, the email (read-only), the language and, for a Teacher, the school name.
3. The user edits the display name, the language (Arabic or English) or, for a Teacher, the school name.
4. The system validates and saves the changes.
5. The system shows the new values and applies the language immediately.

**Exceptions**
- **3a** The user wants to change the email or password → the system directs them to the identity provider → ends.
- **4a** The display name or school name is empty → refused, nothing saved → step 3.

**Traces:** FR-03 · NFR-11

### UC-05 Manage Consent and Privacy

| | |
|---|---|
| **Actor** | Quran Reader (consents and data) or Teacher (data only) |
| **Trigger** | The user opens Privacy. Readers are also asked for consent inside UC-10 (recitation) and UC-26 (teacher sharing). |
| **Preconditions** | The user is logged in. |
| **Outcome** | The user has seen what is stored and who can see it. Any consent change is recorded with its date, and its effects are applied. |

**Main flow**
1. The user opens Privacy.
2. The system shows the stored-data summary: each data category kept for this user. For a Reader, it also shows the status and dates of the recitation consent and the teacher-sharing consent.
3. The user chooses an action → one of the alternatives below.

**Alternatives**
- **3a Grant a consent** (Reader) → the system creates a new consent record dated today → step 2.
- **3b Withdraw recitation consent** (Reader) → the system records the withdrawal date. New sessions are blocked; stored results remain → step 2.
- **3c Withdraw teacher-sharing consent** (Reader) → the system records the withdrawal date and ends all of the reader's active enrolments with end reason *consent withdrawn*. Teachers lose access → step 2.
- **3d Request correction** → profile data only, through UC-04. Session results and mistakes are system-generated and cannot be edited.
- **3e Request deletion** → UC-06.

**Traces:** FR-27, FR-03, FR-28 · BR-09, BR-16 · state rules §9 (Consent, Enrolment)

### UC-06 Delete Account

| | |
|---|---|
| **Actor** | Quran Reader or Teacher |
| **Trigger** | The user chooses Delete Account, or requests deletion in UC-05. |
| **Preconditions** | The user is logged in. |
| **Outcome (success)** | All of the user's data is permanently erased; only an anonymous deletion log entry (account type and date) remains. The user cannot log in, and no one can see the deleted data. |
| **Outcome (cancelled)** | Nothing changes. |

**Main flow**
1. The user chooses Delete Account.
2. The system explains what will be deleted and asks for confirmation.
3. The user confirms.
4. The system erases the user's data:
   - **Reader:** account, sessions and mistakes, enrolments, consent records and received messages.
   - **Teacher:** account, all their classes with their join codes and every enrolment in them, and their sent messages. Readers' own sessions are not affected.
5. The system writes an anonymous deletion log entry.
6. The system removes the identity-provider account.
7. The system logs the user out.

**Exceptions**
- **3a** The user cancels → ends; nothing changes.

**Traces:** FR-28 · BR-11, BR-17 · state rules §9 (Account)

---

## Quran content and recitation

### UC-07 Browse and Read Surah

| | |
|---|---|
| **Actor** | Quran Reader |
| **Trigger** | The reader opens the surah list. |
| **Preconditions** | The reader is logged in. No network connection is needed. |
| **Outcome** | The reader has read the chosen surah, or has moved on to recite it. |

**Main flow**
1. The reader opens the surah list.
2. The system shows the 37 surahs of Juz Amma in order (An-Naba 78 to An-Nas 114).
3. The reader picks a surah.
4. The system shows its verses in Uthmani script, from bundled data.

**Alternatives**
- **4a** The reader taps Recite → UC-10 starts with this surah already selected (UC-08 is satisfied).

**Traces:** FR-04, FR-06 · §1 (connectivity)

### UC-08 Select Surah

*Included by UC-10.*

| | |
|---|---|
| **Actor** | Quran Reader |
| **Trigger** | UC-10 step 1. |
| **Preconditions** | The reader is logged in. |
| **Outcome** | One surah is selected and stays fixed for the session. |

**Main flow**
1. The system shows the surah list (UC-07, steps 1–2).
2. The reader picks a surah.
3. The system records the selection for the session.

**Alternatives**
- **1a** A surah was already chosen through UC-07, step 4a → step 3.

**Traces:** FR-05 · BR-07

### UC-09 Select AI Mode

*Included by UC-10, after UC-08.*

| | |
|---|---|
| **Actor** | Quran Reader |
| **Trigger** | UC-10 step 2. |
| **Preconditions** | A surah is selected. |
| **Outcome** | One mode is selected and stays fixed for the session. |

**Main flow**
1. The system offers Al-Mujawwid (direct correction) and Al-Mushajji (encouraging wording, same analysis and score).
2. The reader picks one.
3. The system records the mode for the session.

**Notes:** Teachers never select a mode; Al-Mu'allim comes with the Teacher account (FR-10).

**Traces:** FR-07, FR-08, FR-09 · BR-07

### UC-10 Recite Surah

| | |
|---|---|
| **Actor** | Quran Reader |
| **Trigger** | The reader chooses to recite. |
| **Preconditions** | The reader is logged in. |
| **Outcome (success)** | A session is stored with its summary, end reason, Mastery Score (or "no score") and its mistakes. Audio and all other session data are discarded. Progress and streak are recalculated, and the reader has seen the results. |
| **Outcome (not started)** | No session exists (consent declined or microphone denied). |

**Main flow**
1. Include **UC-08 Select Surah**.
2. Include **UC-09 Select AI Mode**.
3. The system checks the recitation consent and the microphone permission, then starts the session (state **Started**).
4. The system shows the verses and starts capture (state **Active**).
5. The reader recites the current verse.
6. The system detects the end of the verse by itself and sends that verse's audio for analysis, while the reader goes on with the next verse.
7. The analysis returns phonemes. The system compares them with the expected verse, detects errors (wrong, skipped or added word, mispronounced letter; Ghunnah, Qalqalah or Madd) and links each error to one word.
8. The system highlights the verse's mistaken words and states each error type, worded for the chosen mode, while the reader continues.
9. Steps 5–8 repeat for each verse. Extension points: *word highlighted* → UC-11; *pause detected* → UC-28.
10. The session ends when the last verse is analysed (end reason **completed**) or the reader ends it (**ended early**) (state **Ended**).
11. The system counts the words reached and analysed, and calculates the Mastery Score (BR-01, BR-02).
12. The system stores the session summary and its mistakes, and discards the audio and all other session data (BR-05).
13. The system recalculates progress and streak (BR-03, BR-04, BR-06).
14. Include **UC-12 View Session Results**.

**Exceptions**
- **3a** No recitation consent → the system asks for it (UC-05, 3a). If the reader grants it → step 3; if the reader declines → ends, not started.
- **3b** Microphone permission denied → the system explains how to grant it → ends, not started.
- **6a** A verse cannot be analysed reliably → the system shows "could not analyse" for that verse and leaves its words out of the score. No mistake is invented → step 9.
- **6b** The connection is lost → the session is interrupted (6c).
- **6c** Interruption at any point after step 4 (app closed or sent to the background, a call, connection lost, logout) → the session ends with end reason **interrupted** → step 11, on the words analysed so far. If needed, this runs when the app is next opened.
- **11a** No words were counted → the session is stored with no score and is excluded from averages and mastery → step 12. Results say "no score".

**Business rules:** BR-01, BR-02, BR-05, BR-07, BR-14, BR-18 · NFR-03 (feedback while reciting)
**Traces:** FR-06, FR-11–FR-16, FR-18, FR-19, FR-27 · state rules §9 (Recitation session)

### UC-11 Receive Audio Assistance

*Extends UC-10 at **word highlighted**.*

| | |
|---|---|
| **Actor** | Quran Reader |
| **Trigger** | The reader taps a highlighted word, or the word shown by a Smart Prompting hint. |
| **Preconditions** | An active session, with the word highlighted (UC-10 step 8) or shown as a hint (UC-28). |
| **Outcome** | The reader has heard the correct recitation of the word. Nothing is stored. |

**Main flow**
1. The reader taps the word.
2. The system plays the word's reference recitation from bundled audio. This works offline.
3. The session continues at UC-10 step 9.

**Notes:** audio plays only on request. Tapping a word that is neither highlighted nor hinted does nothing.

**Traces:** FR-17 · BR-14

### UC-12 View Session Results

*Included by UC-10 (step 14) and UC-13 (step 3).*

| | |
|---|---|
| **Actor** | Quran Reader |
| **Trigger** | A session ends, or the reader opens a past session. |
| **Preconditions** | A stored session of this reader. |
| **Outcome** | The reader has seen the score and the mistakes. |

**Main flow**
1. The system shows the surah, date, mode and end reason.
2. The system shows the Mastery Score.
3. The system lists the mistaken words with their error types and, for Tajweed errors, the rule.

**Alternatives**
- **1a** The session ended early or was interrupted → the screen says that the score covers only the words reached.
- **2a** The session has no score (0 words counted) → "no score" instead of a percentage.
- **3a** No mistakes → the screen shows that none were detected.

**Traces:** FR-20 · BR-01, BR-02, BR-05

### UC-13 View Session History

| | |
|---|---|
| **Actor** | Quran Reader |
| **Trigger** | The reader opens History. |
| **Preconditions** | The reader is logged in. |
| **Outcome** | The reader has seen their past sessions and, optionally, one session's results. |

**Main flow**
1. The reader opens History.
2. The system lists the reader's sessions, newest first, each with surah, date, mode and score.
3. The reader opens a session → include **UC-12**.

**Exceptions**
- **2a** No sessions yet → empty state with a "Start reciting" action (→ UC-10).

**Traces:** FR-20

### UC-14 View User Progress

| | |
|---|---|
| **Actor** | Quran Reader |
| **Trigger** | The reader opens Progress. |
| **Preconditions** | The reader is logged in. |
| **Outcome** | The reader has seen their progress, calculated from stored sessions. |

**Main flow**
1. The reader opens Progress.
2. The system shows:
   - the number of surahs completed with full mastery (a whole-surah session at 90% or more);
   - the average mastery (the average of the best score on each practised surah);
   - the best score for each practised surah.

**Exceptions**
- **2a** No scored sessions → empty state.

**Traces:** FR-21 · BR-03, BR-04

### UC-15 View Practice Streak

| | |
|---|---|
| **Actor** | Quran Reader |
| **Trigger** | The reader opens the streak. |
| **Preconditions** | The reader is logged in. |
| **Outcome** | The reader has seen their current streak. |

**Main flow**
1. The reader opens the streak.
2. The system counts consecutive practice days up to today or yesterday. A practice day is a day, by the device's local calendar, with at least one ended, scored session.
3. The system shows the streak in days.

**Exceptions**
- **2a** No practice days, or a missed day → streak 0.

**Traces:** FR-22 · BR-06

---

## Classes and messages

### UC-16 View Teacher Messages

| | |
|---|---|
| **Actor** | Quran Reader |
| **Trigger** | The reader opens the inbox. The badge shows the unread count. |
| **Preconditions** | The reader is logged in. |
| **Outcome** | The opened message is marked read for both the reader and the teacher. |

**Main flow**
1. The reader opens the inbox.
2. The system lists received messages, newest first, each with teacher display name, class, date and read status.
3. The reader opens a message.
4. The system shows the text and records the read date.

**Exceptions**
- **2a** No messages → empty state.

**Notes:** there is no reply control. Messages stay after the reader leaves the class, but are erased if the teacher deletes their account.

**Traces:** FR-25, FR-03 · BR-12, BR-13 · state rules §9 (Message recipient)

### UC-17 Manage Class

| | |
|---|---|
| **Actor** | Teacher |
| **Trigger** | The teacher chooses to create a class or rename one. |
| **Preconditions** | Logged in as a Teacher. |
| **Outcome** | A new class with a unique, permanent join code exists, or a class has a new name. |

**Main flow (create)**
1. The teacher chooses Create Class and enters a name.
2. The system checks that the name is not empty. Names need not be unique.
3. The system creates the class and generates a unique join code that never changes.
4. The system shows the join code. The teacher shares it outside the app.

**Alternative (rename)**
- **1a** The teacher picks an existing class, enters a new name → step 2 → the system saves the name; the join code is unchanged → ends.

**Exceptions**
- **2a** Empty name → refused → step 1.

**Notes:** teachers cannot delete a single class, or add or remove readers (BR-09, BR-11).

**Traces:** FR-24, FR-10 · BR-09, BR-10, BR-11

### UC-18 View Teacher Dashboard

| | |
|---|---|
| **Actor** | Teacher |
| **Trigger** | The teacher opens the dashboard. |
| **Preconditions** | Logged in as a Teacher. |
| **Outcome** | The teacher has seen permitted results only. No audio is ever shown. |

**Main flow**
1. The teacher opens the dashboard.
2. The system lists the teacher's classes.
3. The teacher picks a class.
4. The system lists the class's actively enrolled readers, each with activity (number of sessions and last practice date), completion (surahs with full mastery) and average mastery. Each summary uses only sessions from the reader's join date.
5. The teacher picks a reader.
6. The system checks that the enrolment is still active and lists that reader's sessions ended on or after the join date, each with surah, date, mode and score.
7. The teacher picks a session.
8. The system shows the session's mistakes (word, error type, Tajweed rule).

**Exceptions**
- **2a** The teacher has no classes → prompt to create one (→ UC-17) → ends.
- **4a** No reader is enrolled → the system shows the class's join code → ends.
- **6a** The reader left or withdrew consent meanwhile → access denied → step 4.
- **6b** No visible sessions yet → empty list.

**Traces:** FR-23, FR-10 · BR-08 · NFR-06

### UC-19 Send Student Messages

| | |
|---|---|
| **Actor** | Teacher |
| **Trigger** | The teacher chooses to send a message. |
| **Preconditions** | Logged in as a Teacher with at least one class. |
| **Outcome** | The message is delivered as unread to each actively enrolled recipient. The teacher's sent list shows its read status per recipient. |

**Main flow**
1. The teacher picks a class, then either the whole class or one enrolled reader.
2. The teacher writes the message.
3. The system checks the active enrolment of each recipient.
4. The system stores the message and one recipient entry per reader, each marked unread.
5. The teacher's sent list shows the message with its read status per recipient.

**Exceptions**
- **2a** Empty message → refused → step 2.
- **3a** The chosen reader is no longer enrolled → refused for that reader.
- **3b** Whole-class message, but the class has no actively enrolled readers → refused: "this class has no readers yet". Nothing is stored → ends.

**Notes:** one-way only; readers cannot reply (BR-12).

**Traces:** FR-25, FR-10 · BR-12, BR-13

### UC-26 Join Class via Code

| | |
|---|---|
| **Actor** | Quran Reader |
| **Trigger** | The reader enters a join code they received from a teacher. |
| **Preconditions** | Logged in as a Quran Reader. |
| **Outcome (success)** | An active enrolment exists with today's join date. The teacher can see the reader's sessions from that date on. |
| **Outcome (failure)** | No enrolment is created. |

**Main flow**
1. The reader enters the join code.
2. The system finds the class and shows its name and the teacher's display name.
3. The system asks for teacher-sharing consent.
4. The reader gives consent.
5. The system records the consent and creates an active enrolment with today's join date.

**Exceptions**
- **2a** The code matches no class (including a class erased with its teacher) → "code not found" → ends.
- **2b** The reader is already actively enrolled in this class → "already in this class" → ends.
- **4a** The reader declines consent → ends; the reader does not join.

**Notes:** a reader who left can rejoin with the same code. That creates a new enrolment and a new join date, and the teacher sees only sessions from the new date (BR-09, BR-08).

**Traces:** FR-24, FR-27 · BR-08, BR-09, BR-16 · state rules §9 (Enrolment)

### UC-27 Leave Class

| | |
|---|---|
| **Actor** | Quran Reader |
| **Trigger** | The reader chooses to leave a class. |
| **Preconditions** | The reader has an active enrolment in the class. |
| **Outcome (success)** | The enrolment has ended with end reason *left* and a leave date. The teacher can no longer see the reader. |
| **Outcome (cancelled)** | Nothing changes. |

**Main flow**
1. The reader opens My Classes.
2. The system lists the reader's active classes.
3. The reader picks a class and chooses Leave.
4. The system asks for confirmation.
5. The reader confirms.
6. The system ends the enrolment and records the leave date.

**Exceptions**
- **2a** No active classes → empty state.
- **5a** The reader cancels → ends.

**Notes:** messages already received are kept (BR-12).

**Traces:** FR-24 · BR-09, BR-12 · state rules §9 (Enrolment)

---

## Recitation extension

### UC-28 Receive Smart Prompting

*Extends UC-10 at **pause detected**.*

| | |
|---|---|
| **Actor** | Quran Reader. The system triggers it; the reader does not request it. |
| **Trigger** | During an active session, the system detects a pause, hesitation or apparent forgetting. |
| **Preconditions** | An active session (UC-10 step 4 onward). |
| **Outcome** | The reader has seen the next expected word. Nothing is stored. |

**Main flow**
1. The system detects a pause, hesitation or forgetting.
2. The system shows the next expected word as a text hint.
3. The reader continues reciting → UC-10 step 9.

**Alternatives**
- **3a** The reader taps the hint → UC-11 plays the word → UC-10 step 9.

**Notes:** the timing thresholds are set in IS499 (O-3). Prompts are not stored (BR-14).

**Traces:** FR-26, FR-17 · BR-14

---

## Review findings

Reviewing every §7.3 flow at this level showed five behaviours the requirements did not decide. Saud decided them on 2026-10-29, and each decision was added to `Itqan_Requirements.md` before these scenarios were written:

| # | Gap | Decision | Updated in the requirements |
|---|---|---|---|
| 1 | Can two classes have the same name? | Yes. The join code identifies the class. | FR-24, §8.1 |
| 2 | A whole-class message to a class with no readers | Refused; nothing is stored. | BR-12, UC-19 flow |
| 3 | What "request correction" covers | Profile data only. Results cannot be edited. | FR-27 |
| 4 | Logout or inactivity timeout during a session | No timeout while reciting. Logging out ends the session as interrupted. | FR-19, FR-29, UC-10 flow, §9 |
| 5 | What happens to a deleted Teacher's classes | They are erased with their enrolments, so the Class has no states. | FR-28, BR-11, §8.1, §9, UC-26 flow |

No conflicts remain. Every scenario can be turned into an activity or sequence diagram without guessing.
