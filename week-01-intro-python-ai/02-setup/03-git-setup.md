# 03. Git Setup

## Why Git

Git helps you track changes and recover earlier versions of your code.

## Install Git

> Watch a complete walkthrough of these steps:<br>
> https://youtu.be/UWyL7jVmU9g?si=CGv0kpjtWgaz5C6h

### Download Git

Download and install Git from the following link:<br>
https://git-scm.com/downloads

You can use the default settings during installation. These exceptions are my recommendation:

- Override the default branch name to `main`.
- Override the default text editor to Visual Studio Code.

### Verify Installation

Open a terminal and run the following command to verify Git is installed:

```bash
git --version
```

> Expected output: `git version 2.xx.x`

### Configure Git

Open a terminal and run the following commands to configure Git:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## Navigation

- ⬅️ Previous: [02-vscode-setup.md](./02-vscode-setup.md).
- 🧭 Week Overview: [week-01-overview.md](../week-01-overview.md).
- ➡️ Next: [04-pycharm-setup-optional.md](./04-pycharm-setup-optional.md).
