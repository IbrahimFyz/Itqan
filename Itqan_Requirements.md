# Itqan — Final Requirements Specification

**Baseline:** IS498 report (`Itqan_IS498.docx`) §6 and Appendix E.
**Finalised:** 2026-10-29 by Saud. Every decision the diagrams need is fixed here. The only open items are the IS499 measurements in §11.
**Rule for all diagrams:** use only the names, IDs, flows, data and states in this file. If a diagram needs something that is not here, add it here first.
**Markers:** 🟡 the wording changed from the report · ✚ new requirement · §12 lists every change.

---

## Contents

1. Scope and constraints
2. Actors
3. AI modes
4. Functional requirements (FR-01 to FR-29)
5. Non-functional requirements (NFR-01 to NFR-11)
6. Business rules (BR-01 to BR-18)
7. Use case catalogue (IDs, relationships, flows, exceptions)
8. Data requirements (what is stored and what is never stored)
9. State rules (session, enrolment, class, consent, message, account)
10. System parts (for sequence, architecture and data-flow diagrams)
11. Items left to IS499
12. Changes from the IS498 report
13. Diagram checklist

---

## 1. Scope and constraints

| | |
|---|---|
| Product | Standalone mobile application (Android and iOS) for Quran recitation practice. |
| Content scope | Juz Amma only: 37 surahs (An-Naba 78 to An-Nas 114), 564 verses, 2,308 words. Text bundled from the King Fahd Glorious Quran Printing Complex. |
| Audio | Recitation audio is processed in memory and is never stored, logged, shown to a teacher or used for training. |
| Stored session data | Only the session summary and its Mastery Score, plus the detected mistakes (§8). Everything else from a session is discarded when the session ends. |
| Teacher access | Only to readers with an active enrolment in a class the teacher owns, and only for sessions ended on or after the join date. |
| Connectivity | Recitation analysis needs a network connection. Browsing, reading and audio assistance use bundled data and work offline. |
| Language | Quranic content is in Arabic. The interface supports Arabic (default, right-to-left) and English. |
| Notifications | In-app only: an unread-message badge. No push notifications. |
| Out of scope | Full Quran; integration with other apps or AI agents; Admin role; invitation links; teachers adding or removing learners; deleting classes; two-way chat; push notifications; challenges, rewards and badges; any claim of 100% accuracy. |

## 2. Actors

| Actor | Description |
|---|---|
| **Quran Reader** | Registers as a Reader. Reads surahs, practises recitation in Al-Mujawwid or Al-Mushajji, views results, history, progress and streak, joins and leaves classes by code, and reads teacher messages. |
| **Teacher** | Registers as a Teacher, which gives the Al-Mu'allim mode. Creates and renames classes, views the dashboard for enrolled readers, and sends messages. |

- Each account has exactly one type, Reader or Teacher, and the type never changes. A teacher who wants to practise uses a separate Reader account.
- There is no Admin actor. The identity provider and the analysis service are **system parts** (§10), not actors.
- The label "Quran Reader" is used in every diagram. "Learner" and "student" mean the same actor and are not used as separate names.

## 3. AI modes

| Mode | Who | Behaviour |
|---|---|---|
| Al-Mujawwid | Reader, chosen per session | Full recitation analysis, with direct corrective feedback. |
| Al-Mushajji | Reader, chosen per session | The same analysis, Mastery Score and stored mistakes as Al-Mujawwid. Feedback is worded encouragingly, with praise after each verse and at the end of the session. No challenges, rewards or badges. |
| Al-Mu'allim | Teacher, automatic | Comes with every Teacher account and is never selected. Covers class management, the dashboard and messaging. |

The mode and the surah are fixed for a session. To change either, the reader ends the session and starts a new one.

---

## 4. Functional requirements

29 requirements, prioritised with MoSCoW: **19 Must · 8 Should · 2 Could · 0 Won't**.

### A. Account and user management

**FR-01 — Create Account** · Must 🟡
The system shall allow a new user to create either a Quran Reader account or a Teacher account, and each account shall have exactly one type. Both account types shall provide a display name and an email address. A Teacher account shall also require the school name. Passwords are handled by the managed identity provider. No age, gender, phone number or other personal data shall be collected.
*Acceptance:* a Reader can register with a name and email. A Teacher cannot register without a school name. Itqan stores no password.

**FR-02 — User Login** · Must
The system shall allow registered users to log in through the managed identity provider and shall take each user to the area for their account type.
*Acceptance:* a Reader lands in the Reader area and a Teacher in the Teacher area. Wrong-role screens and data are denied.

**FR-03 — Manage User Profile** · Should 🟡
The system shall allow users to view their profile and edit their display name and interface language (Arabic or English). Teachers may also edit their school name. The language setting is saved with the account. The email address and credentials are managed through the identity provider.
*Acceptance:* an edited name or language appears on the next screen and on another device after login. Readers see the teacher's display name, not the email, on messages.

### B. Quran content

**FR-04 — Browse Juz Amma** · Must
The system shall allow users to browse the 37 surahs of Juz Amma.
*Acceptance:* all 37 surahs are listed in order, and the list works offline.

**FR-05 — Select Surah** · Must
The system shall allow the reader to select a surah from Juz Amma before selecting an AI mode and starting a recitation session.
*Acceptance:* a session cannot start until a surah is selected.

**FR-06 — Display Surah Verses** · Must 🟡
The system shall display the verses of a selected surah in Uthmani script, both for reading without a session and during a recitation session.
*Acceptance:* any surah can be opened and read offline without starting a session. During a session, the verses are on screen.

### C. AI modes

**FR-07 — Select AI Mode** · Must 🟡
The system shall allow a Quran Reader to select Al-Mujawwid or Al-Mushajji after selecting a surah and before starting a session. Teachers do not select a mode (FR-10).
*Acceptance:* a session cannot start until a mode is selected. The Teacher area offers no mode selection.

**FR-08 — Al-Mujawwid Mode** · Must
The system shall provide the Al-Mujawwid mode, which analyses the reader's recitation and gives direct feedback on detected pronunciation and Tajweed errors.

**FR-09 — Al-Mushajji Mode** · Should 🟡
The system shall provide the Al-Mushajji mode, which performs the same analysis and scoring as Al-Mujawwid but words its feedback encouragingly, with praise after each verse and at the end of the session. Challenges, rewards and badges are not included.
*Acceptance:* the same recitation gives the same detected mistakes and Mastery Score in both modes. Only the feedback wording differs.

**FR-10 — Al-Mu'allim Mode** · Should 🟡
The system shall give the Al-Mu'allim mode to every Teacher account automatically on registration. It covers class management (FR-24), the teacher dashboard (FR-23) and messaging (FR-25).
*Acceptance:* a newly registered Teacher reaches these features without selecting a mode.

### D. Recitation session

**FR-11 — Start Recitation Session** · Must
The system shall allow the reader to start a recitation session for the selected surah and mode, provided that the reader has given recitation consent (FR-27) and microphone permission.
*Acceptance:* the session starts with the first verse on screen. Without consent or microphone permission, it does not start and the reader is told why.

**FR-12 — Capture Recitation Audio** · Must
The system shall capture the reader's recitation through the device microphone during an active session. The audio shall be processed in memory only and never stored.
*Acceptance:* no audio file or audio record exists after the session, including after a failure.

**FR-13 — Analyze Recitation** · Must 🟡
The system shall analyse the recitation one verse at a time. It shall detect the end of each verse automatically, without the reader pressing anything. If a verse cannot be analysed reliably, the system shall tell the reader so and shall not invent feedback for it. Words that could not be analysed are left out of the score (BR-02).
*Acceptance:* when analysis fails for a verse, the reader sees a "could not analyse" message for it and can continue. Reading, progress and classes stay available.

**FR-14 — Detect Recitation Errors** · Must 🟡
The system shall detect pronunciation errors at word level (wrong word, skipped word, added word, mispronounced letter) and Tajweed errors for three rules: **Ghunnah, Qalqalah and Madd**. Other Tajweed rules are future work. Accuracy for each rule is measured in IS499.
*Acceptance:* each detected error is recorded with its type and, for Tajweed errors, its rule.

**FR-15 — Identify Error Location** · Must
The system shall link each detected error to one word of the selected surah. An added word is linked to the expected word it was inserted before.
*Acceptance:* every error has exactly one surah, verse and word position.

**FR-16 — Provide Recitation Feedback** · Must 🟡
After each verse is analysed, the system shall highlight that verse's mistaken words and state each error type while the reader continues reciting. The wording depends on the mode (FR-08, FR-09).
*Acceptance:* the mistakes in verse *n* appear while the reader recites verse *n+1*, with no pause needed.

**FR-17 — Provide Audio Assistance** · Should 🟡
When the reader taps a highlighted word, the system shall play the correct recitation of that word from bundled reference audio.
*Acceptance:* audio plays only when the reader requests it, only for a highlighted or prompted word, and works offline.

**FR-18 — Continue Recitation** · Must
The system shall allow the reader to continue reciting after feedback, audio assistance or a prompt, without restarting the session.

**FR-19 — End Recitation Session** · Must 🟡
The system shall end a session when the reader ends it, when the last verse is analysed, or automatically when the session is interrupted (the app is closed or sent to the background, a call arrives, or the connection is lost). In every case, the session is scored on the words analysed so far and nothing already analysed is lost.
*Acceptance:* closing the app mid-session produces a scored session marked "interrupted".

### E. Results and progress

**FR-20 — Display Session Results** · Must 🟡
When a session ends, the system shall show the reader the Mastery Score and the mistaken words with their error types. It shall keep the session summary and its mistakes and discard all other session data (BR-05). The reader shall be able to open a session history and reopen the results of any past session.
*Acceptance:* the results appear at the end of the session. A past session reopens later with the same score and mistakes.

**FR-21 — Track User Progress** · Should 🟡
The system shall show the reader:
- the number of surahs **completed with full mastery** (BR-03);
- the **average mastery**: the average of the reader's best score on each surah practised (BR-04);
- the best score for each surah.

*Acceptance:* two sessions on An-Nas scoring 70% and 95% give An-Nas a best score of 95%, which counts as full mastery if that session covered the whole surah.

**FR-22 — Track Practice Streaks** · Could 🟡
The system shall show the reader's current practice streak: the number of consecutive practice days (BR-06) up to today or yesterday. Missing a day resets the streak to 0.
*Acceptance:* sessions ended on 3 consecutive days give a streak of 3. A day with no ended session resets it to 0.

### F. Teacher functions and classes

**FR-23 — Teacher Dashboard** · Must 🟡
The system shall give each teacher a dashboard that drills down **class → reader → session**:
- **Class view:** the class's actively enrolled readers, each with a summary of activity (number of sessions and last practice date), completion (surahs completed with full mastery) and average mastery.
- **Reader view:** that reader's sessions, each with surah, date, mode and Mastery Score.
- **Session view:** that session's mistakes (word, error type, Tajweed rule).

Only sessions ended on or after the reader's join date are shown (BR-08). Audio is never shown.
*Acceptance:* T1 sees L1's sessions from L1's join date onward but not earlier ones. T1 cannot see a reader who is not enrolled in one of T1's classes.

**FR-24 — Manage Class** · Should 🟡
The system shall allow a teacher to create classes and rename them. The system shall generate a unique join code for each class, and the code never changes. A Quran Reader shall join a class by entering its code and giving teacher-sharing consent (FR-27). A reader may belong to several classes, may leave any class, and may rejoin a class later with the same code (BR-09).
*Acceptance:* a valid code with consent creates an active enrolment, and an invalid code is rejected. After the reader leaves, the teacher can no longer see them. Rejoining shows the teacher only sessions from the new join date.

**FR-25 — Send Student Messages** · Could 🟡
The system shall allow a teacher to send a one-way text message to one actively enrolled reader or to a whole class. A class message goes to the readers enrolled at the moment it is sent. Readers read messages in an in-app inbox with an unread count and cannot reply. The teacher sees their sent messages and whether each recipient has read them.
*Acceptance:* a message appears unread in each recipient's inbox, and opening it marks it read on both sides. Sending to a reader who is not enrolled is refused. The inbox has no reply control.

### G. Recitation assistance

**FR-26 — Receive Smart Prompting** · Should 🟡
When the system detects that the reader has paused, hesitated or appears to have forgotten during a session, it shall automatically show the next expected word as a text hint, without the reader asking. The reader may then tap the hint to hear it (FR-17). Prompts are not stored. The timing thresholds are set in IS499.
*Acceptance:* during a detected pause, the next word appears without any reader action.

### H. Privacy and account control

**FR-27 — Manage Consent and Privacy** · Must ✚
The system shall record two consents per Quran Reader, each with a date:
1. **Recitation consent:** processing recitation and storing results. Asked before the first session and required to start a session.
2. **Teacher-sharing consent:** showing results to the teacher of a joined class. Asked when joining a class and required to join.

A reader can withdraw either consent:
- Withdrawing recitation consent blocks new sessions. Stored results stay until the reader deletes them.
- Withdrawing teacher-sharing consent ends all of the reader's active enrolments.

All users can view a summary of their stored data and request correction of their profile or deletion of their data (FR-28). Granting a consent again creates a new record.
*Acceptance:* without recitation consent, no session starts. After teacher-sharing consent is withdrawn, no teacher sees the reader. The data summary lists every stored item category.

**FR-28 — Delete Account** · Should ✚
The system shall allow users to delete their account permanently and immediately:
- **Reader:** deletes the account, all sessions and mistakes, enrolments, consents and received messages.
- **Teacher:** deletes the account, closes all their classes (ending every enrolment in them) and deletes their sent messages.

Only an anonymous deletion log entry (account type and date) remains. The identity-provider account is also removed.
*Acceptance:* after deletion, the user cannot log in, and no other user can see any of the deleted user's data.

**FR-29 — Logout** · Must ✚
The system shall allow users to log out, and shall log them out automatically after a period of inactivity, which is set in IS499.
*Acceptance:* after logout, no protected screen or data can be reached until the user logs in again.

---

## 5. Non-functional requirements

Numeric targets are set during the IS499 evaluation (§11).

| ID | Name | Requirement |
|---|---|---|
| NFR-01 | Accuracy | The system shall provide a high level of accuracy in detecting pronunciation and Tajweed errors. Accuracy shall be measured per error type and per rule (Ghunnah, Qalqalah, Madd) against an expert-labelled test set, reporting precision, recall and location accuracy. |
| NFR-02 | Performance | The system shall respond without delays that significantly affect the recitation experience. Latency from the end of a verse to its feedback shall be measured (median and 95th percentile). |
| NFR-03 | Real-Time Interaction | Feedback for each verse shall arrive while the reader continues reciting, without the reader having to stop after each verse or word. |
| NFR-04 | Usability | A reader shall be able to select a surah, select a mode, start a session and find results with minimal complexity. |
| NFR-05 | Reliability | No stored data (results, mistakes, progress, enrolments, messages) shall be lost when a session is interrupted. An interrupted session is still scored (FR-19). |
| NFR-06 | Security | Accounts and data shall be protected from unauthorised access. Every teacher read is checked against an active enrolment and its join date in the data layer. Identifiers are non-sequential. |
| NFR-07 | Privacy | Only the data in §8 shall be stored. Audio is never stored, logged or shown. Users are told what is kept and who can see it (FR-27). |
| NFR-08 | Scalability | The design shall allow more surahs, more Tajweed rules and more features without a complete redesign. |
| NFR-09 | Maintainability | The system shall be modular, matching the parts in §10. |
| NFR-10 | Compatibility | The app shall run on the target Android and iOS versions and support the device microphone. |
| NFR-11 | Language Support | Arabic is primary for Quranic content and analysis. The interface supports Arabic (right-to-left, default) and English (FR-03). |

---

## 6. Business rules

| ID | Rule |
|---|---|
| **BR-01 Mastery Score** | `(Total Words − Effective Errors) / Total Words × 100`, rounded to one decimal place, on a 0–100 scale. A whole-word pronunciation error (wrong, skipped, added or mispronounced) counts as 1 effective error, a Tajweed-only error as 0.5, and no word counts for more than 1. Example: 10 words with one wrong word and one Tajweed-only error give (10 − 1.5) / 10 × 100 = 85.0%. |
| **BR-02 Total Words** | The surah's words that the reader reached in the session and that the system analysed. Words never reached (early end or interruption) and words in verses that could not be analysed are excluded. A session with 0 counted words is stored with no score and is excluded from averages and mastery. |
| **BR-03 Full mastery** | A surah is completed with full mastery when one session that analysed every verse of the surah scored at least 90%. |
| **BR-04 Average mastery** | The average, over the surahs the reader has practised, of the reader's best score on each surah. |
| **BR-05 What is kept** | Per session: surah, mode, start and end time, end reason, counted words, effective errors, Mastery Score and whether the whole surah was analysed. Per mistake: word, error type, Tajweed rule and penalty. Nothing else is kept (§8.3). |
| **BR-06 Practice day** | A day, by the device's local calendar, on which the reader ended at least one session, of any end reason, with a score. |
| **BR-07 Session order** | Select Surah, then Select AI Mode, then Start Session. The surah and mode are fixed for the session. |
| **BR-08 Teacher visibility** | A teacher sees a reader's sessions only while the reader has an active enrolment in one of the teacher's classes, and only sessions ended on or after that enrolment's join date. With several classes of the same teacher, the earliest active join date applies. |
| **BR-09 Enrolment** | Joining requires a valid join code and teacher-sharing consent. There is at most one active enrolment per reader per class. Leaving ends the enrolment, and rejoining creates a new one with a new join date. Teachers cannot add or remove readers. |
| **BR-10 Join code** | Generated by the system when a class is created, unique across all classes, never changed. Its format is an IS499 design detail. |
| **BR-11 Class lifecycle** | A class is active from creation and closes only when its teacher deletes their account. A closed class accepts no joins and gives no access. |
| **BR-12 Messages** | One-way, teacher to reader. A class message is delivered to the readers enrolled when it is sent. A reader keeps received messages after leaving the class. Messages can be sent only to actively enrolled readers. |
| **BR-13 Read status** | A message is unread until the recipient opens it. Both the reader and the teacher see the status. |
| **BR-14 Assistance** | Audio Assistance is requested by the reader for a highlighted or prompted word (FR-17). Smart Prompting is triggered by the system on a pause (FR-26). Neither is stored. |
| **BR-15 Account type** | Exactly one type per account, fixed at registration. Al-Mu'allim comes with the Teacher type. |
| **BR-16 Consent** | Two purposes: recitation, and teacher sharing. Each grant and withdrawal is dated. Withdrawal effects are in FR-27. |
| **BR-17 Deletion** | Permanent and immediate (FR-28). Only an anonymous log entry remains. |
| **BR-18 Analysis failure** | Never shown as a mistake. Reported as "could not analyse" and excluded from the score (BR-02). |

---

## 7. Use case catalogue

### 7.1 Use case list

UC-26 and UC-28 keep their official IDs from the report. The other IDs are assigned here, and UC-20 to UC-25 are unused.

| ID | Use case | Actor | FRs |
|---|---|---|---|
| UC-01 | Register | Reader, Teacher | FR-01, FR-10 |
| UC-02 | Login | Reader, Teacher | FR-02 |
| UC-03 | Logout | Reader, Teacher | FR-29 |
| UC-04 | Manage Profile | Reader, Teacher | FR-03 |
| UC-05 | Manage Consent and Privacy | Reader, Teacher | FR-27 |
| UC-06 | Delete Account | Reader, Teacher | FR-28 |
| UC-07 | Browse and Read Surah | Reader | FR-04, FR-06 |
| UC-08 | Select Surah | Reader (included) | FR-05 |
| UC-09 | Select AI Mode | Reader (included) | FR-07, FR-08, FR-09 |
| UC-10 | Recite Surah | Reader | FR-06, FR-11 to FR-16, FR-18, FR-19 |
| UC-11 | Receive Audio Assistance | Reader (extends UC-10) | FR-17 |
| UC-28 | Receive Smart Prompting | Reader (extends UC-10) | FR-26 |
| UC-12 | View Session Results | Reader (included by UC-10 and UC-13) | FR-20 |
| UC-13 | View Session History | Reader | FR-20 |
| UC-14 | View User Progress | Reader | FR-21 |
| UC-15 | View Practice Streak | Reader | FR-22 |
| UC-26 | Join Class via Code | Reader | FR-24, FR-27 |
| UC-27 | Leave Class | Reader | FR-24 |
| UC-16 | View Teacher Messages | Reader | FR-25 |
| UC-17 | Manage Class | Teacher | FR-10, FR-24 |
| UC-18 | View Teacher Dashboard | Teacher | FR-10, FR-23 |
| UC-19 | Send Student Messages | Teacher | FR-10, FR-25 |

### 7.2 Relationships

| From | Relationship | To | Condition |
|---|---|---|---|
| UC-10 Recite Surah | «include» | UC-08 Select Surah | Always, before the session (BR-07). |
| UC-10 Recite Surah | «include» | UC-09 Select AI Mode | Always, after Select Surah (BR-07). |
| UC-10 Recite Surah | «include» | UC-12 View Session Results | Always, when the session ends. |
| UC-13 View Session History | «include» | UC-12 View Session Results | When the reader opens a past session. |
| UC-11 Receive Audio Assistance | «extend» | UC-10 Recite Surah | Extension point *word highlighted*: the reader taps a highlighted or prompted word. |
| UC-28 Receive Smart Prompting | «extend» | UC-10 Recite Surah | Extension point *pause detected*: the system detects a pause, hesitation or forgetting. |

There are no other «include» or «extend» relationships. Internal steps (capture, analyse, detect, locate, score, update progress) are not use cases; they appear inside the UC-10 flow and in the activity and sequence diagrams.

### 7.3 Flows

Each flow lists a precondition (*Pre*), the main steps and the exceptions (*Ex*).

**UC-01 Register**
- *Pre:* none.
- *Main:* (1) the user chooses Reader or Teacher; (2) enters display name and email, plus school name for a Teacher; (3) the identity provider creates the credentials; (4) the system creates the account, with Arabic as the default language. A Teacher gets Al-Mu'allim.
- *Ex:* the email is already registered → refused. School name missing for a Teacher → refused. Identity provider unavailable → "try again later".

**UC-02 Login**
- *Pre:* a registered account.
- *Main:* (1) the user signs in through the identity provider; (2) the system opens the Reader or Teacher area.
- *Ex:* wrong credentials → the identity provider rejects them. Provider unavailable → "try again later".

**UC-03 Logout**
- *Main:* (1) the user logs out, or the inactivity timeout expires; (2) the system ends the login session and shows the login screen.

**UC-04 Manage Profile**
- *Main:* (1) the user opens the profile; (2) edits display name and language, plus school name for a Teacher; (3) the system validates and saves the changes.
- *Ex:* empty name or school name → refused.

**UC-05 Manage Consent and Privacy**
- *Main:* (1) the user opens Privacy; (2) the system shows the stored-data summary and, for a Reader, the status of both consents; (3) the user may grant or withdraw a consent, or request correction or deletion.
- *Withdraw recitation consent:* new sessions are blocked. *Withdraw teacher-sharing consent:* all active enrolments end. *Request deletion:* goes to UC-06.

**UC-06 Delete Account**
- *Main:* (1) the user asks to delete; (2) the system asks for confirmation; (3) the user confirms; (4) the system deletes the data per FR-28, writes an anonymous log entry, removes the identity-provider account and logs the user out.
- *Ex:* the user cancels at step 2 → nothing changes.

**UC-07 Browse and Read Surah**
- *Main:* (1) the reader opens the surah list (37 surahs); (2) picks a surah; (3) the system shows its verses. This works offline.
- *Alternative:* the reader taps "Recite" → UC-10 with this surah pre-selected.

**UC-10 Recite Surah**
- *Pre:* logged in as a Reader, with recitation consent.
- *Main:*
  1. Include UC-08: select the surah.
  2. Include UC-09: select the mode.
  3. The system checks microphone permission and starts the session.
  4. The verses are shown, and the reader recites.
  5. The system detects the end of each verse and sends that verse's audio for analysis.
  6. Analysis returns the phonemes. The system compares them with the expected verse, detects the errors and links each error to a word.
  7. The system highlights the mistaken words with their error types, worded for the mode, while the reader continues.
  8. Steps 5–7 repeat for each verse, with extension points *word highlighted* (UC-11) and *pause detected* (UC-28).
  9. The session ends when the last verse is analysed or the reader ends it.
  10. The system calculates the Mastery Score (BR-01, BR-02), stores the session summary and its mistakes (BR-05) and discards everything else.
  11. Include UC-12: show the results.
- *Ex:*
  - No recitation consent → go to UC-05 to grant it.
  - Microphone permission denied → explain how to grant it; the session does not start.
  - Analysis fails for a verse → "could not analyse"; the verse is excluded from the score and the session continues.
  - Interrupted (app closed, call, connection lost) → the session ends automatically, with end reason "interrupted", and steps 10–11 run on the words analysed so far (on the next app open if needed).
  - 0 words counted → stored with no score; the results screen says so.

**UC-11 Receive Audio Assistance**
- *Main:* (1) the reader taps a highlighted or prompted word; (2) the system plays the word's bundled reference audio; (3) the session continues.

**UC-28 Receive Smart Prompting**
- *Main:* (1) the system detects a pause, hesitation or forgetting; (2) it shows the next expected word as a text hint; (3) the reader continues or taps the hint (UC-11).

**UC-12 View Session Results**
- *Main:* the system shows the Mastery Score (or "no score") and the mistaken words with their error types and Tajweed rules. For a session that ended early or was interrupted, the screen says the score covers only the words reached.

**UC-13 View Session History**
- *Main:* (1) the reader opens the history; (2) the system lists past sessions, newest first, with surah, date, mode and score; (3) the reader opens one → UC-12.
- *Ex:* no sessions yet → empty state with a "Start reciting" action.

**UC-14 View User Progress**
- *Main:* the system shows the surahs completed with full mastery, the average mastery and the best score per surah.
- *Ex:* no scored sessions → empty state.

**UC-15 View Practice Streak**
- *Main:* the system shows the current streak in days (BR-06).
- *Ex:* no practice days → streak 0.

**UC-26 Join Class via Code**
- *Pre:* logged in as a Reader.
- *Main:* (1) the reader enters a join code; (2) the system finds the active class and shows its name and teacher; (3) the system asks for teacher-sharing consent; (4) the reader consents; (5) the system creates an active enrolment with today's join date.
- *Ex:* invalid code or closed class → "code not found". Already actively enrolled → "already in this class". Consent declined → the reader does not join.

**UC-27 Leave Class**
- *Main:* (1) the reader opens My Classes and picks a class; (2) chooses Leave and confirms; (3) the system ends the enrolment and records the leave date; the teacher's access ends.

**UC-16 View Teacher Messages**
- *Main:* (1) the reader opens the inbox, whose badge shows the unread count; (2) the system lists messages, newest first, with teacher name, class and date; (3) the reader opens a message, and the system marks it read.
- *Ex:* no messages → empty state.

**UC-17 Manage Class**
- *Pre:* logged in as a Teacher.
- *Main:* (1) the teacher creates a class with a name; the system generates the join code, which the teacher shares outside the app; or (2) the teacher renames an existing class.
- *Ex:* empty name → refused.

**UC-18 View Teacher Dashboard**
- *Main:* (1) the teacher opens the dashboard and the system lists their classes; (2) the teacher picks a class, and the system lists its actively enrolled readers with summaries; (3) the teacher picks a reader, and the system lists that reader's visible sessions (BR-08); (4) the teacher picks a session, and the system shows its mistakes. Every step checks the enrolment and join date.
- *Ex:* no classes → prompt to create one. A class with no readers → show the join code. A reader leaves meanwhile → access is denied.

**UC-19 Send Student Messages**
- *Main:* (1) the teacher chooses a class, then either the whole class or one enrolled reader; (2) writes the message; (3) the system checks each recipient's active enrolment and delivers it; (4) the teacher's sent list shows the read status per recipient.
- *Ex:* empty message → refused. Recipient no longer enrolled → refused for that recipient.

---

## 8. Data requirements

This section says **what must be stored**. Table design is left to the ERD and schema, which must contain these items.

### 8.1 Stored data

| Data group | Items stored | Notes |
|---|---|---|
| **Account** | account ID (non-sequential), identity-provider subject, account type (Reader or Teacher), display name, email, language (ar or en), created date | One type per account. No password. |
| **Teacher detail** | school name | Teacher accounts only; required. |
| **Consent record** | consent ID, reader, purpose (recitation or teacher sharing), granted date, withdrawn date (empty while active) | A new grant creates a new record. |
| **Surah** (bundled, read-only) | surah number (78–114), Arabic name, English name, verse count | 37 rows. |
| **Verse** (bundled) | surah, verse number, Uthmani text, plain (imlaei) text | 564 rows. |
| **Word** (bundled) | verse, word position, word text, reference-audio start and end times | 2,308 rows. Every mistake links here. |
| **Tajweed rule** (reference) | rule ID, name (Ghunnah, Qalqalah, Madd) | 3 rows in phase one. |
| **Recitation session** | session ID, reader, surah, mode (Mujawwid or Mushajji), start time, end time, end reason (completed, ended early or interrupted), counted words, effective errors, Mastery Score (empty if 0 words), whole surah analysed (yes or no) | One row per session. |
| **Mistake** | mistake ID, session, word, error type (wrong word, skipped word, added word, mispronounced letter or Tajweed), Tajweed rule (only for Tajweed errors), penalty (1 or 0.5) | 0 or more per session. |
| **Class** | class ID, teacher, name, join code (unique), status (active or closed), created date | |
| **Enrolment** | enrolment ID, class, reader, join date, leave date (empty while active), status (active or ended), end reason (left, consent withdrawn, account deleted or class closed) | At most one active per reader per class. |
| **Message** | message ID, teacher, class, audience (one reader or whole class), text, sent date | |
| **Message recipient** | message, reader, read date (empty while unread) | One row per recipient, which gives read status on both sides. |
| **Deletion log** | log ID, account type, deleted date | Anonymous: no name, email or ID. |

**Derived, not entered by users** (may be stored as a cache): best score per surah, surahs with full mastery, average mastery, streak, and the teacher's summaries. All are calculated from sessions using BR-03, BR-04, BR-06 and BR-08.

### 8.2 Relationships and cardinality

| Relationship | Cardinality |
|---|---|
| Teacher account – teacher detail | 1 – 1 |
| Reader – consent record | 1 – 0..* |
| Reader – recitation session | 1 – 0..* |
| Surah – verse – word | 1 – 1..* – 1..* |
| Surah – recitation session | 1 – 0..* |
| Recitation session – mistake | 1 – 0..* |
| Word – mistake | 1 – 0..* |
| Tajweed rule – mistake | 0..1 – 0..* (Tajweed mistakes only) |
| Teacher – class | 1 – 0..* |
| Class – enrolment – reader | class 1 – 0..* enrolment; reader 1 – 0..* enrolment |
| Teacher – message | 1 – 0..* |
| Class – message | 1 – 0..* |
| Message – message recipient – reader | message 1 – 1..* recipient; reader 1 – 0..* recipient |

### 8.3 Never stored

Recitation audio; audio segments; raw analysis output (phonemes); feedback and praise text; audio-assistance requests; Smart Prompting events; voiceprints or speaker data; location; device identifiers beyond what the identity provider needs; age, gender or phone number.

**Effect on the report's ERD:** these entities are not stored any more, so they must be dropped or made transient:
- because of the "nothing else kept" rule: RECITATION_SEGMENT, RECITATION_ANALYSIS, ERROR_FEEDBACK, AUDIO_ASSISTANCE, PAUSE_EVENT;
- because nothing requires them: the proposed CLASS_ASSIGNMENT, ASSIGNMENT_PROGRESS and LEARNER_PERFORMANCE_SNAPSHOT;
- because of the Al-Mushajji decision: CHALLENGE, LEARNER_CHALLENGE, REWARD and LEARNER_REWARD.

The **Message recipient** and **Deletion log** entities are new.

---

## 9. State rules

Each state machine diagram uses exactly these states and transitions.

**Recitation session**
`Started → Active → Ended`
- Started → Active: the first verse is shown and capture begins.
- Active → Ended, with end reason **completed** (last verse analysed), **ended early** (the reader ends it) or **interrupted** (app closed, call, connection lost).
- On Ended: the score is calculated, the summary and mistakes are stored, and everything else is discarded. Ended is final.

**Enrolment**
`Active → Ended`
- Created Active by UC-26, after a valid code and consent.
- Active → Ended, with end reason **left** (UC-27), **consent withdrawn** (FR-27), **account deleted** (FR-28, reader) or **class closed** (FR-28, teacher).
- Ended is final. Rejoining creates a new Active enrolment.

**Class**
`Active → Closed`
- Active on creation. Closed only when the teacher deletes their account. Closed is final.

**Consent record**
`Granted → Withdrawn`
- Withdrawn is final. A new grant creates a new record.

**Message recipient**
`Unread → Read`
- Read is set when the reader opens the message.

**Account**
`Active → Deleted`
- Deleted is final. All of the account's data is erased and an anonymous log entry is written.

---

## 10. System parts

These are the parts of the system that appear in sequence, architecture and data-flow diagrams. They are not actors.

| Part | Where | Responsibility | FRs |
|---|---|---|---|
| **Itqan App** | Phone (Flutter) | Screens; microphone capture (16 kHz mono, segmented by verse); bundled Quran content and reference audio; offline reading and audio assistance; detecting pauses for Smart Prompting. | FR-01–FR-29 (user interface) |
| **Identity Provider** | External, managed | Credentials, login, logout, account removal. Returns the identity subject. | FR-01, FR-02, FR-28, FR-29 |
| **Account Service** | Backend (FastAPI) | Accounts, profiles, language, consent records, data summary, account deletion and the deletion log. | FR-01–FR-03, FR-10, FR-27, FR-28 |
| **Recitation Service** | Backend | Orchestrates each session: start, send each verse to the Analysis Service, call the Comparison Engine, return feedback, end the session, calculate the score, store the results. **All session traffic goes through it.** | FR-11–FR-20 |
| **Comparison Engine** | Backend (inside the Recitation Service) | Aligns the returned phonemes with the expected verse, classifies errors, links each error to a word. | FR-14, FR-15 |
| **Analysis Service** | Separate stateless Python/GPU service (`obadx/muaalem-model-v3_2`) | Receives a verse's audio and returns phonemes with articulation attributes. Keeps nothing. | FR-13 |
| **Progress Service** | Backend | Best score per surah, full mastery, average mastery, streak, session history. | FR-20–FR-22 |
| **Class Service** | Backend | Classes, join codes, enrolments, the teacher dashboard with enrolment and join-date checks, messages and read status. | FR-23–FR-25 |
| **Database** | PostgreSQL | Stores only §8.1. | All stored data |

**Main recitation path (for the sequence diagram):**
`Itqan App → Recitation Service → Analysis Service → Recitation Service (Comparison Engine) → Itqan App`. At the end of the session: `Recitation Service → Database` (summary and mistakes), then `Progress Service` recalculates.

---

## 11. Items left to IS499

These are measurements and vendor choices. None of them changes a diagram.

| ID | Item |
|---|---|
| O-1 | Production hosting. |
| O-2 | Numeric targets for accuracy, latency and usability, and the device and OS list. |
| O-3 | Time thresholds for pause, hesitation and forgetting (Smart Prompting). |
| O-4 | Reference audio source (reciter) and word-timing data. |
| O-5 | Identity provider vendor. |
| O-6 | Inactivity timeout length (FR-29). |
| O-7 | Join code format (BR-10). |
| O-8 | Guardian-consent process for minors: the responsibility of the deploying organisation. |

---

## 12. Changes from the IS498 report

| Item | Change |
|---|---|
| FR-01 | One type per account; name and email, plus school name for teachers; no other personal data. |
| FR-03 | Editable: display name and language, plus school name for teachers. |
| FR-06 | Surahs can be read outside a session. |
| FR-07, FR-10 | Mode selection is for Readers only; Teachers get Al-Mu'allim on registration. |
| FR-09 | Same analysis as Al-Mujawwid with encouraging wording; no challenges or rewards. |
| FR-11 | Requires recitation consent and microphone permission. |
| FR-13, FR-16 | Analysis and feedback per verse, with automatic end-of-verse detection; failures are reported, never invented. |
| FR-14 | Tajweed scope: Ghunnah, Qalqalah, Madd. |
| FR-15 | Added words are linked to the following expected word. |
| FR-17 | The reader taps a word to hear its bundled reference audio. |
| FR-19 | Interrupted sessions end automatically and are scored. |
| FR-20 | Score and mistakes kept, all else discarded; session history added. |
| FR-21 | Full mastery = whole surah at 90% or more; average = best score per surah. |
| FR-22 | Practice day = at least one ended, scored session, by local calendar. |
| FR-23 | Dashboard drills down class → reader → session; shows mistakes; only from the join date. |
| FR-24 | Create and rename only; join needs consent; readers can join several classes, leave and rejoin. |
| FR-25 | One-way, to one reader or a class; inbox with unread badge; read status on both sides. |
| FR-26 | Next-word text hint; not stored (PAUSE_EVENT is no longer persisted). |
| FR-27 ✚ | Two consents, with withdrawal effects; data summary; correction and deletion requests. |
| FR-28 ✚ | Permanent deletion with an anonymous log. |
| FR-29 ✚ | Logout and inactivity timeout. |
| Priorities | 19 Must, 8 Should, 2 Could (29 FRs). The report's §6.3 needs updating. |
| Use cases | IDs UC-01 to UC-19, UC-26 to UC-28 (§7). |
| Data | 9 report entities dropped or made transient; Message recipient and Deletion log added (§8.3). |

---

## 13. Diagram checklist

Before finalising any diagram, check:

- [ ] Only the actors **Quran Reader** and **Teacher** (§2). Identity Provider and Analysis Service appear only as system parts.
- [ ] Use case names and IDs exactly as in §7.1; «include» and «extend» exactly as in §7.2.
- [ ] Activity and sequence flows follow §7.3, including the exceptions.
- [ ] Sequence and architecture diagrams use only the parts in §10, and recitation traffic goes through the Recitation Service.
- [ ] ERD, schema and class diagram contain every item in §8.1 and nothing in §8.3.
- [ ] State machines use exactly the states in §9.
- [ ] Data-flow diagrams show audio going **into** the Analysis Service and **never** into the Database.
- [ ] Every element traces to an FR, BR or UC ID in this file.
