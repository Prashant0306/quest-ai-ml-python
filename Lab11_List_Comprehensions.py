# ============================================
# Lab 2: List Comprehensions
# ============================================
# A short way to build a list from another iterable.
#
#   [ expression  for item in iterable  if condition ]
#         |              |                    |
#       what to keep   loop               optional filter
#
# Think of it like C# LINQ:  numbers.Where(n => n > 3).Select(n => n * n)

numbers = [1, 2, 3, 4, 5, 6]

# ---- The long way (plain loop) ----
# squares_loop = []
# for n in numbers:
#     squares_loop.append(n * n)
# print("loop   :", squares_loop)

# # ---- The comprehension way (same result, one line) ----
# suqares = numbers.select(n=>n*n);
# squares = [n * n for n in numbers]
# print("comp   :", squares)


# # ---- With a filter (if) ----
# suqares = numbers.where(n=>n > 3).select(n=>n*n);

a = 1
b = 2

# max = a > b ? a : b
# max = a if a > b else b

# big = [n * n for n in numbers if n > 3]            # keep only n > 3
# print("filter :", big)                          # [4, 5, 6]

# even_squares = [n * n for n in numbers if n % 2 == 0]
# print("even^2 :", even_squares)                 # [4, 16, 36]


# # ---- Transform any iterable, not just numbers ----
words = ["hello", "world", "python"]
# upper = [w.upper() for w in words]
# lengths = [len(w) for w in words]
# print("upper  :", upper)
# print("lengths:", lengths)


# # ---- if/else INSIDE the expression (note: goes before 'for') ----
# labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
# print("labels :", labels)


# # ---- Nested loops in a comprehension ----
# pairs = [(x, y) for x in [1, 2] for y in ["a", "b"]]
# print("pairs  :", pairs)   # [(1,'a'), (1,'b'), (2,'a'), (2,'b')]


# people = ["sagar","amit","rahul"]
# attributes = ["name","email"]

# # for p in people:
# #     for a in attributes:
# #         print(p,a)

# result = [ (p,a) for a in attributes for p in people]

# print(result)


# # Flatten a 2D list:
# matrix = [[1, 2, 3], [4, 5, 6]]
# # flat = []
# # for row in matrix:
# #     for value in row:
# #         flat.append(value)

# # print(flat)
# flat = [value for row in matrix for value in row]
# print("flat   :", flat)    # [1, 2, 3, 4, 5, 6]


# # ---- Set and dict comprehensions use the same idea ----
# numbers = [1,2,2,2,3,5,4,4,5]
# clone = [n for n in numbers]
# set = {n for n in numbers}
# print(clone)
# print(set)
# unique_lengths = {len(w) for w in words}     # set comprehension
# print("set    :", unique_lengths)


# ---- TRY THIS (uncomment to explore) ----
# Build a list from a string:
vowels = [ch for ch in "sagar" if ch in "aeiou"]
print(vowels)
#
# Careful: comprehensions are great for SIMPLE transforms. If logic gets
# complex, a normal loop is more readable.
