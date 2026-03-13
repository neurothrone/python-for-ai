# 03. Practice: Files, CSV, and JSON

## Tasks

1. Create `notes.txt` with these two lines:
    ```text
    Week 4 practice
    Text files come first
    ```
2. Write Python code to read `notes.txt` and print all content.
3. Write Python code that appends this line to `notes.txt`:
   ```text
   Now I can use append mode
   ```
4. Read `notes.txt` again and print the updated content.
5. Create `students.csv` with this content:
   ```text
   name,score
   Ana,92
   Bo,85
   Lia,78
   ```
6. Write Python code to read `students.csv` and print each name and score.
7. Create `config.json` with this content:
   ```json
   {
     "course": "python-for-ai",
     "week": 4,
     "active": true
   }
   ```
8. Write Python code to load `config.json` and print `course` and `week`.
9. Create a list of two dictionaries and write it to `results.csv`.
10. Save a dictionary to `summary.json` with `json.dump`.
11. Use `Path("notes.txt").exists()` to print whether `notes.txt` exists.
12. Write one short `try/except FileNotFoundError` example that tries to read `missing.txt`.

## Expected Output Examples

Possible first text read output:

```text
Week 4 practice
Text files come first
```

Possible text output after appending:

```text
Week 4 practice
Text files come first
Now I can use append mode
```

Possible CSV read output:

```text
Ana 92
Bo 85
Lia 78
```

Possible JSON read output:

```text
python-for-ai
4
```

Possible exists output:

```text
True
```

Possible error-handling output:

```text
The file was not found.
```

## Debug Task 1

Code:

```python
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("One more line\n")
```

Expected behavior:

```text
You expected to add one new line to the file.
```

Actual behavior:

```text
Old content is replaced because "w" writes a new file version instead of appending.
```

## Debug Task 2

Code:

```python
import csv

with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=";")
    for row in reader:
        print(row["name"])
```

Expected behavior:

```text
You expected to print each student name.
```

Actual behavior:

```text
It fails or prints wrong values because the file uses commas (,) not semicolons `;` as the delimiter (separator).
```

## Debug Task 3

Code:

```python
import json

with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)

print(config["course_name"])
```

Expected behavior:

```text
You expected to print the course value.
```

Actual behavior:

```text
It raises a KeyError because the key is "course", not "course_name".
```

## Debug Task 4

Code:

```python
with open("notes.txt", "x", encoding="utf-8") as file:
    file.write("New file\n")
```

Expected behavior:

```text
You expected Python to create the file.
```

Actual behavior:

```text
It raises a FileExistsError because "x" only works when the file does not already exist.
```

## Debug Task 5

Code:

```python
from pathlib import Path

if Path("missing.txt").exists():
    print("Found it")
```

Expected behavior:

```text
You expected the program to tell you when the file is missing.
```

Actual behavior:

```text
Nothing happens because the code only prints something when the file exists.
```

## Self-Review

- I can read, write, and append text files.
- I know why `with open(...)` is safer than manual open and close.
- I can check whether a file exists before reading it.
- I can use `try/except` for a simple missing-file case.
- I can read and write CSV with headers.
- I can read and write JSON with dictionaries.
- I can check path, mode, delimiter, and key names when debugging.
- I can use `encoding="utf-8"` explicitly.

## Navigation

- ⬅️ Previous: [02-worked-examples.md](./02-worked-examples.md).
- 🧭 Week Overview: [week-04-overview.md](../week-04-overview.md).
- ➡️ Next: [04-challenge.md](./04-challenge.md).
