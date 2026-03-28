# 03. Practice: Apply k-NN to a New Dataset

## Setup

1. Create a folder called `week6-knn-practice`.
2. Inside it, create these folders:
   ```text
   data/
   outputs/
   scripts/
   ```
3. Inside `data/`, create a file called `course_progress.csv`.
4. Put this exact content in `data/course_progress.csv`:
   ```text
   study_days,completed_tasks,status
   1,0,needs_support
   1,1,needs_support
   1,2,needs_support
   2,1,needs_support
   2,2,needs_support
   2,3,needs_support
   3,1,needs_support
   3,2,needs_support
   3,3,on_track
   4,2,needs_support
   4,3,on_track
   4,4,on_track
   5,2,on_track
   5,3,on_track
   6,3,on_track
   6,4,on_track
   ```
5. Inside `scripts/`, create `train_knn_course_progress.py`.
6. Add this starter code:
    ```python
    from pathlib import Path
    
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import accuracy_score
    
    # Path to the project folder that contains data/, outputs/, and scripts/
    BASE_DIR = Path(__file__).resolve().parent.parent
    DATA_DIR = BASE_DIR / "data"
    OUTPUTS_DIR = BASE_DIR / "outputs"
    
    OUTPUTS_DIR.mkdir(exist_ok=True)
    
    df = pd.read_csv(DATA_DIR / "course_progress.csv")
    
    print("--- df.head() ---")
    print(df.head())
    
    print("\n--- df.columns ---")
    print(df.columns)
    
    print("\n--- df.dtypes ---")
    print(df.dtypes)
    
    print("\n--- df['status'].value_counts() ---")
    print(df["status"].value_counts())
    ```

`pathlib` helps the script find `data/` and `outputs/` even though the script is inside `scripts/`.

`BASE_DIR = Path(__file__).resolve().parent.parent` means "start from this script file, then go up to the main project
folder."

This practice is meant to feel familiar but not identical to the worked example. The goal is to reuse the workflow on
new column names and a new situation.

## Tasks

1. Run the starter code and confirm the file loads correctly.
2. Store the feature names in a list called `feature_columns`.
3. Store the target column name in `target_column`.
4. Create `X` from `study_days` and `completed_tasks`.
5. Create `y` from `status`.
6. Split the data with `test_size=0.25`, `random_state=42`, and `stratify=y`.
7. Create `KNeighborsClassifier(n_neighbors=3)`.
8. Fit the model with the training data.
9. Predict the outcomes for `X_test`.
10. Build a `results_df` that includes:
    - `study_days`
    - `completed_tasks`
    - `actual_status`
    - `predicted_status`
11. Calculate the accuracy.
12. Save `results_df` to `outputs/course_progress_knn_results.csv`.
13. Create a new DataFrame for these two new rows:
    - `study_days=2`, `completed_tasks=3`
    - `study_days=5`, `completed_tasks=2`
14. Predict the outcomes for those new rows.
15. Print:
    - `results_df`
    - the accuracy
    - the new predictions
    - `Saved: outputs/course_progress_knn_results.csv`

In these tasks, `X` is the input data and `y` is the label column you want the model to predict.

## Expected Output Examples

Possible label count output:

```text
status
needs_support    9
on_track         7
Name: count, dtype: int64
```

Your exact formatting can vary a little depending on the `pandas` version. That is normal.

Possible `results_df` output:

```text
    study_days  completed_tasks  actual_status predicted_status
3            2                1  needs_support    needs_support
15           6                4       on_track         on_track
6            3                1  needs_support    needs_support
11           4                4       on_track         on_track
```

Possible accuracy output:

```text
Accuracy: 1.0
```

Possible new prediction output:

```text
New predictions: ['needs_support', 'on_track']
```

Possible saved-file message:

```text
Saved: outputs/course_progress_knn_results.csv
```

## Debug Task 1

Code:

```python
X = df["study_days"]
y = df["status"]
```

Expected behavior:

```text
You wanted the model to use both study_days and completed_tasks.
```

Actual behavior:

```text
The model only receives one feature column, so it is answering a simpler question than you planned.
```

## Debug Task 2

Code:

```python
model = KNeighborsClassifier(n_neighbors=3)
predictions = model.predict(X_test)
```

Expected behavior:

```text
You expected the model to predict outcomes for the test rows.
```

Actual behavior:

```text
It raises a NotFittedError because the model was never trained with model.fit(...).
```

## Debug Task 3

Code:

```python
new_students = pd.DataFrame(
    {
        "study_days": [2],
        "tasks_done": [3],
    }
)

print(model.predict(new_students))
```

Expected behavior:

```text
You expected a prediction for one new row.
```

Actual behavior:

```text
The column names do not match the training data, so prediction can fail or behave in a confusing way.
```

## Self-Review

- I can explain what a classification label is.
- I can choose feature columns and a target column clearly.
- I can fit a `KNeighborsClassifier` and make predictions.
- I can save test predictions to `outputs/` instead of touching the raw file.
- I can adapt the same workflow to a new dataset with different column names.
- I can debug missing `fit()` steps and wrong column choices.

## Navigation

- ⬅️ Previous: [02-worked-examples.md](./02-worked-examples.md).
- 🧭 Week Overview: [week-06-overview.md](../week-06-overview.md).
- ➡️ Next: [04-challenge.md](./04-challenge.md).
