# 04. Challenge: Integration

## Challenge Tasks

1. Create a small project with folders `data`, `outputs`, and `scripts`.
2. Create `data/phone_ads.csv` with this content:
   ```text
   ad_views,orders
   1000,15
   1500,19
   2000,24
   2500,28
   3000,33
   3500,37
   4000,42
   4500,47
   ```
3. Create one script that:
    - Loads and inspects the data.
    - Makes a scatter plot for `ad_views` and `orders`.
    - Saves the plot to `outputs/phone_orders_scatter.png`.
    - Fits a linear regression model with `ad_views` as feature and `orders` as target.
    - Creates a results table with actual and predicted orders.
    - Saves that table to `outputs/phone_ads_predictions.csv`.
4. Print one short interpretation of the chart and one short interpretation of the model.

## Expected Output Example

Possible printed lines:

```text
The scatter plot shows an upward pattern.
The model suggests that more ad views are linked to more orders.
```

## Hint

Keep the full workflow in order: load, inspect, plot, label, save plot, fit, predict, save results. If your script is
inside `scripts/`, use `pathlib` so it can still find `data/` and `outputs/` clearly.

## Navigation

- ⬅️ Previous: [03-practice.md](./03-practice.md).
- 🧭 Week Overview: [week-05-overview.md](../week-05-overview.md).
- ➡️ Next: [05-reflection.md](./05-reflection.md).
