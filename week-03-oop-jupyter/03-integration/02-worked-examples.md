# 02. Worked Examples: Integration

## Example A: Add History to a Calculator

```python
class Calculator:
    def __init__(self):
        self.history = []

    def add(self, x, y):
        result = x + y
        self.history.append(f"{x} + {y} = {result}")
        return result

calc = Calculator()
print(calc.add(5, 3))
print(calc.history)
```

## Example B: Add More Operations

```python
class Calculator:
    def __init__(self):
        self.history = []

    def subtract(self, x, y):
        result = x - y
        self.history.append(f"{x} - {y} = {result}")
        return result

calc = Calculator()
calc.subtract(9, 2)
print(calc.history)
```

## Example C: Show History Method

```python
class Calculator:
    def __init__(self):
        self.history = []

    def add(self, x, y):
        result = x + y
        self.history.append(f"{x} + {y} = {result}")
        return result

    def show_history(self):
        for row in self.history:
            print(row)

calc = Calculator()
calc.add(1, 4)
calc.add(10, 5)
calc.show_history()
```

## Navigation

- ⬅️ Previous: [01-theory.md](./01-theory.md).
- 🧭 Week Overview: [week-03-overview.md](../week-03-overview.md).
- ➡️ Next: [03-practice.md](./03-practice.md).
