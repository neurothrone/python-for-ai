# 04. Challenge: ML and Linear Regression Basics

## Challenge Tasks

1. Create `ad_budget_sales.csv` with this content:
   ```text
   ad_budget,sales
   100,20
   150,24
   200,29
   250,35
   300,39
   350,44
   400,48
   450,53
   ```
2. Load the file with Pandas.
3. Set `ad_budget` as the feature and `sales` as the target.
4. Split the data with `test_size=0.25` and `random_state=42`.
5. Fit a linear regression model.
6. Print predicted and actual sales for the test data.
7. Predict sales for a new ad budget of `320`.
8. Print one simple sentence about what the model seems to have learned.

## Expected Output Example

Possible printed sentence:

```text
The model suggests that higher ad budget is linked to higher sales.
```

## Hint

If **Scikit-learn** complains about input shape, check whether `X` was created with double brackets:
`df[["ad_budget"]]`.

## Navigation

- ⬅️ Previous: [03-practice.md](./03-practice.md).
- 🧭 Week Overview: [week-05-overview.md](../week-05-overview.md).
- ➡️ Next: [05-reflection.md](./05-reflection.md).
