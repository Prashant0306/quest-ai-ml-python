# ============================================
# Lab 5: Conditionals (if / elif / else)   (NEW)
# ============================================
# Goal: make decisions in code.

# age = 20

# # ---- Basic if / elif / else ----
# if age < 13:
#     print("child")
# elif age < 18:
#     print("teenager")
# else:
#     print("adult")


# # ---- Comparison operators ----
# # ==  !=  <  >  <=  >=
# print(5 == 5, 5 != 4, 5 > 3, 5 <= 5)


# # ---- Logical operators: and / or / not ----
# has_ticket = True
# has_id = False
# if has_ticket and has_id:
#     print("Allowed in")
# elif has_ticket and not has_id:  # (has_ticket && !has_id)
#     print("Need an ID")
# else:
    # print("Denied")


# value = "None"

# if value:
#     print("true")
# else:
#     print("false")


# # ---- "Truthiness": empty things are False ----
# # Falsy: 0, 0.0, "", [], {}, (), None, False
# name = ""
# if name:
#     print(f"Hello {name}")
# else:
#     print("Name is empty")     # this runs

# items = [1, 2, 3]
# if items:                      # non-empty list is truthy
#     print(f"{len(items)} items in the cart")


# # ---- Ternary (one-line if/else) ----


# score = 72

# # result = score >= 50? "pass" : "fail"
# result = "pass" if score >= 50 else "fail"
# print(result)


# # ---- Chained comparisons (very Pythonic) ----
# temperature = 25
# #if (temperature >=18 && temperature <= 30)
# if 18 <= temperature <= 30:     # same as: 18 <= temp AND temp <= 30
#     print("Comfortable")


# # ---- 'in' membership test ----
# fruit = "apple"
# if fruit in ["apple", "banana", "mango"]:
#     print("We have it")


# # ---- match / case (Python 3.10+, like switch) ----
# command = "start"
# match command:
#     case "start":
#         print("Starting...")
#     case "stop":
#         print("Stopping...")
#     case _:                    # _ = default / anything else
#         print("Unknown command")


# ---- TRY THIS (uncomment to explore) ----
# Guard against bad input:
while True:
    user = input("Enter age: ")
    if user.isdigit():
        print("Valid:", int(user))
    else:
        print("Please enter a number")
