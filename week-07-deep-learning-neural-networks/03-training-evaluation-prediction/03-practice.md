# 03. Practice: Training, Evaluation, and Prediction

## Setup

1. Create a folder called `week7-training-practice`.
2. Inside it, create these folders:
   ```text
   data/
   outputs/
   scripts/
   ```
3. Reuse the same `student_completion.csv` dataset from the earlier Week 7 sections.
4. Inside `scripts/`, create `train_student_completion_network.py`.
5. Add this starter code:

```python
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers

keras.utils.set_random_seed(42)

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUTS_DIR = BASE_DIR / "outputs"

OUTPUTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_DIR / "student_completion.csv")

feature_columns = ["study_hours", "practice_sessions", "review_sessions"]
target_column = "completed_course"

X = df[feature_columns].astype("float32")
y = df[target_column].astype("float32")
```

This practice is where the Keras workflow starts to feel more complete.

The main goal is to:

- Keep training and test data separate.
- Save useful outputs.
- Read the result carefully instead of trusting one number too quickly.

## Tasks

1. Split the data with:
    - `test_size=0.25`.
    - `random_state=42`.
    - `stratify=y`.
2. Build a `Sequential` model with:
    - Input shape `(3,)`.
    - `Dense(8, activation="relu")`.
    - `Dense(4, activation="relu")`.
    - `Dense(1, activation="sigmoid")`.
3. Compile the model with:
    - `optimizer="adam"`.
    - `loss="binary_crossentropy"`.
    - `metrics=["accuracy"]`.
4. Train the model with:
    - `validation_split=0.2`.
    - `epochs=30`.
    - `verbose=0`.
5. Turn `history.history` into a DataFrame.
6. Save the history DataFrame to `outputs/training_history.csv`.
7. Create a simple loss plot from the history data and save it to `outputs/training_history_plot.png`.
8. Evaluate the model on `X_test` and `y_test`.
9. Predict probabilities for `X_test`.
10. Convert the probabilities into labels using a `0.5` threshold.
11. Build `results_df` with:
    - The test feature values.
    - `actual_completed_course`.
    - `predicted_probability`.
    - `predicted_label`.
12. Save `results_df` to `outputs/test_predictions.csv`.
13. Write 2 short sentences after the code:
    - One sentence explaining what the history plot helps you notice.
    - One sentence explaining what extra evidence you would still need before claiming this network is better than a
      simpler Week 6 baseline.
14. Print:
    - The history columns.
    - The last rows of the history DataFrame.
    - The test loss.
    - The test accuracy.
    - `results_df`.
    - The three saved-file messages.

## Expected Output Examples

Possible printed lines:

```text
Saved: outputs/training_history.csv
Saved: outputs/training_history_plot.png
Saved: outputs/test_predictions.csv
```

Possible result-table columns:

```text
study_hours
practice_sessions
review_sessions
actual_completed_course
predicted_probability
predicted_label
```

Your exact history values will vary a little. That is normal because training is not completely identical every time.

## Debug Task 1

Code:

```python
history = model.fit(
    X_test,
    y_test,
    epochs=30,
    validation_split=0.2,
    verbose=0,
)
```

Expected behavior:

```text
You wanted the test data to stay separate for honest evaluation.
```

Actual behavior:

```text
This trains on the test data instead, so you no longer have a clean final check.
```

## Debug Task 2

Code:

```python
predicted_labels = probabilities.astype(int)
```

Expected behavior:

```text
You wanted to turn probabilities into `0` or `1` labels.
```

Actual behavior:

```text
This truncates the decimal values directly, so even a probability like `0.84` becomes `0` instead of the intended
threshold-based class label.
```

## Debug Task 3

Code:

```python
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"],
)
```

Expected behavior:

```text
You wanted a clear loss for one-output binary classification.
```

Actual behavior:

```text
This loss setup does not match the intended binary workflow clearly, so the model configuration becomes confusing 
and may fail depending on the output/label shape.
```

## Hint

One clear order is:

- Split the data first.
- Build the model.
- Compile the model.
- Train it and keep the `history` object.
- Save the history table.
- Save the history plot.
- Evaluate on the test set.
- Predict probabilities.
- Convert probabilities to labels.
- Save the final prediction table.

## Self-Review

- I can explain what `compile(...)` does.
- I can explain what `fit(...)` does.
- I can explain what `evaluate(...)` does.
- I can explain what `predict(...)` gives me.
- I can turn sigmoid probabilities into labels with a clear threshold.
- I can save a simple training-history plot as useful evidence.
- I can explain what extra evidence I would need before saying this network is better than a Week 6 baseline.

## Navigation

- ⬅️ Previous: [02-worked-examples.md](./02-worked-examples.md).
- 🧭 Week Overview: [week-07-overview.md](../week-07-overview.md).
- ➡️ Next: [04-challenge.md](./04-challenge.md).
