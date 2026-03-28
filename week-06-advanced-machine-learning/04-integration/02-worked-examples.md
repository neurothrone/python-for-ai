# 02. Worked Examples: Integration

## Example A: Create the Project Structure

Create this structure:

```text
week6-model-comparison-demo/
  data/
    student_support.csv
  outputs/
  scripts/
    compare_classification_models.py
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

## Example C: Load the Data and Build One Shared Split

Create `scripts/compare_classification_models.py` with this code:

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

df = pd.read_csv(DATA_DIR / "student_support.csv")

print("--- df.head() ---")
print(df.head())

print("\n--- df.columns ---")
print(df.columns)

print("\n--- df.dtypes ---")
print(df.dtypes)

print("\n--- df['outcome'].value_counts() ---")
print(df["outcome"].value_counts())

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
```

The shared split is important. It means both models are tested on the same rows.

The path line can look unusual at first:

- `BASE_DIR = Path(__file__).resolve().parent.parent` means "start from this script file, then go up to the main
  project folder".

## Example D: Define Both Models Clearly

Now add this model setup:

```python
model_configs = [
    {
        "display_name": "k-NN (k=3)",
        "prediction_column": "knn_prediction",
        "model": KNeighborsClassifier(n_neighbors=3),
    },
    {
        "display_name": "Decision Tree",
        "prediction_column": "tree_prediction",
        "model": DecisionTreeClassifier(max_depth=3, random_state=42),
    },
]
```

This structure helps because:

- The display name is used in the comparison table.
- The prediction column name is used in the saved test-results file.
- The actual model object stays tied to the right name.

Each `{...}` block is a dictionary. Here we use dictionaries, so each model keeps its name, output column, and settings
together in one place.

## Example E: Build the Shared Result Containers

Add this code:

```python
predictions_df = X_test.copy()
predictions_df["actual_outcome"] = y_test.values

comparison_rows = []
cv_folds = 3
```

`predictions_df` will let you compare both models on the same test rows.

Why `copy()` and an empty list here?

- `X_test.copy()` gives you a separate table for saved results
- `comparison_rows = []` starts an empty list that will get one summary row per model

## Example F: Train, Predict, and Compare

Add this loop:

```python
for config in model_configs:
    model = config["model"]
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    predictions_df[config["prediction_column"]] = predictions

    cv_scores = cross_val_score(model, X, y, cv=cv_folds, scoring="accuracy")

    comparison_rows.append(
        {
            "model_name": config["display_name"],
            "test_accuracy": round(accuracy_score(y_test, predictions), 2),
            "cv_score_1": float(round(cv_scores[0], 2)),
            "cv_score_2": float(round(cv_scores[1], 2)),
            "cv_score_3": float(round(cv_scores[2], 2)),
            "cv_mean_accuracy": float(round(cv_scores.mean(), 2)),
        }
    )
```

This is the main integration step:

- Each model is trained on the same training rows.
- Each model predicts the same test rows.
- Each model gets the same cross-validation check.
- The `for config in model_configs:` loop repeats the same steps for each model so the comparison stays consistent.

## Example G: Save the Comparison Files

Add this final output step:

```python
comparison_df = pd.DataFrame(comparison_rows)

predictions_df.to_csv(OUTPUTS_DIR / "model_test_predictions.csv", index=False)
comparison_df.to_csv(OUTPUTS_DIR / "model_comparison.csv", index=False)

print("\n--- Test predictions ---")
print(predictions_df.to_string(index=False))

print("\n--- Model comparison ---")
print(comparison_df.to_string(index=False))

print("\nSaved: outputs/model_test_predictions.csv")
print("Saved: outputs/model_comparison.csv")
```

Saving two files is useful here:

- One file shows row-by-row predictions.
- One file shows model-by-model summary results.

Using `to_string(index=False)` also helps because these tables are a bit wider, so this makes them easier to read
without `...`.

Possible test-prediction output:

```text
 study_hours  practice_sessions actual_outcome knn_prediction tree_prediction
           3                  1  needs_support  needs_support   needs_support
           2                  2  needs_support  needs_support   needs_support
           4                  4           pass           pass            pass
           2                  1  needs_support  needs_support   needs_support
           6                  2           pass           pass            pass
```

Possible comparison output:

```text
   model_name  test_accuracy  cv_score_1  cv_score_2  cv_score_3  cv_mean_accuracy
   k-NN (k=3)            1.0        0.83        0.83        0.67              0.78
Decision Tree            1.0        0.83        0.67        0.50              0.67
```

## Example H: Read the Comparison Carefully

One short interpretation could be:

- Both models were correct on this one test split.
- `k-NN` had the stronger average cross-validation score on this small dataset.
- That does not mean `k-NN` is always better, but it is the stronger result in this specific comparison.

This kind of conclusion is straightforward, careful, and realistic.

## Full Script

If you want to see the whole file in one place, here is one clear version with comment headers:

```python
from pathlib import Path

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

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

# Step 3: Choose features and build one shared split.
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

# Step 4: Define both models.
model_configs = [
  {
    "display_name": "k-NN (k=3)",
    "prediction_column": "knn_prediction",
    "model": KNeighborsClassifier(n_neighbors=3),
  },
  {
    "display_name": "Decision Tree",
    "prediction_column": "tree_prediction",
    "model": DecisionTreeClassifier(max_depth=3, random_state=42),
  },
]

# Step 5: Build the shared result containers.
predictions_df = X_test.copy()
predictions_df["actual_outcome"] = y_test.values

comparison_rows = []
cv_folds = 3

# Step 6: Train, predict, and compare.
for config in model_configs:
  model = config["model"]
  model.fit(X_train, y_train)

  predictions = model.predict(X_test)
  predictions_df[config["prediction_column"]] = predictions

  cv_scores = cross_val_score(model, X, y, cv=cv_folds, scoring="accuracy")

  comparison_rows.append(
    {
      "model_name": config["display_name"],
      "test_accuracy": round(accuracy_score(y_test, predictions), 2),
      "cv_score_1": float(round(cv_scores[0], 2)),
      "cv_score_2": float(round(cv_scores[1], 2)),
      "cv_score_3": float(round(cv_scores[2], 2)),
      "cv_mean_accuracy": float(round(cv_scores.mean(), 2)),
    }
  )

# Step 7: Save and print the comparison files.
comparison_df = pd.DataFrame(comparison_rows)

predictions_df.to_csv(OUTPUTS_DIR / "model_test_predictions.csv", index=False)
comparison_df.to_csv(OUTPUTS_DIR / "model_comparison.csv", index=False)

print("\n--- Test predictions ---")
print(predictions_df.to_string(index=False))

print("\n--- Model comparison ---")
print(comparison_df.to_string(index=False))

print("\nSaved: outputs/model_test_predictions.csv")
print("Saved: outputs/model_comparison.csv")
```

## Navigation

- ⬅️ Previous: [01-theory.md](./01-theory.md).
- 🧭 Week Overview: [week-06-overview.md](../week-06-overview.md).
- ➡️ Next: [03-practice.md](./03-practice.md).
