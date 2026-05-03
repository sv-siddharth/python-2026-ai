"""
==========================================================
🐍 DAY 6 - PYTHON FUNCTIONS (ANGELA YU STYLE NOTES)
==========================================================

This file contains:
- Concepts
- Examples
- Exercises
- Mini Project

⚠️ MOST IMPORTANT DAY SO FAR
Functions = foundation of backend + AI systems

==========================================================
"""

# ==========================================================
# 1. BASIC FUNCTION
# ==========================================================

def greet():
    print("Hello")

greet()


# ==========================================================
# 2. FUNCTION WITH PARAMETERS
# ==========================================================

def greet_with_name(name):
    print(f"Hello {name}")

greet_with_name("Siddharth")


# ==========================================================
# 3. MULTIPLE PARAMETERS
# ==========================================================

def introduce(name, age):
    print(f"My name is {name} and I am {age} years old")

introduce("Sid", 26)


# ==========================================================
# 4. RETURN VALUES (VERY IMPORTANT)
# ==========================================================

def add(a, b):
    return a + b

result = add(2, 3)
print("Addition Result:", result)


# ❌ BAD PRACTICE (DO NOT DO THIS)
def bad_add(a, b):
    print(a + b)

bad_add(2, 3)


# ==========================================================
# 5. FUNCTION WITH LOGIC
# ==========================================================

def is_even(number):
    return number % 2 == 0

print("Is 4 even?", is_even(4))


# ==========================================================
# 6. SCOPE (IMPORTANT)
# ==========================================================

def scope_test():
    x = 10
    print("Inside function:", x)

scope_test()

# print(x)  # ❌ ERROR (x is not defined outside)


# ==========================================================
# FIX FOR SCOPE (RETURN VALUE)
# ==========================================================

def get_number():
    x = 10
    return x

num = get_number()
print("Outside function:", num)


# ==========================================================
# 7. DEFAULT PARAMETERS
# ==========================================================

def greet_default(name="Guest"):
    print(f"Hello {name}")

greet_default()
greet_default("Sid")


# ==========================================================
# 8. KEYWORD ARGUMENTS
# ==========================================================

def greet_keyword(name, age):
    print(name, age)

greet_keyword(age=25, name="Sid")


# ==========================================================
# 9. NESTED FUNCTION CALLS
# ==========================================================

def multiply(a, b):
    return a * b

nested_result = multiply(add(2, 3), 4)
print("Nested Result:", nested_result)


# ==========================================================
# 10. EXERCISES
# ==========================================================

# Exercise 1: Format Name
def format_name(first, last):
    return f"{first.title()} {last.title()}"

print(format_name("siddharth", "verma"))


# Exercise 2: Days in Month
def days_in_month(month):
    if month == 2:
        return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

print("Days in month 2:", days_in_month(2))


# Exercise 3: Calculator Function
def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b

print("Calculator Result:", calculator(5, 3, "+"))


# ==========================================================
# 🚀 MINI PROJECT: CALCULATOR (FUNCTION-BASED)
# ==========================================================

def add_fn(a, b):
    return a + b

def subtract_fn(a, b):
    return a - b

def multiply_fn(a, b):
    return a * b

def divide_fn(a, b):
    return a / b


operations = {
    "+": add_fn,
    "-": subtract_fn,
    "*": multiply_fn,
    "/": divide_fn
}


print("\n--- Calculator ---")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Choose operation (+ - * /): ")

if op in operations:
    result = operations[op](num1, num2)
    print(f"Result: {result}")
else:
    print("Invalid operation")


# ==========================================================
# 🧠 SUMMARY
# ==========================================================

"""
YOU LEARNED:

✔ Functions using def
✔ Parameters vs arguments
✔ Return values (MOST IMPORTANT)
✔ Scope (local vs global)
✔ Default arguments
✔ Keyword arguments
✔ Function chaining
✔ Clean coding practices

==========================================================

🎯 RULE TO REMEMBER:

If you need a value outside a function → USE return

==========================================================
"""