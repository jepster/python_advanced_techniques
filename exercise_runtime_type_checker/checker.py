# define check_types
#     if the severity is zero, return a no-op decorator
#     define a generic messaging function that prints a message if the severity is 1 and raises a TypeError if the severity is 2
#     define checker, which will itself be a decorator!
#         look at the function's `__annotations__` - if there aren't any, forward the function through!
#             make sure that each of the function's annotations is a type (e.g. int) and not some other value (e.g. 5)
#         define a wrapper function, itself decorated with `functools.wraps`, which takes in *args and **kwargs
#             bind the arguments *args and **kwargs to the original function, to see what _would_ go into the function
#             check that each of the arguments match the expected type in the annotations dictionary, if its present
#                 if any fail, send a message that there was a violation
#             compute the function's actual return value on the supplied arguments
#             check that the return value matches the expected type of the return value in the annotations dictionary, if present
#                 if it fails, send a message that there was a violation
#             return the return value
#         return the wrapper function
#     return the checker decorator


import functools

import helper
import inspect


def check_types(severity=1):
    if severity == 0:
        return lambda function: function

    def message(msg):
        if severity == 1:
            print(msg)
        else:
            raise TypeError(msg)
    def checker(function):
        expected = function.__annotations__

        assert(all(map(lambda exp: isinstance(exp, type), expected.values())))
        if not expected:
            return function
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            bound_arguments = helper.bind_args(function, *args, **kwargs)
            for arg, val in bound_arguments.items():
                if arg not in expected:
                    continue
                if not isinstance(val, expected[arg]):
                    message(f"Bad Argument! Received {arg}={val}, expecting object of type {expected[arg]}")
            retval = function(*args, **kwargs)
            if 'return' in expected and not isinstance(retval, expected['return']):
                message(f"Bad Return Value! Received {retval}, but expected value of type {expected['return']}")
            return retval
        return wrapper
    return checker

@check_types(severity=1)
def foo(a: int, b: str) -> bool:
    return b[a] == 'X'


foo('WXYZ', 1)
