# 03. Practice: Integration

## Tasks

1. Create a class `Calculator` with `self.history = []` in `__init__`.
2. Add methods `add(x, y)` and `subtract(x, y)` that return results.
3. In each method, store a string in history like `"8 - 3 = 5"`.
4. Add method `show_history()` that prints all rows in `self.history`.
5. Create one calculator object.
6. Run at least three operations.
7. Call `show_history()`.
8. Predict output before running:

```python
class Calculator:
    def __init__(self):
        self.history = []

    def add(self, x, y):
        result = x + y
        self.history.append(f"{x} + {y} = {result}")
        return result

calc = Calculator()
print(calc.add(2, 6))
print(calc.history)
```

## Expected Output Examples

Task 7 possible output:

```text
5 + 3 = 8
8 - 2 = 6
4 + 1 = 5
```

Task 8 expected output:

```text
8
['2 + 6 = 8']
```

## Debug Task 1

Find and fix the bug:

```python
class Calculator:
    def __init__(self):
        history = []

    def add(self, x, y):
        result = x + y
        self.history.append(f"{x} + {y} = {result}")
        return result
```

Expected behavior:

```text
Each add() call should save a row to calculator history.
```

Actual behavior:

```text
It raises an AttributeError because history was not saved as self.history.
```

## Debug Task 2

Find and fix the bug:

```python
class Calculator:
    def __init__(self):
        self.history = []

    def add(self, x, y):
        result = x + y
        self.history.append(f"{x} + {y} = {result}")

calc = Calculator()
value = calc.add(3, 2)
print(value + 1)
```

Expected behavior:

```text
add(3, 2) should return 5 so value + 1 prints 6.
```

Actual behavior:

```text
It raises a TypeError because add() does not return the result.
```

## Self-Review

- I can combine methods and state in one class.
- I can keep history in a list attribute.
- I can print saved history correctly.
- I can debug missing self and missing return issues.

## Navigation

- ⬅️ Previous: [02-worked-examples.md](./02-worked-examples.md).
- 🧭 Week Overview: [week-03-overview.md](../week-03-overview.md).
- ➡️ Next: [04-challenge.md](./04-challenge.md).
