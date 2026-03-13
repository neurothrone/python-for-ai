# 02. Worked Examples: Git Basics

## Example A: Start a Repo

```bash
mkdir mini-data-project
cd mini-data-project
git init
git status
```

Possible status output part:

```text
On branch main
No commits yet
```

## Example B: First Commit

Create `notes.txt` with one line:

```text
Week 4 practice repo
```

Then run:

```bash
git add notes.txt
git commit -m "add initial notes file"
```

Here `-m` means message. It lets you write the commit message directly in the command.

Possible output part:

```text
1 file changed, 1 insertion(+)
```

## Example C: Second Commit

Add one new line in `notes.txt`:

```text
Next: add CSV and JSON tasks
```

Then run:

```bash
git add notes.txt
git commit -m "add next task note"
```

## Example D: Connect a Remote Repo

On [GitHub](https://github.com/), create an empty repository first. Then connect your local repo to that remote:

```bash
git branch -M main
git remote add origin https://github.com/your-username/mini-data-project.git
git remote -v
```

Why these options are used:

- `-M` renames the current branch to `main`. We use `main` because it is the common default branch name now.
- `origin` is the common name for the main remote repo on GitHub.
- `-v` means verbose. Here it shows the full remote URLs for fetch and push.

If your local branch is already called `main`, this command is still safe. It just keeps the branch name as `main`.

You may also see `master` on some computers, older tutorials, or older repositories. `master` was the old common default
branch name, and many projects still use it. In this course, we use `main` for consistency.

Possible output part:

```text
origin  https://github.com/your-username/mini-data-project.git (fetch)
origin  https://github.com/your-username/mini-data-project.git (push)
```

If you want a full video walkthrough for this step, use these videos. You can find the links on the Week 4 overview
page.

- [Week 4.3 - Git Basics: Push and Pull with GitHub](https://www.youtube.com/watch?v=ep2MtoYlqMQ&list=PLQ10yv3WDdnYsEqGoAq6Komz_BWNBOY6q)
- [Week 4.5 - Git Basics: Starting from a GitHub Workflow](https://www.youtube.com/watch?v=REP2hulf_Yc&list=PLQ10yv3WDdnYsEqGoAq6Komz_BWNBOY6q)

## Example E: First Push and Later Pull

After the remote is connected, use:

```bash
git push -u origin main
git pull
```

- `push` sends your commits to the remote repo.
- `pull` gets commits from the remote repo to your local repo.
- `-u origin main` connects your local `main` branch to the remote branch the first time.
- After you do this once, later pushes can usually be just `git push`.

Possible first push output part:

```text
branch 'main' set up to track 'origin/main'
```

This means:

- your local branch is `main`
- the matching branch on GitHub is `origin/main`
- Git now remembers that these two branches belong together

So after this setup, Git knows where `git push` and `git pull` should go by default.

## Navigation

- ⬅️ Previous: [01-theory.md](./01-theory.md).
- 🧭 Week Overview: [week-04-overview.md](../week-04-overview.md).
- ➡️ Next: [03-practice.md](./03-practice.md).
