# ============================================
# Lab 1: List Indexing & Slicing
# ============================================
# Syntax:  list[start : stop : step]   (stop is EXCLUSIVE)

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#          0   1   2   3   4   5   6   7   8   9     <- positive index
#         -10 -9  -8  -7  -6  -5  -4  -3  -2  -1     <- negative index

# ---- Indexing ----
# print("first:", numbers[0])       # 10
# print("first:", numbers[-10])       # 10
# print("last :", numbers[-11])      # 100 (negative counts from the end)
# print("2nd last:", numbers[-2])   # 90


# ---- Basic slicing [start:stop] ----
# print("first three :", numbers[0:3])   # [10, 20, 30]  (indexes 0,1,2)
# print("from index 7:", numbers[:-9])    # [80, 90, 100]
# print("up to index 3:", numbers[:3])   # [10, 20, 30]
# print("middle      :", numbers[3:6])   # [40, 50, 60]


# # ---- Step [start:stop:step] ----
# print("every 2nd   :", numbers[::3])   # [10, 30, 50, 70, 90]
# print("reversed    :", numbers[::-1])  # [100, 90, ... 10]
# print("every 3rd   :", numbers[1::3])  # [20, 50, 80]


# # ---- Negative slicing ----
# print("last three  :", numbers[-3:])   # [80, 90, 100]
# print("drop last   :", numbers[:-1])   # everything except the last


# # ---- Slices create a COPY (original is untouched) ----
# chunk = numbers[2:5]
# print("chunk:", chunk)
# chunk[0] = 999
# print("chunk:", chunk)
# print("original unchanged:", numbers)


# # ---- Slice assignment: replace a section in place ----
# letters = ["a", "b", "c", "d", "e"]
# letters[1] = ["X", "Y", "Z"]    # replace b with [X,Y,Z]
# print("after slice assign:", letters)   # ['a',['X','Y','Z'],'c','d','e']

# letters[1:2] = ["X", "Y", "Z"]    # replace b,c with X,Y,Z
# print("after slice assign:", letters)   # ['a','X','Y','Z','d','e']


# # ---- Common list operations ----
# nums = [3, 1, 4, 1, 5]
# nums.append(9)            # add to end
# print(nums)
# nums.insert(0, 0)         # insert at index 0
# print(nums)
# nums.remove(1)            # remove first occurrence of value 1
# print(nums)
# popped = nums.pop()       # remove & return the last item
# print(nums)
# print("nums:", nums, "| popped:", popped)
# print("count of 1:", [3, 1, 4, 1, 5].count(1))
# print("index of 4:", [3, 1, 4, 1, 5].index(4))


# ---- TRY THIS (uncomment to explore) ----
# print(numbers[1:-1])      # drop first and last
# print(numbers[::-2])      # reversed, every other one
# matrix = [[1, 2], [3, 4]]
# print(matrix[1][0])       # 3  (row 1, col 0)
