# 03. Practice: Loops

## Tasks

1. Use a `for` loop to print numbers from `1` to `10`.
2. Use a loop to find the sum of `[4, 9, 2, 5]`.
3. Use a `while` loop to print numbers from `10` down to `1`.
4. Ask the user for a positive number. Keep asking until they enter a valid value.
5. Count how many even numbers are in `[3, 8, 11, 14, 20]`.
6. Print each letter of a word using a loop.
7. Predict output before running:

```python
total = 0
for n in [1, 2, 3]:
    total = total + n
print(total)
```

## Expected Output Examples

Task 2 example output:

```text
20
```

Task 3 example output (first lines):

```text
10
9
8
...
1
```

Task 5 example output:

```text
3
```

Task 7 expected output:

```text
6
```

## Debug Task 1

Find and fix the bug:

```python
count = 1
while count <= 5:
print(count)
count = count + 1
```

Expected behavior:

```text
It should print 1, 2, 3, 4, 5 on separate lines.
```

Actual behavior:

```text
It raises an IndentationError because the loop body is not indented.
```

## Debug Task 2

Find and fix the bug:

```python
numbers = [2, 4, 6]
for i in range(len(numbers) + 1):
    print(numbers[i])
```

Expected behavior:

```text
It should print 2, 4, 6.
```

Actual behavior:

```text
It raises an IndexError because the loop goes one step too far.
```

## Self-Review

- I used both `for` and `while` correctly.
- I updated variables in `while` loops.
- I checked indentation and loop limits.
- I tested with small data first.

## Navigation

- ⬅️ Previous: [02-worked-examples.md](./02-worked-examples.md).
- 🧭 Week Overview: [week-02-overview.md](../week-02-overview.md).
- ➡️ Next: [04-challenge.md](./04-challenge.md).
