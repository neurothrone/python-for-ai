# 02. Worked Examples: Pandas Basics

## Example A: Create the CSV, Then Load and Preview

Create this structure:

```text
week4-pandas-demo/
  data/
    students.csv
  scripts/
    inspect_students.py
```

Create `data/students.csv` with this content:

```text
name,score,city
Ana,92,Stockholm
Bo,,Gothenburg
Lia,78,Malmo
Noa,74,Uppsala
```

Then create `scripts/inspect_students.py` and load it:

```python
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "students.csv")

print(df.head())
print(df.columns)
print(df.shape)
```

We use `pathlib` here because the script is inside `scripts/`, while the CSV is inside `data/`.

## Example B: Inspect Types with `info()`

```python
df.info()
```

This helps you see row count, column names, and data types.

## Example C: Select a Column and Row

```python
name_series = df["name"]  # Select the "name" column
print(name_series)
print(type(name_series))  # <class 'pandas.Series'>

print(df.loc[0])  # Select the first row
print(df.loc[0, "name"])  # Select the first row's "name" value
print(type(df.loc[0]))  # <class 'pandas.Series'>
```

- `df["name"]` returns a Series. A Series is one column of data.
- `df.loc[0]` also returns a Series, but this time it represents one full row.
- `df.loc[0, "name"]` returns one single value, not a Series or DataFrame.

## Example D: Simple Null Check

```python
print(df.isna().sum())
```

Possible output:

```text
name     0
score    1
city     0
dtype: int64
```

This shows how many missing values each column has. It is a good early check because you can quickly see where cleaning
is needed.

## Example E: Clean and Convert Type

```python
df["score"] = df["score"].fillna(0)
df["score"] = df["score"].astype(int)
print(df)
```

- `fillna(0)` replaces missing scores with `0`.
- After that, Pandas may still keep the column as float because missing values were involved earlier.
- `astype(int)` changes values like `92.0` back to `92` when whole numbers are the correct type for that column.

## Example F: Transform with a New Column

```python
df["passed"] = df["score"] >= 75
print(df[["name", "score", "passed"]])
```

This is a simple transformation. We create a new column from existing data. This is useful because transformed columns
can make the table easier to understand and use later.

## Example G: Save to a New File

```python
df.to_csv(DATA_DIR / "students_cleaned.csv", index=False)
```

- Save to a new file so the raw file stays unchanged. This makes it easier to compare the original data with the cleaned
  version.
- The `index=False` keyword argument means Pandas will not save the row numbers as an extra column.

## Navigation

- ⬅️ Previous: [01-theory.md](./01-theory.md).
- 🧭 Week Overview: [week-04-overview.md](../week-04-overview.md).
- ➡️ Next: [03-practice.md](./03-practice.md).
