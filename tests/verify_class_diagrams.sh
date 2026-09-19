#!/bin/sh
set -eu

diagram_dir="docs/diagrams/class"
complete="$diagram_dir/itqan-class-diagram.mmd"

test -f "$complete"

for name in User Role UserRole LearnerProfile TeacherProfile Juz Surah Verse VerseWord TajweedRule AIMode RecitationSession RecitationSegment RecitationAnalysis PauseEvent ErrorType RecitationError ErrorFeedback AudioAssistance LearnerSurahProgress MasteryScoreHistory DailyPractice PracticeStreak LearningClass ClassEnrollment ClassAssignment AssignmentProgress TeacherMessage StudentPerformanceSnapshot Challenge LearnerChallenge Reward LearnerReward; do
  rg -q "class $name([ {]|$)" "$complete" || { echo "Missing class: $name"; exit 1; }
done

for name in AuthenticationService QuranCatalogService RecitationService AnalysisService FeedbackService ProgressService ClassService TeacherMonitoringService MessagingService GamificationService UserRepository QuranRepository RecitationRepository ProgressRepository ClassRepository GamificationRepository AudioCapturePort AIAnalysisPort; do
  rg -q "class $name([ {]|$)" "$complete" || { echo "Missing boundary: $name"; exit 1; }
done

for name in RecitationSession RecitationSegment RecitationAnalysis RecitationError AudioCapturePort AIAnalysisPort AudioData; do
  rg -q "class $name([ {]|$)" "$complete" || { echo "Missing transient-audio model element: $name"; exit 1; }
done

if rg -ni '\b(Admin|Flutter|FastAPI|SQLAlchemy|ORM|HttpController)\b' "$diagram_dir"/*.mmd; then
  echo "Forbidden implementation or Admin class found"
  exit 1
fi

if rg -n 'User[[:space:]]+<\|--[[:space:]]+(Learner|Teacher)' "$complete"; then
  echo "Learner and Teacher must be profiles, not User subclasses"
  exit 1
fi

for name in ClassAssignment AssignmentProgress StudentPerformanceSnapshot Challenge LearnerChallenge Reward LearnerReward GamificationService GamificationRepository; do
  rg -A4 "class $name" "$complete" | rg -qi 'proposed' || { echo "Missing proposed marker: $name"; exit 1; }
done

for signature in \
  '+UUID? recitationErrorId' \
  '+UUID? pauseEventId' \
  '+findById(UUID) User?' \
  '+findByEmail(String) User?' \
  '+findSession(UUID) RecitationSession?' \
  '+findSurahProgress(UUID, Integer) LearnerSurahProgress?' \
  '+findClass(UUID) LearningClass?' \
  '+findActiveEnrollment(UUID, UUID) ClassEnrollment?'; do
  rg -Fq "$signature" "$complete" || { echo "Missing nullable UML signature: $signature"; exit 1; }
done

for signature in \
  '<<proposed: addAssignment>>' \
  '<<proposed: createAssignment>>' \
  '<<proposed: getLearnerPerformance>>'; do
  rg -Fq "$signature" "$complete" || { echo "Missing proposed operation marker: $signature"; exit 1; }
done

for name in AssignmentStatus AssignmentData; do
  rg -A4 "class $name" "$complete" | rg -qi 'proposed' || { echo "Missing proposed supporting type marker: $name"; exit 1; }
done

check_view() {
  view="$1"
  shift
  test -f "$view" || { echo "Missing view: $view"; exit 1; }
  for name in "$@"; do
    rg -q "class $name([ {]|$)" "$view" || { echo "Missing $name in $view"; exit 1; }
  done
}

check_view "$diagram_dir/identity-quran-classes.mmd" User Role UserRole LearnerProfile TeacherProfile Juz Surah Verse VerseWord TajweedRule AuthenticationService QuranCatalogService
check_view "$diagram_dir/recitation-feedback-classes.mmd" RecitationSession RecitationSegment RecitationAnalysis PauseEvent RecitationError ErrorFeedback AudioAssistance RecitationService AnalysisService FeedbackService
check_view "$diagram_dir/progress-teacher-classes.mmd" LearnerSurahProgress MasteryScoreHistory DailyPractice PracticeStreak LearningClass ClassEnrollment ClassAssignment AssignmentProgress TeacherMessage StudentPerformanceSnapshot ProgressService ClassService TeacherMonitoringService MessagingService
check_view "$diagram_dir/gamification-classes-proposed.mmd" Challenge LearnerChallenge Reward LearnerReward GamificationService GamificationRepository

erd="docs/database/itqan-erd.mmd"
test -f "$erd"

while read -r erd_name uml_name; do
  rg -q "^[[:space:]]+${erd_name}[[:space:]]+\{" "$erd" || { echo "Missing ERD entity: $erd_name"; exit 1; }
  rg -q "class ${uml_name}([ {]|$)" "$complete" || { echo "Missing UML class for ERD entity: $erd_name"; exit 1; }
done <<'ENTITY_MAP'
USER User
ROLE Role
USER_ROLE UserRole
LEARNER_PROFILE LearnerProfile
TEACHER_PROFILE TeacherProfile
JUZ Juz
SURAH Surah
VERSE Verse
VERSE_WORD VerseWord
TAJWEED_RULE TajweedRule
AI_MODE AIMode
RECITATION_SESSION RecitationSession
RECITATION_SEGMENT RecitationSegment
RECITATION_ANALYSIS RecitationAnalysis
PAUSE_EVENT PauseEvent
ERROR_TYPE ErrorType
RECITATION_ERROR RecitationError
ERROR_FEEDBACK ErrorFeedback
AUDIO_ASSISTANCE AudioAssistance
LEARNER_SURAH_PROGRESS LearnerSurahProgress
MASTERY_SCORE_HISTORY MasteryScoreHistory
DAILY_PRACTICE DailyPractice
PRACTICE_STREAK PracticeStreak
LEARNING_CLASS LearningClass
CLASS_ENROLLMENT ClassEnrollment
CLASS_ASSIGNMENT ClassAssignment
ASSIGNMENT_PROGRESS AssignmentProgress
TEACHER_MESSAGE TeacherMessage
STUDENT_PERFORMANCE_SNAPSHOT StudentPerformanceSnapshot
CHALLENGE Challenge
LEARNER_CHALLENGE LearnerChallenge
REWARD Reward
LEARNER_REWARD LearnerReward
ENTITY_MAP

for source in docs/database/itqan-erd.mmd docs/database/RELATIONAL_SCHEMA.md docs/database/ERD_REQUIREMENTS_TRACEABILITY.md "$diagram_dir"/*.mmd "$diagram_dir"/CLASS_DIAGRAM_NOTES.md; do
  if rg -qi 'AUDIO_RECORDING|AudioRecording|AudioStoragePort|storageUri|storage_uri|retentionExpiresAt|retention_expires_at|deletedAt|deleted_at' "$source"; then
    echo "Persisted learner-audio storage is forbidden: $source"
    exit 1
  fi
done

for source in "$diagram_dir"/*.mmd; do
  rg -q '^direction TB$' "$source" || { echo "Diagram is not using the verified landscape-producing direction: $source"; exit 1; }
  output="/tmp/$(basename "${source%.mmd}").svg"
  npx -y @mermaid-js/mermaid-cli -i "$source" -o "$output" -b white
  test -s "$output"
done
