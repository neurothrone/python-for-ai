# 02. Worked Examples: Integration

## Example A: Start Project and Repo

```bash
mkdir week4-mini-project
cd week4-mini-project
git init
mkdir data scripts
```

## Example B: Add Small Dataset

Create `data/students.csv` with this content:

```text
name,score,city
Ana,92,Stockholm
Bo,,Gothenburg
Lia,78,Malmo
Noa,74,Uppsala
```

Commit it:

```bash
git add data/students.csv
git commit -m "add raw students dataset"
```

## Example C: Clean with Pandas

Create `scripts/clean_students.py` with this content:

```python
import pandas as pd

df = pd.read_csv("data/students.csv")

print(df.head())
print(df.columns)
print(df.isna().sum())

df["score"] = df["score"].fillna(0)
df["score"] = df["score"].astype(int)
df["passed"] = df["score"] >= 75

df.to_csv("data/students_cleaned.csv", index=False)

print(df.isna().sum())
print(df[["name", "score", "passed"]])
print("Saved: data/students_cleaned.csv")
```

Run the script and commit the new file:

```bash
# These commands assume you are in the project root directory
python scripts/clean_students.py
git add scripts/clean_students.py data/students_cleaned.csv
git commit -m "add cleaning script and cleaned dataset"
```

This example follows the full beginner workflow:

1. Load raw data
2. Inspect it
3. Clean missing values
4. Transform with a new `passed` column
5. Save to a new file

## Example D: Push/Pull Reminder

After remote repository setup:

```bash
git push
git pull
```

Keep this order simple: commit locally first, then push.

## Navigation

- ⬅️ Previous: [01-theory.md](./01-theory.md).
- 🧭 Week Overview: [week-04-overview.md](../week-04-overview.md).
- ➡️ Next: [03-practice.md](./03-practice.md).
