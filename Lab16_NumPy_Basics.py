# ============================================
# Lab 16: NumPy Basics
# ============================================
# Agenda (~50 min):
#   1. What NumPy is and why it's important   (~8 min)
#   2. Creating and working with arrays        (~10 min)
#   3. Array indexing and slicing              (~10 min)
#   4. Mathematical operations on arrays       (~12 min)
#   5. Common NumPy functions                  (~10 min)
#
# Install first if needed:  pip install numpy

import numpy as np

# ---- A list vs an array: same data, different power ----
prices_list = [100, 102, 105, 103]        # plain Python list
prices_arr  = np.array([100, 102, 105, 103])

# print(type(prices_list))                  # <class 'list'>
# print(type(prices_arr))                   # <class 'numpy.ndarray'>

# # # With a list, math needs a loop:
# doubled_list = [p * 2 for p in prices_list]
# # # With an array, math is direct (vectorized):
# doubled_arr = prices_arr * 2

# print(doubled_list)                       # [200, 204, 210, 206]
# print(doubled_arr)                        # [200 204 210 206]


# ---- WHY it matters: speed (vectorization runs in C, not Python) ----
# import time

# n = 10_000_000
# py_list = list(range(n))
# np_arr = np.arange(n)

# start = time.time()
# py_sum = sum(x * 2 for x in py_list)      # Python loop, one item at a time
# print("Python list:", round(time.time() - start, 3), "sec")

# start = time.time()
# np_sum = (np_arr * 2).sum()               # whole array at once, in C
# print("NumPy array:", round(time.time() - start, 3), "sec")
# # # Typically 10-100x faster. Also uses far less memory (fixed types).


# ============================================
# 2. CREATING AND WORKING WITH ARRAYS
# ============================================

# ---- Creating arrays from Python lists ----
# a = np.array([1, 2, 3, 4, 5])             # 1D array
# b = np.array([[1, 2, 3],
#               [4, 5, 6]])                 # 2D array (matrix: 2 rows, 3 cols)

# print(a)
# print(b)


# ---- Key attributes: every array knows its own shape and type ----
# b = np.array([1,2,3])
# # b = np.array([[1, 2, 3],
# #               [4, 5, 6]])
# print(b.shape)                            # (2, 3) -> 2 rows, 3 columns
# print(b.ndim)                             # 2      -> number of dimensions
# print(b.size)                             # 6      -> total elements
# print(b.dtype)                            # int64/int32 -> ONE type for all
#                                           # (lists can mix types; arrays can't
                                          #  -> that's why they're fast)


# ---- Builder functions: create arrays without typing data ----
# print(np.zeros(5))                        # [0. 0. 0. 0. 0.]
# print(np.ones((2, 3)))                    # 2x3 matrix of 1s
# print(np.full((2, 2), 7))                 # 2x2 matrix filled with 7
# print(np.arange(0, 10, 2))                # [0 2 4 6 8]  like range()
# print(np.linspace(0, 1, 5))               # [0. 0.25 0.5 0.75 1.]
#                                           # 5 evenly spaced points 0..1


# ---- Random arrays (very common in ML: weights, sampling) ----
# rng = np.random.default_rng()               
# print(rng.random(30))                      # 3 floats in [0, 1)
# print(rng.integers(1, 100, size=5))       # 5 random ints between 1 and 99
# print(rng.normal(0, 1, size=4))           # 4 samples from normal dist


# ---- Reshaping: same data, new shape ----
# nums = np.arange(12)                      # [0 1 2 ... 11]
# # print(nums)
# grid = nums.reshape(2, 6)                 # bend it into 3 rows x 4 cols
# print(grid)
# print(grid.flatten())                     # back to 1D


# ============================================
# 3. ARRAY INDEXING AND SLICING
# ============================================
# Works like list slicing (Lab 10) — plus 2D and boolean superpowers.

# ---- 1D: same as lists ----
# arr = np.array([10, 20, 30, 40, 50])
# print(arr[0])                             # 10   first
# print(arr[-1])                            # 50   last
# print(arr[1:4])                           # [20 30 40]
# print(arr[::2])                           # [10 30 50] every 2nd
# print(arr[::-1])                          # [50 40 30 20 10] reversed


# ---- 2D: [row, column] — one bracket, comma-separated ----
# m = np.array([[1,  2,  3,  4],
#               [5,  6,  7,  8],
#               [9, 10, 11, 12]])
# print(m[0, 0])                            # 1    top-left
# print(m[1, 2])                            # 7    row 1, col 2
# print(m[0])                               # [1 2 3 4]   whole first row
# print(m[:, 1])                            # [2 6 10]    whole 2nd column!
# print(m[0:2, 1:3])                        # [[2 3] [6 7]] sub-matrix


# ---- Boolean indexing: filter with a condition (THE killer feature) ----
# scores = np.array([45, 82, 91, 30, 67, 78])
# mask = scores >= 60                       # compares EVERY element
# print(mask)                               # [False True True False True True]
# # print(scores[mask])                       # [82 91 67 78] only passing scores
# # print(scores[scores >= 60])               # same thing, one line
# print(scores[(scores >= 60) & (scores < 90)])   # AND -> use & (not 'and')


# ---- Fancy indexing: pick elements by a list of positions ----
# arr = np.array([10, 20, 30, 40, 50])
# print(arr[[0, 2, 4]])                     # [10 30 50]


# ---- Careful: slices are VIEWS, not copies ----
# arr = np.array([100, 200, 300, 400, 500])
# slice = arr[1:4]
# # print(part) 
# print(slice[0])                             # view into the same data
# slice[0] = 999
# print(slice[0])
# print(arr)                                # [100 999 300 400 500]  original changed!
# # safe = arr[1:4].copy()                    # use .copy() when you need one


# ============================================
# 4. MATHEMATICAL OPERATIONS ON ARRAYS
# ============================================

# ---- Element-wise math: no loops needed ----
# a = np.array([1, 2, 3, 4])
# b = np.array([10, 20, 30, 40])
# print(a + b)                              # [11 22 33 44]
# print(b - a)                              # [ 9 18 27 36]
# print(a * b)                              # [10 40 90 160]  element-wise!
# print(b / a)                              # [10. 10. 10. 10.]
# print(a ** 2)                             # [1 4 9 16]


# ---- Array with a single number (broadcasting) ----
# prices = np.array([100, 250, 80, 120])
# with_tax = prices * 1.18                  # 18% tax on every price at once
# print(with_tax)
# print(prices + 10)                        # add 10 to all
# print(prices > 100)                       # compare all -> boolean array



# ---- Aggregations: reduce an array to summary numbers ----
# sales = np.array([250, 300, 180, 420, 390])
# print(sales.sum())                        # 1540
# print(sales.mean())                       # 308.0
# print(sales.min(), sales.max())           # 180 420
# print(sales.std())                        # standard deviation


# ---- Matrix multiplication (the heart of neural networks) ----
# A = np.array([[1, 2],
#               [3, 4]])
# B = np.array([[5, 6],
#               [7, 8]])
# print(A * B)                              # element-wise (NOT matrix mult)
# print(A @ B)                              # true matrix multiplication
#                                           # [[19 22]
#                                           #  [43 50]]


# ============================================
# 5. COMMON NUMPY FUNCTIONS
# ============================================

# ---- Universal functions (ufuncs): math on every element ----
# x = np.array([1, 4, 9, 16])
# print(np.sqrt(x))                         # [1. 2. 3. 4.]
# print(np.exp(np.array([0, 1])))           # [1. 2.718...]
# print(np.log(np.array([1, np.e])))        # [0. 1.]
# print(np.abs(np.array([-3, 5, -7])))      # [3 5 7]
# print(np.round(np.array([3.14159, 2.71828]), 2))   # [3.14 2.72]


# ---- unique: distinct values and their counts ----
# votes = np.array(["yes", "no", "yes", "yes", "no"])
# values, counts = np.unique(votes, return_counts=True)
# print(values)                             # ['no' 'yes']
# print(counts)                             # [2 3]


# ---- Stacking arrays together ----
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
# print(np.concatenate([a, b]))             # [1 2 3 4 5 6]
print(np.vstack([a, b]))                  # stack as rows -> 2x3
# print(np.hstack([a, b]))                  # side by side -> [1 2 3 4 5 6]

