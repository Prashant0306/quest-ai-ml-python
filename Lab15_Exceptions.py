# ============================================
# Lab 5: Exception Handling (try / except)
# ============================================
# Handle errors gracefully instead of letting the program crash.

# ---- Basic try / except ----
# try:
#     result = 10 / 0
#     print()
#     print()
# except ZeroDivisionError:
#     print("Cannot divide by zero")


# # ---- Catching different errors separately ----
# def safe_divide(text):
#     try:
#         num = int(text)            # might raise ValueError
#         return 10 / num            # might raise ZeroDivisionError
#     except ValueError:
#         return "Not a valid number"
#     except ZeroDivisionError:
#         return "Cannot divide by zero"

# print(safe_divide("5"))            # 2.0
# print(safe_divide("abc"))          # Not a valid number
# print(safe_divide("0"))            # Cannot divide by zero


# # ---- Capturing the error object with 'as' ----
# try:
#     int("hello")
# except ValueError as e:
#     print("Error was:", e)         # see the actual message


# # ---- try / except / else / finally ----
# #   else    -> runs only if NO exception happened
# #   finally -> ALWAYS runs (cleanup), error or not
# def parse(text):
#     try:
#         value = int(text)
#     except ValueError:
#         print("parse failed")
#     else:
#         print("parsed ok:", value)
#     finally:
#         print("done trying")

# parse("42")
# parse("---")
# parse("oops")


# # ---- raise = throw: trigger an exception yourself ----
# def set_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative")
#     if age > 150:
#         raise ValueError("Age is unrealistic")
#     return age

# try:
#     set_age(-5)
# except ValueError as e:
#     print("Rejected:", e)


# # ---- Custom exception classes ----
# # Subclass Exception to create domain-specific errors.
class InsufficientFundsError(Exception):
    pass

class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(f"Need {amount}, have {self.balance}")
        self.balance -= amount
        return self.balance

acc = Account(100)
try:
    acc.withdraw(500)
except InsufficientFundsError as e:
    print("Blocked:", e)
except ValueError as e:
    print(e)


# # ---- Catching multiple types in one line ----
try:
    data = {"a": 1}
    print(data["b"])
except (KeyError, IndexError) as e:
    print("Lookup failed:", repr(e))


# ---- TRY THIS (uncomment to explore) ----
# A bare 'except:' catches EVERYTHING — avoid it; it hides real bugs.
# Prefer catching the specific exception you expect.
