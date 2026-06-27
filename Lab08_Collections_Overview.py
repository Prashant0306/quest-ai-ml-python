# ============================================
# Lab 8: Built-in Collections Overview
# ============================================
# Goal: meet the 4 core containers. (Session 2 dives deeper into each.)
#
#   list  -> ordered, changeable, allows duplicates      [ ]
#   tuple -> ordered, FIXED (immutable)                  ( )
#   set   -> unordered, no duplicates                    { }
#   dict  -> key -> value pairs                          {k: v}

# ---- LIST: an ordered, mutable sequence ----
# fruits: list[str] = ["apple", "banana", "mango"]
# fruits.append("orange")        # add to the end
# fruits[0] = "avocado"          # change by index
# print("list:", fruits, "| length:", len(fruits))
# print("first:", fruits[0], "| last:", fruits[-1])
# print(fruits[1:2])

# # ---- TUPLE: like a list but cannot be changed ----
# point = (10, 20)               # good for fixed groups of data
# x, y = point                   # unpack into variables
# print("tuple:", point, "| x:", x, "| y:", y)
# # point[0] = 99                # would raise TypeError (immutable)


# # ---- SET: unique items, no order ----
# numbers = {1, 2, 2, 3, 3, 3}   # duplicates are dropped automatically
# numbers.add(4)
# print("set:", numbers)         # {1, 2, 3, 4}
# print("is 2 in set?", 20 in numbers)


# # ---- DICT: key/value lookup table ----
# person = {"name": "Alice", "age": 30}
# print("dict:", person)
# print("name:", person["name"])         # access by key
# person["city"] = "Pune"                # add a new key
# person["age"] = 31                     # update a value
# print("keys:", list(person.keys()))
# print("values:", list(person.values()))


# ---- Choosing the right one ----
# Need order + changes?            -> list
# Need fixed, unchangeable data?   -> tuple
# Need uniqueness / fast 'in'?     -> set
# Need to look things up by name?  -> dict


# ---- Quick conversions ----
# print(list((1, 2, 3)))         # tuple -> list
# print(set([1, 1, 2, 3]))       # list  -> set (removes dups)
# print(tuple([1, 2, 3]))        # list  -> tuple
# print(set((1, 2, 3,6,7,7,1,8)))        # tuple  -> set


# ---- TRY THIS (uncomment to explore) ----
# nums = [5, 3, 8, 1]
# nums.sort()
# print(nums)                  # [1, 3, 5, 8]
# print(sorted(nums, reverse=True))
# print(sum(nums), max(nums), min(nums))
