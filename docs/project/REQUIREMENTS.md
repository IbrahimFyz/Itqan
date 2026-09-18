# Itqan — Project Requirements

## 1. Introduction

Itqan (إتقان) is an AI-powered Quran recitation coaching application designed to help Quran readers improve their recitation through intelligent voice-based interaction and personalized feedback. The application focuses initially on Juz Amma, which contains 37 Surahs, and aims to provide users with an accessible and interactive way to practice their Quran recitation.

The system is designed to listen to the user's recitation, analyze it, and identify relevant recitation and Tajweed errors. It then provides appropriate feedback to help the user recognize and correct mistakes during their practice. In addition to recitation correction, Itqan provides motivational and educational interactions through different AI modes designed to support users according to their needs.

The application is intended for anyone who reads the Quran, regardless of gender, and supports different user needs through three main AI modes: Al-Mujawwid, which focuses on recitation and Tajweed correction; Al-Mushajji, which focuses on motivation and encouragement; and Al-Mu'allim, which supports the teacher-oriented aspects of monitoring and following learners' progress.

Itqan is developed as a standalone application. Its current scope is focused on Juz Amma, while its future vision includes the possibility of integrating with other Quran applications and supporting AI-agent capabilities.

---

## 2. Motivation

Quran recitation requires continuous practice and correction to improve accuracy and maintain proper pronunciation and Tajweed. However, not every Quran reader has regular access to a qualified teacher who can listen to their recitation and identify their mistakes. This can make it difficult for users to recognize and correct errors during independent practice.

Itqan is motivated by the need for a more accessible and interactive way to support Quran recitation practice. By using AI-powered voice analysis, the application aims to provide users with immediate feedback while they recite, helping them identify mistakes and improve their recitation through repeated practice.

The project also aims to make the learning experience more engaging by providing different interaction modes. These modes allow the system to focus on correction, encouragement, or teaching according to the user's needs. Through this approach, Itqan seeks to support users in developing their recitation skills and maintaining consistent practice.

---

## 3. Problem Statement

Many Quran readers practice recitation independently without having continuous access to a qualified teacher who can listen to their recitation and identify their mistakes. As a result, pronunciation and Tajweed errors may remain unnoticed or uncorrected during practice. In addition, users may forget previously learned corrections when practicing on their own.

Existing methods of Quran recitation practice may not provide users with immediate, interactive, and personalized feedback while they are reciting. This creates a need for a system that can listen to the user's recitation, analyze it, identify relevant errors, and provide clear feedback to support correction and improvement.

Therefore, the problem addressed by Itqan is the lack of an accessible AI-powered system that can provide interactive recitation guidance and immediate feedback to Quran readers during their practice, particularly within the scope of Juz Amma.

---

## 4. Objectives

The main objective of Itqan is to develop an AI-powered Quran recitation coaching application that supports Quran readers in improving their recitation through intelligent voice-based interaction and feedback.

The project aims to:

1. Provide real-time recitation feedback by listening to the user's Quran recitation and identifying relevant pronunciation and Tajweed errors.
2. Help users recognize and correct their mistakes by providing clear and understandable feedback during recitation practice.
3. Support independent Quran practice by providing guidance without requiring the continuous presence of a qualified teacher.
4. Provide personalized interaction through three AI modes: Al-Mujawwid, Al-Mushajji, and Al-Mu'allim, each supporting a different aspect of the recitation experience.
5. Encourage consistent practice by providing motivational interactions and tracking relevant user progress.
6. Focus the initial system scope on Juz Amma, covering its 37 Surahs.
7. Provide an accessible and interactive recitation-learning experience for anyone who reads the Quran.

---

## 5. Scope and Boundaries

The initial scope of Itqan is focused on Juz Amma, which consists of 37 Surahs and 564 verses. The system is designed to support Quran readers during their recitation practice by providing AI-powered voice interaction, recitation analysis, error identification, and feedback.

### The system scope includes:

- Allowing users to select and recite Surahs from Juz Amma.
- Receiving the user's recitation through the microphone.
- Analyzing the recitation using AI-based voice processing.
- Identifying relevant pronunciation and Tajweed errors.
- Providing feedback to help users recognize and correct their mistakes.
- Providing audio-based assistance when appropriate.
- Supporting the three AI interaction modes: Al-Mujawwid, Al-Mushajji, and Al-Mu'allim.
- Supporting user progress and practice-related information.
- Providing teacher-oriented functionality for monitoring learners' recitation activity and performance.
- Providing a system experience suitable for anyone who reads the Quran.

### Boundaries

- The application will initially cover Juz Amma only.
- The project is a standalone application and is not currently implemented as a feature inside another Quran application.
- The current project focuses on recitation coaching and support, rather than replacing qualified Quran teachers.
- The implementation of the proposed system is planned for IS499; IS498 focuses on the problem definition, requirements, analysis, and system design.
- Integration with other Quran applications and future AI-agent capabilities are considered part of the future vision, not the current project scope.

---

## 6. Stakeholder Analysis

The development and use of Itqan involve several stakeholders who may have different interests and interactions with the system.

| Stakeholder | Role / Interest |
|---|---|
| Quran Readers / Users | The primary users of Itqan. They use the application to practice Quran recitation, receive feedback, and improve their recitation. |
| Teachers | Can use the teacher-oriented capabilities of the system to support monitoring and following learners' recitation practice and progress. |
| Project Team | Responsible for analyzing, designing, and developing the Itqan system and ensuring that its requirements are addressed. |
| University / Academic Supervisors | Evaluate the project according to the requirements and academic standards of the IS498/IS499 graduation project. |

### Stakeholder Interests

- **Quran Readers:** Accurate feedback, ease of use, useful guidance, and an engaging practice experience.
- **Teachers:** Useful information that can support following learners' progress and recitation improvement.
- **Project Team:** Clear requirements, feasible system design, and successful implementation of the proposed solution.
- **University / Supervisors:** A well-defined problem, appropriate analysis and design, proper documentation, and fulfillment of project requirements.

---

## 7. Target Users

The primary target users of Itqan are anyone who reads the Quran and wants to practice and improve their recitation. The application is designed to support users with different levels of Quran recitation experience by providing interactive AI-based guidance and feedback.

The system supports the following main user roles:

### Quran Reader / Learner

Uses the application to select a Surah from Juz Amma, recite through the microphone, receive feedback on pronunciation and Tajweed errors, and practice improving their recitation.

### Teacher

Uses the teacher-oriented capabilities of Itqan to support monitoring and following learners' recitation practice and progress.

Although the system includes these roles, the overall target audience is not limited to students or teachers. Itqan is intended for any Quran reader, whether they practice independently or with the support of a teacher.

---

## 8. User Research

User research for Itqan focuses on understanding the needs and challenges faced by Quran readers during recitation practice. The research considers the difficulties users may encounter when practicing independently, particularly the difficulty of identifying pronunciation and Tajweed mistakes without immediate guidance.

The research focuses on the following areas:

- The need for immediate feedback during Quran recitation.
- The difficulty of continuously accessing a qualified Quran teacher for correction.
- The need to identify and correct pronunciation and Tajweed errors during practice.
- The importance of receiving understandable guidance that helps users improve their recitation.
- The need for motivation and consistent practice.
- The need for an interactive experience that can support users with different learning needs.

These findings help define the requirements of Itqan and guide the design of its AI-powered recitation coaching features.

---

## 9. Gap Analysis

The analysis of existing Quran recitation learning approaches indicates several gaps that can affect users who practice independently. Traditional learning methods can provide valuable guidance through qualified teachers, but continuous access to a teacher may not always be available. On the other hand, digital Quran applications can provide access to Quranic content and support practice, but may not provide the same level of interactive, real-time recitation coaching.

Itqan addresses these gaps by proposing an AI-powered system that can:

- Listen to the user's Quran recitation through the microphone.
- Analyze the user's recitation.
- Identify relevant pronunciation and Tajweed errors.
- Provide immediate feedback during the practice session.
- Provide interactive guidance according to the user's needs.
- Encourage users to maintain consistent practice.
- Support teacher-oriented monitoring through the Al-Mu'allim mode.

Therefore, the main gap addressed by Itqan is the need for an interactive AI-based recitation coaching experience that combines recitation analysis, immediate feedback, motivation, and teacher-oriented support within one standalone application.

---

# 10. Functional Requirements

## A. Account & User Management

### FR-01 — Create Account

**Priority:** Must Have

The system shall allow new users to create an account by providing the required registration information.

### FR-02 — User Login

**Priority:** Must Have

The system shall allow registered users to log in using their account credentials.

### FR-03 — Manage User Profile

**Priority:** Should Have

The system shall allow users to view and manage their profile information.

## B. Quran & Surah Selection

### FR-04 — Browse Juz Amma

**Priority:** Must Have

The system shall allow users to browse the Surahs available within Juz Amma.

### FR-05 — Select Surah

**Priority:** Must Have

The system shall allow users to select a Surah from Juz Amma before selecting an AI interaction mode and starting a recitation session.

### FR-06 — Display Surah Verses

**Priority:** Must Have

The system shall display the verses of the selected Surah to the user during the recitation session.

## C. AI Mode Selection

### FR-07 — Select AI Mode

**Priority:** Must Have

The system shall allow users to select an AI interaction mode after selecting a Surah and before starting a recitation session.

### FR-08 — Al-Mujawwid Mode

**Priority:** Must Have

The system shall provide the Al-Mujawwid mode to analyze the user's Quran recitation and provide feedback on detected pronunciation and Tajweed errors.

### FR-09 — Al-Mushajji Mode

**Priority:** Should Have

The system shall provide the Al-Mushajji mode to support users through motivational and encouraging interactions during their recitation practice.

### FR-10 — Al-Mu'allim Mode

**Priority:** Should Have

The system shall provide the Al-Mu'allim mode to support teacher-oriented functionality for monitoring learners' recitation activity, completion, mastery scores, and overall progress, as well as class management and student communication.

## D. Recitation Session

### FR-11 — Start Recitation Session

**Priority:** Must Have

The system shall allow users to start a recitation session for the selected Surah and AI mode.

### FR-12 — Capture Recitation Audio

**Priority:** Must Have

The system shall capture the user's Quran recitation through the device microphone during an active recitation session.

### FR-13 — Analyze Recitation

**Priority:** Must Have

The system shall analyze the user's recitation during an active recitation session.

### FR-14 — Detect Recitation Errors

**Priority:** Must Have

The system shall identify relevant pronunciation and Tajweed errors detected in the user's recitation.

### FR-15 — Identify Error Location

**Priority:** Must Have

The system shall identify the location of a detected recitation error within the selected Quranic content.

### FR-16 — Provide Recitation Feedback

**Priority:** Must Have

The system shall provide the user with feedback for detected recitation errors to help the user recognize and correct them.

### FR-17 — Provide Audio Assistance

**Priority:** Should Have

The system shall provide audio-based assistance for detected recitation errors when appropriate.

### FR-18 — Continue Recitation

**Priority:** Must Have

The system shall allow users to continue their recitation after receiving feedback during an active session.

### FR-19 — End Recitation Session

**Priority:** Must Have

The system shall allow users to end an active recitation session.

## E. Results & Progress

### FR-20 — Display Session Results

**Priority:** Must Have

The system shall display the user's recitation result as a mastery percentage out of 100% and identify the words in which recitation errors were detected.

### FR-21 — Track User Progress

**Priority:** Should Have

The system shall track the number of Surahs that the user has completed with full mastery and calculate the user's average mastery percentage out of 100%.

### FR-22 — Track Practice Streaks

**Priority:** Could Have

The system shall track the user's consecutive days of practice and display the user's current practice streak.

## F. Teacher Functions

### FR-23 — Teacher Dashboard

**Priority:** Must Have

The system shall provide teachers with a dashboard to view students' recitation activity, completion status, mastery scores, and overall progress.

### FR-24 — Manage Class

**Priority:** Should Have

The system shall allow teachers to create and manage classes and add students to a class.

### FR-25 — Send Student Messages

**Priority:** Could Have

The system shall allow teachers to send messages to students based on their recitation activity and performance.

---

# 11. Non-Functional Requirements

### NFR-01 — Accuracy

The system shall provide a high level of accuracy in analyzing Quran recitation and identifying relevant pronunciation and Tajweed errors. The accuracy of the system shall be evaluated using defined testing criteria during the system evaluation phase.

### NFR-02 — Performance

The system shall provide timely responses to user interactions and recitation analysis without causing delays that significantly affect the user's recitation experience.

### NFR-03 — Real-Time Interaction

The system shall support real-time or near-real-time processing of recitation audio and provide feedback during an active recitation session without requiring the user to pause after every verse or word.

### NFR-04 — Usability

The system shall provide a clear and user-friendly interface that enables users to select a Surah, select an AI mode, start a recitation session, and access session results with minimal complexity.

### NFR-05 — Reliability

The system shall operate reliably during recitation sessions and shall preserve relevant user and session data without unintended loss in the event of an unexpected interruption.

### NFR-06 — Security

The system shall protect user accounts, personal information, and system data from unauthorized access through appropriate security mechanisms.

### NFR-07 — Privacy

The system shall protect users' personal information and recitation-related data and shall handle the collection, storage, and retention of recitation audio in accordance with applicable privacy requirements and user consent where required.

### NFR-08 — Scalability

The system shall be designed to support future expansion, including additional Surahs and system functionalities, without requiring a complete redesign of the system.

### NFR-09 — Maintainability

The system shall be designed in a modular and organized manner that facilitates maintenance, updates, troubleshooting, and future enhancements.

### NFR-10 — Compatibility

The system shall be compatible with the target mobile platform(s) and shall support the device microphone and other essential functionalities required for Quran recitation sessions.

### NFR-11 — Language Support

The system shall support Arabic as the primary language for Quranic content and recitation analysis and shall support both Arabic and English for the user interface.

---

# 12. Requirements Prioritization

| ID | Requirement | Priority |
|---|---|---|
| FR-01 | Create Account | Must Have |
| FR-02 | User Login | Must Have |
| FR-03 | Manage User Profile | Should Have |
| FR-04 | Browse Juz Amma | Must Have |
| FR-05 | Select Surah | Must Have |
| FR-06 | Display Surah Verses | Must Have |
| FR-07 | Select AI Mode | Must Have |
| FR-08 | Al-Mujawwid Mode | Must Have |
| FR-09 | Al-Mushajji Mode | Should Have |
| FR-10 | Al-Mu'allim Mode | Should Have |
| FR-11 | Start Recitation Session | Must Have |
| FR-12 | Capture Recitation Audio | Must Have |
| FR-13 | Analyze Recitation | Must Have |
| FR-14 | Detect Recitation Errors | Must Have |
| FR-15 | Identify Error Location | Must Have |
| FR-16 | Provide Recitation Feedback | Must Have |
| FR-17 | Provide Audio Assistance | Should Have |
| FR-18 | Continue Recitation | Must Have |
| FR-19 | End Recitation Session | Must Have |
| FR-20 | Display Session Results | Must Have |
| FR-21 | Track User Progress | Should Have |
| FR-22 | Track Practice Streaks | Could Have |
| FR-23 | Teacher Dashboard | Must Have |
| FR-24 | Manage Class | Should Have |
| FR-25 | Send Student Messages | Could Have |

**Priority Summary:**

- Must Have: 17 requirements
- Should Have: 6 requirements
- Could Have: 2 requirements
- Won't Have: 0 requirements

---

# 13. Requirements Traceability

| FR | Requirement | Priority | Related System Function / Use Case |
|---|---|---|---|
| FR-01 | Create Account | Must Have | Register |
| FR-02 | User Login | Must Have | Login |
| FR-03 | Manage User Profile | Should Have | Manage Profile |
| FR-04 | Browse Juz Amma | Must Have | Browse Juz Amma |
| FR-05 | Select Surah | Must Have | Select Surah |
| FR-06 | Display Surah Verses | Must Have | View Surah Verses |
| FR-07 | Select AI Mode | Must Have | Select AI Mode |
| FR-08 | Al-Mujawwid Mode | Must Have | Al-Mujawwid |
| FR-09 | Al-Mushajji Mode | Should Have | Al-Mushajji |
| FR-10 | Al-Mu'allim Mode | Should Have | Realized through FR-23, FR-24, and FR-25 (Umbrella Requirement) |
| FR-11 | Start Recitation Session | Must Have | Start Recitation Session |
| FR-12 | Capture Recitation Audio | Must Have | Capture Recitation Audio |
| FR-13 | Analyze Recitation | Must Have | Analyze Recitation |
| FR-14 | Detect Recitation Errors | Must Have | Detect Recitation Errors |
| FR-15 | Identify Error Location | Must Have | Identify Error Location |
| FR-16 | Provide Recitation Feedback | Must Have | Provide Feedback |
| FR-17 | Provide Audio Assistance | Should Have | Receive Audio Assistance |
| FR-18 | Continue Recitation | Must Have | Continue Recitation |
| FR-19 | End Recitation Session | Must Have | End Recitation Session |
| FR-20 | Display Session Results | Must Have | View Session Results |
| FR-21 | Track User Progress | Should Have | View User Progress |
| FR-22 | Track Practice Streaks | Could Have | View Practice Streak |
| FR-23 | Teacher Dashboard | Must Have | View Teacher Dashboard, View Students, View Student Recitation Activity, View Student Completion, View Student Score |
| FR-24 | Manage Class | Should Have | Create Class, Manage Class, Add Students to Class |
| FR-25 | Send Student Messages | Could Have | Send Student Messages |

# 14. Business Model Canvas

| Element | Itqan |
|---|---|
| Customer Segments | Quran Readers / Learners, Teachers |
| Value Propositions | AI-powered Quran recitation coaching, real-time feedback, pronunciation and Tajweed error detection, motivational and teacher-oriented modes |
| Channels | Standalone mobile application |
| Customer Relationships | Personalized AI interaction, progress tracking, motivational support |
| Key Activities | Quran recitation analysis, error detection, feedback generation, progress tracking, teacher-oriented monitoring |
| Key Resources | AI models, Quranic content, recitation analysis components, application infrastructure |
| Key Partners | Potential future integration partners with Quran applications |
| Cost Structure | Application development, AI processing/infrastructure, maintenance, and future improvements |
| Revenue Streams | Not defined yet |
