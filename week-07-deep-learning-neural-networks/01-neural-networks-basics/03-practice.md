# 03. Practice: Neural Networks Basics

## Setup

1. Create a folder called `week7-network-basics-practice`.
2. Inside it, create these folders:
   ```text
   data/
   scripts/
   ```
3. Inside `data/`, create `student_completion.csv`.
4. Put this exact content in `data/student_completion.csv`:
   ```text
   study_hours,practice_sessions,review_sessions,completed_course
   1,0,1,0
   1,1,1,0
   1,2,1,0
   2,1,1,0
   2,1,2,0
   2,2,2,0
   2,3,2,0
   3,1,2,0
   3,2,2,0
   3,2,3,0
   3,3,3,1
   4,2,3,0
   4,3,3,1
   4,3,4,1
   4,4,4,1
   5,2,3,1
   5,3,4,1
   5,4,4,1
   5,4,5,1
   6,2,4,1
   6,3,4,1
   6,4,5,1
   7,3,5,1
   7,4,5,1
   8,4,5,1
   ```
5. Inside `scripts/`, create `inspect_first_network.py`.
6. Add this starter code:

```python
from pathlib import Path

import pandas as pd
from tensorflow import keras
from tensorflow.keras import layers

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "student_completion.csv")
```

This practice is meant to feel close to the worked example, but with more responsibility on your side.

The main goal is not to train a useful model yet. The main goal is to:

- Inspect the data clearly.
- Match the input shape to the feature columns.
- Build one tiny network without getting lost.

## Tasks

1. Create `feature_columns` with:
    - `study_hours`.
    - `practice_sessions`.
    - `review_sessions`.
2. Create `target_column = "completed_course"`.
3. Build `X` from the feature columns.
4. Build `y` from the target column.
5. Convert both to `float32`.
6. Print:
    - `df.head()`.
    - `df["completed_course"].value_counts()`.
    - `X.shape`.
    - `y.shape`.
7. Create a `keras.Sequential(...)` model with:
    - `keras.Input(shape=(3,))`.
    - `layers.Dense(1, activation="sigmoid")`.
8. Give the model a name.
9. Print `model.summary()`.
10. Build `sample_batch` from the first 3 rows of `X`.
11. Call the model on `sample_batch`.
12. Print:
    - The sample batch shape.
    - The sample output shape.
13. Write 2 short sentences after the code:
    - One sentence that says why this dataset could fit a small neural network.
    - One sentence naming one simpler Week 6 baseline you would still consider first.

## Expected Output Examples

Possible shape lines:

```text
Feature shape: (25, 3)
Target shape: (25,)
Sample batch shape: (3, 3)
Sample output shape: (3, 1)
```

Possible target count output:

```text
completed_course
1    14
0    11
Name: count, dtype: int64
```

Your exact formatting can vary a little depending on the `pandas` version. That is normal.

## Debug Task 1

Code:

```python
model = keras.Sequential(
    [
        keras.Input(shape=(2,)),
        layers.Dense(1, activation="sigmoid"),
    ]
)
```

Expected behavior:

```text
You wanted the model input shape to match the 3 feature columns.
```

Actual behavior:

```text
The model shape does not match the data shape, so the workflow will 
break when you try to pass 3-feature rows into the model.
```

## Debug Task 2

Code:

```python
y = df[feature_columns]
```

Expected behavior:

```text
You wanted `y` to contain the target labels only.
```

Actual behavior:

```text
This creates another feature table instead of the target column, so the 
model no longer has a clear label to learn from.
```

## Hint

A clear order is:

- Define the feature columns first.
- Define the target column.
- Build `X` and `y`.
- Convert them to `float32`.
- Print the shapes before building the model.
- Match the input shape to the number of feature columns.
- Pass a small sample batch through the model.

## Self-Review

- I can inspect the target values before I jump into the model.
- I can explain why the input shape must match the feature columns.
- I can explain why a binary classification model often uses one output unit.
- I can explain why an untrained model is different from a useful model.
- I can inspect a neural network model without feeling lost.
- I can still name a simpler Week 6 baseline instead of assuming Keras should be the first choice.

## Navigation

- ⬅️ Previous: [02-worked-examples.md](./02-worked-examples.md).
- 🧭 Week Overview: [week-07-overview.md](../week-07-overview.md).
- ➡️ Next: [04-challenge.md](./04-challenge.md).
