# 01. Theory: Jupyter Basics

## Why This Matters

Jupyter helps beginners test code in small steps. You can run one cell, check output, and fix mistakes quickly.

## Where You Can Use It

You can use notebooks in different places:

- Jupyter Notebook or JupyterLab on your computer.
- VS Code with notebook support.
- PyCharm with Jupyter notebook support.
- Google Colab in the browser: https://colab.research.google.com/

Google Colab is useful when you want a quick start without local setup.

## What Is a Notebook

A notebook has cells.

- Code cells run Python.
- Markdown cells hold notes.

## Running Cells

- `Shift + Enter` runs the selected cell.
- Run cells from top to bottom.

This keeps results predictable.

## Notebook State in Simple Words

Notebook memory stays active while the kernel is running.
If you run cells out of order, values may be missing or outdated.

```python
numbers = [2, 4, 6]
print(numbers)
```

If `print(numbers)` runs before the list is created, it fails.

## Light List Practice in Jupyter

Lists are useful for storing many values.

```python
fruits = ["apple", "banana", "orange"]
```

Useful list actions:

- `append(value)` adds at the end.
- `insert(index, value)` adds at a specific position.
- `remove(value)` removes the first matching value.

Lists are ordered and mutable. Ordered means index positions matter. Mutable means the list can change after creation.

## Common Beginner Mistakes

- Running later cells before setup cells.
- Editing a cell but forgetting to run it again.
- Mixing notes into code cells.
- Forgetting that list values stay in memory between runs.

## Navigation

- 🧭 Week Overview: [week-03-overview.md](../week-03-overview.md).
- ➡️ Next: [02-worked-examples.md](./02-worked-examples.md).
