# 01. Theory: Integration (Visualization plus Linear Regression)

## Why This Matters

Real data work is not only about making a chart or only about fitting a model. A more realistic flow is to load data,
inspect it, visualize it, decide what question you want to ask, build a simple model, and compare the model output with
the data you already saw. That is the kind of connected workflow this section introduces.

This matters because it starts to feel like a small project instead of isolated commands. It also helps you build a
healthy habit: look at the data first, then model it. A chart can reveal whether your columns make sense, whether a
pattern looks simple enough for linear regression, and whether your final prediction result is worth checking more
closely.

## Simple Flow

1. Create a small project folder.
2. Add a raw CSV dataset.
3. Load and inspect the data.
4. Make one simple plot.
5. Define feature and target columns.
6. Fit a linear regression model.
7. Make predictions.
8. Save a small output file with prediction results.

## Example Project Structure

```text
week5-mini-project/
  data/
    tutoring_data.csv
  outputs/
    tutoring_predictions.csv
    study_hours_scatter.png
  scripts/
    analyze_tutoring.py
```

## Keep Raw and Derived Files Separate

This week, that means:

- Raw input file stays in `data/`.
- Derived prediction output can be saved as a new CSV in `outputs/`.
- Saved plot files can also go in `outputs/`.
- `pathlib` can help a script in `scripts/` reliably find both folders.

That separation makes your workflow easier to explain and safer to debug.

## What to Check Before Fitting a Model

- Are the column names correct?
- Is the feature numeric?
- Is the target numeric?
- Does a scatter plot show a rough line-like pattern?
- Are you asking a clear question, such as predicting score from study hours?

## Common Mistakes

- Building a model before checking whether the columns are correct.
- Plotting the wrong columns and then training on a different question.
- Saving prediction results over the raw input file.
- Forgetting which values are actual and which are predicted.
- Using a new prediction input with the wrong column name.

## Navigation

- ⬅️ Previous: [05-reflection.md](../03-ml-linear-regression-basics/05-reflection.md).
- 🧭 Week Overview: [week-05-overview.md](../week-05-overview.md).
- ➡️ Next: [02-worked-examples.md](./02-worked-examples.md).
