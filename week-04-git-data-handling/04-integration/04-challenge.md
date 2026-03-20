# 04. Challenge: Integration

## Challenge Tasks

1. Create a local repository for a folder called `week4-shop-data`.
2. Create `data/products.csv` with this content:
   ```text
   product,price,stock
   Pen,10,3
   Book,,2
   Bag,40,3
   ```
3. Commit the raw dataset with message `add raw product dataset`.
4. Create `scripts/clean_products.py` that:
    - Loads the CSV.
    - Prints `head()`, `columns`, and missing values.
    - Fills missing `price` with `0`.
    - Converts `price` to `int`.
    - Creates a new column `inventory_value` using `price * stock`.
    - Saves `data/products_cleaned.csv`.
5. Run the script and print both:
    - The cleaned columns `product` and `inventory_value`.
    - The total stock from the cleaned DataFrame.
6. Make at least three commits:
    - One after setting up the repo.
    - One after adding the raw data.
    - One after adding the cleaning script and cleaned output file.

## Expected Output Example

Possible script output:

```text
   product  inventory_value
0      Pen               30
1     Book                0
2      Bag              120
Total stock: 8
Saved: data/products_cleaned.csv
```

Possible log output:

```text
8f7e6d5 add product cleaning script and cleaned output
4c3b2a1 add raw product dataset
1a2b3c4 initial commit
```

## Hint

Keep each commit focused on a single task. One simple order is:

- Initialize the repo.
- Add the raw CSV.
- Inspect the data.
- Clean missing values.
- Transform with `inventory_value`.
- Save `products_cleaned.csv`.
- Commit the script and cleaned output together.

If your script is inside `scripts/`, use `pathlib` so it can clearly find files in `data/`.

## Navigation

- ⬅️ Previous: [03-practice.md](./03-practice.md).
- 🧭 Week Overview: [week-04-overview.md](../week-04-overview.md).
- ➡️ Next: [05-reflection.md](./05-reflection.md).
