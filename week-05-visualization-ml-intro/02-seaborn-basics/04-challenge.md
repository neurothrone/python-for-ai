# 04. Challenge: Seaborn Basics

## Challenge Tasks

1. Create `delivery_times.csv` with this content:
   ```text
   distance_km,delivery_minutes
   1,8
   2,12
   3,16
   4,21
   5,24
   6,29
   ```
2. Load the file with Pandas.
3. Create a Seaborn scatter plot with `distance_km` and `delivery_minutes`.
4. Add a clear title and axis labels.
5. Create a Seaborn line plot with the same two columns.
6. Show both plots.
7. Print one simple interpretation of the pattern.

## Expected Output Example

Possible printed sentence:

```text
Longer delivery distances seem to be linked to longer delivery times.
```

## Hint

If you are unsure which columns to use, print `df.columns` first. Keep the chart question simple: compare two numeric
columns and describe the pattern.

## Navigation

- ⬅️ Previous: [03-practice.md](./03-practice.md).
- 🧭 Week Overview: [week-05-overview.md](../week-05-overview.md).
- ➡️ Next: [05-reflection.md](./05-reflection.md).
