# 01. Theory: Training, Evaluation, and Prediction

## Why This Matters

Building a neural network architecture is only the start.

To make the model useful, you need to:

- Compile it.
- Train it.
- Evaluate it.
- Make predictions from it.

This is the practical core of the Keras workflow.

It is also where the Week 6 habits matter most. Deep learning does not replace the need for:

- Honest train/test separation.
- Careful interpretation.
- Sensible model choice.
- Realistic claims about the result.

## What `compile(...)` Does

Before training, you configure the model with `compile(...)`.

For a beginner-friendly binary classification setup, that usually means:

- An optimizer such as `adam`.
- A loss such as `binary_crossentropy`.
- One or more metrics such as `accuracy`.

Example:

```python
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"],
)
```

In simple words:

- The optimizer controls how the model updates its weights.
- The loss tells the model what kind of mistake it should reduce.
- The metric gives you a human-readable way to track progress.

## What `fit(...)` Does

`fit(...)` trains the model.

Example:

```python
history = model.fit(
    X_train,
    y_train,
    epochs=30,
    validation_split=0.2,
    verbose=0,
)
```

Important ideas here:

- `X_train` and `y_train` are the training data.
- `validation_split=0.2` means part of the training data is used as validation during training.
- `epochs=30` means the model sees the training data 30 times.

Training for more epochs does not automatically make the model better. The goal is not to make the number bigger. The
goal is to understand what the model is doing and whether the result is trustworthy.

## What `history.history` Gives You

The object returned by `fit(...)` stores training information.

With:

```python
history.history
```

you can inspect values such as:

- Training loss.
- Training accuracy.
- Validation loss.
- Validation accuracy.

This is useful because it helps you see whether the model is improving over time.

## What `evaluate(...)` Does

`evaluate(...)` checks the model on data that was not used for training.

Example:

```python
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
```

This gives you a more honest view than training results alone.

That matters because a model can look strong while it is training and still be less convincing when you check it on
held-out data.

## What `predict(...)` Does

`predict(...)` produces model outputs for input rows.

For binary classification with a `sigmoid` output layer, the output values are usually between `0` and `1`.

Example:

```python
probabilities = model.predict(X_test, verbose=0).flatten()
```

These are probability-like values, not final class labels yet.

## From Probabilities to Labels

For a basic binary workflow, you often turn probabilities into labels with a threshold.

Example:

```python
predicted_labels = (probabilities >= 0.5).astype(int)
```

This means:

- Probability `>= 0.5` becomes label `1`.
- Probability `< 0.5` becomes label `0`.

That threshold is a good starting default, not a magical rule for every task.

## Honest Evaluation Still Matters

Deep learning does not remove the need for careful evaluation.

The same Week 6 habits still matter:

- Keep training data and test data separate.
- Avoid letting test data influence the training workflow.
- Describe results carefully instead of claiming too much from one score.

## What You Would Need Before Saying, "The Neural Network Is Better"

Before making that claim, you would want stronger evidence such as:

- The same problem and dataset.
- A simpler baseline model for comparison.
- A fair evaluation method.
- Results that still look convincing after careful interpretation.

One trained Keras model can still be a useful learning result even if you are not ready to make a stronger comparison.

## Common Mistakes

- Training on the test data by accident.
- Confusing validation results with final test results.
- Treating raw probabilities as final class labels without a threshold.
- Using a loss setup that does not match the task clearly.
- Assuming more epochs automatically means a better model.
- Treating one good test score as proof that deep learning was the best choice.

## Navigation

- ⬅️ Previous: [05-reflection.md](../02-keras-sequential-models/05-reflection.md).
- 🧭 Week Overview: [week-07-overview.md](../week-07-overview.md).
- ➡️ Next: [02-worked-examples.md](./02-worked-examples.md).
