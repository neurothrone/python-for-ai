# 04. Challenge: Try k-NN in a Fresh Scenario

## Challenge Tasks

1. Create `weekly_checkins.csv` with this content:
   ```text
   study_days,practice_sessions,review_sessions,status
   1,1,0,needs_support
   1,2,1,needs_support
   2,1,1,needs_support
   2,2,1,needs_support
   3,2,1,needs_support
   3,3,2,on_track
   4,2,2,needs_support
   4,3,2,on_track
   4,4,3,on_track
   5,3,2,on_track
   5,4,3,on_track
   6,4,3,on_track
   ```
2. Load the file with Pandas.
3. Use all three input columns as features:
    - `study_days`
    - `practice_sessions`
    - `review_sessions`
4. Use `status` as the target.
5. Split the data into training and test parts.
6. Train a `KNeighborsClassifier(n_neighbors=3)`.
7. Print the test predictions and the accuracy.
8. Create one new row with:
    - `study_days=3`
    - `practice_sessions=3`
    - `review_sessions=2`
9. Predict the status for that new row.
10. Save the test result rows to a CSV inside `outputs/`.

This challenge is meant to push you one step beyond the worked example by changing both the scenario and the number of
input columns.

## Expected Output Example

Possible printed line:

```text
Prediction for the new check-in row: on_track
```

Possible saved-file message:

```text
Saved: outputs/weekly_checkins_knn_results.csv
```

## Hint

A clear order is:

- Create the folders first.
- Copy and paste the CSV.
- Print `df.columns` before building the model.
- Keep the feature names in a list.
- Use all three feature columns, not only two.
- Fit the model before calling `predict()`.
- Save results to `outputs/`, not `data/`.

## Navigation

- ⬅️ Previous: [03-practice.md](./03-practice.md).
- 🧭 Week Overview: [week-06-overview.md](../week-06-overview.md).
- ➡️ Next: [05-reflection.md](./05-reflection.md).
