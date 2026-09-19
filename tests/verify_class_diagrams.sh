#!/bin/sh
set -eu

diagram_dir="docs/diagrams/class"
complete="$diagram_dir/itqan-class-diagram.mmd"

test -f "$complete"

for name in User Role UserRole LearnerProfile TeacherProfile Juz Surah Verse VerseWord TajweedRule AIMode RecitationSession AudioRecording RecitationSegment RecitationAnalysis PauseEvent ErrorType RecitationError ErrorFeedback AudioAssistance LearnerSurahProgress MasteryScoreHistory DailyPractice PracticeStreak LearningClass ClassEnrollment ClassAssignment AssignmentProgress TeacherMessage StudentPerformanceSnapshot Challenge LearnerChallenge Reward LearnerReward; do
  rg -q "class $name([ {]|$)" "$complete" || { echo "Missing class: $name"; exit 1; }
done

for name in AuthenticationService QuranCatalogService RecitationService AnalysisService FeedbackService ProgressService ClassService TeacherMonitoringService MessagingService GamificationService UserRepository QuranRepository RecitationRepository ProgressRepository ClassRepository GamificationRepository AudioCapturePort AudioStoragePort AIAnalysisPort; do
  rg -q "class $name([ {]|$)" "$complete" || { echo "Missing boundary: $name"; exit 1; }
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

for source in "$diagram_dir"/*.mmd; do
  output="/tmp/$(basename "${source%.mmd}").svg"
  npx -y @mermaid-js/mermaid-cli -i "$source" -o "$output" -b white
  test -s "$output"
done
