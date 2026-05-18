"""
Train a first machine learning model

This script connects the normal data workflow with a first machine learning workflow:
- Load data.
- Inspect data.
- Clean data if needed.
- Visualize before modeling.
- Choose features and the target.
- Split data into training data and test data.
- Train a Linear Regression model.
- Make predictions.
- Save the model and prediction output.

This is a small learning example, not a strong real-world model.
The important part is the workflow and the vocabulary.
"""

from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# ----------------------------------------------------------------------------------------
# Data display settings: improve readability when printing DataFrames
# ----------------------------------------------------------------------------------------

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)

# ----------------------------------------------------------------------------------------
# Path handling: reliably locate files relative to this script
# ----------------------------------------------------------------------------------------

# The script lives in the lecture folder.
# Keeping data, model files, and outputs beside the lecture scripts makes this folder
# easier to move, share, or expand later.
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"
OUTPUTS_DIR = BASE_DIR / "outputs"

# Create folders if they do not already exist.
MODELS_DIR.mkdir(exist_ok=True)
OUTPUTS_DIR.mkdir(exist_ok=True)

# ----------------------------------------------------------------------------------------
# Step 1: Load the dataset
# ----------------------------------------------------------------------------------------

# Load the CSV file into a pandas DataFrame.
df = pd.read_csv(DATA_DIR / "music_regression_data.csv")

print("--- Data preview ---")
print(df.head())

print("\n--- Columns ---")
print(df.columns.tolist())

print("\n--- Shape ---")
print(df.shape)

# ----------------------------------------------------------------------------------------
# Step 2: Clean data if needed
# ----------------------------------------------------------------------------------------

# This small demo dataset is already clean, so we do not change anything here.
# In a real dataset, this step could include missing values, wrong data types,
# duplicate rows, or text values that need to be converted.
# ...

# ----------------------------------------------------------------------------------------
# Step 3: Visualize the data before modeling
# ----------------------------------------------------------------------------------------

# Visualization helps us check whether the model idea makes sense before we train anything.
# Here we ask a simple question: do age and listening minutes seem related?
sns.set_theme(style="whitegrid")

# The model later uses the numeric gender column.
# For the plot, text labels are easier to read than 0 and 1.
plot_df = df.copy()
plot_df["gender_label"] = plot_df["gender"].map(
    {
        0: "Male",
        1: "Female",
    }
)

fig, ax = plt.subplots(figsize=(8, 4))

# A scatter plot shows each row as one point.
# This is often a useful first plot before machine learning.
sns.scatterplot(
    data=plot_df,
    x="age",
    y="minutes_listened",
    hue="gender_label",
    s=90,
    ax=ax,
)

ax.set_title("Age and Listening Minutes")
ax.set_xlabel("Age")
ax.set_ylabel("Minutes Listened")

plt.tight_layout()
fig.savefig(OUTPUTS_DIR / "demo_train_model_visualization.png")
plt.show()
plt.close(fig)

# ----------------------------------------------------------------------------------------
# Machine learning workflow
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# Step 4: Choose input columns (features) and the output column (target)
# ----------------------------------------------------------------------------------------

# Features are the input columns the model is allowed to look at.
# In this example, the model can look at age and gender.
feature_columns = ["age", "gender"]

# The target is the value we want the model to predict.
# In this example, we want to predict listening minutes.
target_column = "minutes_listened"

# `X` is commonly used for the feature table in machine learning examples.
# It is uppercase because it can contain many columns.
X = df[feature_columns]

# `y` is commonly used for the target column.
# It is lowercase because it is often one column of values.
y = df[target_column]

print("\n--- Features and target ---")
print(f"Features: {feature_columns}")
print(f"Target: {target_column}")

# ----------------------------------------------------------------------------------------
# Step 5: Split data into training and test sets
# ----------------------------------------------------------------------------------------

# Training data is used to teach the model.
# Test data is used afterward for a more honest first check.
X_train, X_test, y_train, y_test = train_test_split(
    X,  # The input columns.
    y,  # The target column.
    test_size=0.25,  # Use 25% of the rows for testing and 75% for training.
    random_state=42,  # Keeps the split reproducible so we get the same result each run.
)

print("\n--- Train/test sizes ---")
print(f"Training rows: {len(X_train)}")
print(f"Test rows: {len(X_test)}")

# `random_state=42` is not special for the model.
# It is just a common example number used in programming culture.
# We could use another number, but then the train/test split may be different.

# ----------------------------------------------------------------------------------------
# Step 6: Create the model
# ----------------------------------------------------------------------------------------

# Linear Regression tries to learn a straight-line relationship between inputs and output.
# It is a good first model because the idea is easier to understand than many other models.
model = LinearRegression()

# ----------------------------------------------------------------------------------------
# Step 7: Train the model with the training data
# ----------------------------------------------------------------------------------------

# `fit` means that the model learns a pattern from the training data.
model.fit(X_train, y_train)

# ----------------------------------------------------------------------------------------
# Step 8: Make predictions for the test rows
# ----------------------------------------------------------------------------------------

# `predict` means that the model uses the learned pattern on input data.
predictions = model.predict(X_test)

# Put the input rows, real answers, and predictions side by side.
# This makes the result easier to read than printing only raw arrays.
results_df = X_test.copy()
results_df["actual_minutes"] = y_test.values
results_df["predicted_minutes"] = predictions.round(1)
results_df["difference"] = (
        results_df["predicted_minutes"] - results_df["actual_minutes"]
).round(1)

print("\n--- Predictions vs actual values ---")
print(results_df)

# ----------------------------------------------------------------------------------------
# Step 9: Save outputs and the trained model
# ----------------------------------------------------------------------------------------

# Save the prediction table so it can be inspected later.
results_df.to_csv(OUTPUTS_DIR / "music_minutes_predictions.csv", index=False)

# Save the trained model so another script can load it without training again.
joblib.dump(model, MODELS_DIR / "music_minutes_model.joblib")
