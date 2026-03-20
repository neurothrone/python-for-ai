# 03. Practice: ML and Linear Regression Basics

## Setup

1. Create a folder called `week5-regression-practice`.
2. Inside it, create these folders:
   ```text
   data/
   scripts/
   ```
3. Inside `data/`, create a file called `apartment_rent.csv`.
4. Put this exact content in `data/apartment_rent.csv`:
    ```text
    size_sqm,rent
    25,650
    30,720
    35,790
    40,860
    45,930
    50,1010
    55,1080
    60,1160
    ```
5. Inside `scripts/`, create a script called `rent_model.py`.
6. Add this starter code:

```python
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "apartment_rent.csv")

print(df.head())
print(df.columns)
```

We use `pathlib` here because the script is inside `scripts/`, while the CSV is inside `data/`.

## Tasks

1. Define `X` as the `size_sqm` (_size in square meters_) feature column.
2. Define `y` as the `rent` target column.
3. Store the column names in variables such as `feature_column` and `target_column` if that helps you read the code.
4. Split the data into training and test sets with `test_size=0.25` and `random_state=42`.
5. Create a `LinearRegression()` model.
6. Fit the model with the training data.
7. Make predictions for `X_test`.
8. Build a small comparison table that includes the test input values, actual rents, and predicted rents.
9. Print the test inputs, predicted values, and actual values.
10. Create a new DataFrame for one apartment size of `48`.
11. Predict the rent for size `48`.
12. Print the prediction in a sentence.

## Expected Output Examples

Possible final sentence:

```text
Predicted rent for 48 sqm: 975.0
```

Your exact test rows may print in a different order, but the workflow should clearly show:

- A feature column `size_sqm`.
- A target column `rent`.
- Predicted values.
- Actual values for comparison.

## Debug Task 1

Code:

```python
X = df["size_sqm"]
y = df["rent"]
```

Expected behavior:

```text
You expected X to be ready for Scikit-learn as the feature input.
```

Actual behavior:

```text
This creates a Series, not a one-column DataFrame. That can lead to shape confusion for beginners.
```

## Debug Task 2

Code:

```python
model = LinearRegression()
predictions = model.predict(X_test)
```

Expected behavior:

```text
You expected predicted rent values.
```

Actual behavior:

```text
It raises an error because the model was never fitted with model.fit(...).
```

## Debug Task 3

Code:

```python
X = df[["rent"]]
y = df["size_sqm"]
```

Expected behavior:

```text
You wanted to predict rent from apartment size.
```

Actual behavior:

```text
The feature and target are reversed, so the model is learning the wrong question.
```

## Debug Task 4

Code:

```python
new_data = pd.DataFrame({"area": [48]})
print(model.predict(new_data))
```

Expected behavior:

```text
You expected a prediction for an apartment of size 48.
```

Actual behavior:

```text
The column name does not match the training feature name, so prediction can fail or behave unexpectedly.
```

## Self-Review

- I can explain what a feature is and what a target is.
- I can split data into training and test sets in simple terms.
- I can fit a linear regression model and make predictions.
- I can compare predicted values with actual values without overcomplicating the interpretation.
- I can debug wrong-shape, wrong-column, and missing-fit mistakes.

## Navigation

- ⬅️ Previous: [02-worked-examples.md](./02-worked-examples.md).
- 🧭 Week Overview: [week-05-overview.md](../week-05-overview.md).
- ➡️ Next: [04-challenge.md](./04-challenge.md).
