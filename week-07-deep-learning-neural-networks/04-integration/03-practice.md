# 03. Practice: Integration

## Setup

1. Create a folder called `week7-keras-integration-practice`.
2. Inside it, create these folders:
   ```text
   data/
   outputs/
   scripts/
   ```
3. Reuse the same `student_completion.csv` dataset from the earlier Week 7 sections.
4. Inside `scripts/`, create `run_keras_classification_workflow.py`.
5. Add this starter code:

```python
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers

keras.utils.set_random_seed(42)

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUTS_DIR = BASE_DIR / "outputs"

OUTPUTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_DIR / "student_completion.csv")

feature_columns = ["study_hours", "practice_sessions", "review_sessions"]
target_column = "completed_course"

X = df[feature_columns].astype("float32")
y = df[target_column].astype("float32")
```

This practice is meant to feel like one complete Keras workflow in one file.

The goal is not to build a large model. The goal is to:

- Keep the workflow organized.
- Save outputs clearly.
- Leave behind enough evidence to explain what happened.

## Tasks

1. Split the data into training and test sets.
2. Build a small binary-classification `Sequential` model.
3. Compile the model clearly for binary classification.
4. Train the model with a validation split.
5. Save the training history to `outputs/training_history.csv`.
6. Create and save a simple training-history plot to `outputs/training_history_plot.png`.
7. Save the model summary to `outputs/model_summary.txt`.
8. Evaluate the model on the test set.
9. Save the test prediction table to `outputs/test_predictions.csv`.
10. Create 3 new cases in a DataFrame.
11. Predict probabilities and labels for the new cases.
12. Save the new-case results to `outputs/new_case_predictions.csv`.
13. Create `outputs/model_choice_note.txt` with:
    - One possible Week 6 baseline model.
    - One sentence explaining why Keras is optional here.
    - One sentence explaining what evidence you would need before claiming Keras is better.
14. Print:
    - The test loss.
    - The test accuracy.
    - The saved-file messages.

## Expected Output Examples

Possible saved-file messages:

```text
Saved: outputs/training_history.csv
Saved: outputs/training_history_plot.png
Saved: outputs/model_summary.txt
Saved: outputs/test_predictions.csv
Saved: outputs/new_case_predictions.csv
Saved: outputs/model_choice_note.txt
```

Your exact metric values will vary a little. That is normal.

## Debug Task 1

Code:

```python
test_results_df.to_csv(DATA_DIR / "student_completion.csv", index=False)
```

Expected behavior:

```text
You wanted to save generated results from the workflow.
```

Actual behavior:

```text
This overwrites the raw dataset instead of keeping the derived output in `outputs/`.
```

## Debug Task 2

Code:

```python
print("Deep learning is definitely the best choice for this problem.")
```

Expected behavior:

```text
You wanted to summarize the result of one trained model.
```

Actual behavior:

```text
This claims too much from one workflow. A careful conclusion should still mention 
limits, dataset size, and the fact that simpler models may remain valid alternatives.
```

## Hint

If the workflow feels large, keep this order:

- Split the data.
- Build the model.
- Compile and train it.
- Save the history outputs.
- Save the model summary.
- Evaluate on the test set.
- Save test predictions.
- Predict new cases.
- Write the short model-choice note.

## Self-Review

- I can run a small Keras workflow from dataset to saved outputs.
- I can keep raw data separate from generated results.
- I can save files that make the workflow easier to review.
- I can describe a neural-network result carefully instead of overselling it.
- I can explain why a simpler Week 6 baseline still belongs in the workflow discussion.

## Navigation

- ⬅️ Previous: [02-worked-examples.md](./02-worked-examples.md).
- 🧭 Week Overview: [week-07-overview.md](../week-07-overview.md).
- ➡️ Next: [04-challenge.md](./04-challenge.md).
