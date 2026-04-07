# 01. Theory: Keras Sequential Models

## Why This Matters

Once you understand the basic idea of a neural network, you need a practical way to build one.

In Week 7, we use `keras.Sequential` because it is a clean beginner-friendly way to define a model as a simple stack of
layers.

This works well for small course examples where:

- One input goes in.
- Layers are applied one after another.
- One prediction comes out.

The important point is that `Sequential` helps you build the model clearly. It does not decide whether a neural network
is the right tool for the task in the first place.

## What `Sequential` Means

A `Sequential` model is a straight layer stack.

In simple words:

1. The first layer receives the input.
2. The next layer receives the previous layer's output.
3. This continues until the output layer produces the prediction.

This is a good fit for the kind of small tabular classification workflow we want this week.

## What `Sequential` Does Not Decide

`Sequential` helps with model structure, but it does not answer these workflow questions for you:

- Is the problem clear?
- Is the data suitable?
- Should I start with a simpler baseline first?
- Do I have enough evidence to say this model is worth using?

Those are still workflow questions from Weeks 5 and 6.

## When `Sequential` Is a Good Choice

`Sequential` is a good choice when:

- The model is a plain stack of layers.
- The data has one input path.
- You want a clear starting workflow.

It is not the best fit when the model needs:

- Multiple inputs.
- Multiple outputs.
- Branching paths.
- More complex architectures.

You do not need those advanced cases for this week.

## Why Start With `keras.Input(...)`

When you already know how many features you have, it is a good habit to define the input shape clearly.

Example:

```python
keras.Input(shape=(3,))
```

This makes it easier to:

- Confirm the intended model shape.
- Print `model.summary()`.
- Notice shape mistakes earlier.

It also supports a useful habit: make the plan visible instead of guessing.

## Dense Layers in Simple Words

A `Dense` layer means every unit in one layer connects to every unit in the next layer.

For small tabular examples, `Dense` layers are a natural starting point.

Example:

```python
layers.Dense(8, activation="relu")
```

This means:

- The layer has 8 units.
- It uses `relu` as the activation function.

## A Small Binary Classification Pattern

A common pattern is:

```python
keras.Sequential(
    [
        keras.Input(shape=(3,)),
        layers.Dense(8, activation="relu"),
        layers.Dense(4, activation="relu"),
        layers.Dense(1, activation="sigmoid"),
    ]
)
```

Why this shape makes sense:

- Hidden layers use `relu`.
- The output layer uses `sigmoid`.
- One output unit matches a binary target such as `0` or `1`.

This is a first model, not a claim that more layers are always better.

## Keep the First Architecture Small

For this week, small is a strength.

A smaller first model is easier to:

- Explain.
- Debug.
- Compare with a simpler baseline.
- Connect to the rest of the workflow.

## Why `model.summary()` Is So Useful

`model.summary()` is one of the best debugging tools in Keras.

It helps you check:

- Output shapes.
- Layer order.
- Parameter counts.

This is especially useful when you are building a model for the first time and want to confirm that your architecture
matches your plan.

## Common Mistakes

- Choosing an architecture before checking whether the dataset really fits the task.
- Forgetting to define the input shape clearly.
- Using a final layer that does not match the task.
- Adding many layers before understanding a small model.
- Treating `Sequential` as the only model style Keras can use.
- Reading `model.summary()` too quickly and missing a shape mismatch.
- Treating architecture size as more important than questioning clarity and evaluation quality.

## Navigation

- ⬅️ Previous: [05-reflection.md](../01-neural-networks-basics/05-reflection.md).
- 🧭 Week Overview: [week-07-overview.md](../week-07-overview.md).
- ➡️ Next: [02-worked-examples.md](./02-worked-examples.md).
