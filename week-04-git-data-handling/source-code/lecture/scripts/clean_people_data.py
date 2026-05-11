"""
Data Cleaning and Transformation with pandas

A data workflow is a common process in data analysis and machine learning projects. It
involves several steps that are typically performed in sequence to prepare the data
for analysis or modeling. The main steps in a typical data workflow include:
- Load
- Inspect
- Clean
- Transform
- Save

This script demonstrates how to clean and transform a dataset using pandas. It includes
steps for loading the data, inspecting it to understand its structure and quality,
cleaning the data by fixing issues like missing values and duplicates, transforming the
data to create new features or modify existing ones, and finally saving the cleaned and
transformed data to a new file for further analysis or sharing.
"""

from pathlib import Path

import pandas as pd

# ----------------------------------------------------------------------------------------
# Data display settings: improve readability when printing DataFrames
# ----------------------------------------------------------------------------------------

# Shows all columns instead of truncating them with `...` when printing a DataFrame.
pd.set_option("display.max_columns", None)

# Prevents pandas from wrapping columns awkwardly when printing.
pd.set_option("display.width", 1000)

# ----------------------------------------------------------------------------------------
# Path handling: reliably locate files relative to the script
# ----------------------------------------------------------------------------------------

# - `Path(__file__)` gives the path to the current file (clean_people_data.py).
# - The `resolve()` method gives the absolute path, which is useful for reliably locating
#   files relative to the script, regardless of where the script is run from.
# - The `parent` attribute gives the directory containing the file, which is useful for
#   navigating to other directories like data and outputs.
# - By using `Path(__file__).resolve().parent.parent` we can reliably locate the base directory
#   of the project, which allows us to construct paths to the data and outputs directories
#   in a way that works regardless of the current working directory when running the script.

# Path(__file__).resolve()  # .../lecture/scripts/clean_people_data.py
# Path(__file__).resolve().parent  # .../lecture/scripts
# Path(__file__).resolve().parent.parent  # .../lecture

BASE_DIR = Path(__file__).resolve().parent.parent  # .../lecture
DATA_DIR = BASE_DIR / "data"  # .../lecture/data
OUTPUTS_DIR = BASE_DIR / "outputs"  # .../lecture/outputs

# Create outputs directory if it doesn't exist
OUTPUTS_DIR.mkdir(exist_ok=True)

# ----------------------------------------------------------------------------------------
# Step 1: Load data
# ----------------------------------------------------------------------------------------

# Read the CSV file into a pandas' DataFrame
df = pd.read_csv(DATA_DIR / "people_raw.csv")

# ----------------------------------------------------------------------------------------
# Step 2: Inspect data
# ----------------------------------------------------------------------------------------
# - When working with data we rarely look at every row. Instead we inspect the dataset
#   using tools like head(), sample(), and describe() to quickly understand the data.

# View first rows
print("--- df.head() ---")
print(df.head())

# View random rows
# - Instead of always showing the first rows, show random rows and explore data much
#   more like analysts do in real life
print("\n--- df.sample(5) ---")
print(df.sample(5))

# Show dataset size
print("\n--- Dataset size (rows, columns) ---")
print(df.shape)

# Show column names and types
print("\n--- df.columns ---")
print(df.columns)

# Show data types of each column
print("\n--- df.dtypes ---")
print(df.dtypes)

# Inspect structure and column types
print("\n--- df.info() ---")
print(df.info())

# Show summary statistics
# - Extremely useful inspection tool that shows count, mean, std, min, 25%, 50%, 75%,
#   max for each numeric column.
# - Only works for numeric columns, so it will ignore text columns like names and cities.
print("\n--- df.describe() ---")
print(df.describe())

# Count missing values in each column
print("\n--- Missing values in each column ---")
print(df.isna().sum())

# Detect duplicate rows (excluding id)
print("\n--- Duplicate rows based on first name, last name, age, and city ---")
duplicates = df.duplicated(subset=["first_name", "last_name", "age", "city"])
print(df[duplicates])

# ----------------------------------------------------------------------------------------
# Step 3: Clean data
# ----------------------------------------------------------------------------------------

# Remove extra whitespace from names
df["first_name"] = df["first_name"].str.strip()
df["last_name"] = df["last_name"].str.strip()

# Standardize name formatting
# - The `str.capitalize()` method capitalizes only the first letter of the string and
#   makes the rest lowercase.
df["first_name"] = df["first_name"].str.capitalize()

# Standardize city formatting
# - The `str.title()` method capitalizes the first letter of each word and makes the
#   rest lowercase.
df["city"] = df["city"].str.strip().str.title()

# Convert columns to numeric values
# - The `pd.to_numeric()` function is used to convert a column to numeric values. If there
#   are any values that cannot be converted to numbers (like "unknown" or "N/A"), they will
#   be replaced with NaN (Not a Number) when `errors="coerce"` is used. This allows us to
#   handle invalid data gracefully without crashing the program.
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["score"] = pd.to_numeric(df["score"], errors="coerce")

# Fill missing numeric values with the median
# - This is often a better approach than filling with 0, especially if 0 is not a meaningful
#   value for the column. The median is less affected by outliers than the mean.
# - The method `.astype(int)` converts the column to an integer type after filling missing
#   values. This is important if the original column is supposed to be integers (like ages),
#   but filling with the median can result in a float.
df["age"] = df["age"].fillna(df["age"].median()).astype(int)

# Fill missing scores with 0 and convert to integer
# - In this case, filling missing scores with 0 might make sense if a missing score indicates
#   that the person did not take the test or scored 0. However, this depends on the context
#   of the data and should be considered carefully.
df["score"] = df["score"].fillna(0).astype(int)

# Remove duplicate rows based on first name, last name, age, and city
# - The `drop_duplicates()` method removes duplicate rows from the DataFrame. By specifying
#   the `subset` parameter, we tell pandas to consider only the specified columns when
#   identifying duplicates. This way, if there are multiple rows with the same first name,
#   last name, age, and city, only the first occurrence will be kept, and the others will
#   be removed. This is important for cleaning the data and ensuring that we have unique
#   records for each person based on these key attributes.
df = df.drop_duplicates(subset=["first_name", "last_name", "age", "city"])

# ----------------------------------------------------------------------------------------
# Step 4: Transform data
# ----------------------------------------------------------------------------------------
# - Cleaning fixes problems in the data. Transforming creates new information
#   from the data.
# - The transformations below are just examples. In real life, the transformations you
#   create will depend on the specific questions you want to answer with the data.
# - For example, if you want to analyze how age affects test scores, you might create a new
#   column that categorizes people into age groups (e.g., "child", "adult", "senior") based
#   on their age. Or if you want to analyze the relationship between city and test scores,
#   you might create a new column that indicates whether the city is a large metropolitan
#   area or a small town based on the city name.

# Create a new column combining first and last names
df["full_name"] = df["first_name"] + " " + df["last_name"]

# Examples of numeric transformations
df["age_next_year"] = df["age"] + 1
df["score_bonus"] = df["score"] + 5

# Create a new boolean column indicating if the person passed a test (score > 75)
df["passed_test"] = df["score"] > 75

# Convert comma-separated foods into a list
df["favorite_food_list"] = df["favorite_foods"].str.split(",")

# Remove a column which is not needed for analysis
df = df.drop(columns=["id"])

# ----------------------------------------------------------------------------------------
# Step 5: Save cleaned data
# ----------------------------------------------------------------------------------------

# Export the cleaned dataset to a new CSV file
# - The `index=False` argument prevents pandas from writing the row index to the CSV file,
#   which is usually not needed and can be confusing if it appears as an extra column
#   in the output.
# - By saving the cleaned data to a new file, we can keep the original raw data intact and
#   have a clear record of the cleaning and transformation steps we applied to the data.
# - This also allows us to easily share the cleaned data with others or use it for further
#   analysis without having to repeat the cleaning steps.
df.to_csv(OUTPUTS_DIR / "people_cleaned.csv", index=False)

# Show the cleaned result
print("\n--- Cleaned and transformed DataFrame ---")
print(df.head())

# Show data types of each column after cleaning and transformation
print("\n--- Data types after cleaning and transformation ---")
print(df.dtypes)
