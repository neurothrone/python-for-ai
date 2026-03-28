# 02. Worked Examples: Metrics and Cross-Validation

## Example A: Create the Project Structure

Create this structure:

```text
week6-evaluation-demo/
  data/
    student_support.csv
  outputs/
  scripts/
    evaluate_knn_student_support.py
```

This keeps the workflow easy to follow:

- `data/` stores the raw CSV.
- `scripts/` stores the Python code.
- `outputs/` stores result files made by the script.

## Example B: Create the Dataset

Create `data/student_support.csv` with this content:

```text
study_hours,practice_sessions,outcome
1,0,needs_support
1,1,needs_support
1,2,needs_support
2,1,needs_support
2,2,needs_support
2,3,needs_support
3,1,needs_support
3,2,needs_support
3,3,pass
4,2,needs_support
4,3,pass
4,4,pass
5,1,needs_support
5,2,pass
5,3,pass
6,1,pass
6,2,pass
6,3,pass
```

## Example C: Load and Inspect the Data

Create `scripts/evaluate_knn_student_support.py` with this starter code:

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

df = pd.read_csv(DATA_DIR / "student_support.csv")

print("--- df.head() ---")
print(df.head())

print("\n--- df.columns ---")
print(df.columns)

print("\n--- df.dtypes ---")
print(df.dtypes)

print("\n--- df['outcome'].value_counts() ---")
print(df["outcome"].value_counts())
```

Why this setup helps:

- `pathlib` lets the script find `data/` and `outputs/` even though the script is inside `scripts/`.
- `BASE_DIR = Path(__file__).resolve().parent.parent` means "start from this script file, then go up to the project
  folder".
- `OUTPUTS_DIR.mkdir(exist_ok=True)` makes sure the output folder exists before you save files there.
- `value_counts()` is useful in classification because it shows how many rows belong to each label.

Possible label count output:

```text
outcome
needs_support    10
pass              8
Name: count, dtype: int64
```

Your exact formatting can vary a little depending on the `pandas` version. That is normal.

## Example D: Choose Features, Split the Data, and Train the Model

Add this code below the inspection step:

```python
feature_columns = ["study_hours", "practice_sessions"]
target_column = "outcome"

X = df[feature_columns]
y = df[target_column]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=1,
    stratify=y,
)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
```

Important details:

- `X` is the input data and `y` is the label column you want the model to predict.
- `random_state=1` is used on purpose here so this split includes one mistake.
- That makes the evaluation output more interesting to read than a perfect result.

## Example E: Predict and Build a Result Table

Add this code next:

```python
predictions = model.predict(X_test)

results_df = X_test.copy()
results_df["actual_outcome"] = y_test.values
results_df["predicted_outcome"] = predictions

results_df.to_csv(OUTPUTS_DIR / "knn_evaluation_results.csv", index=False)

print("\n--- Results ---")
print(results_df.to_string(index=False))
print("Saved: outputs/knn_evaluation_results.csv")
```

`X_test.copy()` creates a separate table for the saved results, so you can add new columns without changing the
original test data.

Possible output:

```text
 study_hours  practice_sessions actual_outcome predicted_outcome
           2                  3  needs_support     needs_support
           3                  2  needs_support     needs_support
           6                  3           pass              pass
           6                  1           pass              pass
           4                  2  needs_support              pass
Saved: outputs/knn_evaluation_results.csv
```

## Example F: Check Accuracy and the Confusion Matrix

Add this code below the result table:

```python
label_order = ["needs_support", "pass"]

accuracy = accuracy_score(y_test, predictions)
matrix = confusion_matrix(y_test, predictions, labels=label_order)

print("\n--- Accuracy and confusion matrix ---")
print("Accuracy:", accuracy)
print("Confusion Matrix:")
print(matrix)
```

Possible output:

```text
Accuracy: 0.8
Confusion Matrix:
[[2 1]
 [0 2]]
```

How to read it:

- `2` real `needs_support` rows were predicted correctly.
- `1` real `needs_support` row was predicted as `pass`.
- `2` real `pass` rows were predicted correctly.

## Example G: Print a Classification Report

Now add a fuller summary:

```python
report = classification_report(y_test, predictions, labels=label_order)

print("\n--- Classification report ---")
print(report)
```

Possible output:

```text
               precision    recall  f1-score   support

needs_support       1.00      0.67      0.80         3
         pass       0.67      1.00      0.80         2

     accuracy                           0.80         5
    macro avg       0.83      0.83      0.80         5
 weighted avg       0.87      0.80      0.80         5
```

You do not need to memorize every number. The main goal is to notice:

- The model made one mistake.
- The report explains that mistake more clearly than accuracy alone.

## Example H: Run Cross-Validation

Now check the same model in repeated rounds:

```python
cv_folds = 3
cv_scores = cross_val_score(model, X, y, cv=cv_folds, scoring="accuracy")
rounded_cv_scores = [float(round(score, 2)) for score in cv_scores]
average_cv_score = float(round(cv_scores.mean(), 2))

print("\n--- Cross-validation ---")
print("Cross-validation scores:", rounded_cv_scores)
print("Average cross-validation accuracy:", average_cv_score)
```

Here:

- `cv_folds = 3` means the model is checked in 3 rounds.
- `rounded_cv_scores` makes the printed scores easier to read.
- `float(...)` keeps the output cleaner than raw NumPy values.

Possible output:

```text
Cross-validation scores: [0.83, 0.83, 0.67]
Average cross-validation accuracy: 0.78
```

This is the important learning point:

- One test split gave `0.8`.
- Repeated checks gave an average of `0.78`.

Those results are close, but cross-validation gives a steadier picture than one split alone.

## Example I: Save the Metrics to a Text File

Add this final step:

```python
metrics_lines = [
    f"Accuracy: {accuracy}",
    "",
    "Confusion Matrix:",
    str(matrix),
    "",
    "Classification Report:",
    report,
    f"Cross-validation scores: {rounded_cv_scores}",
    f"Average cross-validation accuracy: {average_cv_score}",
]

with open(OUTPUTS_DIR / "knn_metrics.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(metrics_lines))

print("Saved: outputs/knn_metrics.txt")
```

Saving the metrics is useful because you can read them again without having to remember every printed step from the run.

## Full Script

If you want to see the whole file in one place, here is one clear version with comment headers:

```python
from pathlib import Path

import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Step 1: Define project paths.
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUTS_DIR = BASE_DIR / "outputs"

OUTPUTS_DIR.mkdir(exist_ok=True)

# Step 2: Load and inspect the data.
df = pd.read_csv(DATA_DIR / "student_support.csv")

print("--- df.head() ---")
print(df.head())

print("\n--- df.columns ---")
print(df.columns)

print("\n--- df.dtypes ---")
print(df.dtypes)

print("\n--- df['outcome'].value_counts() ---")
print(df["outcome"].value_counts())

# Step 3: Choose features, split the data, and train the model.
feature_columns = ["study_hours", "practice_sessions"]
target_column = "outcome"

X = df[feature_columns]
y = df[target_column]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=1,
    stratify=y,
)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Step 4: Predict and save the result rows.
predictions = model.predict(X_test)

results_df = X_test.copy()
results_df["actual_outcome"] = y_test.values
results_df["predicted_outcome"] = predictions

results_df.to_csv(OUTPUTS_DIR / "knn_evaluation_results.csv", index=False)

print("\n--- Results ---")
print(results_df.to_string(index=False))
print("Saved: outputs/knn_evaluation_results.csv")

# Step 5: Check accuracy and the confusion matrix.
label_order = ["needs_support", "pass"]

accuracy = accuracy_score(y_test, predictions)
matrix = confusion_matrix(y_test, predictions, labels=label_order)

print("\n--- Accuracy and confusion matrix ---")
print("Accuracy:", accuracy)
print("Confusion Matrix:")
print(matrix)

# Step 6: Print a classification report.
report = classification_report(y_test, predictions, labels=label_order)

print("\n--- Classification report ---")
print(report)

# Step 7: Run cross-validation.
cv_folds = 3
cv_scores = cross_val_score(model, X, y, cv=cv_folds, scoring="accuracy")
rounded_cv_scores = [float(round(score, 2)) for score in cv_scores]
average_cv_score = float(round(cv_scores.mean(), 2))

print("\n--- Cross-validation ---")
print("Cross-validation scores:", rounded_cv_scores)
print("Average cross-validation accuracy:", average_cv_score)

# Step 8: Save the metrics summary.
metrics_lines = [
    f"Accuracy: {accuracy}",
    "",
    "Confusion Matrix:",
    str(matrix),
    "",
    "Classification Report:",
    report,
    f"Cross-validation scores: {rounded_cv_scores}",
    f"Average cross-validation accuracy: {average_cv_score}",
]

with open(OUTPUTS_DIR / "knn_metrics.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(metrics_lines))

print("Saved: outputs/knn_metrics.txt")
```

## Navigation

- ⬅️ Previous: [01-theory.md](./01-theory.md).
- 🧭 Week Overview: [week-06-overview.md](../week-06-overview.md).
- ➡️ Next: [03-practice.md](./03-practice.md).
