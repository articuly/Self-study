import functools
import timeit


def fib(n):
    if n < 2:
        return [0]
    else:
        lst = [0, 1]
        [lst.append(lst[-1] + lst[-2]) for i in range(n - 2)]
        return lst


print(timeit.timeit('fib(1000)', number=10000, globals=globals()))


@functools.lru_cache(maxsize=4)
def fib_cache(n):
    if n < 2:
        return [0]
    else:
        lst = [0, 1]
        [lst.append(lst[-1] + lst[-2]) for i in range(n - 2)]
        return lst


print(timeit.timeit('fib_cache(1000)', number=10000, globals=globals()))
