# 02. Worked Examples: Integration

## Example A: Create the Folder Structure

Create this structure:

```text
week7-keras-integration-demo/
  data/
    student_completion.csv
  outputs/
  scripts/
    run_keras_classification_workflow.py
```

Use the same `student_completion.csv` dataset from the previous Week 7 sections.

This is an optional extension workflow, not a signal that every task should switch to Keras. In a longer workflow, a
simple Week 6 baseline is still a sensible normal starting point.

## Example B: Start the Full Script

Create `scripts/run_keras_classification_workflow.py` with this code:

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

## Example C: Build, Compile, and Train

Add this:

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

history = model.fit(
    X_train,
    y_train,
    epochs=30,
    validation_split=0.2,
    verbose=0,
)
```

## Example D: Save the Training History, History Plot, and Model Summary

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

summary_lines = []
model.summary(print_fn=summary_lines.append)

with open(OUTPUTS_DIR / "model_summary.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(summary_lines))

print("\n--- Saved files ---")
print("Saved: outputs/training_history.csv")
print("Saved: outputs/training_history_plot.png")
print("Saved: outputs/model_summary.txt")
```

Why save these files?

- The history CSV records how training changed over time.
- The history plot gives one meaningful visualization for the workflow.
- The model summary records the architecture you actually trained.
- Together, they make the workflow easier to review later.

## Example E: Save the Test Prediction Table

Add this:

```python
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)

probabilities = model.predict(X_test, verbose=0).flatten()
predicted_labels = (probabilities >= 0.5).astype(int)

test_results_df = X_test.copy()
test_results_df["actual_completed_course"] = y_test.values
test_results_df["predicted_probability"] = probabilities.round(3)
test_results_df["predicted_label"] = predicted_labels

test_results_df.to_csv(OUTPUTS_DIR / "test_predictions.csv", index=False)

print("\n--- Test metrics ---")
print("Test loss:", round(float(test_loss), 3))
print("Test accuracy:", round(float(test_accuracy), 3))

print("\n--- Test predictions ---")
print(test_results_df)

print("\n--- Saved files ---")
print("Saved: outputs/test_predictions.csv")
```

## Example F: Predict New Cases

Add this:

```python
new_cases = pd.DataFrame(
    {
        "study_hours": [2, 5, 7],
        "practice_sessions": [1, 3, 4],
        "review_sessions": [1, 4, 5],
    }
).astype("float32")

new_probabilities = model.predict(new_cases, verbose=0).flatten()
new_labels = (new_probabilities >= 0.5).astype(int)

new_cases_df = new_cases.copy()
new_cases_df["predicted_probability"] = new_probabilities.round(3)
new_cases_df["predicted_label"] = new_labels

new_cases_df.to_csv(OUTPUTS_DIR / "new_case_predictions.csv", index=False)

print("\n--- New-case predictions ---")
print(new_cases_df)

print("\n--- Saved files ---")
print("Saved: outputs/new_case_predictions.csv")
```

This is a useful final step because it makes the model feel like a complete workflow:

- Train on known rows.
- Evaluate on held-out rows.
- Predict on new rows.

## Example G: A Careful Interpretation

One careful interpretation could sound like this:

- The small neural network produced useful predictions on this dataset.
- The saved outputs make the workflow easier to explain and review.
- This is a working deep learning workflow, but a simpler Week 6 model could still be a valid baseline option.
- Before claiming Keras is better, you would still want a fair comparison with that simpler baseline.

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

# Step 5: Build, compile, and train the model.
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

history = model.fit(
    X_train,
    y_train,
    epochs=30,
    validation_split=0.2,
    verbose=0,
)

# Step 6: Save the training history, plot, and model summary.
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

summary_lines = []
model.summary(print_fn=summary_lines.append)

with open(OUTPUTS_DIR / "model_summary.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(summary_lines))

print("\n--- Saved files ---")
print("Saved: outputs/training_history.csv")
print("Saved: outputs/training_history_plot.png")
print("Saved: outputs/model_summary.txt")

# Step 7: Evaluate on the test set and save test predictions.
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)

probabilities = model.predict(X_test, verbose=0).flatten()
predicted_labels = (probabilities >= 0.5).astype(int)

test_results_df = X_test.copy()
test_results_df["actual_completed_course"] = y_test.values
test_results_df["predicted_probability"] = probabilities.round(3)
test_results_df["predicted_label"] = predicted_labels

test_results_df.to_csv(OUTPUTS_DIR / "test_predictions.csv", index=False)

print("\n--- Test metrics ---")
print("Test loss:", round(float(test_loss), 3))
print("Test accuracy:", round(float(test_accuracy), 3))

print("\n--- Test predictions ---")
print(test_results_df)

print("\n--- Saved files ---")
print("Saved: outputs/test_predictions.csv")

# Step 8: Predict new cases and save the result.
new_cases = pd.DataFrame(
    {
        "study_hours": [2, 5, 7],
        "practice_sessions": [1, 3, 4],
        "review_sessions": [1, 4, 5],
    }
).astype("float32")

new_probabilities = model.predict(new_cases, verbose=0).flatten()
new_labels = (new_probabilities >= 0.5).astype(int)

new_cases_df = new_cases.copy()
new_cases_df["predicted_probability"] = new_probabilities.round(3)
new_cases_df["predicted_label"] = new_labels

new_cases_df.to_csv(OUTPUTS_DIR / "new_case_predictions.csv", index=False)

print("\n--- New-case predictions ---")
print(new_cases_df)

print("\n--- Saved files ---")
print("Saved: outputs/new_case_predictions.csv")
```

## Navigation

- ⬅️ Previous: [01-theory.md](./01-theory.md).
- 🧭 Week Overview: [week-07-overview.md](../week-07-overview.md).
- ➡️ Next: [03-practice.md](./03-practice.md).
