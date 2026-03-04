# 03. Practice: OOP Basics

## Tasks

1. Create a class `Car` with attributes `brand` and `year`.
2. Create one car object and print its `brand`.
3. Add method `show_info()` that prints both attributes.
4. Create class `Counter` with attribute `value` starting at `0`.
5. Add method `increase()` that adds 1 to `value`.
6. Call `increase()` twice and print `value`.
7. Predict output before running:

```python
class User:
    def __init__(self, username):
        self.username = username

    def show(self):
        print(self.username)

u = User("leo")
print(u.username)
u.show()
```

## Expected Output Examples

Task 2 example output:

```text
Volvo
```

Task 6 example output:

```text
2
```

Task 7 expected output:

```text
leo
leo
```

## Debug Task 1

Find and fix the bug:

```python
class Dog:
    def __init__(name):
        self.name = name
```

Expected behavior:

```text
Creating Dog("Milo") should work and store the name.
```

Actual behavior:

```text
It raises an error because self is missing in __init__.
```

## Debug Task 2

Find and fix the bug:

```python
class Phone:
    def __init__(self, model):
        self.model = model

    def show_model(self):
        print(self.model)

p = Phone("Pixel")
print(p.show_model)
```

Expected behavior:

```text
It should print Pixel by calling the method.
```

Actual behavior:

```text
It prints a method reference because show_model is not called with ().
```

## Self-Review

- I can create classes and objects.
- I can store data as attributes.
- I can define methods with `self`.
- I can call methods correctly.

## Navigation

- ⬅️ Previous: [02-worked-examples.md](./02-worked-examples.md).
- 🧭 Week Overview: [week-03-overview.md](../week-03-overview.md).
- ➡️ Next: [04-challenge.md](./04-challenge.md).
