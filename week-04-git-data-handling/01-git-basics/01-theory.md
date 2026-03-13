# 01. Theory: Git Basics

## Why This Matters

Git is one of the most practical tools you can learn early. It helps you save meaningful versions of your work, try
ideas without panic, and recover when something goes wrong. That alone makes programming less stressful.

It also prepares you for real projects. In school, at work, or in AI projects later, code is rarely written once and
finished. You change files, improve them, break things, fix them, and often share that work with others. Git gives
structure to that process. When you start to feel that Git is not just a command list but a safety net and a work
history, it usually becomes much easier to trust your own progress.

## What Git Tracks

Git tracks changes in files inside a repository (repo). A repo starts with:

```bash
git init
```

## Core Commands for This Week

- `git init` creates a new local repo.
- `git status` shows changed files and staging status.
- `git add <file>` stages a file for commit.
- `git commit -m "message"` saves a snapshot.
- `git push` sends commits to a remote repo.
- `git pull` gets new commits from a remote repo.

## Staging vs Commit (Simple)

- Staging (`git add`) means **prepare this file**.
- Commit means **save this prepared version**.

You usually do:

```bash
git add student.py
git commit -m "add Student class"
```

## Commit Messages

Good commit messages are short, clear, and written in **imperative** style. Imperative means command form, like "add", "
fix", or "update". Think of it as completing this sentence: "If applied, this commit will ...".

- Good: `add CSV reader for student data`
- Good: `update README and AIConcepts.md links`
- Weak: `update`

We start with lowercase so names like `README`, `Week4`, or `AIConcepts.md` stand out clearly.

## Common Beginner Mistakes

- Running `git commit` before `git add`.
- Writing unclear commit messages.
- Running commands in the wrong folder.
- Trying `git push` before connecting a remote repo.
- Pulling with local changes and getting merge conflicts.

## Navigation

- 🧭 Week Overview: [week-04-overview.md](../week-04-overview.md).
- ➡️ Next: [02-worked-examples.md](./02-worked-examples.md).
