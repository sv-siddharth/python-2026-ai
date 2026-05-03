"""
DAY 5 - LOOPS (Angela Yu Style Notes)

Topics Covered:
- for loop
- while loop
- range()
- break, continue, pass
- nested loops
- FizzBuzz
"""

# FOR LOOP
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# RANGE
for i in range(5):
    print(i)

# SUM PATTERN
total = 0
for i in range(1, 11):
    total += i
print("Sum:", total)

# WHILE LOOP
count = 1
while count <= 5:
    print(count)
    count += 1

# BREAK
for i in range(10):
    if i == 5:
        break
    print(i)

# CONTINUE
for i in range(5):
    if i == 2:
        continue
    print(i)

# NESTED LOOP
for i in range(3):
    for j in range(3):
        print(i, j)

# MAX FINDER
numbers = [3, 7, 2, 9, 5]
max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num

print("Max:", max_num)

# FIZZBUZZ
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)