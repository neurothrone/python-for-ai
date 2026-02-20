# 01. Python Setup

## Install Python

### Windows

#### Using the Windows Store (recommended)

1. Open the Microsoft Store app.
2. Search for `Python install manager`, install it then open it (the terminal should open automatically).
3. Follow the prompts:
    - `Windows is not configured to allowed paths longer than 260 characters.`: Type `y` and press enter.
    - `The global shortcuts directory is not configured.`: Type `n` and press enter.
    - `You do not have the latest Python runtime`: Type `y` and press enter.
    - `View online help?`: Optional, type `y` to open the documentation or `n` to skip and press enter.

> Watch a complete walkthrough of these steps:<br>
> https://youtu.be/FL-Kwokp32A?si=3PPEThjZLMvrec6C

#### Using the standalone installer (not recommended)

1. Download Python 3 from the following link:<br>https://www.python.org/downloads/
2. Install it using default options.
3. If on Windows, enable the option to add Python to PATH.

> Source link for why this approach is not recommended:<br>
> https://www.python.org/downloads/release/pymanager-252/

### macOS

1. Download Python 3 from the following link:<br>https://www.python.org/downloads/
2. Install it using default options.

## Verify Installation

Open a terminal and run:

```bash
python --version
```

You should see something like: `Python 3.x.x`

If `python` does not work, run:

```bash
python3 --version
```

## Navigation

- ⬅️ Previous: [02-course-roadmap.md](./../01-intro/02-course-roadmap.md).
- 🧭 Week Overview: [week-01-overview.md](../week-01-overview.md).
- ➡️ Next: [02-vscode-setup.md](./02-vscode-setup.md).
