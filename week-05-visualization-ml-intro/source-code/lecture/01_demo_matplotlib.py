"""
First plots with Matplotlib

This script shows a simple visualization workflow:
- Load a small dataset.
- Inspect it briefly.
- Make a quick plot.
- Make a more controlled plot with `fig` and `ax`.
- Save plots as image files.

The goal is not to make a perfect chart. The goal is to understand the pattern:
choose data -> create a plot -> add labels -> save the result.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# ----------------------------------------------------------------------------------------
# Path handling: reliably locate files relative to this script
# ----------------------------------------------------------------------------------------

# `Path(__file__)` means "the path to this Python file".
# `.resolve()` gives the full absolute path.
# `.parent` gives the folder containing this file, which is the lecture folder.
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUTS_DIR = BASE_DIR / "outputs"

# Create the outputs folder if it does not already exist.
OUTPUTS_DIR.mkdir(exist_ok=True)

# ----------------------------------------------------------------------------------------
# Step 1: Load and inspect the data
# ----------------------------------------------------------------------------------------

# A DataFrame is a table-like object from pandas.
# It has rows and columns, similar to a spreadsheet.
df = pd.read_csv(DATA_DIR / "music_regression_data.csv")

print("--- Data preview ---")
print(df.head())

print("\n--- Columns ---")
print(df.columns.tolist())

# ----------------------------------------------------------------------------------------
# Step 2: Choose values for the x-axis and y-axis
# ----------------------------------------------------------------------------------------

# For this plot we want to compare age with listening minutes.
# The x-axis usually shows the value we compare from.
# The y-axis usually shows the value we want to understand.
ages = df["age"]
minutes = df["minutes_listened"]

# ----------------------------------------------------------------------------------------
# Step 3: Make the quickest possible line plot
# ----------------------------------------------------------------------------------------

# `plt.plot()` is a fast way to draw a line plot.
# It is useful when we want to quickly check what the data looks like.
plt.plot(ages, minutes)

# A plot should have a title and axis labels so that another person can understand it.
plt.title("Quick Plot: Age and Listening Minutes")
plt.xlabel("Age")
plt.ylabel("Minutes Listened")

plt.show()

# Close the current figure after showing it.
# This prevents plots from mixing together later in the script.
plt.close()

# ----------------------------------------------------------------------------------------
# Step 4: Use the recommended `fig, ax` pattern
# ----------------------------------------------------------------------------------------

# `fig` means the whole figure.
# `ax` means the plotting area inside the figure.
# This style gives us more control, especially when we make several plots.
fig, ax = plt.subplots(figsize=(8, 4))

# `marker="o"` adds a small circle for each data point.
# This helps us see the individual rows behind the line.
ax.plot(ages, minutes, marker="o")

ax.set_title("Controlled Plot: Age and Listening Minutes")
ax.set_xlabel("Age")
ax.set_ylabel("Minutes Listened")

# `tight_layout()` helps prevent titles and labels from being cut off.
plt.tight_layout()

# Save the plot so it can be used later in a report, README, or presentation.
fig.savefig(OUTPUTS_DIR / "demo_matplotlib_line_plot.png")
plt.show()
plt.close(fig)

# ----------------------------------------------------------------------------------------
# Step 5: Show two plots side by side
# ----------------------------------------------------------------------------------------

# This creates one figure with 1 row and 2 columns of plots.
# `axes` contain the two plotting areas.
fig, axes = plt.subplots(1, 2, figsize=(11, 4))

# A line plot connects the points.
# This can be useful for ordered values, but it can also suggest a stronger connection
# than the data really supports.
axes[0].plot(ages, minutes, marker="o")
axes[0].set_title("Line Plot")
axes[0].set_xlabel("Age")
axes[0].set_ylabel("Minutes")

# A scatter plot shows each row as a separate point.
# For many machine learning datasets, this is often a good first visualization.
axes[1].scatter(ages, minutes)
axes[1].set_title("Scatter Plot")
axes[1].set_xlabel("Age")
axes[1].set_ylabel("Minutes")

plt.tight_layout()
fig.savefig(OUTPUTS_DIR / "demo_matplotlib_two_plots.png")
plt.show()
plt.close(fig)
