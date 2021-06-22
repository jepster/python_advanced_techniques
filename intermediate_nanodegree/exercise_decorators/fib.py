from memoize import memoize

@memoize
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    print(fib(10))
    print(fib(25))
    print(fib(50))
    print(fib(100))