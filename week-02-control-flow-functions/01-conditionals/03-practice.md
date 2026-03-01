# 03. Practice: Conditionals

## Tasks

1. Ask for temperature and print `Cold`, `Warm`, or `Hot`.
2. Ask for a number and print whether it is even or odd.
3. Ask for username and password and print `Login success` only if both are correct.
4. Ask for age and print whether the user can vote (`18` or older).
5. Ask for exam score and print grade level (`A`, `B`, `C`, `F`) using simple ranges.
6. Ask for two numbers and print which one is larger. If equal, print `Same value`.
7. Predict output before running:

```python
x = 12
if x > 10:
    print("A")
if x > 15:
    print("B")
else:
    print("C")
```

## Expected Output Examples

Task 2 example output if input is `9`:

```text
Odd
```

Task 4 example output if input is `22`:

```text
Can vote
```

Task 6 example output if inputs are `11` and `4`:

```text
11 is larger
```

Task 7 expected output:

```text
A
C
```

## Debug Task 1

Find and fix the bug:

```python
age = input("Enter age: ")
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Expected behavior:

```text
If 20 is entered, the program should print Adult.
```

Actual behavior:

```text
It raises a TypeError because age is text from input() and is compared to a number.
```

## Debug Task 2

Find and fix the bug:

```python
score = int(input("Enter score: "))
if score >= 90:
print("A")
elif score >= 75:
    print("B")
else:
    print("C")
```

Expected behavior:

```text
The program should print one grade based on score.
```

Actual behavior:

```text
It raises an IndentationError because the first print line is not indented.
```

## Self-Review

- I used `if` / `elif` / `else` correctly.
- I converted input to `int` where needed.
- I tested boundary values (like `18`, `75`, `90`).
- I fixed both type and indentation bugs.

## Quick Reference

- [Python Operators Reference](../../resources/python-operators-reference.md)

## Navigation

- ⬅️ Previous: [02-worked-examples.md](./02-worked-examples.md).
- 🧭 Week Overview: [week-02-overview.md](../week-02-overview.md).
- ➡️ Next: [04-challenge.md](./04-challenge.md).
