"""
===========================================================
🐍 DAY 4 – PYTHON (Angela Yu Style Notes)
TOPIC: RANDOMISATION + LISTS (CORE FOUNDATION)
===========================================================

This day is VERY IMPORTANT.

Why?
→ Lists = used everywhere (APIs, JSON, DB, ML, etc.)
→ Randomisation = used in games, simulations, AI sampling

If you master this → you're entering REAL programming territory.

-----------------------------------------------------------
📌 1. RANDOM MODULE
-----------------------------------------------------------

Python has a built-in module called `random`

Think of it like:
→ A toolkit to generate randomness

IMPORTING:
"""

import random

"""
-----------------------------------------------------------
🎯 1.1 RANDOM INTEGER
-----------------------------------------------------------
"""

random_integer = random.randint(1, 10)
print("Random Integer:", random_integer)

"""
✔ randint(a, b)
→ includes BOTH a and b

Example:
random.randint(1, 10)
→ can give 1 or 10

-----------------------------------------------------------
🎯 1.2 RANDOM FLOAT
-----------------------------------------------------------
"""

random_float = random.random()
print("Random Float:", random_float)

"""
✔ random.random()
→ 0.0 <= number < 1.0

Example:
0.23423, 0.999, etc.

Custom Range:
"""

custom_float = random.random() * 10
print("0 to 10 float:", custom_float)

"""
-----------------------------------------------------------
🎯 1.3 RANDOM DECIMAL RANGE
-----------------------------------------------------------
"""

random_uniform = random.uniform(1, 10)
print("Uniform Float:", random_uniform)

"""
✔ random.uniform(a, b)
→ float between a and b

-----------------------------------------------------------
📌 2. LISTS (VERY IMPORTANT)
-----------------------------------------------------------

List = collection of items

Think:
→ JS array
→ Ordered + mutable

-----------------------------------------------------------
🎯 2.1 CREATING LISTS
-----------------------------------------------------------
"""

fruits = ["apple", "banana", "cherry"]
print(fruits)

"""
-----------------------------------------------------------
🎯 2.2 ACCESSING ITEMS
-----------------------------------------------------------
"""

print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[-1])  # cherry (reverse indexing)

"""
-----------------------------------------------------------
🎯 2.3 MODIFYING LIST
-----------------------------------------------------------
"""

fruits[1] = "mango"
print(fruits)

"""
-----------------------------------------------------------
🎯 2.4 ADDING ITEMS
-----------------------------------------------------------
"""

fruits.append("orange")  # add at end
print(fruits)

fruits.extend(["grape", "kiwi"])  # add multiple
print(fruits)

"""
-----------------------------------------------------------
🎯 2.5 LIST LENGTH
-----------------------------------------------------------
"""

print(len(fruits))

"""
-----------------------------------------------------------
🎯 2.6 RANDOM CHOICE FROM LIST
-----------------------------------------------------------
"""

random_fruit = random.choice(fruits)
print("Random Fruit:", random_fruit)

"""
-----------------------------------------------------------
📌 3. INDEX ERRORS (VERY COMMON BUG)
-----------------------------------------------------------

If index out of range → crash
"""

# print(fruits[100])  ❌ IndexError

"""
-----------------------------------------------------------
📌 4. NESTED LISTS
-----------------------------------------------------------

List inside list
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])      # [1,2,3]
print(matrix[1][2])   # 6

"""
-----------------------------------------------------------
📌 5. PRACTICE PROJECTS
-----------------------------------------------------------

These are EXACTLY what build your fundamentals.

-----------------------------------------------------------
🚀 PROJECT 1: BANKER ROULETTE (WHO PAYS?)
-----------------------------------------------------------
"""

names = input("Enter names separated by comma: ").split(", ")

payer = random.choice(names)

print(f"{payer} will pay the bill 💸")

"""
-----------------------------------------------------------
🚀 PROJECT 2: TREASURE MAP
-----------------------------------------------------------
"""

row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]

map = [row1, row2, row3]

print("Initial Map:")
print(f"{row1}\n{row2}\n{row3}")

position = input("Enter position (rowcol): ")

row = int(position[0]) - 1
col = int(position[1]) - 1

map[row][col] = "X"

print("\nUpdated Map:")
print(f"{row1}\n{row2}\n{row3}")

"""
-----------------------------------------------------------
🚀 PROJECT 3: ROCK PAPER SCISSORS (IMPORTANT)
-----------------------------------------------------------
"""

rock = """
    🪨
"""

paper = """
    📄
"""

scissors = """
    ✂️
"""

game_images = [rock, paper, scissors]

user_choice = int(input("0 for Rock, 1 for Paper, 2 for Scissors: "))

if user_choice >= 3 or user_choice < 0:
    print("Invalid choice")
else:
    print("You chose:")
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == computer_choice:
        print("Draw")
    elif user_choice == 0 and computer_choice == 2:
        print("You win")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win")
    else:
        print("You lose")

"""
-----------------------------------------------------------
📌 6. LISTS VS STRINGS
-----------------------------------------------------------

String → immutable
List → mutable

Example:
"""

name = "hello"
# name[0] = "H" ❌

letters = ["h", "e", "l", "l", "o"]
letters[0] = "H"  # ✅

"""
-----------------------------------------------------------
📌 7. KEY TAKEAWAYS (VERY IMPORTANT)
-----------------------------------------------------------

✔ Lists = most used data structure
✔ Indexing starts from 0
✔ Negative indexing works
✔ Lists are mutable
✔ random module is powerful
✔ Nested lists = foundation for grids, matrices

-----------------------------------------------------------
📌 8. REAL-WORLD CONNECTION
-----------------------------------------------------------

Lists are used in:
→ API responses (JSON arrays)
→ Database rows
→ AI datasets
→ Chat history storage
→ Recommendation systems

Random used in:
→ Games
→ ML sampling
→ A/B testing
→ Simulations

-----------------------------------------------------------
📌 9. INTERVIEW TIPS
-----------------------------------------------------------

Be ready for:
→ Reverse a list
→ Find max/min
→ Remove duplicates
→ Iterate efficiently

-----------------------------------------------------------
📌 10. NEXT LEVEL (PREVIEW DAY 5)
-----------------------------------------------------------

Next you’ll learn:
→ for loops
→ iteration patterns
→ range()
→ aggregation logic

THIS is where real logic building starts.

-----------------------------------------------------------
🔥 FINAL THOUGHT
-----------------------------------------------------------

If Day 3 = logic

Then Day 4 = DATA STRUCTURES START

Without mastering lists:
→ You cannot build real systems

Practice these projects again until:
✔ You write without looking
✔ You understand indexing deeply

===========================================================
END OF DAY 4
===========================================================
"""