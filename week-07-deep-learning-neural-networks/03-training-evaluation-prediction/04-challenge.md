# 04. Challenge: Training, Evaluation, and Prediction

## Challenge Tasks

1. Reuse the Week 7 `student_completion.csv` dataset.
2. Train a small neural network with:
    - Input shape `(3,)`.
    - One hidden layer.
    - One output layer.
3. Compile it for binary classification.
4. Train it for at least `20` epochs.
5. Save the training history to `outputs/`.
6. Create and save a simple training-history plot.
7. Evaluate the model on a test split.
8. Save a prediction table that includes:
    - The feature values.
    - Actual labels.
    - Predicted probabilities.
    - Predicted labels.
9. Write 2 short notes:
    - One short note explaining why probability and label are not the same thing.
    - One short note explaining what evidence you would still need before claiming the neural network is better than a
      simpler Week 6 baseline.

This challenge is meant to make you run the full training-and-evaluation loop with a little less support than the
practice task.

## Expected Output Example

Possible saved-file messages:

```text
Saved: outputs/training_history.csv
Saved: outputs/training_history_plot.png
Saved: outputs/test_predictions.csv
```

Possible result-table columns:

```text
actual_completed_course
predicted_probability
predicted_label
```

## Hint

One simple order is:

- Split first.
- Build the model.
- Compile.
- Fit.
- Save the history.
- Save the history plot.
- Evaluate.
- Predict.
- Threshold the probabilities.
- Save the final table.

Try not to skip the save steps. They make the workflow much easier to review later.

## Navigation

- ⬅️ Previous: [03-practice.md](./03-practice.md).
- 🧭 Week Overview: [week-07-overview.md](../week-07-overview.md).
- ➡️ Next: [05-reflection.md](./05-reflection.md).
