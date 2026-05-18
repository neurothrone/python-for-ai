"""
First plots with Seaborn

Seaborn is a visualization library that works well with pandas DataFrames.
It uses Matplotlib underneath but often needs less code for common data plots.

This script shows how to:
- Load a small dataset.
- Add a clearer label column for plotting.
- Make a scatter plot with color groups.
- Add a simple trend line.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# ----------------------------------------------------------------------------------------
# Path handling: reliably locate files relative to this script
# ----------------------------------------------------------------------------------------

# The script lives in the lecture folder, so BASE_DIR points there.
# This keeps the data and outputs paths correct even if we run the script from another
# working directory.
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUTS_DIR = BASE_DIR / "outputs"

OUTPUTS_DIR.mkdir(exist_ok=True)

# ----------------------------------------------------------------------------------------
# Step 1: Load the dataset
# ----------------------------------------------------------------------------------------

df = pd.read_csv(DATA_DIR / "music_regression_data.csv")

# ----------------------------------------------------------------------------------------
# Step 2: Add a helper column for clearer plotting
# ----------------------------------------------------------------------------------------

# In this small demo dataset, gender is stored as numbers:
# 0 = Male and 1 = Female.
# These numbers are fine for code, but text labels are easier to read in a plot.
# This mapping belongs to this dataset only. Other datasets may use other values.
df["gender_label"] = df["gender"].map(
    {
        0: "Male",
        1: "Female",
    }
)

print("--- Data preview ---")
print(df.head())

print("\n--- Columns ---")
print(df.columns.tolist())

print("\n--- Gender labels ---")
print(df["gender_label"].value_counts())

# ----------------------------------------------------------------------------------------
# Step 3: Set a Seaborn theme
# ----------------------------------------------------------------------------------------

# A theme changes the default style of the plots.
# `whitegrid` adds a light grid, which can make values easier to compare.
sns.set_theme(style="whitegrid")

# ----------------------------------------------------------------------------------------
# Step 4: Create a scatter plot with one extra visual dimension
# ----------------------------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(8, 4))

# `data=df` tells Seaborn which DataFrame to use.
# `x` and `y` choose the columns for the axes.
# `hue` adds color based on another column.
# Here, color helps us compare the two groups without creating two separate plots.
sns.scatterplot(
    data=df,
    x="age",
    y="minutes_listened",
    hue="gender_label",
    s=90,  # Point size.
    ax=ax,  # Draw on this Matplotlib axis.
)

ax.set_title("Age and Listening Minutes by Group")
ax.set_xlabel("Age")
ax.set_ylabel("Minutes Listened")

plt.tight_layout()
fig.savefig(OUTPUTS_DIR / "demo_seaborn_scatter_by_group.png")
plt.show()
plt.close(fig)

# ----------------------------------------------------------------------------------------
# Step 5: Add a simple trend line
# ----------------------------------------------------------------------------------------

# A trend line can help us see the general direction in the data.
# It does not prove that age causes listening minutes to increase.
# It is only the first visual clue.
fig, ax = plt.subplots(figsize=(8, 4))

sns.regplot(
    data=df,
    x="age",
    y="minutes_listened",
    scatter_kws={"s": 80},  # Settings for the dots.
    line_kws={"color": "darkred"},  # Settings for the trend line.
    ax=ax,
)

ax.set_title("Simple Trend: Age and Listening Minutes")
ax.set_xlabel("Age")
ax.set_ylabel("Minutes Listened")

plt.tight_layout()
fig.savefig(OUTPUTS_DIR / "demo_seaborn_regression_trend.png")
plt.show()
plt.close(fig)
