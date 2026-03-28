# 03. Practice: Compare Two Models on a New Dataset

## Setup

1. Create a folder called `week6-model-comparison-practice`.
2. Inside it, create these folders:
   ```text
   data/
   outputs/
   scripts/
   ```
3. Inside `data/`, create a file called `study_progress.csv`.
4. Put this exact content in `data/study_progress.csv`:
   ```text
   study_days,completed_tasks,status
   1,0,follow_up
   1,1,follow_up
   1,2,follow_up
   2,1,follow_up
   2,2,follow_up
   2,3,follow_up
   3,1,follow_up
   3,2,follow_up
   3,3,steady_progress
   4,2,follow_up
   4,3,steady_progress
   4,4,steady_progress
   5,2,steady_progress
   5,3,steady_progress
   6,3,steady_progress
   6,4,steady_progress
   ```
5. Inside `scripts/`, create `compare_study_progress_models.py`.
6. Add this starter code:

```python
from pathlib import Path

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

# Path to the project folder that contains data/, outputs/, and scripts/
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUTS_DIR = BASE_DIR / "outputs"

OUTPUTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_DIR / "study_progress.csv")

feature_columns = ["study_days", "completed_tasks"]
target_column = "status"

X = df[feature_columns]
y = df[target_column]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y,
)
```

This practice is meant to feel familiar but not identical to the worked example. The goal is to compare the same two
model types on a new dataset with different column names and class labels.

## Tasks

1. Create a list called `model_configs` that includes:
    - `KNeighborsClassifier(n_neighbors=3)`
    - `DecisionTreeClassifier(max_depth=3, random_state=42)`
2. Give each model a clear display name.
3. Give each model a clear prediction-column name.
4. Build `predictions_df` from `X_test`.
5. Add `actual_status` to `predictions_df`.
6. Create an empty list called `comparison_rows`.
7. Set `cv_folds = 3`.
8. Loop through both model configs.
9. Inside the loop:
    - fit the model
    - predict the test rows
    - add the prediction column to `predictions_df`
    - run `cross_val_score(...)`
    - append one comparison row with:
        - `model_name`
        - `test_accuracy`
        - `cv_score_1`
        - `cv_score_2`
        - `cv_score_3`
        - `cv_mean_accuracy`
10. Create `comparison_df = pd.DataFrame(comparison_rows)`.
11. Save `predictions_df` to `outputs/study_progress_predictions.csv`.
12. Save `comparison_df` to `outputs/study_progress_model_comparison.csv`.
13. Print both DataFrames.
14. Print the two saved-file messages.
15. Print one short conclusion about which model had the stronger average cross-validation score.

In this practice, `model_configs` is a list of small dictionaries. Each dictionary keeps one model together with its
display name and saved prediction-column name.

## Expected Output Examples

Possible prediction-table output:

```text
 study_days  completed_tasks   actual_status  knn_prediction tree_prediction
          2                1       follow_up       follow_up       follow_up
          6                4 steady_progress steady_progress steady_progress
          3                1       follow_up       follow_up       follow_up
          4                4 steady_progress steady_progress steady_progress
```

Possible comparison-table output:

```text
   model_name  test_accuracy  cv_score_1  cv_score_2  cv_score_3  cv_mean_accuracy
   k-NN (k=3)            1.0        0.67         1.0         0.8              0.82
Decision Tree            1.0        0.50         0.6         0.4              0.50
```

Possible printed conclusion:

```text
k-NN (k=3) had the stronger average cross-validation score in this comparison.
```

Possible saved-file messages:

```text
Saved: outputs/study_progress_predictions.csv
Saved: outputs/study_progress_model_comparison.csv
```

## Debug Task 1

Code:

```python
knn_X = df[["study_days", "completed_tasks"]]
tree_X = df[["study_days"]]
```

Expected behavior:

```text
You wanted to compare two models fairly on the same question.
```

Actual behavior:

```text
The models are using different feature inputs, so the comparison is no longer fair.
```

## Debug Task 2

Code:

```python
comparison_rows.append(
    {
        "model_name": config["display_name"],
        "test_accuracy": round(cv_scores.mean(), 2),
    }
)
```

Expected behavior:

```text
You wanted test_accuracy to show the score from the test split.
```

Actual behavior:

```text
The table mixes up test accuracy and cross-validation average, so the result labels become misleading.
```

## Debug Task 3

Code:

```python
predictions_df["actual_status"] = predictions
predictions_df["knn_prediction"] = y_test.values
```

Expected behavior:

```text
You wanted actual labels in one column and model predictions in another.
```

Actual behavior:

```text
The two columns are swapped, so the saved comparison table becomes misleading.
```

## Debug Task 4

Code:

```python
comparison_df.to_csv(DATA_DIR / "study_progress.csv", index=False)
```

Expected behavior:

```text
You wanted to save the model comparison output.
```

Actual behavior:

```text
This overwrites the raw dataset instead of saving a new file in outputs/.
```

## Self-Review

- I can compare two classification models on the same dataset and split.
- I can keep the comparison fair by using the same features and metrics.
- I can save both row-level predictions and model-level comparison results.
- I can explain why cross-validation helps when two models look similar on one test split.
- I can spot misleading comparison tables before trusting them.

## Navigation

- ⬅️ Previous: [02-worked-examples.md](./02-worked-examples.md).
- 🧭 Week Overview: [week-06-overview.md](../week-06-overview.md).
- ➡️ Next: [04-challenge.md](./04-challenge.md).
