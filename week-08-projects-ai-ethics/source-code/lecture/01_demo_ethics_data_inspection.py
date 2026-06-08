"""
Inspect data for ethical reflection

This Week 8 lecture demo is not a machine learning demo.
It does not train a model.

The goal is to show how simple data inspection can help us ask better
questions about:
- Representation.
- Sensitive columns.
- Possible bias.
- Data leakage.
- Human responsibility.

Important:
This script does not prove that a dataset is fair or unfair.
It only helps us find questions worth discussing.
"""

from pathlib import Path

import pandas as pd

# ----------------------------------------------------------------------------------------
# Path handling: reliably locate files relative to this script
# ----------------------------------------------------------------------------------------

# The dataset is large, so it is not included in this source-code folder.
# See `dataset-instructions.md` for download and placement instructions.
DATASET_FILENAME = "research_grade_type2_diabetes_dataset_v3.csv"

BASE_DIR = Path(__file__).resolve().parent


def find_dataset():
    """Find the downloaded dataset in one of the expected locations."""
    candidate_paths = [
        BASE_DIR / "data" / DATASET_FILENAME,
        BASE_DIR / DATASET_FILENAME,
        Path.cwd() / "data" / DATASET_FILENAME,
        Path.cwd() / DATASET_FILENAME,
    ]

    for path in candidate_paths:
        if path.exists():
            return path

    raise FileNotFoundError(
        f"Could not find {DATASET_FILENAME}. "
        "Download the dataset from Kaggle and place the CSV file in this "
        "folder or in this folder's data directory."
    )


def print_section(title):
    """Print readable section headers so the terminal output is easier to follow."""
    print(f"\n--- {title} ---")


# ----------------------------------------------------------------------------------------
# Step 1: Choose columns for this short ethics-focused inspection
# ----------------------------------------------------------------------------------------

# The full dataset has many columns.
# For this demo, we only load a few columns that help us discuss:
# - Who is represented in the data.
# - Which columns may be sensitive.
# - Which column could be a target.
# - Whether one feature may be too close to the target.
selected_columns = [
    "gender",
    "country",
    "age",
    "BMI",
    "risk_score",
    "future_diabetes_5yr",
]

# `future_diabetes_5yr` is a possible target.
# It contains 0 and 1 values:
# - 0 can mean "no".
# - 1 can mean "yes".
target_column = "future_diabetes_5yr"


def main():
    # ------------------------------------------------------------------------------------
    # Step 2: Load the selected columns
    # ------------------------------------------------------------------------------------

    dataset_path = find_dataset()

    print_section("Dataset source")
    print(dataset_path)

    # `pd.read_csv(...)` loads a CSV file into a DataFrame.
    #
    # `usecols=selected_columns` means:
    # - Only load these columns.
    # - Ignore the rest of the dataset.
    # - Keep the output smaller and easier to discuss.
    df = pd.read_csv(dataset_path, usecols=selected_columns)

    # ------------------------------------------------------------------------------------
    # Step 3: Check the size and preview the data
    # ------------------------------------------------------------------------------------

    # `df.shape` gives us:
    # - number of rows
    # - number of selected columns.
    print_section("Dataset shape")
    print(f"Amount of rows: {df.shape[0]}")
    print(f"Selected columns loaded: {df.shape[1]}")

    # `df.head()` shows the first five rows.
    # This helps us get a first feeling for the data before calculating anything.
    print_section("Preview of selected columns")
    print(df.head())

    # Things to notice:
    # - `future_diabetes_5yr` could be the value a model tries to predict.
    # - `gender` and `country` can help us think about representation.
    # - `risk_score` may be useful, but it may also be too close to the target.

    # ------------------------------------------------------------------------------------
    # Step 4: Check representation in the data
    # ------------------------------------------------------------------------------------

    # Representation means who or what is visible in the dataset.
    # If one group has many rows and another group has few rows, the result may be
    # more reliable for the larger group.
    #
    # `value_counts()` counts how many times each value appears.
    # `dropna=False` includes missing values in the count if they exist.
    print_section("Gender distribution")
    print(df["gender"].value_counts(dropna=False))

    # This is another representation check.
    # We only show the top 10 countries so the output stays readable.
    print_section("Top countries")
    print(df["country"].value_counts(dropna=False).head(10))

    # ------------------------------------------------------------------------------------
    # Step 5: Compare target rate by group
    # ------------------------------------------------------------------------------------

    # Target rate means the percentage of rows where the target is 1.
    #
    # Because the target contains 0 and 1 values, the mean gives us the share
    # of rows where the target is 1.
    #
    # Example:
    # - Mean 0.50 means about 50%.
    # - Mean 0.20 means about 20%.
    #
    # This does not prove bias.
    # It only gives us something to think about.
    print_section("Target rate by gender")
    target_rate_by_gender = (
        df.groupby("gender")[target_column]
        .mean()
        .mul(100)
        .round(2)
        .sort_values(ascending=False)
    )
    print(target_rate_by_gender.rename("target_rate_percent"))

    # Very small groups can give unstable percentages.
    # Sorting by row count first helps us focus on countries with more rows.
    print_section("Target rate by country, top 10 countries only")
    target_rate_by_country = (
        df.groupby("country")[target_column]
        .agg(row_count="count", target_rate="mean")
        .sort_values("row_count", ascending=False)
        .head(10)
    )

    # Turn the target rate into a percentage so it is easier to read.
    target_rate_by_country["target_rate_percent"] = (
            target_rate_by_country["target_rate"] * 100
    ).round(2)

    # Only print the columns that are useful for this discussion.
    print(target_rate_by_country[["row_count", "target_rate_percent"]])

    # ------------------------------------------------------------------------------------
    # Step 6: Think about possible data leakage
    # ------------------------------------------------------------------------------------

    # Data leakage means that a feature may contain information that almost
    # reveals the answer.
    #
    # In this dataset, `risk_score` may be useful, but we should ask:
    # - How was it created?
    # - Does it already summarize the same risk we want to predict?
    # - Would this value be available in a real situation before the prediction?
    print_section("Possible data leakage question")
    print("Could risk_score be too close to the target we want to predict?")

    # ------------------------------------------------------------------------------------
    # Step 7: End with ethical reflection questions
    # ------------------------------------------------------------------------------------

    # These questions can help connect data inspection to ethical reflection.
    print_section("Reflection questions")
    print("- Does the dataset represent all groups equally well?")
    print("- Could a result be misunderstood as medical truth?")
    print("- Should a human review the result before any serious decision?")
    print("- Could risk_score be too close to the target we want to predict?")
    print("- Should this kind of decision be automated at all?")


if __name__ == "__main__":
    main()
