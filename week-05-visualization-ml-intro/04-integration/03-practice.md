# 03. Practice: Integration

## Setup

1. Create a folder called `week5-integration-project`.
2. Inside it, create these folders:
   ```text
   data/
   outputs/
   scripts/
   ```
3. Create `data/coffee_ads.csv` with this content:
    ```text
    ad_spend,cups_sold
    100,40
    150,48
    200,55
    250,63
    300,71
    350,79
    400,86
    450,95
    ```
4. Create `scripts/analyze_coffee_ads.py`.

## Tasks

1. Load `data/coffee_ads.csv` with Pandas.
2. Print `head()`, `columns`, and `dtypes`.
3. Create a scatter plot of `ad_spend` and `cups_sold` with Seaborn.
4. Add the title `Ad Spend and Coffee Sales`.
5. Add clear axis labels.
6. Save the plot to `outputs/coffee_sales_scatter.png`.
7. Show the plot.
8. Define the same question for the model by using `ad_spend` as the feature and `cups_sold` as the target.
9. Split the data into training and test sets with `test_size=0.25` and `random_state=42`.
10. Fit a linear regression model.
11. Make predictions for the test rows.
12. Create a DataFrame called `results_df` that contains:
    - The test feature values.
    - A column `actual_cups_sold`.
    - A column `predicted_cups_sold`.
13. Print `results_df`.
14. Save `results_df` to `outputs/coffee_ads_predictions.csv`.
15. Print two lines:
    - `Saved: outputs/coffee_sales_scatter.png`
    - `Saved: outputs/coffee_ads_predictions.csv`

## Starter Script

Use this starter and complete the missing parts:

```python
from pathlib import Path

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUTS_DIR = BASE_DIR / "outputs"

OUTPUTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_DIR / "coffee_ads.csv")

print(df.head())
print(df.columns)
print(df.dtypes)

# Create and save the scatter plot here

feature_column = "ad_spend"
target_column = "cups_sold"

X = df[[feature_column]]
y = df[target_column]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

model = LinearRegression()

# Fit the model here
# Make predictions here
# Build results_df here
# Save the prediction file here
```

`pathlib` helps here because the script is inside `scripts/`, while the CSV and output files are in other folders.

`OUTPUTS_DIR.mkdir(exist_ok=True)` makes sure the `outputs/` folder exists before you try to save files into it.

## Expected Output Examples

Possible saved-file messages:

```text
Saved: outputs/coffee_sales_scatter.png
Saved: outputs/coffee_ads_predictions.csv
```

Possible `results_df` structure:

```text
   ad_spend  actual_cups_sold  predicted_cups_sold
1       150                48                 47.9
5       350                79                 79.1
```

The exact numbers may vary slightly, but the structure should be similar.

## Debug Task 1

Code:

```python
df = pd.read_csv("coffee_ads.csv")
```

Expected behavior:

```text
You expected the script to load the dataset.
```

Actual behavior:

```text
It raises FileNotFoundError because the file is in data/coffee_ads.csv.
```

## Debug Task 2

Code:

```python
sns.scatterplot(data=df, x="cups_sold", y="ad_spend")
plt.title("Ad Spend and Coffee Sales")
plt.show()
```

Expected behavior:

```text
You wanted to inspect how ad spend might help predict coffee sales.
```

Actual behavior:

```text
The axes are reversed, so the chart does not match the modeling question you plan to ask next.
```

## Debug Task 3

Code:

```python
results_df = X_test.copy()
results_df["actual_cups_sold"] = predictions
results_df["predicted_cups_sold"] = y_test.values
```

Expected behavior:

```text
You wanted actual values in the actual column and predicted values in the predicted column.
```

Actual behavior:

```text
The columns are swapped, which makes the output table misleading.
```

## Debug Task 4

Code:

```python
results_df.to_csv(DATA_DIR / "coffee_ads.csv", index=False)
```

Expected behavior:

```text
You expected to save prediction results.
```

Actual behavior:

```text
This overwrites the raw dataset instead of creating a new output file.
```

## Self-Review

- I can combine plotting and simple machine learning in one small project flow.
- I can keep raw data, plots, and prediction outputs separate.
- I can use the same feature-target question in both the plot and the model.
- I can debug path issues, swapped axes, swapped result columns, and overwritten raw files.

## Navigation

- ⬅️ Previous: [02-worked-examples.md](./02-worked-examples.md).
- 🧭 Week Overview: [week-05-overview.md](../week-05-overview.md).
- ➡️ Next: [04-challenge.md](./04-challenge.md).
