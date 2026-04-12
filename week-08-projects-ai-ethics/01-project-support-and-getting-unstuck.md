# 01. Project Support and Getting Unstuck

## Why This Matters

By the last week of a course, many students do not need more theory. They need a clear way to move forward. If you feel
stuck, the best next step is usually not to make the project bigger. It is to clarify the project.

## Start with the Problem and the Data

Before you write more code, make sure you can answer these two questions:

1. What problem am I trying to solve?
2. What data do I have that could help with that problem?

If those two points are still unclear, that is often the real reason a project feels difficult.

## Look at the Columns First

Before modeling, inspect the dataset in a simple way.

Look at:

- Column names.
- Possible target columns.
- Missing values.
- Categories or labels.
- Values that look confusing or unrealistic.

This early inspection often helps you see what kind of problem the dataset can support.

## Choose a Realistic First Question

A good first question is usually small and concrete.

Examples:

- Can I predict whether something belongs to class A or class B?
- Can I predict a numeric value from the other columns?
- Can I describe and visualize an important pattern in the data?

Try to avoid questions that are too broad for the time you have left.

## Decide Whether It Is Classification or Regression

A useful early decision is:

- If your target is a category or label, the task is usually classification.
- If your target is a number you want to predict, the task is usually regression.

That decision helps you choose a sensible model and evaluation method.

## Start Small

A strong beginner project often looks like this:

- One dataset.
- One clear target.
- One main workflow.
- One or two useful visualizations.
- One model and one honest evaluation.

That is enough to make a clear submission.

## Finish the Core Before the Extras

If you are unsure what to do next, focus on this order:

1. Make the problem clear.
2. Load and inspect the data.
3. Prepare the data carefully.
4. Create at least one useful visualization.
5. Train at least one sensible model.
6. Evaluate the result honestly.
7. Explain what the result means and what its limits are.

Optional extras can come after that.

## If You Feel Stuck, Do This Next

If your project feels stuck, try this sequence:

1. Write one sentence that explains the problem.
2. Write one sentence that explains the target column.
3. Run `df.head()`, `df.info()`, and `df.isna().sum()`.
4. Make one simple plot that helps you understand the data.
5. Train one simple baseline model.
6. Save one result that you can explain.

That is often enough to create momentum again.

## Short Example: Thinking About a Dataset Before Coding

Imagine you start with
the [Research Grade Type 2 Diabetes Dataset](https://www.kaggle.com/datasets/mdmahfuzsumon/research-grade-type2-diabetes-dataset)
on Kaggle. Before you start building the project, you can learn useful things from the column names.

For example:

- `future_diabetes_5yr` looks like a possible target for a classification task.
- `risk_score` may be useful, but it may also overlap strongly with the target and needs careful thought.
- `country`, `gender`, `BMI`, `sleep_hours`, and `physical_activity` look like possible features.
- `patient_id` is probably an identifier, not a useful feature.
- Health-related columns mean you should already start thinking about privacy, sensitivity, and responsible use.

This kind of first look helps you shape a sensible question before you build anything.

## Keep the Final Week Calm

The goal now is not to impress with complexity.

The goal is to produce work that is:

- Clear.
- Complete enough.
- Honest.
- Easy to follow.

That is a strong way to finish.

## Navigation

- 🧭 Week Overview: [week-08-overview.md](./week-08-overview.md).
- ➡️ Next: [02-ethics-for-your-project.md](./02-ethics-for-your-project.md).
