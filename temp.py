import datetime
import time

class A():
    def __init__(self, value: int):
        self.value = value

    # def __str__(self):
    #     return self.value


x = [A(1)] * 3

for i in x:
    print(id(i))
x[1].value = 2

print(x)
for i in x:
    print(id(i))

a = A(1)
z = [a] * 3
z[1].value = 2
print(z)

#
# # что будет?
# #####################
# a = ([1], 2)
# l = 'key'
# d = {a: 12, l: 13}
# print(d)
# ######################
# lst = [1, 11, '17', 'qwerty', None, (1, 44), 4, True]
#
# z = [i for i in lst if isinstance(i, int)]
# print(z)
# #####################
# def foo(x: int):
#     print(f"x=>{x}")
#     return x
#
#
# # r = [foo(i) for i in range(4)]  # сначала был список [], потом поменяли на генератор
# r = (foo(i) for i in range(4))  # сначала был список [], потом поменяли на генератор
#
# for element in r:
#     print(element)
# ################################
# def my_decorator(func):
#     def wrapper(*args):
#         s = func(*args)
#         return s.lower()
#
#     return wrapper
#
#
# @my_decorator
# def my_string(s: str) -> str:
#     return s
#
#
# assert my_string('My String is THE best') == 'my string is the best'
# ##########################
# lst = [0]
# try:
#     i = lst[1]
# except IndexError:
#     print('IndexError raised')
# except Exception:
#     print('Exception raised')
# else:
#     print('Else')
# finally:
#     print('Finally')
#
#
# #############################
#
# class SimpleConnect():
#     def __init__(self, obj):
#         self.obj = obj
#
#     def __enter__(self, *args):
#         self.connect = Connect(args)
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         pass
#
# ##################
#
# class A:
#     a: int = 1
#     _b: int = 2
#     __c: int = 3
#     ___d: int = 4
#
#
# a = A()
# print(a.a, a._b, a._A__c, a._A___d)
#
# ###################
#
# def buf(key:str, value:int, object:dict = {}) -> dict:
#     object.update({key: value})
#     return object
#
# test1 = buf("one", 1)
# test2 = buf("two", 2, {})
# test3 = buf("three", 3)
# print(test1)
# print(test2)
# print(test3)
#
# Что будет в переменных test1, test2 и test3?
# Ответ:
# {'one': 1, 'three': 3}
# {'two': 2}
# {'one': 1, 'three': 3}
#
# ###############
# def timer(pause: int):
#     def _decorator(func):
#         def _wrapper(*args, **kwargs):
#             start_time = datetime.datetime.now()
#             time.sleep(pause)
#             result = func(*args, **kwargs)
#             end_time = datetime.datetime.now()
#             delta = end_time - start_time
#             print(f'Время выполнения функци - {delta} sec')
#             return result
#
#         return _wrapper
#
#     return _decorator
#
#
# @timer(pause=2)
# def some_f():
#     for i in range(1001):
#         print(i)
#
#
# some_f()
#
# ######################################################
# a = [1,2,3]
# b = [1,2,3]
# print(a==b)
# print(a is b)
#
# c = 1234
# d = 1234
# print(c==d)
# print(c is d)
#
# #######################################################
# # iterator
# class MyCounter:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current > self.end:
#             raise StopIteration
#         value = self.current
#         self.current += 1
#         return value
#
#
# c = MyCounter(5, 15)
# for i in c:
#     print(i)
#
#
# def my_counter(start, end):
#     while start <= end:
#         yield start
#         start += 1
#
#
# for i in my_counter(1, 5):
#     print(i)
#
# #######################################################
# from functools import wraps
#
# def show_start_stop(func):
#     @wraps(func)
#     def _wrapper(*args, **kwargs):
#         print(f'Start {func.__name__}')
#         result = func(*args, **kwargs)
#         print(f'Stop {func.__name__}')
#         return result
#
#     return _wrapper
#
#
# @show_start_stop
# def some_f():
#     for i in range(5):
#         print(i)
#
#
# some_f()
# #######################################################
#
# class MyConnect:
#     def __init__(self, connect):
#         self.connect = connect
#
#     def __enter__(self):
#         print('Connecting...')
#         return self.connect.connect()
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('Disconnecting...')
#         return self.connect.disconect()
#
#
# with MyConnect(postgres_instance):
#     ...
#
# from contextlib import contextmanager
#
# @contextmanager
# def conn_to_db(conn):
#     connect = conn.connection()
#     try:
#         print('Connecting...')
#         yield connect
#     finally:
#         print('Disconnecting...')
#         conn.disconect()
#
# ######################################################
#
# Если у тебя есть список словарей, нужно отсортировать его по значению определённого ключа.
# Как это сделать?
# А если в некоторых словарях этого ключа нет — как обработать эту ситуацию, чтобы не получить ошибку?
#
# a = [{'a': 21, 'b': 1}, {'a': 15, 'b': 4}, {'a': 22, 'b': 2}, {'a': 6, 'b': 5}, {'b': 2}]
#
#
# aa = sorted(a, key=lambda x: x['a'] if x.get('a') else 0)
# print(a)
# print(aa)
# x = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#
# cache_key = 'e'
# if len(x) < 5 and not x.get(cache_key, None):
#     x[cache_key] = 5
#
# cache_key = 'e'
# if len(x) < 5 and not x.get(cache_key, None):
#     x[cache_key] = 6
#
# print(x)
#
# # #######################################################
#
# class MyStack:
#     """LIFO - Last In, First Out"""
#     def __init__(self):
#         self.items: list = []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         if self.is_empty():
#             raise IndexError('Pop from empty stack')
#         return self.items.pop()
#
#     def peek(self):
#         if self.is_empty():
#             raise IndexError('Peek from empty stack')
#         return self.items[-1]
#
#     def is_empty(self):
#         return len(self.items) == 0
#
#     def size(self):
#         return len(self.items)
#
#
# class MyQueue:
#     """FIFO - First In, First Out"""
#     def __init__(self):
#         self.queue: list = []
#
#     def enqueue(self, item):
#         self.queue.append(item)
#
#     def dequeue(self):
#         if self.is_empty():
#             raise IndexError('dequeue from empty stack')
#         return self.queue.pop(0) # O(n)
#
#     def is_empty(self):
#         return len(self.queue) == 0
#
#     def size(self):
#         return len(self.queue)
#
#
# ##############################################
#
# a = 5579
# print(a, id(a), hash(a))
# z = ['qrgt', 'bcvb', 3]
# print(z, id(z), hash(z))