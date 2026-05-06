"""
===========================================================
DAY 19 — ADVANCED OOP CONCEPTS IN PYTHON
Angela Yu Style Notes + AI Engineering Perspective
===========================================================

This file covers:

1. Class Variables vs Instance Variables
2. Class Methods
3. Static Methods
4. Encapsulation
5. Inheritance
6. Method Overriding
7. Polymorphism
8. Abstraction
9. Composition vs Inheritance
10. Magic / Dunder Methods
11. Property Decorators
12. Real AI Engineering Architecture

Why this matters:
-----------------
Modern AI frameworks heavily use OOP:
- LangChain
- FastAPI
- OpenAI SDKs
- CrewAI
- LangGraph
- Pydantic

Understanding advanced OOP is critical
for becoming a real AI Engineer.

===========================================================
"""


# =========================================================
# 1. INSTANCE VARIABLES VS CLASS VARIABLES
# =========================================================

print("\n==============================")
print("1. INSTANCE VS CLASS VARIABLES")
print("==============================")


class User:
    # CLASS VARIABLE
    # Shared across all objects
    platform = "DevTrack"

    def __init__(self, name):
        # INSTANCE VARIABLE
        # Unique for every object
        self.name = name


u1 = User("Sid")
u2 = User("Rahul")

print(u1.name)
print(u2.name)

print(u1.platform)
print(u2.platform)

"""
OUTPUT:
Sid
Rahul
DevTrack
DevTrack
"""

# =========================================================
# 2. CLASS METHODS
# =========================================================

print("\n==============================")
print("2. CLASS METHODS")
print("==============================")


class Employee:
    total_employees = 0

    def __init__(self, name):
        self.name = name
        Employee.total_employees += 1

    @classmethod
    def show_total_employees(cls):
        print(f"Total Employees: {cls.total_employees}")


e1 = Employee("Sid")
e2 = Employee("Rahul")

Employee.show_total_employees()

"""
@classmethod uses 'cls'
cls refers to the class itself

Useful for:
- counters
- factory methods
- configuration systems
"""


# =========================================================
# 3. STATIC METHODS
# =========================================================

print("\n==============================")
print("3. STATIC METHODS")
print("==============================")


class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b


result = MathUtils.add(10, 20)

print(result)

"""
Static methods:
- belong to class
- don't use self
- don't use cls

Useful for utility/helper functions
"""


# =========================================================
# 4. ENCAPSULATION
# =========================================================

print("\n==============================")
print("4. ENCAPSULATION")
print("==============================")


class BankAccount:

    def __init__(self):
        # PRIVATE VARIABLE
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount()

account.deposit(1000)

print(account.get_balance())

"""
Why encapsulation?
------------------
Protect internal data.

Instead of:
account.balance = 999999

Use:
account.deposit(1000)
"""


# =========================================================
# 5. INHERITANCE
# =========================================================

print("\n==============================")
print("5. INHERITANCE")
print("==============================")


class Animal:

    def speak(self):
        print("Animal speaks")


class Dog(Animal):

    def bark(self):
        print("Dog barks")


dog = Dog()

dog.speak()
dog.bark()

"""
Dog inherits from Animal

Dog gets:
- speak()

Dog also has:
- bark()
"""


# =========================================================
# 6. METHOD OVERRIDING + SUPER()
# =========================================================

print("\n==============================")
print("6. METHOD OVERRIDING")
print("==============================")


class Parent:

    def show(self):
        print("Parent method")


class Child(Parent):

    def show(self):
        print("Child method")


c = Child()

c.show()

"""
Child overrides Parent method
"""


# SUPER() EXAMPLE

print("\nUsing super()")


class Vehicle:

    def __init__(self):
        print("Vehicle Created")


class Car(Vehicle):

    def __init__(self):
        super().__init__()
        print("Car Created")


car = Car()

"""
super() calls parent class methods
"""


# =========================================================
# 7. POLYMORPHISM
# =========================================================

print("\n==============================")
print("7. POLYMORPHISM")
print("==============================")


class Cat:

    def speak(self):
        print("Meow")


class Cow:

    def speak(self):
        print("Moo")


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.speak()

"""
Same method name:
- speak()

Different behavior:
- Bark
- Meow
- Moo

This is polymorphism.
"""


# =========================================================
# 8. ABSTRACTION
# =========================================================

print("\n==============================")
print("8. ABSTRACTION")
print("==============================")

from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class CreditCard(Payment):

    def pay(self):
        print("Payment using credit card")


card = CreditCard()

card.pay()

"""
Abstract classes force child classes
to implement required methods.
"""


# =========================================================
# 9. COMPOSITION VS INHERITANCE
# =========================================================

print("\n==============================")
print("9. COMPOSITION")
print("==============================")


class Engine:

    def start(self):
        print("Engine Started")


class Tesla:

    def __init__(self):
        # Tesla HAS-A engine
        self.engine = Engine()


tesla = Tesla()

tesla.engine.start()

"""
Inheritance:
Dog IS-A Animal

Composition:
Car HAS-A Engine

Modern software prefers composition
because it is more flexible.
"""


# =========================================================
# 10. MAGIC / DUNDER METHODS
# =========================================================

print("\n==============================")
print("10. MAGIC / DUNDER METHODS")
print("==============================")


class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student Name: {self.name}"


s1 = Student("Sid")

print(s1)

"""
__str__ controls object printing
"""


class Team:

    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)


team = Team(["A", "B", "C"])

print(len(team))

"""
__len__ controls len(object)
"""


# =========================================================
# 11. PROPERTY DECORATORS
# =========================================================

print("\n==============================")
print("11. PROPERTY DECORATORS")
print("==============================")


class Person:

    def __init__(self):
        self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):

        if value < 0:
            print("Invalid age")
        else:
            self._age = value


p = Person()

p.age = 25

print(p.age)

p.age = -5

"""
@property creates getter

@age.setter creates setter

Useful for:
- validation
- cleaner APIs
"""


# =========================================================
# 12. REAL AI ENGINEERING EXAMPLE
# =========================================================

print("\n==============================")
print("12. AI ENGINEERING ARCHITECTURE")
print("==============================")


class BaseLLM(ABC):

    @abstractmethod
    def generate(self, prompt):
        pass


class OpenAIClient(BaseLLM):

    def generate(self, prompt):
        return f"GPT Response: {prompt}"


class ClaudeClient(BaseLLM):

    def generate(self, prompt):
        return f"Claude Response: {prompt}"


class ChatApplication:

    def __init__(self, llm):
        # COMPOSITION + DEPENDENCY INJECTION
        self.llm = llm

    def chat(self, prompt):

        response = self.llm.generate(prompt)

        print(response)


# Create OpenAI model
gpt = OpenAIClient()

# Inject model into app
app = ChatApplication(gpt)

app.chat("Explain RAG pipelines")

"""
This architecture demonstrates:

1. Abstraction
2. Inheritance
3. Polymorphism
4. Composition
5. Dependency Injection

This is VERY close to real AI systems.
"""


# =========================================================
# MINI PROJECT — MULTI MODEL CHATBOT
# =========================================================

print("\n==============================")
print("MINI PROJECT")
print("==============================")


class BaseModel(ABC):

    @abstractmethod
    def generate(self, prompt):
        pass


class GPTModel(BaseModel):

    def generate(self, prompt):
        return f"GPT says: {prompt}"


class ClaudeModel(BaseModel):

    def generate(self, prompt):
        return f"Claude says: {prompt}"


class AIChatBot:

    def __init__(self, model):
        self.model = model

    def ask(self, question):

        answer = self.model.generate(question)

        print(answer)


# Using GPT
gpt_model = GPTModel()

chatbot = AIChatBot(gpt_model)

chatbot.ask("What is vector database?")

# Using Claude
claude_model = ClaudeModel()

chatbot2 = AIChatBot(claude_model)

chatbot2.ask("What is LangChain?")

"""
Why this project matters:
-------------------------
This demonstrates professional OOP design.

You can swap:
- GPT
- Claude
- Gemini
- Local Llama

WITHOUT changing application code.

This is how scalable AI systems are built.
"""


# =========================================================
# FINAL TAKEAWAYS
# =========================================================

"""
===========================================================
FINAL TAKEAWAYS
===========================================================

1. OOP is everywhere in AI Engineering

2. Inheritance helps reuse code

3. Composition is preferred in modern systems

4. Abstraction forces standard interfaces

5. Polymorphism creates flexible architectures

6. Dependency Injection makes systems scalable

7. Advanced OOP is critical for:
   - LangChain
   - FastAPI
   - OpenAI SDK
   - CrewAI
   - LangGraph
   - Enterprise backend systems

===========================================================
END OF DAY 19
===========================================================
"""