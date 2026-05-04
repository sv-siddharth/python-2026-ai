"""
===========================================================
🐍 DAY 9: DICTIONARIES & NESTING (Angela Yu Style Notes)
===========================================================

GOAL:
- Understand dictionaries (key-value pairs)
- Learn how to access, update, loop through dictionaries
- Learn nesting (lists inside dicts, dicts inside dicts)
- Build a mini project (Secret Auction)

WHY IMPORTANT:
- Core for real-world apps (JSON, APIs, configs, DB data)
- Required for RAG, APIs, LLM responses (everything is dict-like)

===========================================================
1. WHAT IS A DICTIONARY?
===========================================================

Dictionary = key-value pairs

Syntax:
dict_name = {
    "key": "value",
    "key2": "value2"
}
"""

# Example
student = {
    "name": "Siddharth",
    "age": 25,
    "skills": ["Python", "React"]
}

print(student)


"""
===========================================================
2. ACCESSING VALUES
===========================================================
"""

print(student["name"])   # Siddharth
print(student["skills"]) # ["Python", "React"]

# ⚠️ Difference vs list:
# list → index
# dict → key


"""
===========================================================
3. ADDING NEW ITEMS
===========================================================
"""

student["city"] = "Delhi"
print(student)


"""
===========================================================
4. UPDATING VALUES
===========================================================
"""

student["age"] = 26
print(student)


"""
===========================================================
5. LOOPING THROUGH DICTIONARY
===========================================================
"""

for key in student:
    print(key)  # prints keys

for key in student:
    print(student[key])  # prints values

for key, value in student.items():
    print(key, value)


"""
===========================================================
6. EMPTY DICTIONARY
===========================================================
"""

empty_dict = {}

# Useful for dynamic data
empty_dict["name"] = "AI Engineer"
print(empty_dict)


"""
===========================================================
7. WIPE DICTIONARY
===========================================================
"""

student.clear()
print(student)  # {}


"""
===========================================================
8. NESTING (VERY IMPORTANT 🔥)
===========================================================

You can store:
- List inside dict
- Dict inside dict
- Dict inside list
"""

# List inside dict
user = {
    "name": "Sid",
    "skills": ["Python", "AI", "React"]
}

# Dict inside dict
dev = {
    "frontend": {
        "framework": "React",
        "level": "Advanced"
    },
    "backend": {
        "language": "Python",
        "level": "Intermediate"
    }
}

print(dev["frontend"]["framework"])


"""
===========================================================
9. DICTIONARY INSIDE LIST (REAL WORLD)
===========================================================

Example: multiple users
"""

users = [
    {"name": "Sid", "age": 25},
    {"name": "Rahul", "age": 28},
    {"name": "Aman", "age": 30}
]

print(users[1]["name"])  # Rahul


"""
===========================================================
10. PRACTICE: GRADING PROGRAM
===========================================================

Convert scores → grades
"""

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]

    if score >= 90:
        student_grades[student] = "Outstanding"
    elif score >= 80:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)


"""
===========================================================
🔥 MINI PROJECT: SECRET AUCTION PROGRAM
===========================================================

Concepts used:
- Dictionaries
- Loops
- Max value logic

Goal:
Find highest bidder
"""

bids = {}

def find_highest_bidder(bidding_dict):
    highest_bid = 0
    winner = ""

    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"Winner is {winner} with bid {highest_bid}")


# Simulated input
bids["Sid"] = 250
bids["Rahul"] = 300
bids["Aman"] = 200

find_highest_bidder(bids)


"""
===========================================================
11. REAL WORLD CONNECTION (VERY IMPORTANT 🚀)
===========================================================

Dictionaries = backbone of:

1. JSON (APIs)
   {
       "user": "sid",
       "messages": [...]
   }

2. LLM responses (OpenAI/Anthropic)
   response["choices"][0]["message"]["content"]

3. RAG systems
   {
       "chunk": "...",
       "embedding": [...]
   }

4. Backend systems (Node/Python)
   request.body → dictionary

👉 If you master dictionaries → you unlock AI systems

===========================================================
12. KEY TAKEAWAYS
===========================================================

- Dict = key:value pairs
- Access via key, not index
- Mutable (can update)
- Loop using .items()
- Nesting = extremely important

===========================================================
NEXT: DAY 10 → FUNCTIONS WITH OUTPUTS
===========================================================
"""