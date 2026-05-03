"""
============================================================
DAY 1 — PYTHON BASICS (ANGELA YU STYLE, UPGRADED)
============================================================

This file is structured like a README + executable Python examples.
You can run sections individually to understand behavior.

------------------------------------------------------------
TABLE OF CONTENTS
------------------------------------------------------------
1. Hello World
2. How Python Runs
3. print() Function
4. Strings
5. Data Types
6. Type Checking & Conversion
7. Math Operations
8. Input Handling
9. Variables
10. Variable Swapping
11. Mini Project (Band Name Generator)
12. Practice Exercises

------------------------------------------------------------
"""

# ----------------------------------------------------------
# 1. HELLO WORLD
# ----------------------------------------------------------
print("Hello World")

# Python is an interpreted language → runs line by line


# ----------------------------------------------------------
# 2. print() FUNCTION
# ----------------------------------------------------------
print("Hello")
print("World")

# New line using escape character
print("Hello\nWorld")

# String concatenation
print("Hello" + " " + "World")

# Type error example (uncomment to test)
# print("Hello" + 5)  # ❌ Error: cannot concatenate str and int

# Correct way
print("Hello " + str(5))


# ----------------------------------------------------------
# 3. STRINGS
# ----------------------------------------------------------
text = "Hello"

# Indexing (0-based)
print(text[0])  # H
print(text[4])  # o

# Uncomment to see error
# print(text[5])  # ❌ IndexError


# ----------------------------------------------------------
# 4. DATA TYPES
# ----------------------------------------------------------
# int
num1 = 123

# float
num2 = 3.14

# string
name = "Python"

print(num1 + 10)
print(num2 * 2)


# ----------------------------------------------------------
# 5. TYPE CHECKING
# ----------------------------------------------------------
print(type("Hello"))
print(type(123))
print(type(3.14))


# ----------------------------------------------------------
# 6. TYPE CONVERSION
# ----------------------------------------------------------
# Convert int → string
num_str = str(123)

# Convert string → int
num_int = int("123")

# Convert string → float
num_float = float("3.14")

# Uncomment to see crash
# int("abc")  # ❌ ValueError


# ----------------------------------------------------------
# 7. MATHEMATICAL OPERATIONS
# ----------------------------------------------------------
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)   # Always float
print(10 // 3)  # Floor division
print(10 % 3)   # Remainder
print(2 ** 3)   # Power

# Order of operations (PEMDAS)
print(3 * (3 + 3) / 3 - 3)


# ----------------------------------------------------------
# 8. USER INPUT
# ----------------------------------------------------------
# input() always returns string
# Uncomment to test interactively

# user_name = input("Enter your name: ")
# print("Hello " + user_name)

# Numeric input
# age = int(input("Enter your age: "))
# print(age + 5)


# ----------------------------------------------------------
# 9. VARIABLES
# ----------------------------------------------------------
user_name = "Aman"
age = 25

# Naming rules:
# ✔ valid_name
# ❌ 1name (invalid)

print(user_name, age)


# ----------------------------------------------------------
# 10. VARIABLE SWAPPING
# ----------------------------------------------------------
a = 10
b = 20

# Pythonic swap
a, b = b, a
print("a:", a, "b:", b)


# ----------------------------------------------------------
# 11. MINI PROJECT — BAND NAME GENERATOR
# ----------------------------------------------------------
# Uncomment to run interactively

# print("Welcome to Band Name Generator!")
# city = input("Which city did you grow up in?\n")
# pet = input("What is your pet's name?\n")
# band_name = city + " " + pet
# print("Your band name could be: " + band_name)


# ----------------------------------------------------------
# 12. PRACTICE EXERCISES
# ----------------------------------------------------------

# 1. Length of name
# name = input("Enter your name: ")
# print(len(name))

# 2. Age in months
# age = int(input("Enter your age: "))
# print(age * 12)

# 3. Swap two numbers manually
x = 5
y = 10

# Manual swap (without Python shortcut)
temp = x
x = y
y = temp

print("x:", x, "y:", y)


# ----------------------------------------------------------
# END OF DAY 1
# ----------------------------------------------------------

# Key Takeaways:
# - Python is interpreted
# - input() returns string
# - Always convert types when needed
# - Index starts from 0
# - Variables store values
# - Basic operators are foundation for everything
