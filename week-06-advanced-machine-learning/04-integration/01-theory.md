# 01. Theory: Integration (Compare Classification Models)

## Why This Matters

Real projects usually do not stop after the first model works once.

A more practical workflow is:

1. Choose one clear classification question.
2. Train more than one suitable model.
3. Evaluate them in the same way.
4. Compare the results before deciding what to trust more.

That matters because model choice is part of machine learning work. If you compare models carefully, you are less likely
to trust a lucky result or mix unfair comparisons.

This section brings the whole week together. You will use the same dataset, the same feature-target question, and the
same evaluation steps for both k-NN and a decision tree.

## A Fair Comparison in Simple Words

When you compare two models, keep these parts the same:

- The dataset.
- The feature columns.
- The target column.
- The train/test split.
- The evaluation method.

If those parts change, the comparison becomes harder to trust.

You can think of it like this: fair comparison means both models are answering the same question under the same
conditions.

## What a Careful Comparison Sounds Like

A careful comparison usually sounds like this:

- Both models were tested on the same split.
- Both models answered the same classification question.
- One model had the stronger repeated score in this comparison.

This kind of wording is useful because it stays honest. It describes what happened in this one comparison instead of
claiming too much.

## A Good Comparison Flow

1. Load the classification dataset.
2. Inspect the columns and label counts.
3. Choose one feature-target question.
4. Create one train/test split.
5. Train the `k-NN` model.
6. Train the decision tree model.
7. Compare predictions on the same test rows.
8. Compare metrics such as accuracy and cross-validation mean.
9. Save the comparison to output files.

## What to Watch For

Two models can look similar on one test split and still differ when you run cross-validation.

That is why a comparison table is useful. It helps you see:

- Test accuracy for this one split.
- Repeated accuracy across several folds.

## Week 6 as a Project Bridge

This section is not only about two small classroom models.

It teaches a project habit that will still matter later:

1. Define one clear question.
2. Start with a simple baseline.
3. Compare models fairly.
4. Describe limitations honestly.

If your final project is a classification problem, `k-NN` or a decision tree can be a sensible starting point.

If your final project later uses regression or a simple neural network instead, the same workflow still matters:

- Keep the question clear.
- Prepare the data carefully.
- Evaluate honestly.
- Avoid unfair comparisons.

## A Good First Project Strategy

For a small course project, a strong starting point is usual:

- One manageable dataset.
- One clearly defined target.
- One simple baseline model.
- One or two relevant evaluation methods.

That is often better than choosing a very ambitious problem that becomes hard to complete or explain.

## One Honest Way to Read the Outcome

A careful conclusion can sound like this:

- Both models worked on this test split.
- One model had a stronger average cross-validation score.
- The dataset is small, so the result is still only an early comparison.

That kind of language is careful and realistic.

## A Simple Habit to Carry Into the Project

Even if your final project does not compare these exact two models, this habit still matters:

1. Keep the question clear.
2. Keep the comparison fair.
3. Save the results so you can explain them later.
4. Write one honest conclusion.

## Common Mistakes

- Comparing models that used different feature columns.
- Using a different train/test split for each model and then calling it a direct comparison.
- Mixing up actual and predicted columns in the result table.
- Writing the comparison output over the raw data file.
- Picking a "winner" from one number without checking repeated evaluation.
- Changing preprocessing between models without noticing that the comparison is no longer fair.

## Navigation

- ⬅️ Previous: [05-reflection.md](../03-metrics-cross-validation/05-reflection.md).
- 🧭 Week Overview: [week-06-overview.md](../week-06-overview.md).
- ➡️ Next: [02-worked-examples.md](./02-worked-examples.md).
