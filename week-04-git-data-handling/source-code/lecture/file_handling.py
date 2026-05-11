# File handling in Python

# File modes:
# r = read
# w = write
# a = append
# x = create

# File types:
# t = text
# b = binary

# Example: "rt" = read text, "wb" = write binary

# Open a file for reading
# file = open("data/notes.txt", "rt", encoding="utf-8")
# line = file.readline().strip("\n")
# print(line) # "Week 4 file practice\n"

# line = file.readline()
# print(line)

# The old and easy approach
# file = open("data/notes.txt", "rt", encoding="utf-8")
# lines = file.readlines()
# file.close()

# The modern approach, safer
# with statement
# with open("data/notes.txt", "rt", encoding="utf-8") as file:
#     lines = file.readlines()

# with open("data/notes_updated.txt", "wt", encoding="utf-8") as file_out:
#     lines[-1] = lines[-1].strip("\n")
#     file_out.writelines(lines)

# with open("data/notes_updated.txt", "at", encoding="utf-8") as file_out:
#     file_out.write("\nHey back")

# import os
from pathlib import Path

# __name__
# print(__file__)
BASE_DIR = Path(__file__).resolve().parent  # .../lecture
DATA_DIR = BASE_DIR / "data"
print(BASE_DIR)
print(DATA_DIR)

if Path.exists(DATA_DIR / "does_not_exist.txt"):
    print("It exists")
else:
    print("It does not exist")

# try:
#     with open("data/does_not_exist.txt", "rt", encoding="utf-8") as file:
#         lines = file.readlines()
# except FileNotFoundError:
#     print("File does not exist")
