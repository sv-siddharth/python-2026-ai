"""
===========================================================
DAY 16 - OBJECT ORIENTED PROGRAMMING (OOP) BASICS
Angela Yu Python Bootcamp Notes
===========================================================

WHY THIS DAY IS IMPORTANT
-------------------------

OOP (Object Oriented Programming) is one of the MOST important
concepts in software engineering.

Without OOP:
- Large applications become messy
- Code becomes difficult to scale
- AI systems become impossible to manage cleanly

Almost every AI framework uses OOP heavily:
- LangChain
- FastAPI
- CrewAI
- LangGraph
- OpenAI SDKs

Today you will learn:
1. Classes
2. Objects
3. Constructors (__init__)
4. Attributes
5. Methods
6. self keyword
7. Real-world modeling

===========================================================
"""

# =========================================================
# 1. BASIC CLASS
# =========================================================

"""
A class is a blueprint/template.

Example:
Car blueprint -> creates multiple cars
Dog blueprint -> creates multiple dogs

Syntax:
class ClassName:
    pass

'pass' means:
"Do nothing for now"
"""

class Dog:
    pass


# Creating objects from class
dog1 = Dog()
dog2 = Dog()

print(type(dog1))
print(type(dog2))


# =========================================================
# 2. CONSTRUCTOR (__init__)
# =========================================================

"""
__init__ is a constructor.

It runs automatically whenever an object is created.

Example:
dog = Dog()

As soon as this line runs:
__init__ executes automatically
"""

class Animal:

    def __init__(self):
        print("Animal object created!")


animal1 = Animal()


# =========================================================
# 3. ATTRIBUTES (VARIABLES INSIDE OBJECTS)
# =========================================================

"""
Attributes = variables belonging to object

self.attribute_name

Example:
self.name
self.age
"""

class Person:

    def __init__(self):
        self.name = "Siddharth"
        self.age = 28


person1 = Person()

print(person1.name)
print(person1.age)


# =========================================================
# 4. PASSING VALUES TO OBJECTS
# =========================================================

"""
Instead of fixed values,
we can pass dynamic values.
"""

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


student1 = Student("Rahul", 90)
student2 = Student("Aman", 85)

print(student1.name)
print(student1.marks)

print(student2.name)
print(student2.marks)


# =========================================================
# 5. UNDERSTANDING self
# =========================================================

"""
VERY IMPORTANT CONCEPT

self = current object

Example:

student1.name
student2.name

Each object has its own separate data.

Without self:
Python won't know WHICH object you are referring to.
"""

class Car:

    def __init__(self, brand):
        self.brand = brand


car1 = Car("BMW")
car2 = Car("Audi")

print(car1.brand)
print(car2.brand)


# =========================================================
# 6. METHODS (FUNCTIONS INSIDE CLASS)
# =========================================================

"""
Methods = functions inside classes

Syntax:

class MyClass:

    def my_method(self):
        pass
"""

class Employee:

    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"{self.name} is working")


employee1 = Employee("Sid")

employee1.work()


# =========================================================
# 7. MULTIPLE METHODS
# =========================================================

class MobilePhone:

    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery

    def charge(self):
        self.battery = 100
        print(f"{self.brand} charged to 100%")

    def use_phone(self):
        self.battery -= 10
        print(f"Battery remaining: {self.battery}%")


phone1 = MobilePhone("iPhone", 80)

phone1.use_phone()
phone1.use_phone()
phone1.charge()


# =========================================================
# 8. DEFAULT VALUES
# =========================================================

"""
You can set default values.
"""

class InstagramUser:

    def __init__(self, username):
        self.username = username
        self.followers = 0
        self.following = 0


user1 = InstagramUser("sid")

print(user1.username)
print(user1.followers)
print(user1.following)


# =========================================================
# 9. OBJECTS INTERACTING WITH OBJECTS
# =========================================================

class User:

    def __init__(self, username):
        self.username = username
        self.followers = 0

    def follow(self, other_user):
        other_user.followers += 1
        print(f"{self.username} followed {other_user.username}")


user1 = User("sid")
user2 = User("rahul")

user1.follow(user2)

print(user2.followers)


# =========================================================
# 10. REAL-WORLD MINI PROJECT
# COFFEE MACHINE
# =========================================================

"""
This is your first REAL OOP project.

We are modeling a coffee machine like a real object.

The coffee machine has:
- attributes (water, milk, coffee)
- methods (make coffee, refill, check resources)
"""

class CoffeeMachine:

    def __init__(self):

        # Initial resources
        self.water = 1000
        self.milk = 500
        self.coffee = 300

    def check_resources(self, water_needed, milk_needed, coffee_needed):

        """
        Checks if enough resources are available.
        """

        if self.water < water_needed:
            print("❌ Not enough water")
            return False

        if self.milk < milk_needed:
            print("❌ Not enough milk")
            return False

        if self.coffee < coffee_needed:
            print("❌ Not enough coffee")
            return False

        return True

    def make_coffee(self):

        """
        Makes coffee if resources exist.
        """

        if self.check_resources(200, 100, 50):

            self.water -= 200
            self.milk -= 100
            self.coffee -= 50

            print("☕ Coffee is ready!")

    def refill(self):

        """
        Refills resources.
        """

        self.water += 500
        self.milk += 300
        self.coffee += 200

        print("✅ Machine refilled")

    def show_resources(self):

        """
        Displays current resources.
        """

        print("\nCurrent Resources:")
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee: {self.coffee}g\n")


# Creating coffee machine object
machine = CoffeeMachine()

machine.show_resources()

machine.make_coffee()
machine.make_coffee()

machine.show_resources()

machine.refill()

machine.show_resources()


# =========================================================
# 11. COMMON BEGINNER MISTAKES
# =========================================================

"""
❌ MISTAKE 1:
Forgetting self

WRONG:
def bark():

CORRECT:
def bark(self):

---------------------------------------------------
❌ MISTAKE 2:
Not using self.variable

WRONG:
name = name

CORRECT:
self.name = name

---------------------------------------------------
❌ MISTAKE 3:
Creating object without required arguments

WRONG:
student = Student()

CORRECT:
student = Student("Sid", 90)
"""

# =========================================================
# 12. JAVASCRIPT VS PYTHON MAPPING
# =========================================================

"""
JavaScript                  Python
------------------------------------------------
class                       class

constructor()               __init__()

this.name                   self.name

method() {}                 def method(self):

new Car()                   Car()

------------------------------------------------

VERY IMPORTANT FOR YOU
since you are transitioning from JS -> Python
"""

# =========================================================
# 13. PRACTICE PROJECT
# BANK ACCOUNT SYSTEM
# =========================================================

"""
YOUR TASK:
Build this yourself first before reading solution.

Features:
- deposit()
- withdraw()
- check_balance()
"""

class BankAccount:

    def __init__(self, owner, balance):

        self.owner = owner
        self.balance = balance

    def deposit(self, amount):

        self.balance += amount

        print(f"₹{amount} deposited successfully")

    def withdraw(self, amount):

        if amount > self.balance:
            print("❌ Insufficient balance")

        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully")

    def check_balance(self):

        print(f"Current Balance: ₹{self.balance}")


# Creating account object
account1 = BankAccount("Sid", 10000)

account1.check_balance()

account1.deposit(5000)

account1.withdraw(3000)

account1.check_balance()


# =========================================================
# 14. WHY OOP MATTERS FOR AI ENGINEERING
# =========================================================

"""
Soon you will use:

class OpenAIClient
class Retriever
class VectorStore
class Agent
class Memory
class PromptTemplate

Everything in AI engineering uses OOP.

This day is the FOUNDATION of:
- LangChain
- FastAPI
- RAG systems
- AI agents
- Production backend systems

Master this properly.
"""

# =========================================================
# 15. FINAL SUMMARY
# =========================================================

"""
TODAY YOU LEARNED:

✅ Classes
✅ Objects
✅ Constructors
✅ __init__
✅ self keyword
✅ Attributes
✅ Methods
✅ Object interaction
✅ Real-world modeling using OOP

MOST IMPORTANT CONCEPT:
Class = Blueprint
Object = Real instance created from blueprint

NEXT:
Day 17 -> Turtle Graphics + GUI + OOP in action
"""

print("\n🎉 DAY 16 COMPLETE 🎉")