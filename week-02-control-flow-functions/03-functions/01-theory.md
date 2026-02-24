# 01. Theory: Functions

## Why This Matters

Functions help you break big problems into small parts. This makes code easier to read, reuse, test, and debug.

## Define and Call a Function

A function is a named block of code.

```python
def greet():
    print("Hello")

greet()
```

`def` creates the function. `greet()` calls it.

## Parameters and Arguments

People often use these words as if they are the same. They are close, but not identical.

- A parameter is the variable in the function definition.
- An argument is the value you pass in the function call.

```python
def greet_user(name):  # name is a parameter
    print("Hello, " + name)

greet_user("Mina")    # "Mina" is an argument
```

## Return Values vs Print

Use `print()` to show text on screen.
Use `return` to send a value back so other code can use it.

```python
def add(a, b):
    return a + b

result = add(4, 6)
print(result)
```

If you only print inside a function, you cannot reuse that value easily later.

## Scope (Local and Global)

A local variable exists only inside its function.

```python
def show_value():
    value = 10
    print(value)

show_value()
# print(value)  # This would fail: value is local
```

This rule helps avoid name conflicts.

## Why Functions Help Beginners

- You avoid repeated code.
- You test one small part at a time.
- Bugs are easier to find.

## Common Beginner Mistakes

- Forgetting to call the function.
- Using `print` when a `return` value is needed.
- Mixing parameter names and variable names.
- Trying to use local variables outside the function.

## Navigation

- ⬅️ Previous: [05-reflection.md](../02-loops/05-reflection.md).
- 🧭 Week Overview: [week-02-overview.md](../week-02-overview.md).
- ➡️ Next: [02-worked-examples.md](./02-worked-examples.md).
