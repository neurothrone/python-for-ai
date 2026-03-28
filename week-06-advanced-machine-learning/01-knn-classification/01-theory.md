# 01. Theory: k-NN Classification

## Why This Matters

Many useful AI tasks do not predict a number. They predict a group or label.

A program might decide whether an email is spam, whether a product review needs follow-up, or whether a student record
looks like it may need extra support. These are classification tasks. This matters because it is one of the most common
ways machine learning is used in practice.

This section also builds directly on Week 5. Last week, you predicted numbers with linear regression. This week, you
predict categories. That step is important because later course work and project work often need both ideas: first
understanding the question, then choosing the right kind of model.

## Classification in Simple Words

Classification means predicting a label or category.

Examples:

- `spam` or `not_spam`.
- `pass` or `needs_support`.
- `approved` or `not_approved`.

The output is a group name, not a numeric measurement.

## Classification vs Regression

| Type           | Predicts            | Example Output |
|:---------------|:--------------------|:---------------|
| Classification | A label or category | `pass`         |
| Regression     | A number            | `82.5`         |

This difference matters because the model and the evaluation methods change with the question.

## Features and Target

Just like in Week 5:

- Features are the input columns you use.
- Target is the output column you want to predict.

Example:

- Features: `study_hours`, `practice_sessions`.
- Target: `outcome`.

## What k-NN Means

`k-NN` stands for k-nearest neighbors.

It is a classification model that works by looking at the closest known examples in the training data.

In simple words:

1. Take a new case.
2. Find the nearest saved examples.
3. Count their labels.
4. Use the most common label as the prediction.

## Why `n_neighbors=3` Is a Good First Choice

In many examples, we use:

```python
KNeighborsClassifier(n_neighbors=3)
```

This means the model checks the three nearest training rows. Using an odd number is often helpful in a two-label example
because it reduces tie situations.

## What k-NN Learns

`k-NN` does not learn one big formula like linear regression. Instead, it keeps the training examples and compares new
rows to them by distance. That is why `k-NN` is often easier to explain at the beginning, but it also means the feature
values should make sense for distance-based comparison.

## Keep Feature Value Ranges Similar in This Week's Examples

`k-NN` uses distance. That means one feature can take over the comparison if its values are much larger than the others.

For this week, we keep the examples easier to follow by using features with similar value ranges, such as:

- `study_hours`
- `practice_sessions`

Here, both columns use small counts, so the distance comparison is easier to understand.

## A Better Habit for Real Projects

For this week's small examples, we keep the feature value ranges similar so the code stays easier to follow.

In a real project, a safer habit is:

1. Split the data into training and test parts first.
2. Fit any scaler on the training data only.
3. Apply that same scaler to the test data.

That matters because `k-NN` depends on distance and because you do not want the test data to influence your training
workflow by accident.

Here, a scaler means a tool that changes numeric values into a more similar range before the model compares them.

In `scikit-learn`, a pipeline is a clean later step for handling this, but you do not need to master that yet to
understand the main idea.

## A Simple Classification Workflow

1. Load the dataset.
2. Inspect the columns and label counts.
3. Choose feature columns and the target column.
4. Split the data into training and test parts.
5. Create the `k-NN` model.
6. Fit the model.
7. Predict on test data.
8. Check whether the predictions look reasonable.

## Why `stratify=y` Can Help

In classification, you will often see:

```python
train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
```

`stratify=y` helps keep a similar mix of labels in both the training set and the test set. That is useful when your
dataset has more than one class, and you want a fairer split.

## Project Bridge: When k-NN Is a Sensible First Model

`k-NN` can be a sensible first model in a small course project when:

- The problem is classification.
- The data is tabular (organized in rows and columns).
- The feature columns are reasonably understandable.
- The feature value ranges can be kept sensible.

It is less helpful when the dataset is huge or when you need a more rule-like explanation of why one prediction was
made. In that case, a decision tree may be easier to explain.

## Common Mistakes

- Confusing classification with regression.
- Using the target column as a feature by mistake.
- Forgetting to call `fit()` before `predict()`.
- Using one feature when you meant to use two.
- Creating new prediction data with the wrong column names.
- Ignoring that `k-NN` uses distance.
- Scaling all rows before the train/test split and then trusting the result too much.

## Navigation

- 🧭 Week Overview: [week-06-overview.md](../week-06-overview.md).
- ➡️ Next: [02-worked-examples.md](./02-worked-examples.md).
