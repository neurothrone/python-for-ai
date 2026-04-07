# 02. Worked Examples: Training, Evaluation, and Prediction

## Example A: Create the Folder Structure

Create this structure:

```text
week7-training-demo/
  data/
    student_completion.csv
  outputs/
  scripts/
    train_student_completion_network.py
```

Use the same `student_completion.csv` dataset from the earlier Week 7 sections.

## Example B: Load the Data and Split It

Create `scripts/train_student_completion_network.py` with this code:

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

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y,
)
```

We use `set_random_seed(42)` here so the training behavior is easier to reproduce while learning.

This example still follows the same workflow logic from Week 6:

- Keep one clear question.
- Split the data honestly.
- Train one small model.
- Save evidence you can explain later.

## Example C: Build and Compile the Model

Now add this:

```python
model = keras.Sequential(
    [
        keras.Input(shape=(len(feature_columns),)),
        layers.Dense(8, activation="relu"),
        layers.Dense(4, activation="relu"),
        layers.Dense(1, activation="sigmoid"),
    ],
    name="student_completion_network",
)

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"],
)
```

This setup is a good pattern:

- `adam` is a common optimizer.
- `binary_crossentropy` matches binary classification clearly.
- `accuracy` gives a readable first metric.

## Example D: Train the Model

Add this:

```python
history = model.fit(
    X_train,
    y_train,
    epochs=30,
    validation_split=0.2,
    verbose=0,
)
```

Even with `verbose=0`, the model still trains. We use quiet output here, so it is easier to focus on the saved results.

## Example E: Save and Visualize the Training History

Add this:

```python
history_df = pd.DataFrame(history.history)
history_df.to_csv(OUTPUTS_DIR / "training_history.csv", index=False)

plt.figure(figsize=(8, 4))
plt.plot(history_df["loss"], label="train_loss")
plt.plot(history_df["val_loss"], label="val_loss")
plt.title("Training and Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.tight_layout()
plt.savefig(OUTPUTS_DIR / "training_history_plot.png")
plt.close()

print("\n--- History columns ---")
print(list(history_df.columns))

print("\n--- history_df.tail() ---")
print(history_df.tail())

print("\n--- Saved files ---")
print("Saved: outputs/training_history.csv")
print("Saved: outputs/training_history_plot.png")
```

You should now have a history table with columns such as:

- `loss`.
- `accuracy`.
- `val_loss`.
- `val_accuracy`.

The plot is useful because Week 7 should still connect to the visualization habit from Week 5. If you keep exploring
Keras, a simple history plot is one good piece of saved evidence.

## Example F: Evaluate on the Test Set

Add this:

```python
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)

print("\n--- Test metrics ---")
print("Test loss:", round(float(test_loss), 3))
print("Test accuracy:", round(float(test_accuracy), 3))
```

This gives you an honest check on rows the model did not train on.

## Example G: Predict Probabilities and Labels

Add this:

```python
probabilities = model.predict(X_test, verbose=0).flatten()
predicted_labels = (probabilities >= 0.5).astype(int)

results_df = X_test.copy()
results_df["actual_completed_course"] = y_test.values
results_df["predicted_probability"] = probabilities.round(3)
results_df["predicted_label"] = predicted_labels

results_df.to_csv(OUTPUTS_DIR / "test_predictions.csv", index=False)

print("\n--- Test predictions ---")
print(results_df)

print("\n--- Saved files ---")
print("Saved: outputs/test_predictions.csv")
```

Why save both probability and label?

- The probability gives a richer view of the model output.
- The label gives the final class decision.

## Example H: Read the Result Carefully

A short, careful interpretation could sound like this:

- The model learned a useful pattern on this small dataset.
- The test accuracy gives one honest check.
- The saved history shows how the training and validation values changed over time.
- This still does not prove that a neural network is always the best choice for the problem.
- Before making a stronger claim, you would want to compare it with a simpler Week 6 baseline.

## Full Script

If you want to see the whole file in one place, here is one clear version with comment headers:

```python
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers

keras.utils.set_random_seed(42)

# Step 1: Define folder paths.
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUTS_DIR = BASE_DIR / "outputs"

OUTPUTS_DIR.mkdir(exist_ok=True)

# Step 2: Load the dataset.
df = pd.read_csv(DATA_DIR / "student_completion.csv")

# Step 3: Define features and target.
feature_columns = ["study_hours", "practice_sessions", "review_sessions"]
target_column = "completed_course"

X = df[feature_columns].astype("float32")
y = df[target_column].astype("float32")

# Step 4: Split the data.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y,
)

# Step 5: Build and compile the model.
model = keras.Sequential(
    [
        keras.Input(shape=(len(feature_columns),)),
        layers.Dense(8, activation="relu"),
        layers.Dense(4, activation="relu"),
        layers.Dense(1, activation="sigmoid"),
    ],
    name="student_completion_network",
)

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"],
)

# Step 6: Train the model.
history = model.fit(
    X_train,
    y_train,
    validation_split=0.2,
    epochs=30,
    verbose=0,
)

# Step 7: Save the training history and loss plot.
history_df = pd.DataFrame(history.history)
history_df.to_csv(OUTPUTS_DIR / "training_history.csv", index=False)

plt.figure(figsize=(8, 4))
plt.plot(history_df["loss"], label="train_loss")
plt.plot(history_df["val_loss"], label="val_loss")
plt.title("Training and Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.tight_layout()
plt.savefig(OUTPUTS_DIR / "training_history_plot.png")
plt.close()

print("\n--- History columns ---")
print(list(history_df.columns))

print("\n--- history_df.tail() ---")
print(history_df.tail())

print("\n--- Saved files ---")
print("Saved: outputs/training_history.csv")
print("Saved: outputs/training_history_plot.png")

# Step 8: Evaluate on the test set.
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)

print("\n--- Test metrics ---")
print("Test loss:", round(float(test_loss), 3))
print("Test accuracy:", round(float(test_accuracy), 3))

# Step 9: Predict probabilities and labels.
probabilities = model.predict(X_test, verbose=0).flatten()
predicted_labels = (probabilities >= 0.5).astype(int)

results_df = X_test.copy()
results_df["actual_completed_course"] = y_test.values
results_df["predicted_probability"] = probabilities.round(3)
results_df["predicted_label"] = predicted_labels

results_df.to_csv(OUTPUTS_DIR / "test_predictions.csv", index=False)

print("\n--- Test predictions ---")
print(results_df)

print("\n--- Saved files ---")
print("Saved: outputs/test_predictions.csv")
```

## Navigation

- ⬅️ Previous: [01-theory.md](./01-theory.md).
- 🧭 Week Overview: [week-07-overview.md](../week-07-overview.md).
- ➡️ Next: [03-practice.md](./03-practice.md).
