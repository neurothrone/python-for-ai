# 04. Challenge: Neural Networks Basics

## Challenge Tasks

1. Create `study_followthrough.csv` with this content:
   ```text
   study_hours,practice_sessions,review_sessions,completed_course
   1,0,1,0
   2,1,1,0
   2,2,2,0
   3,2,2,0
   3,3,3,1
   4,2,3,0
   4,3,3,1
   5,3,4,1
   6,4,5,1
   ```
2. Imagine the question is:
   "Can we classify whether a student is likely to complete the course from a few study-related signals?"
3. Build a small neural network with:
    - Input shape `(3,)`.
    - One hidden layer.
    - One output layer with `sigmoid`.
4. Print `model.summary()`.
5. Print the input shape and output shape for a small sample batch.
6. Write 3 short sentences:
    - One sentence explaining what the output layer means for this binary problem.
    - One sentence that says whether Keras feels sensible for this dataset.
    - One sentence naming one simpler Week 6 baseline you would compare against the first.

This challenge is meant to push you one step beyond the practice task by changing the dataset and asking you to make a
small model choice yourself.

## Expected Output Example

Possible summary idea:

```text
The output shape ends with 1 because the model gives one probability-like value for each row.
```

Possible shape lines:

```text
Sample batch shape: (3, 3)
Sample output shape: (3, 1)
```

## Hint

One simple model is:

```python
keras.Sequential(
    [
        keras.Input(shape=(3,)),
        layers.Dense(4, activation="relu"),
        layers.Dense(1, activation="sigmoid"),
    ]
)
```

You still want the same habits as before:

- Keep the input shape matched to 3 feature columns.
- Keep the model small.
- Use one output unit for this binary task.
- Read the summary before trusting the model.

## Navigation

- ⬅️ Previous: [03-practice.md](./03-practice.md).
- 🧭 Week Overview: [week-07-overview.md](../week-07-overview.md).
- ➡️ Next: [05-reflection.md](./05-reflection.md).
