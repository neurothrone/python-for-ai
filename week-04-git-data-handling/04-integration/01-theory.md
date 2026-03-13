# 01. Theory: Integration (Git + Files + Pandas)

## Why This Matters

Real projects are rarely about one tool at a time. You read data from files, inspect it, clean it, transform it, save
the result, and keep track of your progress with Git. This integration step matters because it starts to feel like a
real workflow instead of separate lessons.

It is also where confidence usually grows. When you can take a raw file, improve it with code, save a clean version, and
commit that work clearly, you will be doing something very close to how you will work in real data projects in practice.
That is a strong foundation for the more advanced analysis and visualization that comes later.

## Simple Week 4 Flow

1. Create a small project repo with Git.
2. Add a CSV dataset.
3. Read and inspect it with Pandas.
4. Fix simple null values.
5. Transform the data with one new column.
6. Save cleaned output to a new file.
7. Commit changes with clear messages.

## Example Project Structure

```text
week4-mini-project/
  data/
    students.csv
    students_cleaned.csv
  scripts/
    clean_students.py
```

## Suggested Commit Sequence

- `initial commit`
- `add raw students dataset`
- `add pandas cleaning script`
- `add cleaned and transformed dataset output`

Use imperative style here too. Remember that imperative means command form (add, fix, rename). It reads as "this
commit will add/fix/rename..." and stays clear when file names contain capitals.

## Common Beginner Mistakes

- Cleaning data but forgetting to save an output file.
- Overwriting the raw file instead of saving to a new file.
- Committing too many unrelated changes at once.
- Running script from the wrong path and missing file errors.
- Forgetting to check if null handling actually changed values.
- Forgetting that cleaned number columns may need `astype(int)`.

## Navigation

- ⬅️ Previous: [05-reflection.md](../03-pandas-basics/05-reflection.md).
- 🧭 Week Overview: [week-04-overview.md](../week-04-overview.md).
- ➡️ Next: [02-worked-examples.md](./02-worked-examples.md).
