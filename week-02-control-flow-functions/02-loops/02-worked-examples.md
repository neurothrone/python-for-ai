# 02. Worked Examples: Loops

## Example A: Sum Numbers from a List

```python
numbers = [3, 5, 7]
total = 0

for n in numbers:
    total = total + n

print(total)
```

## Example B: Count Down with `while`

```python
count = 5

while count > 0:
    print(count)
    count = count - 1

print("Done")
```

## Example C: Input Until Correct Value

```python
answer = ""

while answer != "python":
    answer = input("Type python: ")

print("Correct")
```

## Navigation

- ⬅️ Previous: [01-theory.md](./01-theory.md).
- 🧭 Week Overview: [week-02-overview.md](../week-02-overview.md).
- ➡️ Next: [03-practice.md](./03-practice.md).
