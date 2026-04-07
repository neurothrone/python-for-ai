# 01. Theory: Integration (Keras Classification Workflow)

## Why This Matters

By Week 7, you have seen:

- First machine-learning workflow ideas in Week 5.
- Model comparison and honest evaluation in Week 6.
- Basic neural-network building and training in Week 7.

This section brings those ideas together into one complete Keras workflow.

The most important idea is this:

Week 6 is still the normal starting point.
Week 7 adds an optional extension path.

## A Good Deep Learning Workflow

For this week, a healthy Week 7 workflow looks like this:

1. Define one clear classification question.
2. Choose manageable numeric features.
3. Think about a simple baseline first.
4. Split the data honestly.
5. Build a small network first.
6. Train and evaluate it.
7. Save useful outputs.
8. Describe the result carefully.

That is much stronger than trying to build an ambitious model without a clear workflow.

## Week 7 as a Deeper Workflow Example

Week 7 does not mean every task should become a deep learning task.

Instead, it helps you make a better model choice.

For many beginners, the most practical path is:

1. Start with a simpler `scikit-learn` baseline.
2. Make sure the question, data, and evaluation are clear.
3. Try Keras only if it genuinely adds something useful or interesting.

A neural network may be a sensible choice when:

- The problem is classification.
- The data is numeric or can be prepared clearly.
- You have enough time to train, evaluate, and explain the workflow.

A simpler Week 6 model may still be better when:

- The dataset is small.
- Interpretability matters a lot.
- You need a faster, easier-to-explain baseline.

## Saved Evidence Still Matters

Whether you use `scikit-learn` or Keras, the workflow should leave clear evidence behind.

Useful Week 7 evidence can include:

- Training history.
- A history plot.
- A model summary.
- Test predictions.
- New-case predictions.
- A short, careful conclusion.

## Keep the First Version Small

For a beginner workflow, a good first version is often like this:

- One dataset.
- One clear target.
- One small network.
- One honest evaluation setup.
- One short explanation of limitations.

That is usually better than adding many layers before you understand whether the workflow is working.

## Save Useful Outputs

The workflow becomes easier to review and explain when you save useful outputs such as:

- Training history.
- A history plot.
- Test predictions.
- Model summary.
- New-case predictions.

This helps both the student and the assessor follow what happened.

## Honest Interpretation Still Matters

A careful Week 7 conclusion can sound like this:

- The model learned a useful pattern on this dataset.
- The result is encouraging, but the dataset is still limited.
- A neural network is one working option, not final proof that it is the best option.

That kind of language is especially important because the goal here is workflow quality, not the most advanced-sounding
tool.

## Common Mistakes

- Choosing a neural network before defining the question clearly.
- Skipping a sensible baseline idea and jumping straight to Keras.
- Building a larger model when a small first model has not been understood yet.
- Forgetting to save outputs that explain the workflow.
- Overwriting raw data with generated files.
- Treating one test score as final proof that deep learning was the best choice.

## Navigation

- ⬅️ Previous: [05-reflection.md](../03-training-evaluation-prediction/05-reflection.md).
- 🧭 Week Overview: [week-07-overview.md](../week-07-overview.md).
- ➡️ Next: [02-worked-examples.md](./02-worked-examples.md).
