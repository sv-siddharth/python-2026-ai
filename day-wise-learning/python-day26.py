"""
DAY 26 - LIST COMPREHENSIONS ⭐⭐⭐

Topics Covered:
1. Basic List Comprehensions
2. Conditional List Comprehensions
3. if-else List Comprehensions
4. Nested List Comprehensions
5. Dictionary Comprehensions
6. Set Comprehensions
7. Real AI Engineering Examples
"""

print("========== DAY 26 - LIST COMPREHENSIONS ==========\n")

# =========================================================
# 1. BASIC LIST COMPREHENSION
# =========================================================

print("1. BASIC LIST COMPREHENSION\n")

numbers = [1, 2, 3, 4, 5]

# Traditional Loop
traditional = []

for n in numbers:
    traditional.append(n * 2)

print("Traditional Loop:", traditional)

# List Comprehension
comprehension = [n * 2 for n in numbers]

print("List Comprehension:", comprehension)

print("\n" + "=" * 50 + "\n")

# =========================================================
# 2. SIMPLE EXAMPLES
# =========================================================

print("2. SIMPLE EXAMPLES\n")

# Add 1
numbers = [1, 2, 3, 4]

plus_one = [n + 1 for n in numbers]

print("Add 1:", plus_one)

# Uppercase conversion
names = ["sid", "rahul", "aman"]

upper_names = [name.upper() for name in names]

print("Uppercase Names:", upper_names)

# Convert string to list
word = "python"

letters = [letter for letter in word]

print("Letters:", letters)

print("\n" + "=" * 50 + "\n")

# =========================================================
# 3. CONDITIONAL LIST COMPREHENSION
# =========================================================

print("3. CONDITIONAL LIST COMPREHENSION\n")

numbers = [1, 2, 3, 4, 5, 6]

# Even numbers
even_numbers = [n for n in numbers if n % 2 == 0]

print("Even Numbers:", even_numbers)

# Numbers greater than 3
greater_than_3 = [n for n in numbers if n > 3]

print("Greater Than 3:", greater_than_3)

# Long names
names = ["sid", "rahul", "a", "python"]

long_names = [name for name in names if len(name) > 3]

print("Long Names:", long_names)

print("\n" + "=" * 50 + "\n")

# =========================================================
# 4. IF-ELSE LIST COMPREHENSION
# =========================================================

print("4. IF-ELSE LIST COMPREHENSION\n")

numbers = [1, 2, 3, 4, 5]

result = ["Even" if n % 2 == 0 else "Odd" for n in numbers]

print("Odd/Even:", result)

# Positive or Negative
values = [-2, 5, -1, 8]

status = ["Positive" if x > 0 else "Negative" for x in values]

print("Positive/Negative:", status)

print("\n" + "=" * 50 + "\n")

# =========================================================
# 5. NESTED LIST COMPREHENSION
# =========================================================

print("5. NESTED LIST COMPREHENSION\n")

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

# Flatten matrix
flattened = [num for row in matrix for num in row]

print("Flattened Matrix:", flattened)

print("\n" + "=" * 50 + "\n")

# =========================================================
# 6. DICTIONARY COMPREHENSION
# =========================================================

print("6. DICTIONARY COMPREHENSION\n")

numbers = [1, 2, 3, 4, 5]

squares = {n: n * n for n in numbers}

print("Squares Dictionary:", squares)

# Word lengths
words = ["python", "ai", "backend"]

word_lengths = {word: len(word) for word in words}

print("Word Lengths:", word_lengths)

print("\n" + "=" * 50 + "\n")

# =========================================================
# 7. SET COMPREHENSION
# =========================================================

print("7. SET COMPREHENSION\n")

numbers = [1, 1, 2, 2, 3, 3, 4]

unique_numbers = {n for n in numbers}

print("Unique Numbers:", unique_numbers)

print("\n" + "=" * 50 + "\n")

# =========================================================
# 8. REAL AI ENGINEERING EXAMPLES
# =========================================================

print("8. REAL AI ENGINEERING EXAMPLES\n")

# Example 1 - Extract text from documents
documents = [
    {"text": "Python is awesome"},
    {"text": "AI is the future"},
    {"text": "LangChain is useful"}
]

texts = [doc["text"] for doc in documents]

print("Extracted Texts:")
print(texts)

print()

# Example 2 - Filter similarity scores
scores = [0.91, 0.45, 0.82, 0.30, 0.99]

relevant_scores = [score for score in scores if score > 0.8]

print("Relevant Scores:")
print(relevant_scores)

print()

# Example 3 - API cleanup
users = [
    {"name": "Sid", "active": True},
    {"name": "Rahul", "active": False},
    {"name": "Aman", "active": True}
]

active_users = [user["name"] for user in users if user["active"]]

print("Active Users:")
print(active_users)

print("\n" + "=" * 50 + "\n")

# =========================================================
# 9. ADVANCED EXAMPLES
# =========================================================

print("9. ADVANCED EXAMPLES\n")

# Flatten nested JSON tags
data = [
    {"tags": ["python", "ai"]},
    {"tags": ["backend", "fastapi"]}
]

all_tags = [tag for item in data for tag in item["tags"]]

print("All Tags:")
print(all_tags)

print()

# Create embedding payloads
texts = ["hello", "world", "python"]

payloads = [
    {
        "text": text,
        "length": len(text)
    }
    for text in texts
]

print("Embedding Payloads:")
print(payloads)

print("\n" + "=" * 50 + "\n")

# =========================================================
# 10. MINI PROJECT - STUDENT SCORE FILTER
# =========================================================

print("10. MINI PROJECT - STUDENT SCORE FILTER\n")

students = [
    {"name": "Sid", "score": 85},
    {"name": "Rahul", "score": 45},
    {"name": "Aman", "score": 92},
    {"name": "Karan", "score": 30},
]

passed_students = [
    student["name"]
    for student in students
    if student["score"] >= 50
]

print("Passed Students:")
print(passed_students)

print("\n" + "=" * 50 + "\n")

# =========================================================
# 11. FINAL PRACTICE CHALLENGE
# =========================================================

print("11. FINAL PRACTICE CHALLENGE\n")

products = [
    {"name": "Laptop", "price": 70000},
    {"name": "Mouse", "price": 500},
    {"name": "Keyboard", "price": 2000},
]

expensive_products = [
    product["name"]
    for product in products
    if product["price"] > 5000
]

print("Expensive Products:")
print(expensive_products)

print("\n" + "=" * 50 + "\n")

# =========================================================
# 12. BONUS PRACTICE
# =========================================================

print("12. BONUS PRACTICE\n")

# Square numbers
squares = [n * n for n in range(1, 11)]

print("Squares 1-10:")
print(squares)

print()

# Extract vowels
word = "artificial intelligence"

vowels = [char for char in word if char in "aeiou"]

print("Vowels:")
print(vowels)

print()

# Even squares
even_squares = [n * n for n in range(1, 11) if n % 2 == 0]

print("Even Squares:")
print(even_squares)

print("\n" + "=" * 50 + "\n")

print("DAY 26 COMPLETE ✅")
print("You now understand List Comprehensions in Python.")