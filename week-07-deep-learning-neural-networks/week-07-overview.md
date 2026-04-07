# Week 7 Overview: Deep Learning and Neural Networks

This page is the starting point for Week 7.

## Week Goal

By the end of Week 7, students should be able to explain the basic idea of a neural network, build and evaluate a small
`keras.Sequential` model for classification, and explain when trying a neural network is sensible and when a simpler
earlier workflow is still the better first choice.

## Week 7 as Enrichment

Week 7 expands your toolkit. It does not replace the careful workflow from Weeks 5 and 6.

Week 6 is still the main foundation:

- Define one clear problem.
- Inspect the data before modeling.
- Prepare the data carefully.
- Choose a sensible first model.
- Evaluate honestly.
- Explain the result carefully.

Week 7 adds one optional model family to that same workflow.

You can also work through this week selectively. It is designed as extra depth for students who want a clearer first
look at deep learning and neural networks.

This week helps you practice a useful mindset:

- Deep learning is one possible tool, not an automatic upgrade.
- A simple `scikit-learn` baseline from Week 6 is still a strong choice.
- If you try a neural network, keep the first version small and understandable.
- Do not call a neural network "better" unless you can explain why the data, workflow, and results support that claim.

A small tabular classification workflow with `TensorFlow` and `Keras` can be a sensible starting path. If a simpler
`scikit-learn` model works better for the task, that is still fully valid and often the more practical starting point.

## Week 7 Decision Rule

Use a neural network if the data and question fit, but compare that idea against a simpler baseline before assuming it
is the better first choice.

## Learning Path

### 01. Neural Networks Basics

Start with model choice, problem fit, and the basic language of neural networks.

1. Read Theory: [01-theory.md](./01-neural-networks-basics/01-theory.md).
2. Study Worked Examples: [02-worked-examples.md](./01-neural-networks-basics/02-worked-examples.md).
3. Do Practice: [03-practice.md](./01-neural-networks-basics/03-practice.md).
4. Do Challenge (Optional): [04-challenge.md](./01-neural-networks-basics/04-challenge.md).
5. Write Reflection: [05-reflection.md](./01-neural-networks-basics/05-reflection.md).

### 02. Keras Sequential Models

Learn how to build one small network clearly, without treating architecture size as the main goal.

1. Read Theory: [01-theory.md](./02-keras-sequential-models/01-theory.md).
2. Study Worked Examples: [02-worked-examples.md](./02-keras-sequential-models/02-worked-examples.md).
3. Do Practice: [03-practice.md](./02-keras-sequential-models/03-practice.md).
4. Do Challenge (Optional): [04-challenge.md](./02-keras-sequential-models/04-challenge.md).
5. Write Reflection: [05-reflection.md](./02-keras-sequential-models/05-reflection.md).

### 03. Training, Evaluation, and Prediction

Train, evaluate, and save evidence in a way that still follows the honest workflow from Week 6.

1. Read Theory: [01-theory.md](./03-training-evaluation-prediction/01-theory.md).
2. Study Worked Examples: [02-worked-examples.md](./03-training-evaluation-prediction/02-worked-examples.md).
3. Do Practice: [03-practice.md](./03-training-evaluation-prediction/03-practice.md).
4. Do Challenge (Optional): [04-challenge.md](./03-training-evaluation-prediction/04-challenge.md).
5. Write Reflection: [05-reflection.md](./03-training-evaluation-prediction/05-reflection.md).

### 04. Integration: Keras Classification Workflow

Bring the pieces together and connect them directly to model choice, saved evidence, and clear interpretation.

1. Read Theory: [01-theory.md](04-integration/01-theory.md).
2. Study Worked Examples: [02-worked-examples.md](04-integration/02-worked-examples.md).
3. Do Practice: [03-practice.md](04-integration/03-practice.md).
4. Do Challenge (Optional): [04-challenge.md](04-integration/04-challenge.md).
5. Write Reflection: [05-reflection.md](04-integration/05-reflection.md).

## Week 7 Completion Checklist

- I can explain what a neural network does in simple words.
- I can explain the difference between input, hidden, and output layers.
- I can build a small `keras.Sequential` model with `Dense` layers.
- I can explain why the input shape should match the feature columns.
- I can compile a model with an optimizer, loss, and metric.
- I can train a small model with `fit(...)`.
- I can read basic results from `evaluate(...)`, `predict(...)`, and `history.history`.
- I can explain what evidence I would need before calling a neural network better than a simpler baseline.
- I can explain why a neural network is not automatically the best first choice.
- I can connect Week 7 to the careful workflow from Week 6 without losing clarity.
