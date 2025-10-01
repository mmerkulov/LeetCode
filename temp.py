import datetime
import time


class A():
    def __init__(self, value: int):
        self.value = value

    # def __str__(self):
    #     return self.value


x = [A(1)] * 3
x[1].value = 2

print(x)

a = A(1)
z = [a] * 3
z[1].value = 2
print(z)


# что будет?
######################
# a = ([1], 2)
# l = 'key'
# d = {a: 12,l: 13}
# print(d)
#######################
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
#################################
def my_decorator(func):
    def wrapper(*args):
        s = func(*args)
        return s.lower()

    return wrapper


@my_decorator
def my_string(s: str) -> str:
    return s


assert my_string('My String is THE best') == 'my string is the best'
##########################
lst = [0]
try:
    i = lst[1]
except IndexError:
    print('IndexError raised')
except Exception:
    print('Exception raised')
else:
    print('Else')
finally:
    print('Finally')


#############################

# class SimpleConnect():
#     def __init__(self, obj):
#         self.obj = obj
#
#     def __enter__(self, *args):
#         self.connect = Connect(args)
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         pass

###################

# class A:
#     a: int = 1
#     _b: int = 2
#     __c: int = 3
#     ___d: int = 4
#
#
# a = A()
# print(a.a, a._b, a._A__c, a._A___d)

####################

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

# Что будет в переменных test1, test2 и test3?
# Ответ:
# {'one': 1, 'three': 3}
# {'two': 2}
# {'one': 1, 'three': 3}

################
def timer(pause: int):
    def _decorator(func):
        def _wrapper(*args, **kwargs):
            start_time = datetime.datetime.now()
            time.sleep(pause)
            result = func(*args, **kwargs)
            end_time = datetime.datetime.now()
            delta = end_time - start_time
            print(f'Время выполнения функци - {delta} sec')
            return result

        return _wrapper

    return _decorator


@timer(pause=2)
def some_f():
    for i in range(1001):
        print(i)


some_f()
