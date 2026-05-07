"""
DAY 30 ⭐
ERROR HANDLING & EXCEPTIONS
(try, except, else, finally, raise)

This file contains:
1. Basic try/except
2. Specific exceptions
3. Multiple exceptions
4. else block
5. finally block
6. raise keyword
7. Custom exceptions
8. Mini projects
"""

# =========================================================
# 1. BASIC TRY / EXCEPT
# =========================================================

print("===== BASIC TRY / EXCEPT =====")

try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")

except:
    print("Invalid input")

print()


# =========================================================
# 2. CATCHING SPECIFIC EXCEPTIONS
# =========================================================

print("===== SPECIFIC EXCEPTIONS =====")

try:
    number = int(input("Enter another number: "))
    result = 10 / number

    print(f"Result: {result}")

except ValueError:
    print("Please enter digits only")

except ZeroDivisionError:
    print("Cannot divide by zero")

print()


# =========================================================
# 3. EXCEPTION OBJECT
# =========================================================

print("===== EXCEPTION OBJECT =====")

try:
    number = int("hello")

except ValueError as error:
    print("Actual error message:")
    print(error)

print()


# =========================================================
# 4. ELSE BLOCK
# =========================================================

print("===== ELSE BLOCK =====")

try:
    age = int(input("Enter your age: "))

except ValueError:
    print("Invalid age")

else:
    print("Input successful")
    print(f"Your age is {age}")

print()


# =========================================================
# 5. FINALLY BLOCK
# =========================================================

print("===== FINALLY BLOCK =====")

try:
    file = open("sample.txt")

except FileNotFoundError:
    print("File not found")

finally:
    print("This block always runs")

print()


# =========================================================
# 6. RAISING EXCEPTIONS MANUALLY
# =========================================================

print("===== RAISE KEYWORD =====")

try:
    age = int(input("Enter age: "))

    if age < 0:
        raise ValueError("Age cannot be negative")

    print("Valid age")

except ValueError as error:
    print(error)

print()


# =========================================================
# 7. CUSTOM EXCEPTION
# =========================================================

print("===== CUSTOM EXCEPTION =====")


class InvalidPasswordError(Exception):
    pass


try:
    password = input("Enter password: ")

    if len(password) < 6:
        raise InvalidPasswordError(
            "Password must be at least 6 characters"
        )

    print("Password accepted")

except InvalidPasswordError as error:
    print(error)

print()


# =========================================================
# 8. SAFE CALCULATOR MINI PROJECT
# =========================================================

print("===== SAFE CALCULATOR =====")

try:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    result = number1 / number2

except ValueError:
    print("Please enter valid numbers")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print(f"Result: {result}")

finally:
    print("Calculator finished")

print()


# =========================================================
# 9. SAFE FILE READER MINI PROJECT
# =========================================================

print("===== SAFE FILE READER =====")

try:
    filename = input("Enter filename: ")

    with open(filename, "r") as file:
        content = file.read()

    print("\nFile Content:")
    print(content)

except FileNotFoundError:
    print("File does not exist")

except PermissionError:
    print("Permission denied")

except Exception as error:
    print("Unexpected error occurred")
    print(error)

finally:
    print("File operation complete")

print()


# =========================================================
# 10. COMMON EXCEPTION TYPES DEMO
# =========================================================

print("===== COMMON EXCEPTIONS =====")

# ValueError
try:
    int("abc")
except ValueError:
    print("ValueError caught")

# TypeError
try:
    result = "5" + 5
except TypeError:
    print("TypeError caught")

# IndexError
try:
    numbers = [1, 2]
    print(numbers[10])
except IndexError:
    print("IndexError caught")

# KeyError
try:
    person = {"name": "John"}
    print(person["age"])
except KeyError:
    print("KeyError caught")

print()


# =========================================================
# 11. LOGIN SYSTEM MINI PROJECT
# =========================================================

print("===== LOGIN SYSTEM =====")

CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "python123"

try:
    username = input("Username: ")
    password = input("Password: ")

    if username != CORRECT_USERNAME:
        raise ValueError("Invalid username")

    if password != CORRECT_PASSWORD:
        raise ValueError("Invalid password")

except ValueError as error:
    print(error)

else:
    print("Login successful")

finally:
    print("Login attempt complete")

print()


# =========================================================
# END
# =========================================================

print("DAY 30 COMPLETE ⭐")
print("You learned error handling and exceptions.")