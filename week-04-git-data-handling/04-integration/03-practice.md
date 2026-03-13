# 03. Practice: Integration

## Tasks

1. Create folder `week4-integration-project` and run `git init`.
2. Create `data/students.csv` with this content:
   ```text
   name,score,city
   Ana,92,Stockholm
   Bo,,Gothenburg
   Lia,78,Malmo
   Noa,74,Uppsala
   ```
3. Commit the raw dataset with the message `add raw students file`.
4. Create the script `scripts/process_students.py` that:
    - Reads the CSV.
    - Prints `head()`, `columns`, and missing values.
    - Fills missing `score` with `0`.
    - Converts `score` to `int`.
    - Creates a new column `passed` for scores 75 or more.
    - Writes `data/students_cleaned.csv`.
5. Run the script.
6. Commit the script and cleaned CSV with the message `add script and cleaned dataset`.
7. Run `git log --oneline` and verify at least two commits.

## Expected Output Examples

Possible script output:

```text
Index(['name', 'score', 'city'], dtype='object')
name     0
score    1
city     0
dtype: int64
Saved: data/students_cleaned.csv
```

Possible `git log --oneline` output:

```text
c3d4e5f process dataset with pandas
f1a2b3c add raw students file
```

## Debug Task 1

Code:

```python
df = pd.read_csv("students.csv")
```

Expected behavior:

```text
You expected the script to load the dataset.
```

Actual behavior:

```text
It raises FileNotFoundError because the file is in data/students.csv.
```

## Debug Task 2

Code:

```python
df["score"] = df["score"].fillna(0)
print(df.isna().sum())
```

Expected behavior:

```text
You expected no missing values in score.
```

Actual behavior:

```text
It still shows missing values if the real column is named "Score" or has extra spaces.
```

## Debug Task 3

Code:

```python
df["score"] = df["score"].fillna(0)
df.to_csv("data/students.csv", index=False)
```

Expected behavior:

```text
You expected to save cleaned data.
```

Actual behavior:

```text
You overwrite the raw file, so it is harder to compare before and after.
```

## Self-Review

- I can complete a mini flow from raw CSV to cleaned and transformed CSV.
- I can keep commits small and clear.
- I can debug path errors, column-name mismatches, and type cleanup.
- I can connect Git workflow with basic data work.

## Navigation

- ⬅️ Previous: [02-worked-examples.md](./02-worked-examples.md).
- 🧭 Week Overview: [week-04-overview.md](../week-04-overview.md).
- ➡️ Next: [04-challenge.md](./04-challenge.md).
