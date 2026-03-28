# 04. Challenge: Check a New Model More Carefully

## Challenge Tasks

1. Create `milestone_progress.csv` with this content:
   ```text
   study_days,completed_milestones,status
   1,0,at_risk
   1,1,at_risk
   2,1,at_risk
   2,2,at_risk
   3,1,at_risk
   3,2,at_risk
   3,3,stable
   4,2,stable
   4,3,stable
   5,2,stable
   5,3,stable
   6,3,stable
   ```
2. Load the file with Pandas.
3. Use `study_days` and `completed_milestones` as features.
4. Use `status` as the target.
5. Split the data into training and test parts.
6. Train a `DecisionTreeClassifier(max_depth=3, random_state=42)`.
7. Predict the test rows and calculate the accuracy.
8. Print a confusion matrix.
9. Print a classification report.
10. Run cross-validation with `cv=3`.
11. Save the result rows to `outputs/milestone_progress_results.csv`.
12. Save the metric summary to `outputs/milestone_progress_metrics.txt`.
13. Write one short conclusion about why cross-validation is still useful even if the test split looks perfect.

This challenge changes both the dataset and the model. The main learning goal stays the same: evaluate carefully instead
of trusting one number too quickly.

## Expected Output Example

Possible result table:

```text
 study_days  completed_milestones actual_status predicted_status
          5                     3        stable           stable
          2                     2       at_risk          at_risk
          3                     1       at_risk          at_risk
```

Possible printed lines:

```text
Accuracy: 1.0
Cross-validation scores: [0.75, 1.0, 0.5]
Average cross-validation accuracy: 0.75
```

Possible confusion matrix:

```text
[[2 0]
 [0 1]]
```

Possible saved-file messages:

```text
Saved: outputs/milestone_progress_results.csv
Saved: outputs/milestone_progress_metrics.txt
```

## Hint

A clear order is:

- Load the CSV and build `X` and `y`.
- Split the data and train the model.
- Print the predictions before you read the metrics.
- Use one fixed `label_order` for the confusion matrix.
- Save the result rows and the metric summary as separate files in `outputs/`.
- Keep your written conclusion honest and short.

## Navigation

- ⬅️ Previous: [03-practice.md](./03-practice.md).
- 🧭 Week Overview: [week-06-overview.md](../week-06-overview.md).
- ➡️ Next: [05-reflection.md](./05-reflection.md).
