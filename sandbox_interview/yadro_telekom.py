from functools import lru_cache
import datetime


def swap_dict(d: dict) -> dict:
    if not bool(d):
        return {}
    new_dict = {}

    for k, v in d.items():
        try:
            if not new_dict.get(k, None):
                new_dict[v] = k
        except TypeError:
            continue

    return new_dict


# d0 = {}
# print(swap_dict(d0))
#
# d1 = {1: 2, 3: 4}
# print(swap_dict(d1))
#
# d2 = {1: 2, 3: [1, 2, 3]}
# print(swap_dict(d2))
#
# d3 = {1: 2, 3: 4, 4: 4}
# print(swap_dict(d3))
#
# d4 = {(1, 2): 1, (): 2}
# print(swap_dict(d4))
#
# d5 = {'a': 1}
# print(swap_dict(d5))

###################################
import time


def timer(func):
    def _wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f'Время выполнения = {time.time() - start_time}.')
        return result

    return _wrapper


def fibonacci(n: int):
    a, b = 0, 1
    count = 0
    while count < n:
        a, b = b, a + b
        count += 1
    return a


def fibonacci_recurs(n: int):
    if n <= 1:
        return n
    return fibonacci_recurs(n - 1) + fibonacci_recurs(n - 2)


@lru_cache
def fibonacci_lru(n: int):
    if n <= 1:
        return n
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)


def benchmark():
    n = 30

    start_time = time.time()
    print(fibonacci(n))
    print(f'Время выполнения fibonacci = {time.time() - start_time}.')

    start_time2 = time.time()
    print(fibonacci_recurs(n))
    print(f'Время выполнения fibonacci_recurs = {time.time() - start_time2}.')

    start_time3 = time.time()
    print(fibonacci_lru(n))
    print(f'Время выполнения fibonacci_lru = {time.time() - start_time3}.')


# 0 1 1 2 3 5 8 13 21
# print(fibonacci(12))
# print(fibonacci_recurs(15))
# print(fibonacci_lru(12))
# benchmark()
