# 01. Theory: ML and Linear Regression Basics

## Why This Matters

Machine learning can sound much bigger and more mysterious than it needs to be at the beginning. At a beginner level,
you can think of it as a way to learn a pattern from example data and then use that pattern to make a prediction. That
idea is useful in many real situations, such as estimating prices, predicting sales, or forecasting simple trends.

This section matters because it connects your earlier Python and data skills to a first real model. You already know how
to load data, inspect columns, and make a simple plot. Now you will use that same kind of dataset to define a feature,
choose a target, fit a model, and make predictions. That is a practical foundation for later course work in machine
learning.

## What Is a Model

A model is a program that learns a pattern from data.

You give it example inputs and example outputs. It uses those examples to learn a relationship that can be used for new
predictions.

## Features and Target

These two words matter a lot:

- Features are the input columns you use to make a prediction.
- Target is the output column you want to predict.

Example:

- Feature: `hours_studied`
- Target: `test_score`

If you want to predict score from study hours, then `hours_studied` is the feature and `test_score` is the target.

## Training and Testing in Simple Terms

You usually do not train on all rows and then judge the model on those same rows.

Instead:

- Training data is the part used to learn the pattern.
- Test data is the part used later to check how the model behaves on data it did not train on.

For beginners, the key idea is straightforward: keep one small part of the data aside so you can do a more honest check.

## What Linear Regression Does

Linear regression learns a simple straight-line relationship between numeric inputs and numeric outputs.
If the points on a scatter plot roughly rise together, linear regression is often a good first learning example.

Example idea:

- More study hours may be linked to higher scores.
- Larger apartment size may be linked to higher rent.

## Basic Scikit-learn Workflow

1. Load the data.
2. Choose the feature column or columns.
3. Choose the target column.
4. Split the data into training and test sets.
5. Create the model.
6. Fit the model on the training data.
7. Make predictions.
8. Compare predicted values with actual values in simple terms.

## Important Shape Idea

**Scikit-learn** expects the feature input to be 2-dimensional.

That is why you often see:

```python
X = df[["hours_studied"]]
y = df["test_score"]
```

- `df[["hours_studied"]]` is a DataFrame with one column.
- `df["test_score"]` is a Series.

This difference matters. Beginners often use `df["hours_studied"]` for `X`, which can cause shape problems in some
**Scikit-learn** workflows.

## Fitting and Predicting

```python
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

- `fit(...)` means learn from the training data.
- `predict(...)` means use the learned pattern on new input values.

## Keep Interpretation Small and Honest

This week, keep the interpretation simple:

- Do predicted values go up when the feature goes up?
- Are predictions somewhat close to the actual values?
- Does the scatter plot seem to match the idea of a line?

Do not worry yet about advanced metrics, tuning, or deep theory.

## Common Beginner Mistakes

- Using the wrong column as the target.
- Using `df["feature"]` instead of `df[["feature"]]` for `X`.
- Forgetting to import `train_test_split` or `LinearRegression`.
- Predicting before calling `fit()`.
- Confusing predicted values with the original target column.
- Comparing results without printing both actual and predicted values.

## Navigation

- ⬅️ Previous: [05-reflection.md](../02-seaborn-basics/05-reflection.md).
- 🧭 Week Overview: [week-05-overview.md](../week-05-overview.md).
- ➡️ Next: [02-worked-examples.md](./02-worked-examples.md).
