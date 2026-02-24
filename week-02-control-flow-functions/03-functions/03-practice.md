# 03. Practice: Functions

## Tasks

1. Write a function `square(number)` that returns the square of a number.
2. Write a function `full_name(first, last)` that returns a full name string.
3. Write a function `is_even(number)` that returns `True` if the number is even.
4. Write a function `sum_list(numbers)` that returns the total sum of a list.
5. Write a function `max_of_two(a, b)` that returns the larger value.
6. Write a function `to_celsius(fahrenheit)` that returns Celsius.
7. Predict output before running:

```python
def multiply(a, b):
    return a * b

x = multiply(3, 4)
print(x + 2)
```

## Expected Output Examples

Task 1 example output for `square(4)`:

```text
16
```

Task 4 example output for `[2, 3, 5]`:

```text
10
```

Task 7 expected output:

```text
14
```

## Debug Task 1

Find and fix the bug:

```python
def add(a, b):
    print(a + b)

result = add(2, 3)
print(result + 1)
```

Expected behavior:

```text
It should print 6, because 2 + 3 = 5 and then + 1 = 6.
```

Actual behavior:

```text
It raises a TypeError because add() prints instead of returning, so result is None.
```

## Debug Task 2

Find and fix the bug:

```python
def greet(name):
    message = "Hello " + name

print(message)
```

Expected behavior:

```text
If greet("Ali") is called, the message should print Hello Ali.
```

Actual behavior:

```text
It raises a NameError because message is local inside the function and not available outside.
```

## Self-Review

- I used parameters and arguments correctly.
- I used `return` when I needed to reuse values.
- I checked the local scope when debugging.
- I tested function calls with sample inputs.

## Navigation

- ⬅️ Previous: [02-worked-examples.md](./02-worked-examples.md).
- 🧭 Week Overview: [week-02-overview.md](../week-02-overview.md).
- ➡️ Next: [04-challenge.md](./04-challenge.md).
