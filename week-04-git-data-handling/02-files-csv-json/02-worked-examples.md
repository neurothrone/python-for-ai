# 02. Worked Examples: Files, CSV, and JSON

## Example A: Create and Read a Text File

First create `notes.txt` with this content:

```text
Week 4 file practice
We are learning file handling.
```

Then read it:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    text = file.read()

print(text)
```

Here `read()` gives the whole file as one string.

## Example B: `readline()` and `readlines()`

Use `readline()` when you want one line:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    first_line = file.readline()

print(first_line)
```

Use `readlines()` when you want a list of all lines:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print(lines)
```

## Example C: The Older Manual Style

The older way works too:

```python
file = open("notes.txt", "r", encoding="utf-8")
text = file.read()
file.close()
print(text)
```

The old approach is not recommended. It is too easy to forget `close()`. Use `with open(...)` instead.

## Example D: Write and Append Text

Create or replace a file:

```python
with open("journal.txt", "w", encoding="utf-8") as file:
    file.write("Day 1: Started file handling practice.\n")
```

Append one new line without removing the old line:

```python
with open("journal.txt", "a", encoding="utf-8") as file:
    file.write("Day 2: Learned append mode.\n")
```

Useful mode reminders:

- `"r"` or `"rt"` reads text.
- `"w"` writes and replaces old content.
- `"a"` appends new content at the end.

## Example E: Check If a File Exists Before Reading

```python
from pathlib import Path

file_path = Path("notes.txt")

if file_path.exists():
    with open(file_path, "r", encoding="utf-8") as file:
        print(file.read())
else:
    print("notes.txt was not found")
```

This is useful when the file may or may not be there yet.

## Example F: Handle Missing File with `try/except`

```python
try:
    with open("missing.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("missing.txt was not found. Check the path and filename.")
```

This keeps the program friendly when a file is missing.

## Example G: Read CSV with Headers

`students.csv`:

```text
name,score
Ana,92
Bo,85
```

Python:

```python
import csv

with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["score"])
```

## Example H: Write CSV

```python
import csv

rows = [
    {"name": "Ana", "score": 92},
    {"name": "Bo", "score": 85}
]

with open("output.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerows(rows)
```

This creates `output.csv` with header row and two data rows.

## Example I: Read and Write JSON

Create this file `week.json` first if you want to test reading separately and fill it with this content:

```json
{
  "course": "python-for-ai",
  "week": 4
}
```

You can also create it from Python:

```python
import json

data = {"course": "python-for-ai", "week": 4}

with open("week.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2)

with open("week.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)

print(loaded["course"])
```

This works well because JSON objects become Python dictionaries.

## Example J: `json.dumps()` and `json.loads()`

Use these when you work with JSON as text in memory, not as a file:

```python
import json

data = {"course": "python-for-ai", "week": 4}
json_text = json.dumps(data)
print(json_text)

loaded_again = json.loads(json_text)
print(loaded_again["week"])
```

## Navigation

- ⬅️ Previous: [01-theory.md](./01-theory.md).
- 🧭 Week Overview: [week-04-overview.md](../week-04-overview.md).
- ➡️ Next: [03-practice.md](./03-practice.md).
