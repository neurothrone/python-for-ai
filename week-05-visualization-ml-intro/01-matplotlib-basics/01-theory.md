# 01. Theory: Matplotlib Basics

## Why This Matters

When you work with data, numbers alone are often hard to read. A simple chart can help you notice patterns, compare
values, and explain your results to someone else. This matters in real work because people often understand a visual
faster than a table of raw numbers.

Matplotlib is one of the main plotting libraries in Python. It gives you a practical first workflow: load data, inspect
it, choose a simple plot, label it clearly, and show the result. That same workflow will support later course work when
you explore bigger datasets and start building machine learning projects.

## What Matplotlib Does

Matplotlib is a Python library for making charts.

Matplotlib has many modules for different jobs. For example:

- `matplotlib.pyplot` is used for creating and showing plots.
- `matplotlib.table` can be used to place table-like data inside a figure.
- `matplotlib.colorbar` is used when a chart needs a color scale.

In this course, we focus on `matplotlib.pyplot` because it is the most useful starting point for learning plotting.

This week, we keep it simple and focus on:

- Line plots for values that change across an order such as days.
- Bar charts for comparing categories.
- Scatter plots for checking whether two numeric columns seem related.

## Common Workflow

1. Load the data.
2. Inspect the columns and a few rows.
3. Choose one simple plot type.
4. Add a title.
5. Add axis labels.
6. Show the plot.
7. Say one simple thing the chart seems to show.

## Basic Import

Most examples use this import:

```python
import matplotlib.pyplot as plt
```

`pyplot` gives you common plotting functions such as `plot()`, `bar()`, `scatter()`, `title()`, `xlabel()`, `ylabel()`,
and `show()`.

## The `fig, ax` Pattern

You can make charts with direct `plt.plot(...)` style code, but a clearer pattern is:

```python
fig, ax = plt.subplots()
```

- `fig` means the full figure window.
- `ax` means one set of axes inside that figure.

This is useful because it makes the chart parts more visible:

```python
ax.plot(x_values, y_values)
ax.set_title("Weekly Sales")
ax.set_xlabel("Day")
ax.set_ylabel("Sales")
```

This style also prepares students for later work with multiple charts in one figure.

## Simple Plot Types

### Line Plot

Use a line plot when the order matters, such as day 1, day 2, day 3.

```python
ax.plot(days, sales)
```

It is useful when you want to notice movement across an order, such as rising, falling, or turning points.

### Bar Chart

Use a bar chart when you want to compare categories.

```python
ax.bar(products, sales)
```

It is useful when you want to compare the size of separate values more directly.

### Scatter Plot

Use a scatter plot when you want to compare two numeric columns.

```python
ax.scatter(hours, scores)
```

This is especially useful before linear regression because it can show whether the points move in a rough upward or
downward pattern.

## Titles and Labels

Without labels, a plot is hard to understand.

```python
ax.set_title("Weekly Sales")
ax.set_xlabel("Day")
ax.set_ylabel("Sales")
```

Try to answer these questions with labels:

- What is this chart about?
- What does the x-axis mean?
- What does the y-axis mean?

## `plt.show()`

`plt.show()` displays the plot window in a normal Python script.

```python
plt.show()
```

If you forget this in a script, the chart may not appear.

## Simple Customization

You can also change the size and style of a chart.

```python
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(days, sales, color="green", linestyle="--", linewidth=2)
ax.set_title("Weekly Sales", fontsize=14)
```

Useful options:

- `figsize=(8, 4)` changes figure width and height.
- `fontsize=14` changes text size.
- `color="green"` changes line color.
- `linestyle="--"` changes line style.
- `linewidth=2` changes line thickness.

You do not need all of these at once. The goal is to know that customization is possible.

## Multiple Charts with Subplots

`plt.subplots(...)` can also create more than one chart in one figure.

```python
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
```

Here:

- `1` means one row.
- `2` means two columns.
- `axes[0]` is the first chart.
- `axes[1]` is the second chart.

This is useful when you want to compare two chart types side by side.

## Clearing and Closing Figures

When you make many figures, it is good to know two cleanup actions:

```python
fig.clf()
plt.close(fig)
```

- `fig.clf()` clears the content inside the figure.
- `plt.close(fig)` closes the figure and releases it from memory.

For small scripts, you may not need these every time. They become more useful when you create many charts or save charts
in longer scripts.

## Save vs. Show

This week, showing the chart is enough in most examples. Later you may also save plots to files. When you save outputs,
keep them separate from raw data files. That makes your workflow easier to understand and safer to debug.

## Common Mistakes

- Forgetting `import matplotlib.pyplot as plt`.
- Trying to plot before the data is loaded.
- Using the wrong column name.
- Making a plot with text values where numeric values are needed.
- Forgetting `plt.show()` in a script.
- Adding no title or axis labels, so the chart is hard to read.
- Mixing up which values should go on the x-axis and y-axis.
- Forgetting that `plot(x, y)` means x-axis values first and y-axis values second.
- Making many figures without closing them in longer scripts.

## Resources

- [Matplotlib Documentation](https://matplotlib.org/stable/index.html)
- [Matplotlib Cheat Sheets](https://matplotlib.org/cheatsheets/)

## Navigation

- 🧭 Week Overview: [week-05-overview.md](../week-05-overview.md).
- ➡️ Next: [02-worked-examples.md](./02-worked-examples.md).
