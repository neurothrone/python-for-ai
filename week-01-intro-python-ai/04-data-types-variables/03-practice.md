# 03. Practice: Data Types and Variables

## Tasks

1. Create variables for name, age, and student status.
2. Print one sentence using all variables.
3. Ask for two numbers and print:
    - The sum `(x + y)`
    - The difference `(x - y)`
    - The product `(x * y)`
4. Convert `"42"` to an integer and add `8`.

## Expected Output Examples

Task 2 example output:

```text
Nora is 21 years old. Student: True
```

Task 4 example output:

```text
50
```

## Debug Task

Find and fix the bug:

```python
value = "3.14"
number = int(value)
print(number)
```

Expected behavior:

```text
The program should print 3.14 as a number.
```

Actual behavior:

```text
It raises a ValueError because int() cannot convert a decimal string like "3.14".
```

## Self-Review

- I used `str`, `int`, `float`, or `bool` intentionally.
- I used clear variable names.
- I converted input before doing arithmetic.

## Navigation

- ⬅️ Previous: [02-worked-examples.md](./02-worked-examples.md).
- 🧭 Week Overview: [week-01-overview.md](../week-01-overview.md).
- ➡️ Next: [04-challenge.md](./04-challenge.md).
