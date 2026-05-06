"""
===========================================================
DAY 17 — THE QUIZ PROJECT & BENEFITS OF OOP
Angela Yu 100 Days of Code — Detailed Notes
===========================================================

TODAY'S MAIN TOPICS:
1. Object Oriented Programming (OOP)
2. Classes and Objects
3. Constructors (__init__)
4. Attributes and Methods
5. self keyword
6. Encapsulation
7. Quiz Project using OOP

WHY THIS DAY IS IMPORTANT:
--------------------------
This is the day where Python starts becoming REAL SOFTWARE ENGINEERING.

Everything in modern AI engineering uses OOP:
- LangChain
- FastAPI
- Django
- CrewAI
- LangGraph
- Pydantic

Without OOP, large systems become impossible to manage.

This day is EXTREMELY important for your AI Engineer roadmap.
"""

# ===========================================================
# SECTION 1 — INTRODUCTION TO OOP
# ===========================================================

"""
OOP = Object Oriented Programming

Instead of:
- random variables
- random functions

We group:
- DATA
- BEHAVIOR

inside OBJECTS.

REAL WORLD ANALOGY:
-------------------

Class = Blueprint
Object = Actual thing made from blueprint

Example:
Class = Car blueprint
Object = BMW, Audi, Ferrari
"""

# ===========================================================
# SECTION 2 — YOUR FIRST CLASS
# ===========================================================

# Creating a class
class User:
    pass


# Creating objects from class
user_1 = User()
user_2 = User()

print("Objects created successfully!")
print(user_1)
print(user_2)

"""
OUTPUT WILL LOOK SOMETHING LIKE:

<__main__.User object at 0x000001>
<__main__.User object at 0x000002>

These are memory locations of objects.
"""

# ===========================================================
# SECTION 3 — ADDING ATTRIBUTES MANUALLY
# ===========================================================

"""
Attributes = Variables inside objects
"""

user_1.id = "001"
user_1.username = "sid"

print("\nUser 1 Details:")
print(user_1.id)
print(user_1.username)

# ===========================================================
# SECTION 4 — CONSTRUCTOR (__init__)
# ===========================================================

"""
__init__ runs automatically when object is created.

This is called:
- constructor
- initializer
"""

print("\n================ CONSTRUCTOR EXAMPLE ================")


class Student:

    def __init__(self):
        print("New student object created!")


student_1 = Student()

# ===========================================================
# SECTION 5 — UNDERSTANDING self
# ===========================================================

"""
self refers to CURRENT OBJECT.

Without self, Python cannot know:
which object owns which data.

Example:
student_1.name
student_2.name

Both objects need separate storage.
"""

print("\n================ self KEYWORD EXAMPLE ================")


class Employee:

    def __init__(self, emp_id, name):

        # Attributes attached to current object
        self.emp_id = emp_id
        self.name = name


employee_1 = Employee("E001", "Siddharth")
employee_2 = Employee("E002", "Rahul")

print(employee_1.name)
print(employee_2.name)

# ===========================================================
# SECTION 6 — METHODS
# ===========================================================

"""
Methods = Functions inside class

Attributes = Data
Methods = Actions
"""

print("\n================ METHODS EXAMPLE ================")


class InstagramUser:

    def __init__(self, username):

        self.username = username
        self.followers = 0
        self.following = 0

    # Method
    def follow(self, user):

        user.followers += 1
        self.following += 1


user_a = InstagramUser("sid")
user_b = InstagramUser("rahul")

user_a.follow(user_b)

print(f"{user_a.username} Following: {user_a.following}")
print(f"{user_b.username} Followers: {user_b.followers}")

# ===========================================================
# SECTION 7 — OBJECT MEMORY UNDERSTANDING
# ===========================================================

"""
Each object has separate memory.

Example:

user_a:
    username -> sid
    followers -> 0

user_b:
    username -> rahul
    followers -> 1
"""

# ===========================================================
# SECTION 8 — BUILT-IN CLASSES
# ===========================================================

"""
Everything in Python is actually an object.

Examples:
"""

numbers = [1, 2, 3]
name = "Python"

print("\n================ BUILT-IN CLASSES ================")

print(type(numbers))
print(type(name))

"""
OUTPUT:
<class 'list'>
<class 'str'>

Meaning:
list is a class
str is a class
"""

# ===========================================================
# SECTION 9 — QUIZ PROJECT STARTS
# ===========================================================

"""
PROJECT ARCHITECTURE:

1. question_model.py
   -> Question class

2. data.py
   -> Questions data

3. quiz_brain.py
   -> Quiz logic

4. main.py
   -> Runs app

Below we simulate everything in ONE FILE
for easier understanding.
"""

# ===========================================================
# SECTION 10 — QUESTION CLASS
# ===========================================================

print("\n================ QUESTION CLASS ================")


class Question:

    def __init__(self, text, answer):

        self.text = text
        self.answer = answer


# ===========================================================
# SECTION 11 — QUESTION DATA
# ===========================================================

question_data = [

    {
        "text": "Python is dynamically typed.",
        "answer": "True"
    },

    {
        "text": "Java was created before Python.",
        "answer": "True"
    },

    {
        "text": "HTML is a programming language.",
        "answer": "False"
    },

    {
        "text": "AI stands for Artificial Intelligence.",
        "answer": "True"
    }
]

# ===========================================================
# SECTION 12 — CONVERTING DICTIONARIES INTO OBJECTS
# ===========================================================

"""
Very important concept.

In REAL AI systems:
JSON response -> Python objects

Exactly same thing happening here.
"""

question_bank = []

for question in question_data:

    question_text = question["text"]
    question_answer = question["answer"]

    new_question = Question(question_text, question_answer)

    question_bank.append(new_question)

print("Questions converted into objects successfully!")

print(question_bank[0].text)

# ===========================================================
# SECTION 13 — QUIZ BRAIN CLASS
# ===========================================================

print("\n================ QUIZ BRAIN CLASS ================")


class QuizBrain:

    def __init__(self, question_list):

        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    # Check if quiz still has questions
    def still_has_questions(self):

        return self.question_number < len(self.question_list)

    # Ask next question
    def next_question(self):

        current_question = self.question_list[self.question_number]

        self.question_number += 1

        user_answer = input(
            f"Q.{self.question_number}: "
            f"{current_question.text} (True/False): "
        )

        self.check_answer(user_answer, current_question.answer)

    # Validate answer
    def check_answer(self, user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():

            print("Correct!")
            self.score += 1

        else:
            print("Wrong!")

        print(f"Correct Answer: {correct_answer}")
        print(f"Current Score: {self.score}")
        print("\n")


# ===========================================================
# SECTION 14 — RUNNING QUIZ
# ===========================================================

print("\n================ QUIZ STARTED ================")

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():

    quiz.next_question()

print("Quiz Completed!")
print(f"Final Score: {quiz.score}/{len(question_bank)}")

# ===========================================================
# SECTION 15 — ENCAPSULATION
# ===========================================================

"""
Encapsulation means:
combining DATA + METHODS together.

Example:
QuizBrain class contains:
- score
- question number
- validation logic

inside ONE UNIT.
"""

# ===========================================================
# SECTION 16 — ABSTRACTION
# ===========================================================

"""
User only sees:

quiz.next_question()

Internally:
- question retrieval
- answer validation
- score update

all happen automatically.

Complexity hidden from user.
"""

# ===========================================================
# SECTION 17 — __dict__
# ===========================================================

print("\n================ __dict__ EXAMPLE ================")

print(user_a.__dict__)

"""
OUTPUT:
{
    'username': 'sid',
    'followers': 0,
    'following': 1
}

Internally objects store attributes like dictionary.
"""

# ===========================================================
# SECTION 18 — COMMON BEGINNER MISTAKES
# ===========================================================

"""
MISTAKE 1:
Forgetting self

WRONG:
def follow():

CORRECT:
def follow(self):

---------------------------------

MISTAKE 2:
Calling method without object

WRONG:
InstagramUser.follow()

CORRECT:
user.follow()

---------------------------------

MISTAKE 3:
Confusing class vs object

InstagramUser -> class
user_a -> object
"""

# ===========================================================
# SECTION 19 — MINI EXERCISE 1
# ===========================================================

print("\n================ MINI EXERCISE 1 ================")


class Dog:

    def __init__(self, name, breed):

        self.name = name
        self.breed = breed

    def bark(self):

        print(f"{self.name} says Woof Woof!")


dog_1 = Dog("Bruno", "Labrador")

dog_1.bark()

# ===========================================================
# SECTION 20 — MINI EXERCISE 2
# ===========================================================

print("\n================ MINI EXERCISE 2 ================")


class BankAccount:

    def __init__(self, owner, balance):

        self.owner = owner
        self.balance = balance

    def deposit(self, amount):

        self.balance += amount

    def withdraw(self, amount):

        if amount <= self.balance:

            self.balance -= amount

        else:
            print("Insufficient Balance")


account = BankAccount("Sid", 1000)

account.deposit(500)

account.withdraw(200)

print(account.balance)

# ===========================================================
# SECTION 21 — MINI EXERCISE 3
# ===========================================================

print("\n================ MINI EXERCISE 3 ================")


class StudentMarks:

    def __init__(self, name):

        self.name = name
        self.marks = []

    def add_marks(self, mark):

        self.marks.append(mark)

    def average(self):

        return sum(self.marks) / len(self.marks)


student = StudentMarks("Siddharth")

student.add_marks(90)
student.add_marks(80)
student.add_marks(95)

print(student.average())

# ===========================================================
# SECTION 22 — WHY THIS DAY MATTERS FOR AI ENGINEERING
# ===========================================================

"""
Every major AI framework uses OOP heavily.

Examples:

LangChain:
    LLM classes
    Chain classes
    Agent classes

FastAPI:
    Request objects
    Response objects

Pydantic:
    Model classes

CrewAI:
    Agent objects

LangGraph:
    State objects

Without understanding OOP:
you cannot understand professional AI codebases.
"""

# ===========================================================
# FINAL SUMMARY
# ===========================================================

"""
TODAY YOU LEARNED:

1. What OOP is
2. Classes and Objects
3. Constructors (__init__)
4. self keyword
5. Attributes and Methods
6. Encapsulation
7. Abstraction
8. State Management
9. Quiz Project Architecture
10. Real software engineering structure

MOST IMPORTANT TAKEAWAY:
------------------------

You are no longer writing beginner scripts.

You are now learning PROFESSIONAL SOFTWARE DESIGN.

This is one of the most important days in your
AI Engineer roadmap.

END OF DAY 17
"""