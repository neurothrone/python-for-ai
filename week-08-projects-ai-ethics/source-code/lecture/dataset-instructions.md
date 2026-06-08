# Dataset Instructions

This demo uses the **Research Grade Type 2 Diabetes Dataset** from Kaggle:
et
https://www.kaggle.com/datasets/mubasharahmedrabbani/type-2-diabetes-risk-dataset

The dataset is large, so it is not included in this source-code folder.

## What To Download

Download the dataset from Kaggle and make sure you have this CSV file:

```text
research_grade_type2_diabetes_dataset_v3.csv
```

If the downloaded file is inside a `.zip` file, unzip it first.

## Where To Put The CSV File

Put `research_grade_type2_diabetes_dataset_v3.csv` in one of these places:

- The same folder as `01_demo_ethics_data_inspection.py`.
- A `data` folder next to `01_demo_ethics_data_inspection.py`.

Recommended structure:

```text
project_folder/
├── 01_demo_ethics_data_inspection.py
├── data/
│   └── research_grade_type2_diabetes_dataset_v3.csv
├── dataset-instructions.md
└── requirements.txt
```

## Run The Demo

Install the dependency if needed:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python 01_demo_ethics_data_inspection.py
```

The script does not train a model. It only inspects selected columns to support ethical reflection.
