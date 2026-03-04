# 01. Theory: Integration (Functions + State)

## Why This Matters

In Week 2, you used functions for operations like `add` and `subtract`. In Week 3, you add state, for example, a history
list, so your program can remember previous results.

## From Functions to Class

Week 2 style (functions only):

- `add(x, y)`
- `subtract(x, y)`
- `multiply(x, y)`
- `divide(x, y)`

Week 3 integration style (class and state):

- Methods do calculations.
- One attribute stores history, for example `self.history = []`.

## State in Simple Words

State means stored data that can change over time.

```python
self.history = []
```

Every calculation can append a new text row such as `"5 + 3 = 8"`.

## Encapsulation and Abstraction (Beginner View)

- **Encapsulation**: keep data and methods that belong together in one class.
- **Abstraction**: use simple method names (`add`, `show_history`) without showing internal details each time.

You only need the basic idea this week.

## Example Shape

```python
class Calculator:
    def __init__(self):
        self.history = []

    def add(self, x, y):
        result = x + y
        self.history.append(f"{x} + {y} = {result}")
        return result
```

## Common Beginner Mistakes

- Forgetting to create `self.history` in `__init__`.
- Using `history.append(...)` instead of `self.history.append(...)`.
- Forgetting to return a result.
- Calling methods on the class instead of on an object.

## Navigation

- ⬅️ Previous: [05-reflection.md](../02-oop-basics/05-reflection.md).
- 🧭 Week Overview: [week-03-overview.md](../week-03-overview.md).
- ➡️ Next: [02-worked-examples.md](./02-worked-examples.md).
