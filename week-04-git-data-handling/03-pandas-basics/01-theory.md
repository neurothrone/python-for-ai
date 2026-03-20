# 01. Theory: Pandas Basics

## Why This Matters

The Pandas library is often the moment when data work starts to feel real. Instead of reading one line at a time or
writing many small loops, you can load a table and understand it much faster. That makes it easier to ask useful
questions about the data and to spot problems before they grow.

This is also an important step toward future AI work. Before models, visualizations, or analysis can be trusted, the
data usually needs to be inspected, cleaned, and reshaped. The Pandas library is one of the most common tools for that
job. Learning the basic workflow now will give you a strong foundation for the rest of the course.

## The Typical Data Workflow

A typical data workflow often looks like this:

1. Load the data.
2. Inspect the data.
3. Clean the data.
4. Transform the data.
5. Save the cleaned data to a new file.

This workflow helps you stay organized and avoid confusion.

If you keep CSV files in `data/` and Python files in `scripts/`, your script needs a clear way to find the file. A
simple way to do that is to use `pathlib`.

## DataFrame in Simple Words

A DataFrame is like a table with rows and columns.

```python
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "students.csv")

print(df.head())
```

`Path(__file__).resolve().parent.parent` means "start from this script file, then go up to the project folder." That
helps if the script is inside `scripts/` and the CSV is inside `data/`.

## Series vs DataFrame

In Pandas:

- A `DataFrame` is a full table.
- A `Series` is one single column.

Example:

```python
names = df["name"]
print(type(names))
```

`df["name"]` returns a Series, not a full DataFrame. This matters because some actions work on one column and some work
on the whole table.

## Core Operations

- `pd.read_csv(DATA_DIR / "file.csv")` load a CSV from the `data/` folder.
- `df.head()` preview first rows (5 by default, change with the `n` parameter).
- `df.shape` check number of rows and columns.
- `df.info()` inspect column types and missing values quickly.
- `df.columns` check column names.
- `df["column_name"]` select one column.
- `df.loc[row_index]` select one row.
- `df.isna().sum()` count missing values.
- `df["score"] = df["score"].fillna(0)` fill simple null values.
- `df["score"] = df["score"].astype(int)` convert values to integers.
- `df.to_csv(DATA_DIR / "cleaned.csv", index=False)` save cleaned data.

## Cleaning vs. Transforming

Cleaning means fixing problems in the data.

Examples:

- Fill missing values.
- Fix wrong column names.
- Convert text numbers into numeric values.

Transforming means creating or changing data for easier use.

Examples:

- Add a new column like `total`.
- Change score values into grades.
- Combine the first name and last name into one full name.

## Why Numbers Sometimes Become Floats

If a column has missing values, Pandas may store number data as `float`. For example, after filling a missing score with
`0`, you may see `92.0` instead of `92`.

If that is not what you wanted for your data, you can convert it back:

```python
df["score"] = df["score"].fillna(0)
df["score"] = df["score"].astype(int)
```

Only convert to `int` when all values in that column should really be whole numbers.

## Best Practice: Keep the Raw File Safe

Do not overwrite the raw input file while learning. It is safer to save cleaned data to a new file such as
`students_cleaned.csv`. This makes it easier to compare before and after.

## Keep It Simple This Week

We focus only on:

- Loading one CSV.
- Inspecting shape, columns, and simple types.
- Selecting simple rows and columns.
- Handling missing values with one basic rule.
- Doing one or two simple transformations.
- Saving cleaned data to a new file.

## Common Beginner Mistakes

- Typo in column name (`"Score"` vs `"score"`).
- Forgetting to import pandas as `pd`.
- Treating text numbers like real numbers.
- Confusion between null (`NaN`) and empty strings.
- Forgetting that one selected column is a Series, not a full DataFrame.
- Overwriting the raw file by mistake.
- Forgetting that filling null values can change integer columns into floats.

## Navigation

- ⬅️ Previous: [05-reflection.md](../02-files-csv-json/05-reflection.md).
- 🧭 Week Overview: [week-04-overview.md](../week-04-overview.md).
- ➡️ Next: [02-worked-examples.md](./02-worked-examples.md).
