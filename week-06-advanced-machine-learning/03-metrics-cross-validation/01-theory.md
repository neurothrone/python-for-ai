# 01. Theory: Metrics and Cross-Validation

## Why This Matters

Training a model is only part of the job. You also need a simple way to check how well it is doing.

Without evaluation, it is easy to feel confident too early. A model might look perfect on one small test split and then
look weaker on a different one. Metrics and cross-validation help you check that more carefully.

This matters in real work because model comparison is not only about building a model. It is also about asking honest
questions such as:

- How often was the model correct?
- What kinds of mistakes did it make?
- Do the results stay the same across repeated checks?

## Accuracy

Accuracy is the simplest classification metric.

It answers this question:

- What share of predictions was correct?

Example:

- 4 correct predictions out of 5 test rows means accuracy `0.8`

In code:

```python
accuracy = accuracy_score(y_test, predictions)
```

Accuracy is a useful first check, but it does not tell the whole story by itself.

## Confusion Matrix

A confusion matrix shows where the predictions were correct and where they were wrong. For a two-label problem, it is a
small table.

If we use this label order:

```python
label_order = ["needs_support", "pass"]
```

Then:

- Row 1 means actual `needs_support`.
- Row 2 means actual `pass`.
- Column 1 means predicted `needs_support`.
- Column 2 means predicted `pass`.

So this matrix:

```text
[[2 1]
 [0 2]]
```

Means:

- 2 real `needs_support` rows were predicted correctly.
- 1 real `needs_support` row was predicted as `pass`.
- 2 real `pass` rows were predicted correctly.

## Precision and Recall

These metrics answer more specific questions.

- Precision asks: when the model predicts a label, how often is that prediction correct?
- Recall asks: how many real rows of that label did the model find?

At this stage, you do not need to memorize every formula. It is enough to know that these metrics describe model errors
more clearly than accuracy alone.

## `classification_report()` in Simple Words

Python can print several classification metrics together:

```python
classification_report(y_test, predictions, labels=label_order)
```

This report includes:

- precision
- recall
- f1-score
- support

`support` simply means how many real rows of that class were in the test data.

## Cross-Validation

Cross-validation is a more repeated way to evaluate a model.

Instead of using one train/test split only, it trains and checks the model several times on different parts of the
dataset.

With:

```python
cross_val_score(model, X, y, cv=3, scoring="accuracy")
```

The model is checked in 3 rounds. You can think of `cv=3` as "split the data into 3 parts and repeat the check 3 times".
This helps because one lucky split can make a model look better than it really is.

## `cv=3` in Simple Words

You do not need to imagine every fold in detail right away.

A helpful first understanding is:

- The model gets checked more than once.
- Each round uses a slightly different split.
- The average score is often more trustworthy than one lucky result.

## Why One Split Is Not Always Enough

A single test split can still be useful, but it is only one view of the data.

Cross-validation helps answer a better question:

- Does the model still look reasonable when I test it more than once?

## Honest Evaluation and Data Leakage

Data leakage means information from the test data slips into the model-building process.

A common example could be:

- Scaling all rows before the train/test split.
- Selecting features using the full dataset before the split.
- Choosing settings after repeatedly peeking at the test results.

This makes the final score look more impressive than it really is.

A safer habit is:

1. Split the data first.
2. Fit preprocessing steps on the training data only.
3. Use the test data for honest checking, not for helping the model learn.

Cross-validation also works best when you keep this same careful mindset.

## One Perfect Split Is Still Only One Split

Sometimes a model gets `1.0` accuracy on one test split. That can feel exciting, but it is still only one view of the
data.

A steadier question is:

- What happens when I check the model more than once?

That is why cross-validation matters so much in this section.

## A Simple Evaluation Workflow

1. Train the model.
2. Predict the test rows.
3. Check accuracy.
4. Read the confusion matrix.
5. Read the classification report.
6. Run cross-validation for a steadier check.
7. Describe the result carefully instead of claiming too much from one score.

## Common Mistakes

- Comparing `y_test` to the wrong values.
- Reading the confusion matrix in the wrong direction.
- Using too many folds for a tiny dataset.
- Treating one perfect split as final proof.
- Forgetting that different metrics answer different questions.
- Letting test data influence preprocessing or model choices.

## Navigation

- ⬅️ Previous: [05-reflection.md](../02-decision-trees/05-reflection.md).
- 🧭 Week Overview: [week-06-overview.md](../week-06-overview.md).
- ➡️ Next: [02-worked-examples.md](./02-worked-examples.md).
