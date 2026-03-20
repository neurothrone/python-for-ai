# 01. Theory: Seaborn Basics

## Why This Matters

Matplotlib gives you the core plotting tools. Seaborn builds on that and makes many common data charts easier to create
when you already have your data in a table such as a Pandas DataFrame. This matters because real workflows in data
analysis often involve Pandas plus a plotting library working together.

Seaborn is also useful because it can help your charts look clear with less code. You still need to inspect your data,
choose a sensible chart, and label it well, but Seaborn can reduce some of the manual work. That leaves more attention
for reading the data and building confidence before later machine learning tasks.

## What Seaborn Is

Seaborn is a Python data visualization library. It works especially well with Pandas DataFrames.

A common import is:

```python
import seaborn as sns
```

## Seaborn and Matplotlib Together

You will often see both imports in the same script:

```python
import matplotlib.pyplot as plt
import seaborn as sns
```

Why both?

- Seaborn creates the chart.
- Matplotlib is still often used for title, axis labels, and `show()`.

A clear pattern is:

```python
fig, ax = plt.subplots()
sns.scatterplot(data=df, x="hours_studied", y="test_score", ax=ax)
```

Here:

- `fig` is the full figure.
- `ax` is the chart area.
- `ax=ax` tells Seaborn where to draw the chart.

This is useful because it keeps Seaborn connected to the same `fig, ax` pattern used in Matplotlib.

## Beginner-Friendly Plot Types

This week, keep Seaborn simple:

- `sns.barplot(...)` for category comparison.
- `sns.scatterplot(...)` for two numeric columns.
- `sns.lineplot(...)` for simple ordered data.

## Working with `data=`, `x=`, and `y=`

Seaborn often uses this style:

```python
fig, ax = plt.subplots()
sns.scatterplot(data=df, x="hours_studied", y="test_score", ax=ax)
```

- `data=df` tells Seaborn which DataFrame to use.
- `x="hours_studied"` tells it which column to put on the x-axis.
- `y="test_score"` tells it which column to put on the y-axis.
- `ax=ax` tells Seaborn which axes to use.

This is beginner-friendly because you can name columns directly instead of pulling them out one by one.

Another clear pattern is to store the column names in small variables:

```python
x_column = "hours_studied"
y_column = "test_score"
```

That can make the chart code easier to read, especially when you are seeing Seaborn for the first time.

## Simple Styling with Seaborn

One reason Seaborn is so great is because it allows you to modify the styling of charts with little code. For example:

```python
sns.set_theme(style="whitegrid")
```

This changes the general look of the chart. You can also pass a color:

```python
sns.lineplot(data=df, x="hours_studied", y="test_score", color="teal", ax=ax)
```

You do not need many of the style options at this early stage, but it is enough to know that Seaborn is designed to make
common chart styles easy to use.

## Why It Helps Before Machine Learning

Seaborn is useful before linear regression because a scatter plot can help you look at a feature and a target together.
If the points seem to rise or fall in a simple pattern, that can make the next machine learning step easier to
understand.

## Common Mistakes

- Forgetting to import Seaborn.
- Using a wrong column name in `x=` or `y=`.
- Forgetting that Seaborn still needs `plt.show()` in a script.
- Plotting before the DataFrame exists.
- Confusing a category column with a numeric column.
- Adding no title or labels, so the chart is hard to explain.
- Forgetting that `x=` and `y=` should match the question you want the chart to answer.

## Resources

- [Seaborn Documentation](https://seaborn.pydata.org/)

## Navigation

- ⬅️ Previous: [05-reflection.md](../01-matplotlib-basics/05-reflection.md).
- 🧭 Week Overview: [week-05-overview.md](../week-05-overview.md).
- ➡️ Next: [02-worked-examples.md](./02-worked-examples.md).
