# 04. PyCharm Setup (Optional)

## Install PyCharm

> Watch a complete walkthrough of these steps:<br>
> https://youtu.be/UKyTcJQAYYI?si=jY6FDkA2fHhaBpRn

### Install JetBrains Toolbox (recommended)

Download and install JetBrains Toolbox from the following link:<br>
https://www.jetbrains.com/toolbox-app/

Open JetBrains Toolbox, expand the **Available tools** section and install PyCharm.

### Install standalone (not recommended)

Download and install PyCharm from the following link:<br>
https://www.jetbrains.com/pycharm/download/

## Create Project

1. Click `New Project`.
2. Select `Pure Python` on the sidebar to the left.
3. Uncheck the `Create a Git repository` checkbox if it is checked.
4. Uncheck the `Create a welcome script` checkbox if it is checked.
5. For `Location`, select a location to save the project, for example a folder called `week1-practice` in your `Desktop`
   directory.
6. For the `Interpreter type` select `Project venv`.
7. For `Python version` select the version of Python you installed in previous steps, for example `Python 3.14`.
8. Click on the `Create project` button.

## Run First File

Right-click on the project folder in the sidebar to the left, select `New` and then `Python File`. Name the file
`main.py` and click enter.

Add the following code to the file:

```python
print("PyCharm is operational!")
```

Run the file by right-clicking on the code editor and selecting `Run 'main'` or by clicking the green run button in the
top right corner of the window. You should see the output `PyCharm is operational!` in the Run panel at the bottom of
the window.

## Navigation

- ⬅️ Previous: [03-git-setup.md](./03-git-setup.md).
- 🧭 Week Overview: [week-01-overview.md](../week-01-overview.md).
- ➡️ Next: [01-theory.md](./../03-input-output/01-theory.md).
