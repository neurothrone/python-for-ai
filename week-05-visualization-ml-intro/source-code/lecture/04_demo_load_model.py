"""
Load a trained model and make new predictions

The previous script trained and saved a model.
This script loads that saved model and uses it on new example rows.

This is a common machine learning pattern:
- Train once.
- Save the model.
- Load the model later.
- Give the model new input.
- Read the prediction.
"""

from pathlib import Path

import joblib
import pandas as pd

# ----------------------------------------------------------------------------------------
# Path handling: reliably locate the saved model
# ----------------------------------------------------------------------------------------

# The saved model is expected to be in the lecture/models folder.
BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR / "models"

MODEL_PATH = MODELS_DIR / "music_minutes_model.joblib"

# If this file does not exist yet, run 03_demo_train_model.py first.
# That script creates the saved model file.
if not MODEL_PATH.exists():
    raise FileNotFoundError(
        "The model file was not found. Run 03_demo_train_model.py before this script."
    )

# ----------------------------------------------------------------------------------------
# Step 1: Load the saved model
# ----------------------------------------------------------------------------------------

# `joblib.load()` reads the saved model back into Python.
# After loading, we can use the model without training it again.
model = joblib.load(MODEL_PATH)

# ----------------------------------------------------------------------------------------
# Step 2: Define the same feature columns used during training
# ----------------------------------------------------------------------------------------

# The new input must use the same columns as the training data.
# The names and order should match what the model saw during training.
feature_columns = ["age", "gender"]

# ----------------------------------------------------------------------------------------
# Step 3: Create new input rows
# ----------------------------------------------------------------------------------------

# These are made-up examples.
# The values follow the same format as the training dataset:
# age is a number, and gender uses the same numeric coding as the demo data.
new_examples = pd.DataFrame(
    [
        [21, 1],  # 21-year-old female.
        [34, 0],  # 34-year-old male.
    ],
    columns=feature_columns,
)

print("--- New input rows ---")
print(new_examples)

# ----------------------------------------------------------------------------------------
# Step 4: Use the loaded model to make predictions
# ----------------------------------------------------------------------------------------

# The model returns predicted listening minutes for each new row.
predictions = model.predict(new_examples)

# ----------------------------------------------------------------------------------------
# Step 5: Put input and predictions side by side
# ----------------------------------------------------------------------------------------

# This output is easier to read because it shows the input and prediction together.
results_df = new_examples.copy()
results_df["predicted_minutes"] = predictions.round(1)

print("\n--- New predictions ---")
print(results_df)
