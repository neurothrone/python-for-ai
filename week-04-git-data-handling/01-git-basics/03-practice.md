# 03. Practice: Git Basics

## Tasks

1. Create a folder named `week4-git-practice`.
2. Navigate to the folder by terminal and run `git init`.
3. Create a `README.md` file with one short sentence.
4. Run `git status`.
5. Stage the file with `git add README.md`.
6. Commit with the message `add README file`.
7. Edit `README.md` by adding one more sentence.
8. Commit again with the message `update README with second line`.
9. Run `git log --oneline` and confirm that you see two commits.
10. Optional: if you have a GitHub repo ready, connect it with `git remote add origin <repo-url>` and run
    `git remote -v`.
11. Optional: run `git push -u origin main` to verify your repo can push to GitHub.

## Expected Output Examples

Possible `git status` output before you add the file:

```text
Untracked files:
  README.md
```

Possible commit output:

```text
1 file changed, 1 insertion(+)
```

Possible log output:

```text
a1b2c3d update README with second line
9f8e7d6 add README file
```

Possible remote check output:

```text
origin  https://github.com/your-username/week4-git-practice.git (fetch)
origin  https://github.com/your-username/week4-git-practice.git (push)
```

Possible first push output:

```text
branch 'main' set up to track 'origin/main'
```

## Debug Task 1

You run:

```bash
git commit -m "add README"
```

Expected behavior:

```text
You expected Git to create a commit with your new file.
```

Actual behavior:

```text
Git says there is nothing to commit because the file was not staged with git add.
```

## Debug Task 2

You run in the wrong folder:

```bash
git status
```

Expected behavior:

```text
You expected to see your project file changes.
```

Actual behavior:

```text
Git says "not a git repository" because you are outside your repo folder.
```

## Self-Review

- I can run `git init`, `git add`, and `git commit` in the correct order.
- I can read `git status` and understand file state.
- I can write short commit messages that explain what changed.
- I can use `git log --oneline` to check commit history.
- I can connect a remote repo and confirm it with `git remote -v`.

## Navigation

- ⬅️ Previous: [02-worked-examples.md](./02-worked-examples.md).
- 🧭 Week Overview: [week-04-overview.md](../week-04-overview.md).
- ➡️ Next: [04-challenge.md](./04-challenge.md).
