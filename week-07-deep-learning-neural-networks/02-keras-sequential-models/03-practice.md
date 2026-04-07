# 03. Practice: Keras Sequential Models

## Setup

1. Create a folder called `week7-sequential-practice`.
2. Inside it, create these folders:
   ```text
   data/
   scripts/
   ```
3. Reuse the same `student_completion.csv` dataset from the previous section.
4. Inside `scripts/`, create `build_sequential_model.py`.
5. Add this starter code:

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

This practice is meant to make the model structure feel more readable.

The goal is not to search for the "best" architecture. The goal is to:

- Build a small `Sequential` model on purpose.
- Name the layers clearly.
- Read the summary without guessing.

## Tasks

1. Create a `keras.Sequential(...)` model.
2. Give the model a name.
3. Add `keras.Input(shape=(3,))`.
4. Add a hidden layer with:
    - 8 units.
    - `relu`.
    - A clear name.
5. Add a second hidden layer with:
    - 4 units.
    - `relu`.
    - A clear name.
6. Add an output layer with:
    - 1 unit.
    - `sigmoid`.
    - A clear name.
7. Print `model.summary()`.
8. Print the layer names.
9. Pass the first 2 rows of `X` through the model.
10. Print the sample batch shape and sample output shape.
11. Write 2 short sentences after the code:
    - One sentence explaining why this architecture is only a first model.
    - One sentence naming one simpler Week 6 baseline you would still consider.

## Expected Output Examples

Possible printed line:

```text
Layer names: ['hidden_1', 'hidden_2', 'output']
```

Possible shape lines:

```text
Sample batch shape: (2, 3)
Sample output shape: (2, 1)
```

Your exact summary formatting can vary a little depending on the library version. That is normal.

## Debug Task 1

Code:

```python
model.add(layers.Dense(1, activation="relu", name="output"))
```

Expected behavior:

```text
You wanted a probability-like output for binary classification.
```

Actual behavior:

```text
`relu` is not the usual beginner choice for the final binary output, so the 
model no longer matches the intended Week 7 setup as clearly.
```

## Debug Task 2

Code:

```python
model = keras.Sequential(name="student_completion_network")
model.add(layers.Dense(8, activation="relu"))
model.summary()
```

Expected behavior:

```text
You wanted to inspect the model summary immediately.
```

Actual behavior:

```text
Without a known input shape or a first call on input data, the summary 
is less helpful because the model is not fully built yet.
```

## Hint

A clear order is:

- Start the `Sequential` model.
- Add the input shape first.
- Add the hidden layers one by one.
- Add the output layer last.
- Print the summary.
- Print the layer names.
- Test the model on a small sample batch.

## Self-Review

- I can explain when a `Sequential` model is a good fit.
- I can explain why `keras.Input(...)` is helpful.
- I can read a small `model.summary()` without guessing randomly.
- I can explain why hidden layers and output layers use different activations here.
- I can keep architecture decisions connected to the overall workflow instead of treating them as the whole task.

## Navigation

- ⬅️ Previous: [02-worked-examples.md](./02-worked-examples.md).
- 🧭 Week Overview: [week-07-overview.md](../week-07-overview.md).
- ➡️ Next: [04-challenge.md](./04-challenge.md).
