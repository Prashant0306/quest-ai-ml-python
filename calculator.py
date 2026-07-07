# ============================================
# calculator.py  ->  a MODULE
# ============================================
# A "module" is simply a .py file. Anything defined here (functions,
# classes, variables) can be imported and reused from other files.
#
# Import it elsewhere with:
#   import calculator
#   from calculator import add, Calculator

PI = 3.14159        # module-level constant


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


class Calculator:
    """A small stateful calculator that remembers a running value."""

    def __init__(self, start=0):
        self.value = start

    def add(self, n):
        self.value += n
        return self          # return self -> allows method chaining

    def subtract(self, n):
        self.value -= n
        return self


# # ---- The __name__ == "__main__" guard ----
# # Code under this guard runs ONLY when you execute this file directly
# # (python calculator.py), NOT when another file imports it.
# if __name__ == "__main__":
#     print("Running calculator.py directly")
#     print("add(2, 3) =", add(2, 3))
#     print("chained  =", Calculator(10).add(5).subtract(2).value)   # 13
