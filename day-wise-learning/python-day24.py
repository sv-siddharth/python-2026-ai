"""
DAY 24 - FILE PATHS & WORKING WITH DIRECTORIES
==============================================

Topics Covered:
1. Current working directory
2. Absolute vs relative paths
3. Creating folders
4. Listing files/folders
5. Reading/writing files
6. pathlib module
7. Recursive file searching
8. File organizer project
9. AI engineering use cases

Run this file section by section.
"""

# ============================================================
# 1. CURRENT WORKING DIRECTORY
# ============================================================

import os

print("=== CURRENT WORKING DIRECTORY ===")
print(os.getcwd())


# ============================================================
# 2. LIST FILES IN CURRENT DIRECTORY
# ============================================================

print("\n=== FILES & FOLDERS ===")

items = os.listdir()

for item in items:
    print(item)


# ============================================================
# 3. CREATE A NEW DIRECTORY
# ============================================================

print("\n=== CREATE DIRECTORY ===")

folder_name = "sample_folder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"{folder_name} created")
else:
    print(f"{folder_name} already exists")


# ============================================================
# 4. CREATE NESTED DIRECTORIES
# ============================================================

print("\n=== CREATE NESTED DIRECTORIES ===")

nested_path = "project/data/logs"

os.makedirs(nested_path, exist_ok=True)

print(f"{nested_path} created")


# ============================================================
# 5. CHECK IF PATH EXISTS
# ============================================================

print("\n=== CHECK PATH EXISTS ===")

print(os.path.exists("sample_folder"))
print(os.path.exists("random_folder"))


# ============================================================
# 6. CHECK FILE VS DIRECTORY
# ============================================================

print("\n=== FILE OR DIRECTORY ===")

print(os.path.isdir("sample_folder"))
print(os.path.isfile("sample_folder"))


# ============================================================
# 7. PATH JOINING
# ============================================================

print("\n=== PATH JOINING ===")

path = os.path.join("project", "data", "users.txt")

print(path)


# ============================================================
# 8. WRITE TO FILE
# ============================================================

print("\n=== WRITE TO FILE ===")

with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Hello from Day 24!")

print("sample.txt created")


# ============================================================
# 9. READ FROM FILE
# ============================================================

print("\n=== READ FILE ===")

with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)


# ============================================================
# 10. APPEND TO FILE
# ============================================================

print("\n=== APPEND TO FILE ===")

with open("sample.txt", "a", encoding="utf-8") as file:
    file.write("\nNew line added.")

print("Text appended")


# ============================================================
# 11. PATHLIB BASICS
# ============================================================

print("\n=== PATHLIB BASICS ===")

from pathlib import Path

current = Path.cwd()

print(current)


# ============================================================
# 12. CREATE PATH OBJECT
# ============================================================

print("\n=== PATH OBJECT ===")

file_path = Path("data.txt")

print(file_path)


# ============================================================
# 13. CREATE DIRECTORY USING PATHLIB
# ============================================================

print("\n=== CREATE DIRECTORY WITH PATHLIB ===")

new_folder = Path("pathlib_folder")

new_folder.mkdir(exist_ok=True)

print("pathlib_folder created")


# ============================================================
# 14. CREATE NESTED FOLDERS USING PATHLIB
# ============================================================

print("\n=== CREATE NESTED PATHLIB FOLDERS ===")

nested_folder = Path("ai_project") / "documents" / "embeddings"

nested_folder.mkdir(parents=True, exist_ok=True)

print("Nested folders created")


# ============================================================
# 15. WRITE FILE USING PATHLIB
# ============================================================

print("\n=== WRITE FILE WITH PATHLIB ===")

Path("notes.txt").write_text(
    "This file was created using pathlib",
    encoding="utf-8"
)

print("notes.txt created")


# ============================================================
# 16. READ FILE USING PATHLIB
# ============================================================

print("\n=== READ FILE WITH PATHLIB ===")

content = Path("notes.txt").read_text(encoding="utf-8")

print(content)


# ============================================================
# 17. FILE INFORMATION
# ============================================================

print("\n=== FILE INFORMATION ===")

file = Path("notes.txt")

print("Name:", file.name)
print("Extension:", file.suffix)
print("Filename without extension:", file.stem)
print("Absolute path:", file.resolve())


# ============================================================
# 18. ITERATE THROUGH CURRENT DIRECTORY
# ============================================================

print("\n=== ITERATE DIRECTORY ===")

for item in Path(".").iterdir():
    print(item)


# ============================================================
# 19. RECURSIVE SEARCH
# ============================================================

print("\n=== FIND ALL PYTHON FILES ===")

for py_file in Path(".").rglob("*.py"):
    print(py_file)


# ============================================================
# 20. COUNT TOTAL FILES
# ============================================================

print("\n=== COUNT FILES ===")

count = 0

for item in Path(".").rglob("*"):
    if item.is_file():
        count += 1

print("Total files:", count)


# ============================================================
# 21. AI ENGINEERING EXAMPLE - LOAD DOCUMENTS
# ============================================================

print("\n=== AI DOCUMENT LOADER ===")

docs_folder = Path("documents")

docs_folder.mkdir(exist_ok=True)

# Create sample documents
(Path("documents") / "doc1.txt").write_text(
    "Python is used in AI engineering.",
    encoding="utf-8"
)

(Path("documents") / "doc2.txt").write_text(
    "RAG pipelines use embeddings.",
    encoding="utf-8"
)

documents = []

for file in docs_folder.rglob("*.txt"):

    content = file.read_text(encoding="utf-8")

    documents.append({
        "filename": file.name,
        "content": content
    })

print(documents)


# ============================================================
# 22. MINI PROJECT - FILE ORGANIZER
# ============================================================

print("\n=== FILE ORGANIZER PROJECT ===")

import shutil

downloads = Path("downloads")

downloads.mkdir(exist_ok=True)

# Create sample files
(downloads / "photo.jpg").write_text("image")
(downloads / "movie.mp4").write_text("video")
(downloads / "notes.txt").write_text("text")


for file in downloads.iterdir():

    if file.is_file():

        extension = file.suffix[1:]

        target_folder = downloads / extension

        target_folder.mkdir(exist_ok=True)

        shutil.move(
            str(file),
            str(target_folder / file.name)
        )

print("Files organized by extension")


# ============================================================
# 23. PRINT ORGANIZED STRUCTURE
# ============================================================

print("\n=== ORGANIZED STRUCTURE ===")

for item in downloads.rglob("*"):
    print(item)


# ============================================================
# 24. REMOVE EMPTY DIRECTORY
# ============================================================

print("\n=== REMOVE DIRECTORY ===")

empty_folder = Path("empty_folder")

empty_folder.mkdir(exist_ok=True)

empty_folder.rmdir()

print("empty_folder removed")


# ============================================================
# 25. FINAL SUMMARY
# ============================================================

print("\n=== DAY 24 COMPLETE ===")

print("""
You learned:
- File paths
- Current working directory
- os module
- pathlib module
- File handling
- Directory traversal
- Recursive searching
- File organization
- AI document loading

Most important import:
from pathlib import Path
""")