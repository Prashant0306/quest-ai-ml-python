# ============================================
# Lab 9: Classes & Objects (intro)
# ============================================
# Goal: bundle data + behaviour together. (Session 3 covers inheritance,
# properties, dunder methods, etc.)

# class Person:
#     # __init__ is the constructor: runs when you create an object.
#     # 'self' refers to the specific object being created/used.
#     def __init__(sagar, name, age):
#         sagar.name = name        # instance attribute
#         sagar.age = age

#     # A method is a function that belongs to the class.
#     def greet(this):
#         return f"Hi, I'm {this.name} and I'm {this.age}."

#     def have_birthday(this):
#         this.age += 1           # methods can change the object's state


# # ---- Create objects (no 'new' keyword in Python) ----
# alice = Person("Alice", 30)
# bob = Person("Bob", 25)

# print(alice.greet())
# print(bob.greet())

# # Person.greet()

# alice.have_birthday()
# print("After birthday:", alice.age)   # 31


# ---- Class attribute vs instance attribute ----
# class Dog:
#     species = "Canis familiaris"   # class attribute: shared by ALL dogs

#     def __init__(self, name):
#         self.name = name   
#         self.species = f"test - {name}"
#                 # instance attribute: unique per dog

# rex = Dog("Rex")
# fido = Dog("Fido")
# print(rex.name, "-", rex.species)
# print(fido.name, "-", fido.species)
# print("Shared species:", Dog.species)


# # ---- A slightly bigger example ----
# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient funds")
#             return self.balance
#         self.balance -= amount
#         return self.balance

# acc = BankAccount("Sagar", 100)
# acc.deposit(50)
# acc.withdraw(30)
# print(f"{acc.owner}'s balance: {acc.balance}")   # 120


# ---- TRY THIS (uncomment to explore) ----
# Add a __str__ method so print(obj) shows something readable
# (this is covered in detail in Session 3):
# print(alice)        # default looks like <__main__.Person object at 0x...>
