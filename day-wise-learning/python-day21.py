# =========================================================
# DAY 21 - FILE HANDLING IN PYTHON
# Read / Write Files
# =========================================================

# =========================================================
# 1. READING A FILE
# =========================================================

# Make sure data.txt exists before running

with open("data.txt", "r") as file:
    content = file.read()
    print("File Content:")
    print(content)

# =========================================================
# 2. READING FILE LINE BY LINE
# =========================================================

print("\nReading line by line:")

with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())

# =========================================================
# 3. WRITING TO A FILE
# =========================================================

with open("notes.txt", "w") as file:
    file.write("Learning Python File Handling\n")
    file.write("Writing files is easy!")

print("\nData written to notes.txt")

# =========================================================
# 4. APPENDING TO A FILE
# =========================================================

with open("notes.txt", "a") as file:
    file.write("\nThis line was appended.")

print("Data appended successfully")

# =========================================================
# 5. CREATING A NEW FILE
# =========================================================

with open("new_file.txt", "w") as file:
    file.write("This is a newly created file.")

print("new_file.txt created")

# =========================================================
# 6. USING readlines()
# =========================================================

with open("data.txt", "r") as file:
    lines = file.readlines()

print("\nUsing readlines():")
print(lines)

# =========================================================
# 7. USING readline()
# =========================================================

with open("data.txt", "r") as file:
    first_line = file.readline()

print("\nFirst Line:")
print(first_line)

# =========================================================
# 8. FILE ERROR HANDLING
# =========================================================

try:
    with open("unknown.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("\nError: File does not exist")

# =========================================================
# 9. WRITING JSON FILES
# =========================================================

import json

student_data = {
    "name": "Siddharth",
    "age": 28,
    "skills": ["Python", "AI", "React"]
}

with open("student.json", "w") as file:
    json.dump(student_data, file, indent=4)

print("\nJSON file written successfully")

# =========================================================
# 10. READING JSON FILES
# =========================================================

with open("student.json", "r") as file:
    data = json.load(file)

print("\nJSON Data:")
print(data)

print("\nStudent Name:")
print(data["name"])

# =========================================================
# 11. WRITING CSV FILES
# =========================================================

import csv

rows = [
    ["name", "age"],
    ["Siddharth", 28],
    ["Rahul", 25],
    ["Aman", 30]
]

with open("users.csv", "w", newline="") as file:
    writer = csv.writer(file)

    for row in rows:
        writer.writerow(row)

print("\nCSV file written successfully")

# =========================================================
# 12. READING CSV FILES
# =========================================================

print("\nReading CSV Data:")

with open("users.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# =========================================================
# 13. CHECKING IF FILE EXISTS
# =========================================================

import os

if os.path.exists("data.txt"):
    print("\ndata.txt exists")
else:
    print("\ndata.txt not found")

# =========================================================
# 14. FILE CURSOR EXAMPLE
# =========================================================

with open("data.txt", "r") as file:
    print("\nFirst Read:")
    print(file.read())

    print("\nSecond Read:")
    print(file.read())  # Empty because cursor at end

# =========================================================
# 15. RESETTING FILE CURSOR
# =========================================================

with open("data.txt", "r") as file:
    print("\nReading file:")
    print(file.read())

    file.seek(0)

    print("\nReading again after seek(0):")
    print(file.read())

# =========================================================
# 16. MINI PROJECT - TODO APP
# =========================================================

task = input("\nEnter a task: ")

with open("todos.txt", "a") as file:
    file.write(task + "\n")

print("Task saved successfully")

# =========================================================
# 17. MINI PROJECT - NOTES APP
# =========================================================

note = input("\nWrite a note: ")

with open("my_notes.txt", "a") as file:
    file.write(note + "\n")

print("Note saved")

# =========================================================
# 18. MINI PROJECT - LOGIN LOGGER
# =========================================================

from datetime import datetime

username = input("\nEnter username: ")

with open("log.txt", "a") as file:
    file.write(f"{datetime.now()} - {username} logged in\n")

print("Login logged successfully")

# =========================================================
# 19. MINI PROJECT - AI PROMPT SAVER
# =========================================================

prompt = input("\nEnter AI prompt: ")

with open("prompts.txt", "a") as file:
    file.write(prompt + "\n")

print("Prompt saved")

# =========================================================
# 20. FILE RENAME EXAMPLE
# =========================================================

# Uncomment to test

# os.rename("new_file.txt", "renamed_file.txt")
# print("File renamed successfully")

# =========================================================
# 21. FILE DELETE EXAMPLE
# =========================================================

# Uncomment carefully

# os.remove("renamed_file.txt")
# print("File deleted successfully")

# =========================================================
# END OF DAY 21
# =========================================================

print("\nDay 21 completed successfully!")