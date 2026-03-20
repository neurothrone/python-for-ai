# 02. Worked Examples: ML and Linear Regression Basics

## Example A: Create the Dataset

Create this structure:

```text
week5-regression-demo/
  data/
    study_performance.csv
  scripts/
    linear_regression_demo.py
```

Create `data/study_performance.csv` with this content:

```text
hours_studied,test_score
1,52
2,55
3,60
4,65
5,71
6,76
7,82
8,88
```

Then create `scripts/linear_regression_demo.py`.

## Example B: Load Data and Define Feature and Target

```python
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "study_performance.csv")

print(df.head())
print(df.columns)

feature_column = "hours_studied"
target_column = "test_score"

X = df[[feature_column]]
y = df[target_column]

print(type(X))
print(type(y))
```

We use `pathlib` here because the script is inside `scripts/`, but the CSV is inside `data/`.

- `X` is the feature data.
- `y` is the target data.
- `feature_column` stores the input column name.
- `target_column` stores the output column name.
- We use double brackets for `X` so it stays a DataFrame with one column.

## Example C: Split into Training and Test Data

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)
```

- `test_size=0.25` means 25% of the rows go to the test set.
- `random_state=42` keeps the split repeatable, which helps when learners compare results.

## Example D: Create and Fit the Model

```python
model = LinearRegression()
model.fit(X_train, y_train)
```

- `LinearRegression()` creates the model.
- `fit(...)` teaches the model from the training data.

## Example E: Make Predictions

```python
predictions = model.predict(X_test)

results_df = X_test.copy()
results_df["actual_score"] = y_test.values
results_df["predicted_score"] = predictions

print("Comparison table:")
print(results_df)

print("Predicted values:")
print(predictions)

print("Actual values:")
print(y_test.values)
```

Printing both helps you compare the idea of prediction with the real test values. The comparison table is often easier
to read because it keeps the input, actual values, and predicted values together.

## Example F: Predict a New Value

```python
new_data = pd.DataFrame({feature_column: [9]})
new_prediction = model.predict(new_data)
print("Predicted score for 9 study hours:", new_prediction[0])
```

Why use a DataFrame here? Because it matches the same feature shape as training data.

## Example G: Full Script

```python
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "study_performance.csv")

feature_column = "hours_studied"
target_column = "test_score"

X = df[[feature_column]]
y = df[target_column]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

results_df = X_test.copy()
results_df["actual_score"] = y_test.values
results_df["predicted_score"] = predictions

print("Test inputs:")
print(X_test)
print("Comparison table:")
print(results_df)
print("Predicted values:")
print(predictions)
print("Actual values:")
print(y_test.values)

new_data = pd.DataFrame({feature_column: [9]})
print("Predicted score for 9 study hours:", model.predict(new_data)[0])
```

## Example H: Simple Interpretation

Keep interpretation small:

- The model learned that higher study hours usually go with higher scores.
- The predicted values are close to the actual values for this small dataset.
- This does not mean the model is perfect. It means the workflow is working and the pattern is simple enough for a
  first example.

## Navigation

- ⬅️ Previous: [01-theory.md](./01-theory.md).
- 🧭 Week Overview: [week-05-overview.md](../week-05-overview.md).
- ➡️ Next: [03-practice.md](./03-practice.md).
