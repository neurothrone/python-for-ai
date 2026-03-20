# 03. Practice: Pandas Basics

## Setup

1. Create a folder called `week4-pandas-practice`.
2. Inside it, create these folders:
   ```text
   data/
   scripts/
   ```
3. Create `data/students_pandas.csv` with this content:
    ```text
    name,score,city
    Ana,92,Stockholm
    Bo,,Gothenburg
    Lia,78,Malmo
    Noa,74,Uppsala
    ```
4. Create `scripts/process_students_pandas.py` with this starter code:
   ```python
   from pathlib import Path
   
   import pandas as pd
   
   BASE_DIR = Path(__file__).resolve().parent.parent
   DATA_DIR = BASE_DIR / "data"
   
   df = pd.read_csv(DATA_DIR / "students_pandas.csv")
   ```

`pathlib` helps the script find the CSV in `data/` even when the script lives in `scripts/`.

## Tasks

1. Load the CSV with Pandas.
2. Print `df.head()`, `df.columns`, and `df.shape`.
3. Run `df.info()` to inspect column types.
4. Print only the `name` column and notice that it is a Series.
5. Print the row at index `1`.
6. Check missing values with `df.isna().sum()`.
7. Replace missing `score` values with `0`.
8. Convert `score` back to `int` with `astype(int)`.
9. Create a new column `passed` that is `True` when the score is 75 or more.
10. Print only columns `name`, `score`, and `passed`.
11. Save the cleaned and transformed table to `data/students_pandas_cleaned.csv`.

## Expected Output Examples

Possible shape output:

```text
(4, 3)
```

Possible missing-value output:

```text
name     0
score    1
city     0
dtype: int64
```

Possible selected column type output:

```text
<class 'pandas.Series'>
```

Possible transformed output part:

```text
   name  score  passed
0   Ana     92    True
1    Bo      0   False
2   Lia     78    True
3   Noa     74   False
```

## Debug Task 1

Code:

```python
print(df["Score"])
```

Expected behavior:

```text
You expected to print the score column.
```

Actual behavior:

```text
It raises a KeyError because the real column name is "score".
```

## Debug Task 2

Code:

```python
df["score"].fillna(0)
print(df.isna().sum())
```

Expected behavior:

```text
You expected missing scores to be gone.
```

Actual behavior:

```text
Missing values remain because the result was not assigned back to the DataFrame.
```

## Debug Task 3

Code:

```python
df["score"] = df["score"].fillna(0)
print(df["score"])
```

Expected behavior:

```text
You expected scores to look like whole numbers such as 92 and 78.
```

Actual behavior:

```text
The values may look like 92.0 and 78.0 because Pandas used float for the column after missing values were involved.
```

## Debug Task 4

Code:

```python
df.to_csv(DATA_DIR / "students_pandas.csv", index=False)
```

Expected behavior:

```text
You expected to save cleaned data.
```

Actual behavior:

```text
You overwrite the raw file, which makes it harder to compare before and after.
```

## Self-Review

- I can follow the workflow: load, inspect, clean, transform, save.
- I can explain the difference between a Series and a DataFrame.
- I can select simple columns and rows.
- I can detect null (`NaN`) values and fill them with a basic rule.
- I can convert a float column back to `int` when the data should be whole numbers.
- I can save cleaned data to a new file instead of touching the raw file.

## Navigation

- ⬅️ Previous: [02-worked-examples.md](./02-worked-examples.md).
- 🧭 Week Overview: [week-04-overview.md](../week-04-overview.md).
- ➡️ Next: [04-challenge.md](./04-challenge.md).
