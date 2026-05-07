# =========================================================
# DAY 31 ⭐⭐⭐
# JSON HANDLING
# Serialization / Deserialization
# =========================================================

import json

# =========================================================
# 1. PYTHON DICTIONARY
# =========================================================

student = {
    "name": "Siddharth",
    "age": 28,
    "skills": ["Python", "React", "AI"],
    "is_working": True
}

print("Original Python Dictionary:")
print(student)

# =========================================================
# 2. SERIALIZATION
# Python -> JSON STRING
# json.dumps()
# =========================================================

json_string = json.dumps(student)

print("\nJSON String:")
print(json_string)

print("\nType after serialization:")
print(type(json_string))

# =========================================================
# 3. PRETTY PRINTING JSON
# =========================================================

pretty_json = json.dumps(student, indent=4)

print("\nPretty Printed JSON:")
print(pretty_json)

# =========================================================
# 4. WRITING JSON TO FILE
# json.dump()
# =========================================================

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("\nstudent.json file created successfully!")

# =========================================================
# 5. DESERIALIZATION
# JSON STRING -> PYTHON
# json.loads()
# =========================================================

json_data = '{"city": "Delhi", "country": "India"}'

python_dict = json.loads(json_data)

print("\nConverted JSON -> Python Dictionary:")
print(python_dict)

print("\nType after deserialization:")
print(type(python_dict))

# =========================================================
# 6. READING JSON FILE
# json.load()
# =========================================================

with open("student.json", "r") as file:
    data = json.load(file)

print("\nData read from JSON file:")
print(data)

print("\nStudent Name:")
print(data["name"])

# =========================================================
# 7. NESTED JSON
# =========================================================

company = {
    "employee": {
        "name": "Sid",
        "department": "AI Engineering",
        "skills": {
            "frontend": ["React", "Next.js"],
            "backend": ["Node.js", "FastAPI"],
            "ai": ["LangChain", "OpenAI"]
        }
    }
}

print("\nNested JSON Example:")
print(company)

print("\nAccess Nested Value:")
print(company["employee"]["skills"]["ai"][0])

# =========================================================
# 8. SORTING JSON KEYS
# =========================================================

random_data = {
    "zebra": 1,
    "apple": 2,
    "cat": 3
}

sorted_json = json.dumps(random_data, indent=4, sort_keys=True)

print("\nSorted JSON Keys:")
print(sorted_json)

# =========================================================
# 9. ERROR HANDLING
# =========================================================

bad_json = "{name: Sid}"

try:
    result = json.loads(bad_json)
except json.JSONDecodeError:
    print("\nInvalid JSON detected!")

# =========================================================
# 10. MINI PROJECT
# STUDENT DATABASE USING JSON
# =========================================================

students = []

print("\n===== STUDENT DATABASE =====")

while True:

    name = input("\nEnter student name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    student_record = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student_record)

    choice = input("Add another student? (y/n): ").lower()

    if choice == "n":
        break

# Save to JSON file
with open("students_database.json", "w") as file:
    json.dump(students, file, indent=4)

print("\nStudent database saved successfully!")

# =========================================================
# 11. READ STUDENT DATABASE
# =========================================================

print("\n===== READING STUDENT DATABASE =====")

with open("students_database.json", "r") as file:
    all_students = json.load(file)

for student in all_students:
    print(
        f"Name: {student['name']}, "
        f"Age: {student['age']}, "
        f"Course: {student['course']}"
    )

# =========================================================
# 12. SIMULATING API RESPONSE
# =========================================================

api_response = {
    "id": "chatcmpl-123",
    "model": "gpt-5",
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": "Hello Siddharth!"
            }
        }
    ]
}

print("\n===== API RESPONSE =====")

message = api_response["choices"][0]["message"]["content"]

print("Assistant Message:")
print(message)

# =========================================================
# 13. SAVING API RESPONSE
# =========================================================

with open("api_response.json", "w") as file:
    json.dump(api_response, file, indent=4)

print("\nAPI response saved!")

# =========================================================
# 14. JSON DATA TYPES
# =========================================================

json_example = {
    "string": "Python",
    "number": 100,
    "float": 99.5,
    "boolean": True,
    "null_value": None,
    "list": [1, 2, 3],
    "object": {"a": 1}
}

print("\nJSON Data Types Example:")
print(json.dumps(json_example, indent=4))

# =========================================================
# 15. IMPORTANT DIFFERENCE
# dump vs dumps
# load vs loads
# =========================================================

print("\n===== IMPORTANT MEMORY TRICK =====")

print("""
dump   -> file
dumps  -> string

load   -> file
loads  -> string
""")

# =========================================================
# END OF DAY 31
# =========================================================

print("\nDay 31 completed successfully!")