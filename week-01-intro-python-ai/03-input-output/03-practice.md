# 03. Practice: Input and Output

## Tasks

1. Ask for a first name and last name, then print the full name.
2. Ask for two integers and print their sum.
3. Ask for a city and print a welcome message.
4. Ask for birth year and estimate current age.

## Expected Output Examples

Task 1 example output:

```text
Ada Lovelace
```

Task 2 example output:

If `12` and `5` were inputted:

```text
17
```

## Debug Task 1

Find and fix the bug:

```python
age = input("Enter your age: ")
print(age + 1)
```

Expected behavior:

```text
If 20 is entered, the program should print 21.
```

Actual behavior:

```text
It raises a TypeError because input is text and 1 is a number.
```

## Debug Task 2

Find and fix the bug:

```python
first = input("Enter first number: ")
second = input("Enter second number: ")
print(first + second)
```

Expected behavior:

```text
If 20 and 1 are entered, the program should print 21.
```

Actual behavior:

```text
It prints 201 because both values are strings and are joined as text.
```

## Self-Review

- I used `input()` in all tasks.
- I used `print()` to show clear results.
- I converted text to numbers where needed.

## Navigation

- ⬅️ Previous: [02-worked-examples.md](./02-worked-examples.md).
- 🧭 Week Overview: [week-01-overview.md](../week-01-overview.md).
- ➡️ Next: [04-challenge.md](./04-challenge.md).
