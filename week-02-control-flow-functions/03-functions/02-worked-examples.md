# 02. Worked Examples: Functions

## Example A: Area of a Rectangle

```python
def rectangle_area(width, height):
    return width * height

area = rectangle_area(5, 3)
print(area)
```

## Example B: Reuse One Function Many Times

```python
def is_adult(age):
    return age >= 18

print(is_adult(16))
print(is_adult(21))
```

## Example C: Return vs Print

```python
def get_discount(price):
    discount = price * 0.10
    return discount

saved = get_discount(200)
print(saved)
```

## Navigation

- ⬅️ Previous: [01-theory.md](./01-theory.md).
- 🧭 Week Overview: [week-02-overview.md](../week-02-overview.md).
- ➡️ Next: [03-practice.md](./03-practice.md).
