# 01. Theory: Conditionals

## Why This Matters

Conditionals let your program make decisions. In AI development, data is often messy, so your code must react
differently based on values and rules.

## `if`, `elif`, and `else`

Use `if` to check a condition.
Use `elif` for another condition.
Use `else` when no condition is true.

```python
score = 78

if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
else:
    print("Grade: C or below")
```

## Comparison Operators

- `==` equal to
- `!=` not equal to
- `>` greater than
- `<` less than
- `>=` greater than or equal
- `<=` less than or equal

## Boolean Logic

Use `and` when both conditions must be true.
Use `or` when one condition is enough.
Use `not` to reverse a condition.

```python
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter")
```

## Common Beginner Mistakes

- Using `=` instead of `==` in a condition.
- Forgetting indentation after `if`.
- Comparing text to numbers without conversion.

## Navigation

- 🧭 Week Overview: [week-02-overview.md](../week-02-overview.md).
- ➡️ Next: [02-worked-examples.md](./02-worked-examples.md).
