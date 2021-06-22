import functools


def memoize(function):
    function._cache = {}
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in function._cache:
            function._cache[key] = function(*args, **kwargs)
        return function._cache[key]
    return wrapper


# Different example from https://book.pythontips.com/en/latest/function_caching.html by the lru_cache decorator
# from functools import lru_cache
#
# @lru_cache(maxsize=32)
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)
#
# >>> print([fib(n) for n in range(10)])
# # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]