# # ============================================
# # Lab 6: Loops (for / while)
# # ============================================
# # Goal: repeat work over ranges and collections.

# # ---- for + range(start, stop, step) ----
# # Python equivalent of:  for (int i = 0; i < 10; i += 2)
# for i in range(10,0,-1):
#     print(i, end=" ")
# print()                       # 0 2 4 6 8

# # range(stop) starts at 0:
# for i in range(3):
#     print("tick", i)


# # ---- Looping over a collection directly (no index needed) ----
# fruits = ["apple", "banana", "mango"]
# for fruit in fruits:
#     print("I like", fruit)


# def getValue():
#     a = 10
#     b = 56
#     return a,b


# p,q = getValue()

# print(p,q)


# # ---- enumerate(): index + value together ----
# for index, fruit in enumerate(range(0,10)):
#     print(index, fruit)

# # Start counting from 1:
# for rank, fruit in enumerate(fruits, start=1):
#     print(f"{rank}. {fruit}")


# # ---- zip(): loop over two lists in parallel ----
# names = ["Alice", "Bob","yuu"]
# scores = [90, 85, 89]
# for name, score in zip(names, scores):
#     print(f"{name} scored {score}")


# # ---- while loop: repeat until a condition is False ----
# count = 3
# while count > 0:
#     print("countdown:", count)
#     count -= 1
# print("Lift off!")


# # ---- break and continue ----
# for n in range(1, 11):
#     if n == 7:
#         break                 # stop the loop entirely
#     if n % 2 == 0:
#         continue              # skip to the next iteration
#     print("odd:", n)          # 1 3 5


# # ---- for...else : 'else' runs only if the loop did NOT break ----
# target = 4
# for n in [1, 2, 3]:
#     print("yes")
#     break
#     # if n == target:
#     #     print("found it")
#     #     break
# else:
#     print("target not found")   # runs because we never broke


# # ---- Looping over a dictionary ----
prices = {"pen": 10, "book": 50}
# for key, value in prices.items():
#     print(f"{value}")

my_list = [1,2,3,5,5]

# m_list.select(m=>m)
list_of_price = [value for _, value in prices.items()]

print(list_of_price)
# # ---- TRY THIS (uncomment to explore) ----
# # Infinite loop with a manual break:
# # while True:
# #     text = input("Type 'quit' to stop: ")
# #     if text == "quit":
# #         break
