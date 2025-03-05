import functools
from time import time

def cached(f):
    cache = dict()

    @functools.wraps(f)
    def wrapper(x):
        if x in cache:
            return cache[x]
        else:
            y = f(x)
            cache[x] = y
            return y

    return wrapper

def timed(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        t0 = time()
        res = f(*args, **kwargs)
        dt = time() - t0
        return res, dt
    return wrapper

def fib_slow(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_slow(n-1) + fib_slow(n-2)


@cached
def fib_fast(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_fast(n-1) + fib_fast(n-2)

if __name__ == '__main__':

    for fib in (fib_fast, fib_slow):
        fib = timed(fib)
        for x in (0, 1, 5, 15, 32):
            y, dt = fib(x)
            print(f"{fib.__name__}({x:2}) = {y:>7} in {dt:<7.2} seconds.")
        print("")