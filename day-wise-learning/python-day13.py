"""
DAY 13 - DEBUGGING

Goal:
- Learn how to find and fix errors
- Understand common bug patterns
- Build debugging mindset
"""

# 1. PRINT DEBUGGING
def add(a, b):
    print("a:", a)
    print("b:", b)
    return a + b

print(add(5, 3))


# 2. HANDLE EMPTY INPUT BUG
def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

print(average([1, 2, 3]))
print(average([]))


# 3. ASSERTIONS
x = 10
assert x > 0, "x must be positive"


# 4. TRY-EXCEPT
try:
    number = int("abc")
except ValueError:
    print("Conversion failed!")


# 5. DEBUGGING LOOP
numbers = [1, 2, 3, 4]

for i in range(len(numbers)):
    print(f"Index: {i}, Value: {numbers[i]}")


# 6. LIST MUTATION BUG DEMO
a = [1, 2, 3]
b = a
b.append(4)

print("a:", a)
print("b:", b)


# 7. FIX USING COPY
a = [1, 2, 3]
b = a.copy()
b.append(4)

print("a after fix:", a)
print("b after fix:", b)