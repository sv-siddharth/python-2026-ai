"""
===========================================================
🐍 DAY 2: DATA TYPES & NUMBERS (Angela Yu Python Course)
===========================================================

This file acts as:
1. 📘 A README-style explanation
2. 💻 An executable Python learning script
3. 🧠 A revision guide for interviews

-----------------------------------------------------------
📌 WHAT YOU WILL LEARN
-----------------------------------------------------------
- Primitive data types (str, int, float, bool)
- Type checking and type conversion
- Mathematical operations
- Number formatting and rounding
- f-strings (modern formatting)
- Mini Project: Tip Calculator

===========================================================
"""

# =========================================================
# 🧠 1. DATA TYPES
# =========================================================

# 🔹 String (str)
print("Hello"[0])  # H
print("Hello"[4])  # o

# 🔹 Integer (int)
num = 123
big_num = 1_000_000  # readable number

# 🔹 Float (float)
pi = 3.14159

# 🔹 Boolean (bool)
is_active = True

print(type("Hello"))   # str
print(type(123))       # int
print(type(3.14))      # float
print(type(True))      # bool


# =========================================================
# 🔍 2. TYPE CONVERSION (CASTING)
# =========================================================

# Converting between types
num_str = "123"
num_int = int(num_str)

float_val = float("3.14")
str_val = str(456)

print(num_int, float_val, str_val)

# ⚠️ This will crash:
# int("abc")  # ValueError


# =========================================================
# ⚠️ 3. TYPE ERROR EXAMPLE
# =========================================================

# ❌ Incorrect
# print("Age: " + 25)

# ✅ Correct
print("Age: " + str(25))


# =========================================================
# 🔢 4. MATHEMATICAL OPERATIONS
# =========================================================

print(5 + 3)   # addition
print(5 - 3)   # subtraction
print(5 * 3)   # multiplication
print(5 / 2)   # division → float

# Advanced operators
print(5 ** 2)  # exponent → 25
print(5 // 2)  # floor division → 2
print(5 % 2)   # modulus → 1


# =========================================================
# 📊 5. ORDER OF OPERATIONS (PEMDAS)
# =========================================================

result = 3 * 3 + 3 / 3 - 3
print(result)  # 7.0


# =========================================================
# 🔄 6. NUMBER MANIPULATION
# =========================================================

# Rounding
print(round(3.14159))        # 3
print(round(3.14159, 2))     # 3.14

# Assignment operators
score = 0
score += 1
score *= 2
print(score)


# =========================================================
# 🎯 7. f-STRINGS (IMPORTANT)
# =========================================================

score = 10
height = 1.8
isWinning = True

print(f"Score: {score}, Height: {height}, Winning: {isWinning}")


# =========================================================
# 🧪 8. MINI PROJECT: TIP CALCULATOR
# =========================================================

print("\n--- TIP CALCULATOR ---")

# User input
bill = float(input("Enter total bill (₹): "))
tip = int(input("Enter tip percentage (10, 12, 15): "))
people = int(input("Number of people: "))

# Calculations
tip_amount = bill * (tip / 100)
total_bill = bill + tip_amount
bill_per_person = total_bill / people

# Rounding result
final_amount = round(bill_per_person, 2)

# Output
print(f"Each person should pay: ₹{final_amount}")


# =========================================================
# 🧠 9. KEY TAKEAWAYS
# =========================================================

"""
✔ Python is dynamically typed
✔ Always convert input values
✔ Use f-strings for formatting
✔ Division returns float by default
✔ Use round() for financial calculations
"""


# =========================================================
# 🔥 10. PRACTICE TASKS
# =========================================================

"""
1. Take a 2-digit number and print sum of digits
2. Build BMI calculator
3. Convert seconds → minutes + seconds
4. Build EMI calculator
"""


# =========================================================
# 🚀 END OF DAY 2
# =========================================================