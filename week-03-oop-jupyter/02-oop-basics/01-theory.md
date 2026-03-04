# 01. Theory: OOP Basics

## Why This Matters

Classes help you keep related data and actions together. This makes code easier to understand as programs grow.

## Class and Object

- A class is a blueprint.
- An object is one real instance from that blueprint.

```python
class Book:
    pass

book1 = Book()
```

## Attributes

Attributes store object data.

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
```

`self.title` and `self.author` are object attributes.

## Methods

Methods are functions inside a class.

```python
class Book:
    def __init__(self, title):
        self.title = title

    def show_title(self):
        print(self.title)
```

## `self` in Simple Words

`self` means **this object**.
Use it to read or update the current object's attributes.

## Common Beginner Mistakes

- Missing `self` in `__init__` or other methods.
- Creating an object with the wrong number of arguments.
- Confusing attribute access and method call.
- Forgetting `()` when calling methods.

## Navigation

- ⬅️ Previous: [05-reflection.md](../01-jupyter-basics/05-reflection.md).
- 🧭 Week Overview: [week-03-overview.md](../week-03-overview.md).
- ➡️ Next: [02-worked-examples.md](./02-worked-examples.md).
