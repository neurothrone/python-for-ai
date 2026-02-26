# 02. Worked Examples: Input and Output

## Example A: Greeting

```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

## Example B: Age Next Year

```python
age_text = input("Enter your age: ")
age = int(age_text)
print("Next year you will be " + str(age + 1) + ".")
```

## Example C: City and Country Output

```python
city = input("City: ")
country = input("Country: ")
print("You live in " + city + ", " + country + ".")
```

## Example D: Formatting Text in Different Ways

In previous examples, we used concatenation. With concatenation, numbers must be converted to text with `str()`.

`format()` and f-strings are often easier to read because you can place values directly in a text template.

`:.2f` means "show this float with two digits after the decimal point."

```python
name = "Ana"
score = 9.456

# Concatenation (works, but is less readable)
print("Student " + name + " scored " + str(round(score, 2)))

# format() (clear template, no manual str())
print("Student {} scored {:.2f}".format(name, score))

# f-string (recommended for readability, no manual str())
print(f"Student {name} scored {score:.2f}")
```

## Navigation

- ⬅️ Previous: [01-theory.md](./01-theory.md).
- 🧭 Week Overview: [week-01-overview.md](../week-01-overview.md).
- ➡️ Next: [03-practice.md](./03-practice.md).
