# 03. Practice: Evaluate a New Classification Dataset

## Setup

1. Create a folder called `week6-evaluation-practice`.
2. Inside it, create these folders:
   ```text
   data/
   outputs/
   scripts/
   ```
3. Inside `data/`, create a file called `attendance_status.csv`.
4. Put this exact content in `data/attendance_status.csv`:
   ```text
   attendance_days,submitted_tasks,status
   1,0,at_risk
   1,1,at_risk
   2,1,at_risk
   2,2,at_risk
   3,1,at_risk
   3,2,at_risk
   3,3,stable
   4,2,at_risk
   4,3,stable
   4,4,stable
   5,3,stable
   5,4,stable
   6,3,stable
   6,4,stable
   ```
5. Inside `scripts/`, create `evaluate_knn_attendance_status.py`.
6. Add this starter code:

```python
from pathlib import Path

import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Path to the project folder that contains data/, outputs/, and scripts/
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUTS_DIR = BASE_DIR / "outputs"

OUTPUTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_DIR / "attendance_status.csv")

feature_columns = ["attendance_days", "submitted_tasks"]
target_column = "status"

X = df[feature_columns]
y = df[target_column]
```

This practice is meant to feel familiar but not identical to the worked example. The goal is to reuse the evaluation
workflow on a new dataset with new column names.

## Tasks

1. Split the data with `test_size=0.25`, `random_state=1`, and `stratify=y`.
2. Create `KNeighborsClassifier(n_neighbors=3)`.
3. Fit the model.
4. Predict the outcomes for `X_test`.
5. Build `results_df` with:
    - the test feature values
    - `actual_status`
    - `predicted_status`
6. Save `results_df` to `outputs/attendance_status_knn_results.csv`.
7. Create `label_order = ["at_risk", "stable"]`.
8. Calculate the accuracy.
9. Build the confusion matrix with `confusion_matrix(...)`.
10. Build the classification report with `classification_report(...)`.
11. Run cross-validation with `cv=3` and `scoring="accuracy"`.
12. Round the cross-validation scores so they are easier to read.
13. Calculate the average cross-validation accuracy.
14. Save the metrics to `outputs/attendance_status_metrics.txt`.
15. Print:
    - `results_df`
    - the accuracy
    - the confusion matrix
    - the classification report
    - the rounded cross-validation scores
    - the average cross-validation accuracy
    - the two saved-file messages

`random_state=1` is used on purpose here so you can compare this practice with the worked example pattern.

## Expected Output Examples

Possible label count output:

```text
status
at_risk    7
stable     7
Name: count, dtype: int64
```

Possible result table:

```text
 attendance_days  submitted_tasks actual_status predicted_status
               3                3        stable           stable
               6                3        stable           stable
               3                2       at_risk          at_risk
               2                2       at_risk          at_risk
```

Possible accuracy output:

```text
Accuracy: 1.0
```

Possible confusion matrix output:

```text
[[2 0]
 [0 2]]
```

Possible rounded cross-validation output:

```text
Cross-validation scores: [0.8, 1.0, 0.75]
Average cross-validation accuracy: 0.85
```

Notice the important learning point here:

- One test split gave `1.0`.
- Repeated checks gave an average of `0.85`.

That is a good reminder that one perfect split does not always tell the whole story.

Possible saved-file messages:

```text
Saved: outputs/attendance_status_knn_results.csv
Saved: outputs/attendance_status_metrics.txt
```

## Debug Task 1

Code:

```python
accuracy = accuracy_score(y_test, y_train)
```

Expected behavior:

```text
You wanted to compare the real test labels with the model predictions.
```

Actual behavior:

```text
It raises an error because y_test and y_train are different sets with different lengths.
```

## Debug Task 2

Code:

```python
cv_scores = cross_val_score(model, X, y, cv=20, scoring="accuracy")
```

Expected behavior:

```text
You wanted to repeat the evaluation several times.
```

Actual behavior:

```text
It raises an error because the dataset is too small for 20 folds.
```

## Debug Task 3

Code:

```python
matrix = confusion_matrix(predictions, y_test, labels=["at_risk", "stable"])
```

Expected behavior:

```text
You wanted rows to represent actual labels and columns to represent predicted labels.
```

Actual behavior:

```text
The matrix is built in the opposite direction, so it becomes easy to interpret the rows and columns incorrectly.
```

## Self-Review

- I can explain what accuracy measures.
- I can read a small confusion matrix with a known label order.
- I can use `classification_report(...)` as a summary without memorizing every line.
- I can explain why cross-validation is useful on small datasets.
- I can save both prediction rows and metric summaries in `outputs/`.
- I can reuse the same evaluation workflow on a different dataset.

## Navigation

- ⬅️ Previous: [02-worked-examples.md](./02-worked-examples.md).
- 🧭 Week Overview: [week-06-overview.md](../week-06-overview.md).
- ➡️ Next: [04-challenge.md](./04-challenge.md).
