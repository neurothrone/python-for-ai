# 01. Theory: Neural Networks Basics

## Why This Matters

In Week 6, you practiced a clearer workflow:

- Define the problem.
- Inspect the data.
- Choose a sensible model.
- Evaluate honestly.
- Explain the result carefully.

Week 7 does not replace that workflow. It adds one more possible model family: neural networks.

Neural networks matter because they are widely used in modern AI work. They can learn flexible patterns, but they also
need careful setup, honest evaluation, and realistic expectations.

For this week, the main goal is not to build a complicated model. It is to understand when a small neural network is a
reasonable tool and when a simpler model is still the better first choice.

## Start With the Question, Not the Model

Before you choose deep learning, ask:

- What am I trying to predict or classify?
- Is the data suitable for this?
- Do I already have a sensible, simpler baseline?
- Will a neural network make the workflow clearer, or only more complicated?

That is the same habit you practiced in Week 6.

## A Neural Network in Simple Words

A neural network is a model made of layers. Each layer takes numbers in, transforms them, and passes new numbers to the
next layer.

For a simple tabular classification task, the network learns from feature columns such as:

- `study_hours`.
- `practice_sessions`.
- `review_sessions`.

Then it produces an output such as:

- `0` for `not_completed`.
- `1` for `completed`.

In other words, it is still a model that learns from features and predicts a target. The main difference is how it
transforms the inputs on the way to the final prediction.

## Input, Hidden, and Output Layers

- The input layer receives the feature values.
- One or more hidden layers transform those values.
- The output layer produces the final prediction.

For a small binary classification model, the output layer often has one unit.

## Weights and Activations

Each connection in the network has a weight. During training, the model adjusts these weights so that the predictions
match the real labels better over time.

Layers also use activation functions.

Two common examples are:

- `relu` in hidden layers.
- `sigmoid` in the output layer for binary classification.

You do not need to memorize the math. The important idea is:

- The weights store what the model has learned.
- The activation helps transform the values usefully.

## Why Shape Matters

Neural networks expect inputs with a specific shape.

If your model uses three feature columns, then the input shape should match those three values.

Example:

- Features: `study_hours`, `practice_sessions`, `review_sessions`.
- Input shape: `(3,)`.

This matters because the model needs to know how many input values each row contains.

## Neural Networks vs. Earlier Models

Compared with Week 6 models:

- `k-NN` predicts by comparing distances to nearby rows.
- A decision tree predicts by following rule-like splits.
- A neural network learns layer-by-layer numeric transformations.

This means a neural network can feel less immediately interpretable than a decision tree. That is one reason it should
be chosen because it fits the problem, not because it sounds more advanced.

## When a Small Neural Network Is a Sensible First Step

A small dense neural network can be a sensible first step when:

- The problem is classification.
- The data is already numeric or easy to convert into numbers.
- You want to learn the `TensorFlow`/`Keras` workflow.
- You keep the first version small and manageable.

It is less sensible when:

- The dataset is tiny, and you want the simplest explanation possible.
- You have not yet chosen a clear target.
- You are treating deep learning as an automatic shortcut to better results.
- You have not yet tried a simpler baseline that already fits the task well.

## When a Simpler Week 6 Model May Be Better

A Week 6 model such as `k-NN` or a decision tree may still be the better starting point when:

- The data is small and tabular.
- You want a faster path to a clear first result.
- Interpretability matters.
- The workflow needs to stay easy to explain.

This is why Week 7 should feel like "one more possible path" not "the real work starts now".

## A Good Week 7 Mindset

For this week, a healthy mindset is:

1. Start small.
2. Keep the problem and target clear.
3. Keep the feature columns clear.
4. Make sure the data suits the task.
5. Build a simple network first.
6. Train and evaluate honestly.
7. Compare your deep learning idea with simpler options before assuming it is the best path.

## A Simple Week 7 Decision Rule

Use a neural network if the data and question fit, but compare that idea against a simpler baseline before assuming it
is the better first choice.

## Common Mistakes

- Choosing the model before defining the question clearly.
- Forgetting that the model input shape must match the feature columns.
- Keeping labels as unclear text values when the workflow expects a numeric target.
- Thinking more layers automatically means a better model.
- Expecting an untrained model to give meaningful predictions.
- Treating "deep learning" as a reason by itself instead of starting from the problem.
- Forgetting that Week 6 workflow habits still apply.

## Navigation

- 🧭 Week Overview: [week-07-overview.md](../week-07-overview.md).
- ➡️ Next: [02-worked-examples.md](./02-worked-examples.md).
