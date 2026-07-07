# ============================================
# Lab 1: Modules & Packages
# ============================================
# Run this file from inside the Session3 folder:  python Lab01_Modules_And_Packages.py
#
#   module  = a single .py file              (calculator.py)
#   package = a folder of modules + __init__  (utils/)

# ---- 1) Import an entire module ----
# import calculator
# print(calculator.add(4, 5))          # call with module.name
# print("PI from module:", calculator.PI)



# from calculator import add as addition
# result = addition(3,4)
# print(result)



# # ---- 2) Import specific names from a module ----
# from calculator import subtract, Calculator

# print(subtract(10, 3))               # use directly, no prefix
# print(Calculator(0).add(7).add(3).value)   # method chaining -> 10


# # ---- 3) Import with an alias ----
# import calculator as calc
# print(calc.add(1, 1))


# # ---- 4) Import from a PACKAGE ----
# # Thanks to utils/__init__.py these short names are available:
# from utils import add, multiply, format_box, shout, get_todays_price

# print(add(6, 7))                     # from utils/numbers.py
# print(multiply(6, 7))
# print(format_box("Hello"))           # from utils/strings.py
# print(shout("done"))
# print("AAPL price:", get_todays_price("AAPL"))   # from utils/stocks.py


# # # ---- 5) Import a specific module from inside the package ----
# from utils import numbers
# print("via submodule:", numbers.multiply(3, 4))


# # ---- 6) Standard-library modules come for free ----
# import math
# import random
# from datetime import date

# print("sqrt(144):", math.sqrt(144))
# print("today:", date.today())
# # random gives different output each run:
# print("dice:", random.randint(1, 6))


# from calculator import Calculator

# c = Calculator()

# c.add(1,3)


# ---- TRY THIS (uncomment to explore) ----
# See where a module lives and what it contains:
# print(calculator.__file__)
# print(dir(calculator))
