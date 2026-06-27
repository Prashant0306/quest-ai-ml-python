# ============================================
# Lab 7: Functions
# ============================================
# Goal: define reusable blocks of logic.

# ---- Basic function with a docstring ----
# def greet(name:str) :
#     """Return a greeting for the given name."""   # docstring -> help(greet)
#     return f"Hello, {name}!"

# print(greet("World"))


# # ---- Default arguments ----
# def power(base, exponent=2):       # exponent defaults to 2
#     return base ** exponent

# print(power(6))        # 25  (uses default exponent 2)
# print(power(2, 10))    # 1024


# # ---- Keyword arguments (pass by name, any order) ----
# def make_user(name, city, age):
#     return f"{name}, {age}, from {city}"

# print(make_user(age=30, name="Sagar", city="Mumbai"))


# ---- Returning multiple values (packed as a tuple) ----
# def min_max(numbers):
#     return min(numbers), max(numbers)

# low, high = min_max([3, 1, 4, 1, 5, 9])   # unpack the returned tuple
# print("min:", low, "max:", high)


# # ---- Type hints (optional, but great for readability/tools) ----
# def add(a: int, b: int) -> int:
#     return a + b

# print(add(3, 67))

## ---- Functions are objects: pass them around ----
# def shout(text):
#     return text.upper()

# def whisper(text):
#     return text.lower()

# def apply(fn, value):       # 'func' is a function passed in
#     return value(fn)

# print(apply("hello",shout))   # HELLO
# print(apply("HELLO",whisper)) # hello


# ---- Scope: local vs global ----
# counter = 0                   # global

# def increment():
#     global counter             # without this, assignment makes a NEW local
#     counter += 1

# increment()
# increment()
# print("counter:", counter)    # 2


# # # ---- A function with NO return gives back None ----
# def log(msg):
#     print("LOG:", msg)
#     # return "something"

# result = log("saved")
# print("returned:", result)    # None


# # ---- TRY THIS (uncomment to explore) ----
# Nested function (closure) that remembers its outer variable:
# def multiplier(factor):
#     def multiply(x):
#         return x * factor
#     return multiply

# print(multiplier(5)(7)) # x = 7 , 2 = factor

# def dbConnector(type_of_Db,Connection_string):
#     def connect_to_db(type_of_Db,Connection_string):
#         pass
#     def query(query_str):
#         db = connect_to_db()
#         db = query(str)

#     return query

# def addition():
#     #
#     pass

# void something(){
#     // no line of code
# }

# pg_pb = dbConnector("pg",'dhddh')
# pg_pb("select * from")