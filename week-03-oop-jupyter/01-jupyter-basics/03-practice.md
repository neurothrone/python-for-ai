# 03. Practice: Jupyter Basics

## Tasks

1. Create a notebook with one Markdown title.
2. Create a code cell with `videos = ["Intro", "Loops", "Functions"]`.
3. Print the full list.
4. Add `"OOP"` using `append` and print again.
5. Insert `"Jupyter"` at index `1` and print again.
6. Remove `"Loops"` and print again.
7. Add one cell that prints the number of items with `len(videos)`.
8. Predict output before running:

```python
items = ["A", "B"]
items.append("C")
print(items)
```

## Expected Output Examples

Task 3 possible output:

```text
['Intro', 'Loops', 'Functions']
```

Task 6 possible output:

```text
['Intro', 'Jupyter', 'Functions', 'OOP']
```

Task 8 expected output:

```text
['A', 'B', 'C']
```

## Debug Task 1

Cell 1:

```python
print(videos)
```

Cell 2:

```python
videos = ["Intro", "Loops"]
```

Expected behavior:

```text
The notebook should print the list value.
```

Actual behavior:

```text
It raises a NameError because the setup cell was not run first.
```

## Debug Task 2

```python
videos = ["Intro", "Loops", "Functions"]
videos.remove("OOP")
print(videos)
```

Expected behavior:

```text
You expected to remove one value from the list.
```

Actual behavior:

```text
It raises a ValueError because "OOP" is not in the list.
```

## Self-Review

- I can create and run Markdown and code cells.
- I run setup cells before usage cells.
- I can use `append`, `insert`, and `remove` on lists.
- I can restart and run all when output is confusing.

## Navigation

- ⬅️ Previous: [02-worked-examples.md](./02-worked-examples.md).
- 🧭 Week Overview: [week-03-overview.md](../week-03-overview.md).
- ➡️ Next: [04-challenge.md](./04-challenge.md).
