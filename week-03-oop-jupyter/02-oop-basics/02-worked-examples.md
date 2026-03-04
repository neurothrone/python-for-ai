# 02. Worked Examples: OOP Basics

## Example A: One Simple Object

```python
class Student:
    def __init__(self, name):
        self.name = name

student1 = Student("Chewbacca")
print(student1.name)
```

## Example B: Method Call

```python
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")

student1 = Student("Chewbacca")
student1.greet()
```

## Example C: Update State

```python
class Lamp:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

lamp = Lamp()
lamp.turn_on()
print(lamp.is_on)
```

## Navigation

- ⬅️ Previous: [01-theory.md](./01-theory.md).
- 🧭 Week Overview: [week-03-overview.md](../week-03-overview.md).
- ➡️ Next: [03-practice.md](./03-practice.md).
