# 02. Worked Examples: k-NN Classification

## Example A: Create the Project Structure

Create this structure:

```text
week6-knn-demo/
  data/
    student_support.csv
  outputs/
  scripts/
    train_knn_student_support.py
```

This keeps the workflow clear:

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

The target column is `outcome`.

The two feature columns are:

- `study_hours`
- `practice_sessions`

## Example C: Load and Inspect the Data

Create `scripts/train_knn_student_support.py` with this starter code:

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
  folder."
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

## Example D: Choose Features and Split the Data

Add this code below the inspection step:

```python
feature_columns = ["study_hours", "practice_sessions"]
target_column = "outcome"

X = df[feature_columns]  # X usually means the input columns in machine learning examples
y = df[target_column]  # y usually means the value we want to predict

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y,
)
```

Important details:

- `feature_columns` stores the feature names in one clear place.
- `X = df[feature_columns]` keeps both feature columns together in one table.
- `y = df[target_column]` stores the labels you want to predict.
- In many machine learning examples, `X` means input data and `y` means the target to predict.
- `random_state=42` keeps the split repeatable and reproducible, which makes it easier to learn from the same example.
- `stratify=y` keeps a similar label mix in train and test data.

## Example E: Train the k-NN Model

Add this code next:

```python
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
```

This is the first full model step:

- `KNeighborsClassifier(...)` creates the model.
- `n_neighbors=3` means the model checks the three nearest rows (this is the `k` in `k-NN`).
- `fit(...)` gives the model the training data.

## Example F: Predict, Check Accuracy, and Save Results

Add this code below the model training:

```python
predictions = model.predict(X_test)

results_df = X_test.copy()
results_df["actual_outcome"] = y_test.values
results_df["predicted_outcome"] = predictions

accuracy = accuracy_score(y_test, predictions)

results_df.to_csv(OUTPUTS_DIR / "student_support_knn_results.csv", index=False)

print(results_df)
print("Accuracy:", accuracy)
print("Saved: outputs/student_support_knn_results.csv")
```

Why this is a clear workflow:

- `predictions` stores the model's answers for the test rows.
- `X_test.copy()` creates a separate copy so you can build a result table without changing the original test data.
- `results_df` keeps the feature values, the real label, and the predicted label together.
- `accuracy_score(...)` gives a simple first check.
- Saving the result file in `outputs/` keeps raw data separate from generated output (new files created by the script).

Possible printed result:

```text
    study_hours  practice_sessions actual_outcome predicted_outcome
6             3                  1  needs_support     needs_support
4             2                  2  needs_support     needs_support
11            4                  4           pass              pass
3             2                  1  needs_support     needs_support
16            6                  2           pass              pass
Accuracy: 1.0
Saved: outputs/student_support_knn_results.csv
```

## Example G: Predict New Cases

Now add one small prediction step for new rows:

```python
new_students = pd.DataFrame(
    {
        "study_hours": [2, 5],
        "practice_sessions": [3, 1],
    }
)

new_predictions = model.predict(new_students)

print("New predictions:", list(new_predictions))
```

These two rows describe imagined students:

- `study_hours=2` and `practice_sessions=3` means a student who studied for 2 hours and had 3 practice sessions.
- `study_hours=5` and `practice_sessions=1` means a student who studied for 5 hours and had 1 practice session.

Possible output:

```text
New predictions: ['needs_support', 'pass']
```

This is useful because it shows the real goal of a classifier: use learned patterns for new cases.

In clear words, the output means:

- The first new student was predicted as `needs_support`.
- The second new student was predicted as `pass`.

## Example H: Read the Output in Simple English

A short interpretation could be:

- The model correctly matched the test rows in this split.
- A student with `2` study hours and `3` practice sessions was predicted as `needs_support`.
- A student with `5` study hours and `1` practice session was predicted as `pass`.

Keep the interpretation small and honest. You are describing what happened in this run, not claiming the model is
perfect in every situation.

## Full Script

If you want to see the whole file in one place, here is one clear version with comment headers:

```python
from pathlib import Path

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
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

# Step 3: Choose features and split the data.
feature_columns = ["study_hours", "practice_sessions"]
target_column = "outcome"

X = df[feature_columns]
y = df[target_column]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y,
)

# Step 4: Create and train the model.
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Step 5: Predict on the test rows.
predictions = model.predict(X_test)

# Step 6: Build and save the results table.
results_df = X_test.copy()
results_df["actual_outcome"] = y_test.values
results_df["predicted_outcome"] = predictions

accuracy = accuracy_score(y_test, predictions)

results_df.to_csv(OUTPUTS_DIR / "student_support_knn_results.csv", index=False)

print("\n--- Results ---")
print(results_df)

print("\nAccuracy:", accuracy)
print("Saved: outputs/student_support_knn_results.csv")

# Step 7: Predict outcomes for new rows.
new_students = pd.DataFrame(
    {
        "study_hours": [2, 5],
        "practice_sessions": [3, 1],
    }
)

new_predictions = model.predict(new_students)

print("\n--- New predictions ---")
print("New predictions:", list(new_predictions))
```

## Navigation

- ⬅️ Previous: [01-theory.md](./01-theory.md).
- 🧭 Week Overview: [week-06-overview.md](../week-06-overview.md).
- ➡️ Next: [03-practice.md](./03-practice.md).
