# ============================================
# Lab 2: Inheritance & Polymorphism   (NEW)
# ============================================
# Inheritance lets a class reuse and extend another class.

# ---- Base ("parent" / "super") class ----

# def speak():
#         return "..."


class Animal:
    def __init__(self, name):  # constructor
        self.name = name

    def speak(self):
        return "..."  # default; subclasses will override

    def describe(self):
        return f"{self.name} says {self.speak()}"


# # from calculator import Calculator


# # # ---- Derived ("child" / "sub") classes ----
class Dog(Animal):  # Dog inherits from Animal
    def speak(self):  # OVERRIDE the parent method
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


dog = Dog("Rex")
cat = Cat("Whiskers")

# print( dog.speak())

# print(dog.describe())        # Rex says Woof   (describe() is inherited)
# print(cat.describe())        # Whiskers says Meow


# # ---- Polymorphism: same call, different behaviour ----
# # We don't care what TYPE each animal is; they all have speak().
# amimal_list = [Dog("A"), Cat("B"), Animal("Generic")]

# for animal in amimal_list:
#     print(animal.speak())


# # ---- Extending the constructor with super() ----
class Employee:
    # age = 19 #static | non-instance | cannnot accesed via self

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.age = None

    def info(self):
        return f"{self.name} earns {self.salary}"


class Manager(Employee):
    def __init__(self, name: str, salary: float, team_size: int):
        super().__init__(name, salary)  # call the parent constructor
        self.team_size = team_size  # add new attribute

    def info(self):
        base = super().info()  # reuse parent's logic
        return f"{base}, manages {self.team_size} people"


m = Manager("Alice", 90000, 5)
# print(m.info())


# # ---- isinstance / issubclass ----
# print(isinstance(dog, Dog))  # True
# print(isinstance(dog, Animal))  # True  -> a Dog IS an Animal
# print(issubclass(Manager, Employee))  # True


# m = Manager()

# # ---- "Duck typing": if it has the method, it works ----
# # Python doesn't require a shared base class — just the right method.
# class Robot:
#     def speak(self):
#         return "Beep boop"



# a:Animal = Robot()
# print(a.speak())





# ---- TRY THIS (uncomment to explore) ----
# Multiple inheritance:
# class A:
#     def hi(self): return "A"
# class B:
#     def yo(self): return "B"
# class C(A, B): pass
# c = C()

# print(c.hi(), c.yo())
