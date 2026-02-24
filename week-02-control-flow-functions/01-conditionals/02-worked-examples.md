# 02. Worked Examples: Conditionals

## Example A: Positive, Negative, or Zero

```python
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

## Example B: Password Check

```python
password = input("Enter password: ")

if password == "python123":
    print("Access granted")
else:
    print("Access denied")
```

## Example C: Common Type Mistake and Fix

```python
age_text = input("Enter age: ")
age = int(age_text)

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

## Navigation

- ⬅️ Previous: [01-theory.md](./01-theory.md).
- 🧭 Week Overview: [week-02-overview.md](../week-02-overview.md).
- ➡️ Next: [03-practice.md](./03-practice.md).
