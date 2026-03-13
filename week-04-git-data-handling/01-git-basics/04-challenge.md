# 04. Challenge: Git Basics

## Challenge Tasks

1. Create two files: `todo.txt` and `data_notes.txt`.
2. Stage only `todo.txt` and commit with `add todo file`.
3. Check status and explain why `data_notes.txt` is still not committed.
4. Stage and commit `data_notes.txt` with `add data notes file`.
5. Run `git log --oneline` and identify both commits.
6. Optional: connect a GitHub remote and confirm it with `git remote -v`.

## Expected Output Example

Possible status after the first commit:

```text
Untracked files:
  data_notes.txt
```

Possible log output:

```text
b2c3d4e add data notes file
a8b7c6d add todo file
```

Possible remote output:

```text
origin  https://github.com/your-username/week4-git-challenge.git (fetch)
origin  https://github.com/your-username/week4-git-challenge.git (push)
```

## Hint

A commit only includes staged files.

## Navigation

- ⬅️ Previous: [03-practice.md](./03-practice.md).
- 🧭 Week Overview: [week-04-overview.md](../week-04-overview.md).
- ➡️ Next: [05-reflection.md](./05-reflection.md).
