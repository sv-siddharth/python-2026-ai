"""
========================================
DAY 12: SCOPE & NUMBER GUESSING GAME
========================================

Today’s Concepts:
1. Scope (Local vs Global)
2. Global Constants
3. Modifying Global Variables
4. Python Namespaces
5. Build a Number Guessing Game Project

----------------------------------------
1. LOCAL VS GLOBAL SCOPE
----------------------------------------

Local Scope:
- Variables created inside a function
- Only accessible inside that function

Example:
"""

def local_example():
    x = 10  # local variable
    print(x)

local_example()

# print(x) ❌ ERROR (x not accessible outside function)


"""
Global Scope:
- Variables defined outside all functions
- Accessible everywhere in the file
"""

y = 20  # global variable

def global_example():
    print(y)

global_example()


"""
----------------------------------------
2. BLOCK SCOPE (IMPORTANT DIFFERENCE)
----------------------------------------

Python DOES NOT have block scope like JS

Example:
"""

if True:
    z = 50

print(z)  # ✅ Works in Python


"""
----------------------------------------
3. MODIFYING GLOBAL VARIABLES
----------------------------------------

You cannot modify a global variable directly inside a function
unless you use the 'global' keyword
"""

count = 0

def increase():
    global count
    count += 1

increase()
print(count)


"""
⚠️ BEST PRACTICE:
Avoid modifying global variables directly.
Instead, use return values.
"""

def increase_better(c):
    return c + 1

count = increase_better(count)
print(count)


"""
----------------------------------------
4. GLOBAL CONSTANTS
----------------------------------------

Convention:
- Use ALL CAPS
- These values should NOT change

Example:
"""

PI = 3.14159
URL = "https://api.example.com"


"""
----------------------------------------
5. PYTHON NAMESPACE
----------------------------------------

Namespace = where variables/functions are stored

Types:
- Local namespace
- Global namespace

Each function has its own namespace

Example:
"""

def namespace_example():
    a = 100
    print(a)

namespace_example()

a = 200
print(a)  # Different from inside function


"""
========================================
PROJECT: NUMBER GUESSING GAME
========================================

Game Rules:
- Computer randomly picks a number between 1 and 100
- User has to guess the number
- Two difficulty levels:
    Easy = 10 attempts
    Hard = 5 attempts
- Game gives hints:
    "Too high" or "Too low"
- Game ends when:
    - User guesses correctly
    - User runs out of attempts

----------------------------------------
STEP 1: IMPORT RANDOM
----------------------------------------
"""

import random


"""
----------------------------------------
STEP 2: CONSTANTS
----------------------------------------
"""

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


"""
----------------------------------------
STEP 3: FUNCTION TO CHECK ANSWER
----------------------------------------
"""

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"Correct! The answer was {answer}")


"""
----------------------------------------
STEP 4: SET DIFFICULTY
----------------------------------------
"""

def set_difficulty():
    level = input("Choose difficulty: 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


"""
----------------------------------------
STEP 5: MAIN GAME LOGIC
----------------------------------------
"""

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1, 100)

    turns = set_difficulty()

    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining.")

        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You ran out of guesses. You lose.")
            return
        elif guess != answer:
            print("Guess again.")


"""
----------------------------------------
STEP 6: RUN GAME
----------------------------------------
"""

game()


"""
========================================
KEY TAKEAWAYS
========================================

1. Scope controls where variables can be accessed
2. Local variables exist only inside functions
3. Global variables exist everywhere (but avoid modifying them)
4. Use constants (ALL CAPS) for fixed values
5. Functions should return values instead of modifying globals
6. Project helps combine:
   - Functions
   - Loops
   - Conditionals
   - User input
   - Random module

----------------------------------------
REAL WORLD CONNECTION (IMPORTANT)
----------------------------------------

You will use this in:
- API rate limits (constants)
- Environment configs
- Game logic / backend logic
- Avoiding bugs in large codebases

----------------------------------------
PHASE 1 (YOUR ROADMAP) CONNECTION
----------------------------------------

This day is CRITICAL because:
- Scope bugs = most common real-world bug
- Clean function design = required for AI pipelines
- Constants = used heavily in API configs

----------------------------------------
NEXT: DAY 13
----------------------------------------
Topics:
- Debugging
- Finding and fixing errors
- Improving code reliability

========================================
"""