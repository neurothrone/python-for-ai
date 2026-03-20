# 02. Worked Examples: Integration

## Example A: Set Up the Project

Create this structure:

```text
week5-mini-project/
  data/
  outputs/
  scripts/
```

Create `data/tutoring_data.csv` with this content:

```text
hours_with_tutor,test_score
1,50
2,56
3,62
4,67
5,73
6,79
7,85
```

## Example B: Create the Analysis Script

Create `scripts/analyze_tutoring.py` with this content:

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

df = pd.read_csv(DATA_DIR / "tutoring_data.csv")

print(df.head())
print(df.columns)
print(df.dtypes)

feature_column = "hours_with_tutor"
target_column = "test_score"

fig, ax = plt.subplots()
sns.scatterplot(data=df, x=feature_column, y=target_column, ax=ax)
ax.set_title("Tutor Hours and Test Score")
ax.set_xlabel("Hours with Tutor")
ax.set_ylabel("Test Score")
fig.savefig(OUTPUTS_DIR / "study_hours_scatter.png")
plt.show()
plt.close(fig)

X = df[[feature_column]]
y = df[target_column]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.29,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

results_df = X_test.copy()
results_df["actual_score"] = y_test.values
results_df["predicted_score"] = predictions

print(results_df)

results_df.to_csv(OUTPUTS_DIR / "tutoring_predictions.csv", index=False)
print("Saved: outputs/study_hours_scatter.png")
print("Saved: outputs/tutoring_predictions.csv")
```

`Path(__file__).resolve().parent.parent` means:

- start from this script file,
- go up to the project root,
- then build clear paths to `data/` and `outputs/`.

This helps the script work reliably even when it is stored inside `scripts/`.

## Example C: Why This Flow Works

This script follows a complete workflow:

1. Load raw data.
2. Inspect columns and types.
3. Visualize the relationship with a scatter plot.
4. Define the same question in model form with a feature and a target.
5. Train a model.
6. Compare actual and predicted values.
7. Save outputs to new files.

## Example D: Read the Output in Simple Terms

After running the script, you can say:

- The scatter plot shows an upward pattern.
- The model learned that more tutor hours are linked to higher scores.
- The prediction file lets me compare actual and predicted values side by side.

## Navigation

- ⬅️ Previous: [01-theory.md](./01-theory.md).
- 🧭 Week Overview: [week-05-overview.md](../week-05-overview.md).
- ➡️ Next: [03-practice.md](./03-practice.md).
