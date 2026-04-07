# 04. Challenge: Keras Sequential Models

## Challenge Tasks

1. Imagine you have a small tabular classification task with 3 numeric features and 1 binary target.
2. Build a `Sequential` model for that 3-feature binary classification task.
3. Use this layer pattern:
    - Input shape `(3,)`.
    - `Dense(6, activation="relu")`.
    - `Dense(3, activation="relu")`.
    - `Dense(1, activation="sigmoid")`.
4. Print `model.summary()`.
5. Print the layer names.
6. Pass 4 sample rows through the model and print the output shape.
7. Write 3 short explanations:
    - Why this is still a `Sequential` model.
    - One reason this architecture is still only a first attempt.
    - One simpler Week 6 baseline you would compare it with.

This challenge is meant to help you vary the architecture without losing the basic logic of a `Sequential` workflow.

## Expected Output Example

Possible printed line:

```text
Layer names: ['dense', 'dense_1', 'dense_2']
```

Possible shape line:

```text
Sample output shape: (4, 1)
```

## Hint

It is still `Sequential` because the layers are applied in one straight order with no branches or multiple inputs.

You can also keep this order:

- Define the model.
- Add the layers in order.
- Print the summary.
- Print the layer names.
- Pass a small batch through the model.

## Navigation

- ⬅️ Previous: [03-practice.md](./03-practice.md).
- 🧭 Week Overview: [week-07-overview.md](../week-07-overview.md).
- ➡️ Next: [05-reflection.md](./05-reflection.md).
