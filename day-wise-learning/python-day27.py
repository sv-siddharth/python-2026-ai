"""
DAY 27 ⭐⭐⭐
DICTIONARY COMPREHENSIONS

Topics Covered:
1. Basic dictionary comprehensions
2. Conditions in comprehensions
3. Iterating through dictionaries
4. Conditional values
5. Nested dictionary comprehensions
6. Real-world AI engineering examples
7. Practice exercises
8. Mini project

Author: ChatGPT Notes
"""

print("========== DAY 27: DICTIONARY COMPREHENSIONS ==========\n")

# =========================================================
# 1. BASIC DICTIONARY COMPREHENSION
# =========================================================

print("1. BASIC DICTIONARY COMPREHENSION\n")

numbers = [1, 2, 3, 4, 5]

square_dict = {n: n * n for n in numbers}

print("Original numbers:", numbers)
print("Squared dictionary:", square_dict)

print("\n" + "=" * 60 + "\n")

# =========================================================
# 2. WORD LENGTH DICTIONARY
# =========================================================

print("2. WORD LENGTH DICTIONARY\n")

words = ["python", "java", "golang", "rust"]

word_lengths = {word: len(word) for word in words}

print("Words:", words)
print("Word lengths:", word_lengths)

print("\n" + "=" * 60 + "\n")

# =========================================================
# 3. USING CONDITIONS
# =========================================================

print("3. USING CONDITIONS\n")

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_squares = {
    n: n * n
    for n in numbers
    if n % 2 == 0
}

print("Even squares only:")
print(even_squares)

print("\n" + "=" * 60 + "\n")

# =========================================================
# 4. ITERATING THROUGH EXISTING DICTIONARY
# =========================================================

print("4. ITERATING THROUGH EXISTING DICTIONARY\n")

student_scores = {
    "Alex": 80,
    "Bob": 65,
    "Charlie": 90,
    "David": 55
}

passed_students = {
    student: score
    for student, score in student_scores.items()
    if score >= 70
}

print("Original scores:")
print(student_scores)

print("\nPassed students:")
print(passed_students)

print("\n" + "=" * 60 + "\n")

# =========================================================
# 5. CONDITIONAL VALUE ASSIGNMENT
# =========================================================

print("5. CONDITIONAL VALUE ASSIGNMENT\n")

results = {
    student: "Pass" if score >= 70 else "Fail"
    for student, score in student_scores.items()
}

print(results)

print("\n" + "=" * 60 + "\n")

# =========================================================
# 6. TEMPERATURE CONVERSION
# =========================================================

print("6. TEMPERATURE CONVERSION\n")

celsius = {
    "Delhi": 35,
    "Mumbai": 32,
    "Chennai": 38
}

fahrenheit = {
    city: (temp * 9/5) + 32
    for city, temp in celsius.items()
}

print("Celsius:")
print(celsius)

print("\nFahrenheit:")
print(fahrenheit)

print("\n" + "=" * 60 + "\n")

# =========================================================
# 7. NESTED DICTIONARY COMPREHENSION
# =========================================================

print("7. NESTED DICTIONARY COMPREHENSION\n")

multiplication_table = {
    n: {x: x * n for x in range(1, 6)}
    for n in range(1, 4)
}

print(multiplication_table)

print("\n" + "=" * 60 + "\n")

# =========================================================
# 8. REAL-WORLD EXAMPLE — TOKEN FREQUENCY
# =========================================================

print("8. TOKEN FREQUENCY COUNTER\n")

text = "python ai python rag ai embeddings"

words = text.split()

frequency = {
    word: words.count(word)
    for word in words
}

print("Text:")
print(text)

print("\nFrequency:")
print(frequency)

print("\n" + "=" * 60 + "\n")

# =========================================================
# 9. API RESPONSE CLEANUP
# =========================================================

print("9. API RESPONSE CLEANUP\n")

api_response = {
    "id": "abc123",
    "tokens": 400,
    "cost": 2.5,
    "status": "success"
}

cleaned_response = {
    key: value
    for key, value in api_response.items()
    if key != "id"
}

print("Original response:")
print(api_response)

print("\nCleaned response:")
print(cleaned_response)

print("\n" + "=" * 60 + "\n")

# =========================================================
# 10. DICTIONARY METHODS
# =========================================================

print("10. DICTIONARY METHODS\n")

student = {
    "name": "Alex",
    "age": 24,
    "city": "Delhi"
}

print("Keys:")
print(student.keys())

print("\nValues:")
print(student.values())

print("\nItems:")
print(student.items())

print("\n" + "=" * 60 + "\n")

# =========================================================
# 11. MINI PROJECT — GRADE ANALYZER
# =========================================================

print("11. MINI PROJECT — GRADE ANALYZER\n")

student_scores = {
    "Alex": 92,
    "Bob": 67,
    "Charlie": 81,
    "David": 55,
    "Eva": 74
}

grades = {
    student:
    "A" if score >= 90 else
    "B" if score >= 80 else
    "C" if score >= 70 else
    "F"
    for student, score in student_scores.items()
}

print("Grades:")
print(grades)

print("\n" + "=" * 60 + "\n")

# =========================================================
# 12. PRACTICE EXERCISES
# =========================================================

print("12. PRACTICE EXERCISES\n")

# Exercise 1
print("Exercise 1")

cubes = {x: x ** 3 for x in range(1, 5)}

print(cubes)

print("\n---------------------------\n")

# Exercise 2
print("Exercise 2")

names = ["alex", "bob", "charlie"]

name_lengths = {
    name: len(name)
    for name in names
}

print(name_lengths)

print("\n---------------------------\n")

# Exercise 3
print("Exercise 3")

students = {
    "Alex": 88,
    "Bob": 60,
    "Eva": 95,
    "David": 72
}

top_students = {
    name: marks
    for name, marks in students.items()
    if marks > 75
}

print(top_students)

print("\n---------------------------\n")

# Exercise 4
print("Exercise 4")

data = {
    "a": 1,
    "b": 2
}

updated = {
    key: value * 10
    for key, value in data.items()
}

print(updated)

print("\n---------------------------\n")

# Exercise 5
print("Exercise 5")

languages = ["python", "java"]

upper_languages = {
    lang: lang.upper()
    for lang in languages
}

print(upper_languages)

print("\n" + "=" * 60 + "\n")

# =========================================================
# 13. COMMON MISTAKES
# =========================================================

print("13. COMMON MISTAKES\n")

print("Mistake 1:")
print("Using {x*x for x in range(5)} creates a SET, not a dictionary.")

print("\nMistake 2:")
print("Always use .items() when unpacking key-value pairs.")

print("\nCorrect:")
print("for key, value in dictionary.items()")

print("\n" + "=" * 60 + "\n")

# =========================================================
# 14. PERFORMANCE NOTE
# =========================================================

print("14. PERFORMANCE NOTE\n")

print("Dictionary comprehensions are:")
print("✅ Faster")
print("✅ Cleaner")
print("✅ More Pythonic")
print("✅ Frequently used in AI engineering")

print("\n" + "=" * 60 + "\n")

# =========================================================
# 15. FINAL SUMMARY
# =========================================================

print("15. FINAL SUMMARY\n")

print("Today you learned:")
print("✅ Dictionary comprehensions")
print("✅ Filtering")
print("✅ Conditional transformations")
print("✅ Nested comprehensions")
print("✅ Real-world AI examples")
print("✅ Dictionary methods")
print("✅ Performance benefits")

print("\nEND OF DAY 27 🚀")