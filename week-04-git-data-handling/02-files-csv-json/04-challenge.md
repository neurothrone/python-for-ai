# 04. Challenge: Files, CSV, and JSON

## Challenge Tasks

1. Create `inventory_notes.txt` and write two short lines about your inventory task.
2. Append one extra line to `inventory_notes.txt`.
3. Create `inventory.csv` with this content:
    ```text
    item,quantity
    Pen,10
    Book,5
    Bag,12
    ```
4. Read the CSV and calculate the total quantity.
5. Save the result into `inventory_summary.json` as `{"total_quantity": ...}`.
6. Print the JSON value after reading it back.

## Expected Output Example

Possible printed output:

```text
Total quantity: 27
```

Possible JSON content:

```json
{
  "total_quantity": 27
}
```

## Hint

One simple order is:

- write the first notes file
- append the extra notes line with `"a"` mode
- read `inventory.csv` row by row
- convert each `quantity` value from text to `int`
- add the quantities together
- save the final result as one dictionary in `inventory_summary.json`

## Navigation

- ⬅️ Previous: [03-practice.md](./03-practice.md).
- 🧭 Week Overview: [week-04-overview.md](../week-04-overview.md).
- ➡️ Next: [05-reflection.md](./05-reflection.md).
