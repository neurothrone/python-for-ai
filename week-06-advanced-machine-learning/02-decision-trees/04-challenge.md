# 04. Challenge: Try Decision Trees in a Fresh Scenario

## Challenge Tasks

1. Create `project_checkins.csv` with this content:
   ```text
   study_days,practice_sessions,help_requests,status
   1,1,3,needs_follow_up
   1,2,3,needs_follow_up
   2,1,2,needs_follow_up
   2,2,2,needs_follow_up
   3,2,2,needs_follow_up
   3,3,1,ready
   4,2,2,needs_follow_up
   4,3,1,ready
   4,4,1,ready
   5,3,1,ready
   5,4,0,ready
   6,4,0,ready
   ```
2. Load the file with Pandas.
3. Use all three input columns as features:
    - `study_days`
    - `practice_sessions`
    - `help_requests`
4. Use `status` as the target.
5. Split the data into training and test parts.
6. Train a `DecisionTreeClassifier(max_depth=3, random_state=42)`.
7. Predict the test rows and calculate the accuracy.
8. Export the rules with `export_text(...)`.
9. Save the test result rows to `outputs/project_checkins_tree_results.csv`.
10. Save the exported rules to `outputs/project_checkins_tree_rules.txt`.
11. Create one new row with:
    - `study_days=4`
    - `practice_sessions=3`
    - `help_requests=1`
12. Predict the status for that new row.

This challenge is meant to push you one step beyond the worked example by changing both the scenario and the number of
input columns.

## Expected Output Example

Possible result table:

```text
 study_days  practice_sessions  help_requests   actual_status predicted_status
          5                  4              0           ready            ready
          2                  2              2 needs_follow_up  needs_follow_up
          3                  2              2 needs_follow_up  needs_follow_up
```

Possible accuracy output:

```text
Accuracy: 1.0
```

Possible rules output:

```text
|--- practice_sessions <= 2.50
|   |--- class: needs_follow_up
|--- practice_sessions >  2.50
|   |--- class: ready
```

Possible printed line:

```text
Prediction for the new project check-in row: ready
```

Possible saved-file messages:

```text
Saved: outputs/project_checkins_tree_results.csv
Saved: outputs/project_checkins_tree_rules.txt
```

## Hint

A clear order is:

- Create the folders first.
- Copy and paste the CSV.
- Print `df.columns` before building the model.
- Keep the feature names in one list.
- Use all three feature columns, not only two.
- Fit the model before calling `predict()`.
- Use `results_df.to_string(index=False)` if you want the full table without `...`.
- Save results to `outputs/`, not `data/`.

## Navigation

- ⬅️ Previous: [03-practice.md](./03-practice.md).
- 🧭 Week Overview: [week-06-overview.md](../week-06-overview.md).
- ➡️ Next: [05-reflection.md](./05-reflection.md).
