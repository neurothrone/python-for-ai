# 04. Challenge: Pandas Basics

## Challenge Tasks

1. Create `sales.csv` with this content:
    ```text
    item,price,quantity
    Pen,10,3
    Book,,2
    Bag,40,3
    ```
2. Load the file with Pandas.
3. Inspect the table with `head()`, `columns`, and `isna().sum()`.
4. Fill missing `price` with `0`.
5. Convert `price` to `int`.
6. Create a new column `total` using `price * quantity`.
7. Save the result to `sales_cleaned.csv`.
8. Print only the columns `item` and `total` from the cleaned and transformed DataFrame.

## Expected Output Example

Possible output:

```text
   item  total
0   Pen     30
1  Book      0
2   Bag    120
```

## Hint

Check column names with `df.columns` before using them. Do not overwrite the raw file.

## Navigation

- ⬅️ Previous: [03-practice.md](./03-practice.md).
- 🧭 Week Overview: [week-04-overview.md](../week-04-overview.md).
- ➡️ Next: [05-reflection.md](./05-reflection.md).
