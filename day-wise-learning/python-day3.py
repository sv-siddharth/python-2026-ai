"""
===========================================================
DAY 3: CONTROL FLOW & LOGICAL OPERATORS
Angela Yu Python Bootcamp – Complete Notes
===========================================================

CORE OBJECTIVE:
Learn how to make decisions in Python using:
- if / elif / else
- comparison operators
- logical operators (and, or, not)
- nested conditionals
- multiple conditions
- code logic thinking

WHY THIS MATTERS:
This is the FOUNDATION of:
- Backend logic
- AI decision flows
- APIs
- Real-world applications

===========================================================
"""

# =========================================================
# 1. IF / ELSE STATEMENT
# =========================================================

print("=== IF / ELSE Example ===")

age = 18

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")

# Key Insight:
# if condition must evaluate to True/False


# =========================================================
# 2. COMPARISON OPERATORS
# =========================================================

"""
==  Equal to
!=  Not equal to
>   Greater than
<   Less than
>=  Greater than or equal to
<=  Less than or equal to
"""

print("\n=== Comparison Operators ===")

a = 10
b = 20

print(a == b)   # False
print(a != b)   # True
print(a < b)    # True


# =========================================================
# 3. NESTED IF
# =========================================================

print("\n=== Nested If ===")

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Underage")

# Real-world:
# Login systems, permissions, validations


# =========================================================
# 4. ELIF (ELSE IF)
# =========================================================

print("\n=== ELIF Example ===")

score = 85

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Fail")

# Used when multiple conditions exist


# =========================================================
# 5. LOGICAL OPERATORS
# =========================================================

"""
and → both conditions must be True
or  → at least one condition True
not → reverses condition
"""

print("\n=== Logical Operators ===")

age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive")

if age < 18 or not has_license:
    print("Cannot drive")


# =========================================================
# 6. MODULO OPERATOR (%)
# =========================================================

print("\n=== Modulo Operator ===")

number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# VERY IMPORTANT:
# Used in:
# - Even/Odd checks
# - Cycles
# - Patterns


# =========================================================
# 7. BUILDING REAL LOGIC (PRACTICE)
# =========================================================

# ---------------------------------------------------------
# 1. Odd or Even Checker
# ---------------------------------------------------------

print("\n=== Project 1: Odd or Even ===")

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# ---------------------------------------------------------
# 2. BMI Calculator with Conditions
# ---------------------------------------------------------

print("\n=== Project 2: BMI Calculator ===")

height = float(input("Enter height (m): "))
weight = float(input("Enter weight (kg): "))

bmi = weight / (height ** 2)

print(f"Your BMI is {round(bmi, 2)}")

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")


# ---------------------------------------------------------
# 3. Leap Year Checker
# ---------------------------------------------------------

print("\n=== Project 3: Leap Year Checker ===")

year = int(input("Enter year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")

# Key Logic:
# - Divisible by 4 → leap
# - Divisible by 100 → NOT leap
# - Divisible by 400 → leap


# ---------------------------------------------------------
# 4. Pizza Order System (Mini Backend Logic)
# ---------------------------------------------------------

print("\n=== Project 4: Pizza Order ===")

print("Welcome to Python Pizza!")

size = input("Size (S/M/L): ").upper()
pepperoni = input("Add pepperoni? (Y/N): ").upper()
extra_cheese = input("Extra cheese? (Y/N): ").upper()

bill = 0

# Size pricing
if size == "S":
    bill = 100
elif size == "M":
    bill = 200
else:
    bill = 300

# Pepperoni pricing
if pepperoni == "Y":
    if size == "S":
        bill += 30
    else:
        bill += 50

# Extra cheese
if extra_cheese == "Y":
    bill += 20

print(f"Final bill: ₹{bill}")

# THIS IS IMPORTANT:
# This is EXACTLY how backend systems work:
# - Input
# - Conditions
# - Price calculation
# - Output


# =========================================================
# 8. KEY TAKEAWAYS
# =========================================================

"""
1. if/else controls program flow
2. Logical operators combine conditions
3. Nested conditions = deeper logic
4. Modulo operator is heavily used
5. Real-world backend = just conditions + data

YOU JUST BUILT:
- Decision systems
- Backend logic
- Real-world mini applications

===========================================================
"""


# =========================================================
# 9. INTERVIEW + AI ENGINEER CONNECTION
# =========================================================

"""
These concepts directly map to:

- API validations
- Authentication systems
- AI agent decision trees
- RAG filtering logic
- Business rules engines

If you don't master this:
You cannot build real systems

===========================================================
"""