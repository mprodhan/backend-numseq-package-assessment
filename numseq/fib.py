from functools import lru_cache

def fib(n):
    """Returns the nth fibonnaci number"""
    fib_cache = {}
    result = 0
    if n == 1:
        result = 1
    elif n == 2:
        result = 1
    elif n > 2:
        result = fib(n-1) + fib(n-2)
    fib_cache[n] = result
    return result