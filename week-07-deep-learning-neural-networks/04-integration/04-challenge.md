# 04. Challenge: Integration

## Challenge Tasks

1. Create a folder called `week7-keras-integration-challenge`.
2. Inside it, create these folders:
   ```text
   data/
   outputs/
   scripts/
   ```
3. Create `data/engagement_completion.csv` with this content:
   ```text
   study_hours,practice_sessions,review_sessions,completed_course
   1,0,1,0
   2,1,1,0
   2,2,2,0
   3,2,2,0
   3,3,3,1
   4,2,3,0
   4,3,3,1
   5,3,4,1
   5,4,4,1
   6,4,5,1
   ```
4. Inside `scripts/`, create one full Keras classification workflow for the dataset.
5. Save:
    - A training-history file.
    - A training-history plot.
    - A model-summary file.
    - A test-predictions file.
    - A new-case-predictions file.
6. Write three short notes:
    - One note naming one simpler Week 6 baseline you would compare against.
    - One sentence saying what the workflow did successfully.
    - One sentence explaining why the result still needs careful interpretation.

This challenge is meant to be the most independent Week 7 task. You reuse the full workflow idea, but on a different
dataset and with less step-by-step guidance.

## Expected Output Example

Possible saved-file messages:

```text
Saved: outputs/training_history.csv
Saved: outputs/training_history_plot.png
Saved: outputs/model_summary.txt
Saved: outputs/test_predictions.csv
Saved: outputs/new_case_predictions.csv
```

## Hint

If the workflow feels large, split it into four parts:

- Load and split.
- Build and compile.
- Train and evaluate.
- Save outputs and interpret carefully.

Try to keep the model small and the interpretation careful. The point is to complete the workflow clearly, not to make
it complicated.

You can also reuse the same folder and script pattern as the Week 7 integration worked example and practice task.

## Navigation

- ⬅️ Previous: [03-practice.md](./03-practice.md).
- 🧭 Week Overview: [week-07-overview.md](../week-07-overview.md).
- ➡️ Next: [05-reflection.md](./05-reflection.md).
