# 02. Worked Examples: Jupyter Basics

## Example A: Markdown + Code

Markdown cell text:

```text
## Quick Test
I will store numbers in a list and print them.
```

Code cell:

```python
numbers = [10, 20, 30]
print(numbers)
```

## Example B: Cell Order

Cell 1:

```python
city = "Stockholm"
```

Cell 2:

```python
print(city.upper())
```

Run Cell 1 first, then Cell 2.

## Example C: List Actions

```python
videos = ["Intro", "Loops", "Functions"]
videos.append("OOP")
videos.insert(1, "Jupyter")
videos.remove("Loops")
print(videos)
```

Expected output:

```text
['Intro', 'Jupyter', 'Functions', 'OOP']
```

## Example D: Mutable Behavior

```python
topics = ["Python", "AI"]
more_topics = topics
more_topics.append("Data")
print(topics)
```

Both names point to the same list object, so `topics` also changes.

## Navigation

- ⬅️ Previous: [01-theory.md](./01-theory.md).
- 🧭 Week Overview: [week-03-overview.md](../week-03-overview.md).
- ➡️ Next: [03-practice.md](./03-practice.md).
