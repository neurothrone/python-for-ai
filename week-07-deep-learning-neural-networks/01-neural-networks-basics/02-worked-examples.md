# 02. Worked Examples: Neural Networks Basics

## Example A: Create the Folder Structure

Create this structure:

```text
week7-network-basics-demo/
  data/
    student_completion.csv
  scripts/
    inspect_first_network.py
```

This week still uses the same structure from the previous week:

- Raw data in `data/`.
- Scripts in `scripts/`.

This example is not trying to prove that a neural network is the best model. The goal is simpler:

- Keep one clear classification question.
- Inspect the shape of the data.
- Build one tiny model.
- Understand what the model is expecting before any training starts.

## Example B: Create the Dataset

Create `data/student_completion.csv` with this content:

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

The target column is numeric on purpose:

- `0` means `not_completed`.
- `1` means `completed`.

This kind of small numeric dataset is useful for Week 7 because it keeps the workflow manageable. In a real task, you
would still ask whether a simpler Week 6 model could also be a sensible first baseline.

## Example C: Load the Data and Define Features

Create `scripts/inspect_first_network.py` with this code:

```python
from pathlib import Path

import pandas as pd
from tensorflow import keras
from tensorflow.keras import layers

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "student_completion.csv")

feature_columns = ["study_hours", "practice_sessions", "review_sessions"]
target_column = "completed_course"

X = df[feature_columns].astype("float32")
y = df[target_column].astype("float32")

print("--- df.head() ---")
print(df.head())

print(f"\n--- df['{target_column}'].value_counts() ---")
print(df[target_column].value_counts())

print("\n--- Shapes ---")
print("Feature shape:", X.shape)
print("Target shape:", y.shape)
```

Why convert to `float32` here?

- Neural network workflows usually expect numeric values.
- `float32` is a common Keras/TensorFlow data type for model input.

Why print the target counts?

- It reminds you to inspect the labels before you start building a model.
- It keeps the Week 6 habit of looking at the data before trusting the workflow.

## Example D: Build a Very Small Network

Now add this code:

```python
model = keras.Sequential(
    [
        keras.Input(shape=(len(feature_columns),)),
        layers.Dense(1, activation="sigmoid"),
    ],
    name="student_completion_minimal_network",
)
```

What this model means:

- The input shape is 3 because we use 3 feature columns.
- The output has 1 unit because this is binary classification.
- `sigmoid` keeps the output in a probability-like range between 0 and 1.

This is intentionally small. A first Week 7 model should help you understand the workflow before you worry about model
size.

## Example E: Print the Model Summary

Add this:

```python
model.summary()
```

You should now see that:

- The model has one dense layer.
- The output shape ends with `1`.
- The parameter count is small.

The summary is a good habit because it helps you confirm that the model shape matches your plan.

## Example F: Check a Small Batch Shape

Add this:

```python
sample_batch = X.head(3).to_numpy()
sample_output = model(sample_batch)

print("\n--- Sample shapes ---")
print("Sample batch shape:", sample_batch.shape)
print("Sample output shape:", sample_output.shape)
```

Possible printed lines:

```text
Sample batch shape: (3, 3)
Sample output shape: (3, 1)
```

The important idea is not the actual prediction values yet. The model is still untrained.

The useful thing here is shape:

- 3 rows in.
- 1 output value per row out.

## Example G: Read the First Model in Plain English

A simple plain-English description could be:

- The model reads 3 numeric features for each row.
- It produces 1 output value for each row.
- Later, training will adjust the weights so the output becomes more useful.

One careful note could also be:

- This network may be worth trying on this tabular classification problem.
- A simpler Week 6 baseline could still be a good first comparison.

## Full Script

If you want to see the whole file in one place, here is one clear version with comment headers:

```python
from pathlib import Path

import pandas as pd
from tensorflow import keras
from tensorflow.keras import layers

# Step 1: Define folder paths.
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# Step 2: Load the dataset.
df = pd.read_csv(DATA_DIR / "student_completion.csv")

# Step 3: Define feature columns and target column.
feature_columns = ["study_hours", "practice_sessions", "review_sessions"]
target_column = "completed_course"

# Step 4: Build X and y as float32.
X = df[feature_columns].astype("float32")
y = df[target_column].astype("float32")

# Step 5: Inspect the data.
print("--- df.head() ---")
print(df.head())

print(f"\n--- df['{target_column}'].value_counts() ---")
print(df[target_column].value_counts())

print("\n--- Shapes ---")
print("Feature shape:", X.shape)
print("Target shape:", y.shape)

# Step 6: Build a very small neural network.
model = keras.Sequential(
    [
        keras.Input(shape=(len(feature_columns),)),
        layers.Dense(1, activation="sigmoid"),
    ],
    name="student_completion_minimal_network",
)

# Step 7: Print the model summary.
print("\n--- model.summary() ---")
model.summary()

# Step 8: Pass a small batch through the untrained model.
sample_batch = X.head(3).to_numpy()
sample_output = model(sample_batch)

print("\n--- Sample shapes ---")
print("Sample batch shape:", sample_batch.shape)
print("Sample output shape:", sample_output.shape)
```

## Navigation

- ⬅️ Previous: [01-theory.md](./01-theory.md).
- 🧭 Week Overview: [week-07-overview.md](../week-07-overview.md).
- ➡️ Next: [03-practice.md](./03-practice.md).
