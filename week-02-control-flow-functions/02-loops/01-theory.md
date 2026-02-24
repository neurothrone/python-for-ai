# 01. Theory: Loops

## Why This Matters

Loops help you repeat actions without copying code many times. In AI and data work, loops are common when you check
many values, count results, or when processing lists one item at a time.

## What Is a Loop?

A loop is a block of code that runs again and again.

You choose the loop type based on your task:

- Use `for` when you go through items (or a known count).
- Use `while` when you repeat until a condition becomes false.

## `for` Loop (Item by Item)

Use a `for` loop when you already have a list, string, or range.

```python
numbers = [2, 4, 6]
for n in numbers:
    print(n)
```

You can also loop with a known count:

```python
for i in range(5):
    print(i)
```

This prints `0` to `4`.

## `while` Loop (Condition Based)

Use a `while` loop when you do not know in advance how many times to repeat.

```python
count = 1
while count <= 3:
    print(count)
    count = count + 1
```

The condition `count <= 3` is checked before each round.

## Practical Use Cases

- Menu loop: show choices until user selects `q` to quit.
- Input validation: keep asking until input is valid.
- Retry logic: ask for password again until it is correct.

Example menu pattern:

```python
choice = ""
while choice != "q":
    choice = input("Enter option (q to quit): ")
    print("You entered:", choice)
```

## Loop Safety

- In `while` loops, update the variable used in the condition.
- Keep indentation correct. The loop body must be indented.
- Test with a small input first.

## Common Beginner Mistakes

- Infinite loop because the condition never changes.
- Wrong indentation that causes `IndentationError`.
- Using text from `input()` as a number without conversion.

## Navigation

- ⬅️ Previous: [05-reflection.md](../01-conditionals/05-reflection.md).
- 🧭 Week Overview: [week-02-overview.md](../week-02-overview.md).
- ➡️ Next: [02-worked-examples.md](./02-worked-examples.md).
