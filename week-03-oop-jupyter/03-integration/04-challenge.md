# 04. Challenge: Integration

## Challenge Tasks

1. Extend `Calculator` with methods `multiply(x, y)` and `divide(x, y)`.
2. Store all operation rows in `self.history`.
3. In `divide`, if `y == 0`, store `"Cannot divide by zero"` in history and return `None`.
4. Add method `clear_history()` that removes all history rows.
5. Test this order: add, divide by zero, multiply, show history, clear history, show history again.

## Expected Output Example

Possible output before clear:

```text
5 + 3 = 8
Cannot divide by zero
4 * 2 = 8
```

Possible output after clear:

```text
(no rows printed)
```

## Hint

Keep methods small. One method does one job.

## Navigation

- ⬅️ Previous: [03-practice.md](./03-practice.md).
- 🧭 Week Overview: [week-03-overview.md](../week-03-overview.md).
- ➡️ Next: [05-reflection.md](./05-reflection.md).
