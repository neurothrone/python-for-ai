# 01. Theory: Decision Trees

## Why This Matters

Decision trees are useful because they turn prediction into a series of simple questions.

That makes them easier to explain than many other models. In practical work, that can matter a lot. Sometimes you do
not only want a prediction. You also want to understand the rule path that led to it.

This section also helps you compare model styles. `k-NN` looks at nearby examples. A decision tree builds rule-based
splits. Learning both gives you a better foundation for later course work, model comparison, and project choices.

## What a Decision Tree Does

A decision tree predicts by following question-like splits.

A tiny example could look like this:

1. Is `study_hours <= 2.5`?
2. If yes, predict `needs_support`.
3. If no, ask another question.

The model keeps splitting the data until it reaches a final prediction.

## Read One Tree Question in Simple English

If a tree asks:

1. Is `review_sessions <= 2.5`?
2. If yes, predict `follow_up`.
3. If no, predict `steady_progress`.

Then the model is doing something quite human-readable. It is turning the data into a short rule path. That is one
reason decision trees can feel approachable when you are still getting used to machine learning.

## Important Tree Words

- A split is one decision question.
- A node is one point in the tree.
- A leaf is a final prediction point.

You do not need to memorize the vocabulary deeply. The important idea is simple: the tree keeps asking questions until
it reaches a label.

## Why Trees Feel Different from k-NN

Both models can do classification, but they work in different ways:

- `k-NN` compares a new row to nearby saved examples.
- A decision tree follows rule-like splits such as `practice_sessions <= 2.5`.

This difference is useful because two models can reach the same task in two different ways.

There is also one practical difference from the earlier section:

- `k-NN` is sensitive to distance, so feature value ranges matter more.
- A decision tree asks threshold questions, so it usually cares less about that.

## `max_depth` in Simple Words

You will often see:

```python
DecisionTreeClassifier(max_depth=3, random_state=42)
```

`max_depth=3` means the tree can only grow to a limited depth.

That can be helpful because:

- The tree stays smaller.
- The printed rules stay easier to read.
- The workflow is less overwhelming.

## What `random_state=42` Does Here

`random_state=42` keeps the model behavior repeatable while you learn.

That does not make the model smarter. It only makes the example easier to follow because the same code gives the same
result more reliably and more reproducibly.

## A Simple Decision Tree Workflow

1. Load the dataset.
2. Choose features and target.
3. Split the data.
4. Create the tree model.
5. Fit the model.
6. Predict on test rows.
7. Read the rules and the predictions together.

## Why Decision Trees Can Be Practical

Decision trees are often a good first model because they can:

- Work with clear rule-like splits.
- Be easier to explain in plain English.
- Show why one path leads to one label and another path leads to another.

## When a Decision Tree Is a Sensible First Model

A decision tree can be a sensible first model when:

- You want a result that is easier to explain.
- You want to read simple rule paths after training.
- You are working with a small tabular dataset (data arranged in rows and columns).

That does not mean a tree is always the best model. It means it can be a practical place to start.

## Common Mistakes

- Forgetting to call `fit()` before `predict()`.
- Using the wrong target column name.
- Making the tree harder to read by not controlling depth.
- Giving the wrong feature names when exporting the rules.
- Saving result files over the raw CSV by mistake.

## Navigation

- ⬅️ Previous: [05-reflection.md](../01-knn-classification/05-reflection.md).
- 🧭 Week Overview: [week-06-overview.md](../week-06-overview.md).
- ➡️ Next: [02-worked-examples.md](./02-worked-examples.md).
