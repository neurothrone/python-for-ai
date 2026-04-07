# 02. Worked Examples: Keras Sequential Models

## Example A: Reuse the Same Folder Structure

Use this structure:

```text
week7-sequential-demo/
  data/
    student_completion.csv
  scripts/
    build_sequential_model.py
```

Use the same `student_completion.csv` dataset from the previous section.

The purpose here is still not "build the most advanced network." The purpose is:

- Keep the question stable.
- Define one small architecture clearly.
- Make the model easier to inspect and explain.

## Example B: Load the Data

Create `scripts/build_sequential_model.py` with this code:

```python
from pathlib import Path

import pandas as pd
from tensorflow import keras
from tensorflow.keras import layers

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "student_completion.csv")

feature_columns = ["study_hours", "practice_sessions", "review_sessions"]

X = df[feature_columns].astype("float32")
```

We reuse the same small tabular classification question on purpose. That keeps the model-building step connected to the
workflow instead of turning it into a completely new topic.

## Example C: Build a Small Sequential Model

Now add this code:

```python
model = keras.Sequential(name="student_completion_network")
model.add(keras.Input(shape=(len(feature_columns),)))
model.add(layers.Dense(8, activation="relu", name="hidden_1"))
model.add(layers.Dense(4, activation="relu", name="hidden_2"))
model.add(layers.Dense(1, activation="sigmoid", name="output"))
```

Why this is helpful:

- `add(...)` makes the model feel like a simple stack.
- Each layer gets a clear role.
- Naming the layers makes the summary easier to read.

This architecture is still intentionally small. At this stage, clarity matters more than extra complexity.

## Example D: Print the Model Summary

Add this:

```python
print("\n--- model.summary() ---")
model.summary()
```

You should notice:

- The first hidden layer outputs 8 values.
- The second hidden layer outputs 4 values.
- The output layer gives 1 value per row.

## Example E: Inspect the Layer Names

Add this:

```python
print("\n--- Layer names ---")
print("Layer names:", [layer.name for layer in model.layers])
```

Possible printed line:

```text
Layer names: ['hidden_1', 'hidden_2', 'output']
```

The input object is not shown in `model.layers` because it is not a normal layer in that list.

## Example F: Pass a Small Batch Through the Model

Add this:

```python
sample_batch = X.head(2).to_numpy()
sample_output = model(sample_batch)

print("\n--- Sample shapes ---")
print("Sample batch shape:", sample_batch.shape)
print("Sample output shape:", sample_output.shape)
```

Possible printed lines:

```text
Sample batch shape: (2, 3)
Sample output shape: (2, 1)
```

## Example G: Read the Architecture in Plain English

A short plain English interpretation could be:

- The model reads 3 feature values.
- It transforms them through 2 hidden layers.
- It produces 1 probability-like output for binary classification.

That is enough understanding for a strong beginner start. It is also a reminder that architecture is only one part of a
good model choice. A simpler Week 6 baseline could still be a very reasonable first comparison.

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

# Step 3: Define the feature columns.
feature_columns = ["study_hours", "practice_sessions", "review_sessions"]
X = df[feature_columns].astype("float32")

# Step 4: Build a small Sequential model.
model = keras.Sequential(name="student_completion_network")
model.add(keras.Input(shape=(len(feature_columns),)))
model.add(layers.Dense(8, activation="relu", name="hidden_1"))
model.add(layers.Dense(4, activation="relu", name="hidden_2"))
model.add(layers.Dense(1, activation="sigmoid", name="output"))

# Step 5: Print the model summary.
print("\n--- model.summary() ---")
model.summary()

# Step 6: Print the layer names.
print("\n--- Layer names ---")
print("Layer names:", [layer.name for layer in model.layers])

# Step 7: Pass a small batch through the model.
sample_batch = X.head(2).to_numpy()
sample_output = model(sample_batch)

print("\n--- Sample shapes ---")
print("Sample batch shape:", sample_batch.shape)
print("Sample output shape:", sample_output.shape)
```

## Navigation

- ⬅️ Previous: [01-theory.md](./01-theory.md).
- 🧭 Week Overview: [week-07-overview.md](../week-07-overview.md).
- ➡️ Next: [03-practice.md](./03-practice.md).
