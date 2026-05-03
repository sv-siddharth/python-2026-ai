"""
DAY 7 - DICTIONARIES & NESTING

Core Concept:
Dictionary = Key-Value Pair
Used in APIs, JSON, AI systems

-----------------------------------
1. Creating Dictionary
-----------------------------------
"""

student = {
    "name": "Siddharth",
    "age": 25,
    "city": "Delhi"
}

"""
-----------------------------------
2. Accessing Values
-----------------------------------
"""

print(student["name"])

# Safe access
print(student.get("marks"))        # None
print(student.get("marks", 0))     # default value

"""
-----------------------------------
3. Adding / Updating
-----------------------------------
"""

student["email"] = "test@gmail.com"
student["age"] = 26

"""
-----------------------------------
4. Looping
-----------------------------------
"""

for key, value in student.items():
    print(key, value)

"""
-----------------------------------
5. Nested Dictionary
-----------------------------------
"""

user = {
    "name": "Siddharth",
    "skills": {
        "frontend": ["React", "JS"],
        "backend": ["Node", "Python"]
    }
}

print(user["skills"]["backend"][1])  # Python

"""
-----------------------------------
6. List of Dictionaries
-----------------------------------
"""

users = [
    {"name": "A", "age": 25},
    {"name": "B", "age": 30}
]

print(users[0]["name"])

"""
-----------------------------------
7. Mini Project: Student Grades
-----------------------------------
"""

students = {
    "Siddharth": 90,
    "Rahul": 85,
    "Aman": 78
}

for name, marks in students.items():
    if marks >= 90:
        print(f"{name} scored A")
    elif marks >= 80:
        print(f"{name} scored B")
    else:
        print(f"{name} scored C")