# DAY 10 - LISTS & NESTED LISTS

# 1. Creating a list
fruits = ["apple", "banana", "cherry"]

# 2. Accessing items
print(fruits[0])
print(fruits[-1])

# 3. Modify
fruits[1] = "mango"

# 4. Add
fruits.append("orange")
fruits.extend(["kiwi", "grapes"])

# 5. Remove
fruits.remove("apple")
fruits.pop()

# 6. Loop
for fruit in fruits:
    print(fruit)

# 7. Check existence
if "mango" in fruits:
    print("Found mango")

# 8. Length
print(len(fruits))

# 9. Numbers
numbers = [10, 20, 30, 40]
print(sum(numbers))
print(max(numbers))
print(min(numbers))

# 10. Nested list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])  # 6

# Mini Project - Banker Roulette
import random

names = ["Alice", "Bob", "Charlie", "David"]
print(random.choice(names))

# Mini Project - Highest Score
scores = [78, 65, 89, 55, 91]

highest = 0
for score in scores:
    if score > highest:
        highest = score

print(f"Highest score: {highest}")

# Mini Project - Treasure Map
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]

treasure_map = [row1, row2, row3]

position = "12"  # simulate input

row = int(position[0])
col = int(position[1])

treasure_map[row][col] = "X"

for r in treasure_map:
    print(r)