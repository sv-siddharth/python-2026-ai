"""
=========================================================
DAY 18 - CONSTRUCTORS (__init__) & METHODS
Angela Yu Inspired Python Notes
For AI Engineer Roadmap
=========================================================

Topics Covered:
1. Classes and Objects
2. Constructors (__init__)
3. self keyword
4. Instance variables
5. Methods
6. Object state modification
7. Real-world OOP examples
8. AI Engineer style examples

=========================================================
WHY THIS DAY MATTERS
=========================================================

As an AI Engineer, almost every framework uses OOP:

- OpenAI SDK
- LangChain
- FastAPI
- CrewAI
- LangGraph

You will constantly create:
- clients
- services
- pipelines
- agents
- tools

This day is the foundation of all of that.

=========================================================
SECTION 1 - WHAT IS A CLASS?
=========================================================

A class is a blueprint/template.

Example:
Blueprint -> House
Class -> Object

You can create multiple objects from one class.
"""


# --------------------------------------------
# BASIC CLASS
# --------------------------------------------

class Student:
    pass


# Creating objects
student1 = Student()
student2 = Student()

print(student1)
print(student2)


"""
=========================================================
SECTION 2 - CONSTRUCTOR (__init__)
=========================================================

The constructor runs automatically
when object is created.

Syntax:

def __init__(self):
    ...

self refers to the current object.
"""


class User:

    def __init__(self):
        print("User object created!")


# Constructor automatically runs
user1 = User()


"""
=========================================================
SECTION 3 - INSTANCE VARIABLES
=========================================================

Instance variables belong to objects.

Example:
self.name
self.age

Each object stores separate values.
"""


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Siddharth", 28)
person2 = Person("Rahul", 25)

print(person1.name)
print(person1.age)

print(person2.name)
print(person2.age)


"""
=========================================================
SECTION 4 - UNDERSTANDING self
=========================================================

When you do:

person1 = Person("Siddharth", 28)

Python internally does:

Person.__init__(person1, "Siddharth", 28)

So:
self = person1

self refers to the CURRENT object.
"""


class Animal:

    def __init__(self, species):
        self.species = species

    def show_species(self):
        print(f"Species: {self.species}")


dog = Animal("Dog")
cat = Animal("Cat")

dog.show_species()
cat.show_species()


"""
=========================================================
SECTION 5 - METHODS
=========================================================

Methods are functions inside classes.

They define object behavior.
"""


class Car:

    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"{self.brand} is driving!")

    def stop(self):
        print(f"{self.brand} stopped.")


car1 = Car("BMW")

car1.drive()
car1.stop()


"""
=========================================================
SECTION 6 - MODIFYING OBJECT STATE
=========================================================

Methods can change object variables.
"""


class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print(f"Current Balance: {self.balance}")


account = BankAccount(1000)

account.show_balance()

account.deposit(500)
account.show_balance()

account.withdraw(200)
account.show_balance()


"""
=========================================================
SECTION 7 - MULTIPLE OBJECTS
=========================================================

Each object has its own separate data.
"""


class Laptop:

    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def show_specs(self):
        print(f"Brand: {self.brand}")
        print(f"RAM: {self.ram} GB")


laptop1 = Laptop("Dell", 16)
laptop2 = Laptop("Apple", 32)

laptop1.show_specs()
print()

laptop2.show_specs()


"""
=========================================================
SECTION 8 - COMMON BEGINNER MISTAKES
=========================================================
"""


# --------------------------------------------
# MISTAKE 1 - Forgetting self
# --------------------------------------------

"""
WRONG:

def greet():
    pass

CORRECT:

def greet(self):
    pass
"""


# --------------------------------------------
# MISTAKE 2 - Missing self.variable
# --------------------------------------------

"""
WRONG:

name = name

CORRECT:

self.name = name
"""


# --------------------------------------------
# MISTAKE 3 - Accessing variables before creation
# --------------------------------------------

"""
WRONG:

class User:
    def greet(self):
        print(self.name)

'name' doesn't exist yet.
"""


"""
=========================================================
SECTION 9 - PYTHON VS JAVASCRIPT
=========================================================

JavaScript:

class User {
    constructor(name) {
        this.name = name;
    }
}

Python:

class User:

    def __init__(self, name):
        self.name = name

this -> self
constructor -> __init__
"""


"""
=========================================================
SECTION 10 - AI ENGINEER STYLE EXAMPLE
=========================================================

This resembles future OpenAI wrappers.
"""


class AIChatBot:

    def __init__(self, model):
        self.model = model

    def generate_response(self, prompt):
        print(f"Using Model: {self.model}")
        print(f"Prompt: {prompt}")
        print("Generated Response: AI response here")


bot = AIChatBot("gpt-4")

bot.generate_response("Explain RAG")


"""
=========================================================
SECTION 11 - EMPLOYEE MANAGEMENT PROJECT
=========================================================
"""


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: {self.salary}")


emp1 = Employee("Siddharth", 50000)

emp1.display()

print("\nGiving raise...\n")

emp1.give_raise(10000)

emp1.display()


"""
=========================================================
SECTION 12 - AI MODEL TRACKER PROJECT
=========================================================

Very relevant to future AI engineering.
"""


class AIModel:

    def __init__(self, model_name, provider):
        self.model_name = model_name
        self.provider = provider

    def show_info(self):
        print(f"Model Name: {self.model_name}")
        print(f"Provider: {self.provider}")


model1 = AIModel("gpt-4", "OpenAI")
model2 = AIModel("claude-sonnet", "Anthropic")

model1.show_info()
print()

model2.show_info()


"""
=========================================================
SECTION 13 - ADVANCED AI CONFIGURATION PROJECT
=========================================================

DAY 18 CHALLENGE PROJECT
"""


class AIModelConfig:

    def __init__(self, model_name, provider, temperature):
        self.model_name = model_name
        self.provider = provider
        self.temperature = temperature

    def show_config(self):
        print("\n===== MODEL CONFIG =====")
        print(f"Model: {self.model_name}")
        print(f"Provider: {self.provider}")
        print(f"Temperature: {self.temperature}")

    def update_temperature(self, new_temperature):
        self.temperature = new_temperature
        print("\nTemperature updated successfully!")


model = AIModelConfig(
    "gpt-4",
    "OpenAI",
    0.7
)

model.show_config()

model.update_temperature(0.9)

model.show_config()


"""
=========================================================
SECTION 14 - IMPORTANT OOP TERMINOLOGY
=========================================================

Class
-> Blueprint/template

Object
-> Instance of class

Constructor
-> Special method that runs automatically

Method
-> Function inside class

Attribute
-> Variable inside object

Instance Variable
-> Variable unique to each object

self
-> Current object reference

=========================================================
SECTION 15 - FINAL MENTAL MODEL
=========================================================

Class = Blueprint
Object = Real Thing
__init__ = Setup Object
self = Current Object
Methods = Behaviors
Attributes = Data

=========================================================
PRACTICE EXERCISES
=========================================================

1. Create a Movie class
2. Create a Phone class
3. Create a Book class
4. Create an LLMClient class
5. Create a RAGPipeline class

=========================================================
END OF DAY 18
=========================================================
"""