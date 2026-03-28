# 03. Practice: Apply Decision Trees to a New Dataset

## Setup

1. Create a folder called `week6-decision-tree-practice`.
2. Inside it, create these folders:
   ```text
   data/
   outputs/
   scripts/
   ```
3. Inside `data/`, create a file called `course_readiness.csv`.
4. Put this exact content in `data/course_readiness.csv`:
   ```text
   study_days,review_sessions,status
   1,0,follow_up
   1,1,follow_up
   2,1,follow_up
   2,2,follow_up
   3,1,follow_up
   3,2,follow_up
   3,3,steady_progress
   4,2,follow_up
   4,3,steady_progress
   4,4,steady_progress
   5,3,steady_progress
   5,4,steady_progress
   6,3,steady_progress
   6,4,steady_progress
   ```
5. Inside `scripts/`, create `train_decision_tree_course_readiness.py`.
6. Add this starter code:

```python
from pathlib import Path

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text

# Path to the project folder that contains data/, outputs/, and scripts/
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUTS_DIR = BASE_DIR / "outputs"

OUTPUTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_DIR / "course_readiness.csv")

print("--- df.head() ---")
print(df.head())

print("\n--- df.columns ---")
print(df.columns)

print("\n--- df.dtypes ---")
print(df.dtypes)

print("\n--- df['status'].value_counts() ---")
print(df["status"].value_counts())
```

This practice is meant to feel familiar but not identical to the worked example. The goal is to reuse the workflow on
new column names and a new situation.

## Tasks

1. Run the starter code and confirm the file loads correctly.
2. Store the feature names in a list called `feature_columns`.
3. Store the target column name in `target_column`.
4. Create `X` from `study_days` and `review_sessions`.
5. Create `y` from `status`.
6. Split the data with `test_size=0.25`, `random_state=42`, and `stratify=y`.
7. Create `DecisionTreeClassifier(max_depth=3, random_state=42)`.
8. Fit the model with the training data.
9. Predict the outcomes for `X_test`.
10. Build a `results_df` that includes:
    - `study_days`
    - `review_sessions`
    - `actual_status`
    - `predicted_status`
11. Calculate the accuracy.
12. Export the tree rules with `export_text(...)`.
13. Save `results_df` to `outputs/course_readiness_tree_results.csv`.
14. Save the rules to `outputs/course_readiness_tree_rules.txt`.
15. Create a new DataFrame for these two new rows:
    - `study_days=2`, `review_sessions=2`
    - `study_days=5`, `review_sessions=4`
16. Predict the outcomes for those new rows.
17. Print:
    - `results_df`
    - the accuracy
    - the tree rules
    - the new predictions
    - the two saved-file messages

In these tasks, `X` is the input data and `y` is the label column you want the model to predict.

## Expected Output Examples

Possible label count output:

```text
status
follow_up          7
steady_progress    7
Name: count, dtype: int64
```

Your exact formatting can vary a little depending on the `pandas` version. That is normal.

Possible `results_df` output:

```text
 study_days  review_sessions   actual_status predicted_status
          5                4 steady_progress  steady_progress
          6                4 steady_progress  steady_progress
          2                2       follow_up        follow_up
          4                2       follow_up        follow_up
```

Possible accuracy output:

```text
Accuracy: 1.0
```

Possible rules output:

```text
|--- review_sessions <= 2.50
|   |--- class: follow_up
|--- review_sessions >  2.50
|   |--- class: steady_progress
```

Possible new prediction output:

```text
New predictions: ['follow_up', 'steady_progress']
```

Possible saved-file messages:

```text
Saved: outputs/course_readiness_tree_results.csv
Saved: outputs/course_readiness_tree_rules.txt
```

## Debug Task 1

Code:

```python
target_column = "result"
y = df[target_column]
```

Expected behavior:

```text
You wanted to select the target labels from the CSV.
```

Actual behavior:

```text
It raises a KeyError because the real target column is called "status".
```

## Debug Task 2

Code:

```python
tree_rules = export_text(model, feature_names=["study_days"])
```

Expected behavior:

```text
You wanted the exported rules to show the feature names clearly.
```

Actual behavior:

```text
It raises an error because the model was trained with two features but only one feature name was given.
```

## Debug Task 3

Code:

```python
results_df.to_csv(DATA_DIR / "course_readiness.csv", index=False)
```

Expected behavior:

```text
You wanted to save the prediction results.
```

Actual behavior:

```text
This overwrites the raw dataset instead of keeping generated output in outputs/.
```

## Self-Review

- I can explain how a decision tree uses rule-like splits.
- I can train a `DecisionTreeClassifier` and make predictions.
- I can keep the tree smaller with `max_depth=3`.
- I can export readable rules with `export_text(...)`.
- I can adapt the same workflow to a new dataset with different column names.
- I can keep raw data and output files separate.

## Navigation

- ⬅️ Previous: [02-worked-examples.md](./02-worked-examples.md).
- 🧭 Week Overview: [week-06-overview.md](../week-06-overview.md).
- ➡️ Next: [04-challenge.md](./04-challenge.md).
