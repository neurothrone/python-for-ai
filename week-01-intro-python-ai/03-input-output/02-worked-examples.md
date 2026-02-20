# 02. Worked Examples: Input and Output

## Example A: Greeting

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

## Example B: Age Next Year

```python
age_text = input("Enter your age: ")
age = int(age_text)
print(f"Next year you will be {age + 1}.")
```

## Example C: Formatted Output

```python
city = input("City: ")
country = input("Country: ")
print(f"You live in {city}, {country}.")
```

## Example D: Why f-strings are preferred

```python
name = "Ana"
score = 9.456

# Concatenation (works, but is less readable)
print("Student " + name + " scored " + str(round(score, 2)))

# format() (better, but still more verbose)
print("Student {} scored {:.2f}".format(name, score))

# f-string (recommended for readability)
print(f"Student {name} scored {score:.2f}")
```

## Navigation

- ⬅️ Previous: [01-theory.md](./01-theory.md).
- 🧭 Week Overview: [week-01-overview.md](../week-01-overview.md).
- ➡️ Next: [03-practice.md](./03-practice.md).
