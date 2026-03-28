# 04. Challenge: Compare Two Models in a Fresh Scenario

## Challenge Tasks

1. Create a small project with folders `data`, `outputs`, and `scripts`.
2. Create `learning_signals.csv` with this content:
   ```text
   study_days,practice_sessions,review_sessions,status
   1,1,0,needs_follow_up
   1,2,1,needs_follow_up
   2,1,1,needs_follow_up
   2,2,1,needs_follow_up
   3,2,1,needs_follow_up
   3,3,2,on_track
   4,2,2,needs_follow_up
   4,3,2,on_track
   4,4,3,on_track
   5,3,2,on_track
   5,4,3,on_track
   6,4,3,on_track
   ```
3. Create one script that:
    - loads and inspects the data
    - trains both a k-NN model and a decision tree
    - compares the two models with test accuracy and cross-validation
    - saves a row-level prediction file
    - saves a model-comparison file
4. Use all three input columns as features.
5. Save the row-level file to `outputs/learning_signals_predictions.csv`.
6. Save the model-comparison file to `outputs/learning_signals_model_comparison.csv`.
7. Create one new row with:
    - `study_days=3`
    - `practice_sessions=3`
    - `review_sessions=2`
8. Predict that new row with both models.
9. Print one short conclusion about which model had the stronger average cross-validation score.

This challenge changes both the scenario and the number of input columns. The main learning goal stays the same:
compare models fairly before you trust a result too much.

## Expected Output Example

Possible prediction-table output:

```text
 study_days  practice_sessions  review_sessions   actual_status  knn_prediction tree_prediction
          5                  4                3        on_track        on_track        on_track
          2                  2                1 needs_follow_up needs_follow_up needs_follow_up
          3                  2                1 needs_follow_up needs_follow_up needs_follow_up
```

Possible comparison-table output:

```text
   model_name  test_accuracy  cv_score_1  cv_score_2  cv_score_3  cv_mean_accuracy
   k-NN (k=3)            1.0        0.75         1.0        0.75              0.83
Decision Tree            1.0        1.00         1.0        1.00              1.00
```

Possible printed lines:

```text
k-NN (k=3) prediction for the new row: on_track
Decision Tree prediction for the new row: on_track
Decision Tree had the stronger average cross-validation score in this comparison.
```

Possible saved-file messages:

```text
Saved: outputs/learning_signals_predictions.csv
Saved: outputs/learning_signals_model_comparison.csv
```

## Hint

A clear order is:

- Load and inspect the CSV.
- Choose one shared feature-target question.
- Build one shared train/test split.
- Train both models on that same split.
- Save the row-level prediction table.
- Save the model-level comparison table.
- Use `to_string(index=False)` if the printed tables feel hard to read.
- Write one careful conclusion from the comparison.

## Navigation

- ⬅️ Previous: [03-practice.md](./03-practice.md).
- 🧭 Week Overview: [week-06-overview.md](../week-06-overview.md).
- ➡️ Next: [05-reflection.md](./05-reflection.md).
