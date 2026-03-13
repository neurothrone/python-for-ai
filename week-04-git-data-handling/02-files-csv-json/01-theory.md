# 01. Theory: Files, CSV, and JSON

## Why This Matters

Programming becomes much more useful when your code can work with real files instead of only values typed inside the
program. Many practical tasks start here: reading settings, saving results, loading datasets, writing reports, and
passing information from one step to the next.

This is also the bridge into data work. CSV and JSON appear everywhere in AI and software projects because they are
simple ways to store structured information. If you feel comfortable opening files, understanding paths, and choosing
the right format, then you will be much better prepared for the Pandas library, machine learning datasets, APIs, and
larger projects later.

## File Paths in Simple Words

A path is where a file lives.

- Relative path example: `data/students.csv`
- Wrong path often causes `FileNotFoundError`.

## Text Files Come First

Before CSV and JSON, it helps to understand normal text files. The same `open()` idea is used for all file types.

## The Older Way: Open and Close Manually

Older Python code often looks like this:

```python
file = open("notes.txt", "r", encoding="utf-8")
content = file.read()
file.close()
```

This works, but it is easy to forget `file.close()`. If that happens, the file may stay open longer than you expect.

## The Modern Way: Use `with`

Today we usually write:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

When the `with` block ends, Python closes the file for you. This is why `with open(...)` is the recommended way.

## File Modes in Simple Words

- `"r"` means read.
- `"a"` means append and keep old content.
- `"w"` means write and replace old content.
- `"x"` means create a new file and fail if the file already exists.
- `"t"` means text mode.
- `"b"` means binary mode.

So `"rt"` means read text. Text mode is the default, so `"r"` and `"rt"` mean the same thing. Many examples use `"r"`
because it is shorter.

You might use `"x"` when you want Python to protect you from overwriting an existing file. You might use `"b"` for
binary files such as images, audio, PDFs, or other non-text data. In this week, we use text mode because CSV and JSON
are text files.

## Common File Errors

Some common file errors are:

- `FileNotFoundError` when you try to read a file that does not exist.
- `FileExistsError` when you use `"x"` but the file already exists.
- `PermissionError` when Python is not allowed to read or write that file or folder.

These errors are useful clues. They often tell you whether the problem is the file path, file mode, or file permissions.

## Checking If a File Exists

Sometimes you want to check for a file before reading it. One common way is `Path.exists()` from `pathlib`.

```python
from pathlib import Path

file_path = Path("notes.txt")

if file_path.exists():
    print("File found")
else:
    print("File missing")
```

The `exists()` method is not a special Python keyword by itself. It is a method on a `Path` object.

You may also see the older `os` style:

```python
import os

if os.path.exists("notes.txt"):
    print("File found")
else:
    print("File missing")
```

This also works. In this course, we prefer `pathlib` because it reads more clearly and treats file paths as objects
instead of plain text. That often makes code easier to understand and extend.

This can be useful before:

- Reading a file that may not exist yet.
- Creating a file with `"x"` mode.
- Warning the user before overwriting something.

## Reading a Whole File or Line by Line

There are three ways to read text:

- `read()` gets the whole file as one string.
- `readline()` gets one line.
- `readlines()` gets all lines as a list.

Example:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    all_text = file.read()
```

Use `read()` when the file is small and you want all content at once.
Use `readline()` when you only want the next line.
Use `readlines()` when you want a list of lines to loop through later.

## Error Handling with `try` and `except`

Checking with `exists()` can be helpful, but it is also common to handle file errors directly.

```python
try:
    with open("notes.txt", "r", encoding="utf-8") as file:
        text = file.read()
except FileNotFoundError:
    print("The file was not found.")
```

This is useful when you want the program to fail in a safe and clear way instead of crashing with a long error message.

## CSV Basics

CSV means comma-separated values.

Example content:

```text
name,score
Ana,92
Bo,85
```

You can read CSV with `csv.DictReader` and write with `csv.DictWriter`.

## JSON Basics

JSON stores structured key-value data.

Example content:

```json
{
  "course": "python-for-ai",
  "active": true
}
```

In Python, JSON objects become dictionaries.

## `json.dump` and `json.load` vs `json.dumps` and `json.loads`

These names look similar, but they are used in different situations.

- `json.dump(data, file)` writes Python data into a file.
- `json.load(file)` reads JSON data from a file into Python.
- `json.dumps(data)` turns Python data into a JSON string.
- `json.loads(text)` turns a JSON string into Python data.

Memory trick:

- `dump` and `load` work with files.
- `dumps` and `loads` work with strings.
- The extra `s` can help you remember `string`.

Examples:

Write Python data to a JSON file:

```python
import json

data = {"name": "Ana", "score": 92}

with open("student.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2)
```

In `json.dump(...)`, `indent=2` is a keyword argument that formats the JSON with spaces so it is easier for people to
read. Each nested level is moved in by 2 spaces. This does not change the actual data, only how it looks in the file.
Without indent, JSON is often written on one long line, which is harder to read when you are learning or debugging.

Convert JSON text to Python data:

```python
import json

text = '{"name": "Ana", "score": 92}'
student = json.loads(text)
print(student["name"])
```

## Minimal Read/Write Pattern

Use `with open(...)` so files close safely.

```python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

We often write `encoding="utf-8"` explicitly. Python can sometimes guess the encoding, but writing it clearly is safer.

## Common Beginner Mistakes

- Wrong file path.
- Forgetting that `"w"` replaces old file content.
- Using `"r"` when the file does not exist yet.
- Using `"x"` when the file already exists.
- Forgetting to close a file when using the older manual style.
- Using text mode for a binary file.
- Wrong CSV delimiter (`,` vs `;`).
- Assuming CSV has headers when it does not.
- Accessing a JSON key that does not exist.
- Mixing list and dictionary access in JSON.

## Navigation

- ⬅️ Previous: [05-reflection.md](../01-git-basics/05-reflection.md).
- 🧭 Week Overview: [week-04-overview.md](../week-04-overview.md).
- ➡️ Next: [02-worked-examples.md](./02-worked-examples.md).
