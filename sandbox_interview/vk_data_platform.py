"""
Требуется закодировать решение,
которое выводит в DEBUG-лог длительность выполнения каждого вызова функции
вместе с отметкой успешности или неуспешности вызова/отработки функции.

Реализуйте решение, которое можно было бы переиспользовать и в других подобных случаях.
Вы владелец кодовой базы, у вас есть свобода изменять код под собственные нужд.
"""

import datetime
import time

def logger(func):
    start = datetime.datetime.now()
    def _wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            print(f'Функция выполнилась за {datetime.datetime.now() - start} sec.')
            return result
        except Exception as e:
            print(f'Функция выполнилась с ошибкой. Время - {datetime.datetime.now() - start}')
            raise e
    return _wrapper


@logger
def some_func(val):
    print(1 / val)


@logger
def calling(val):
    try:
        some_func(val)
    except ZeroDivisionError:
        print('make rollback')
        raise ValueError


def call2(val):
    try:
        calling(val)
    except ValueError:
        print('rollback')


@logger
def some_func1(value):
    for i in range(value):
        time.sleep(1)
        if i == 3:
            raise ValueError('Error')
    print('all right')




# calling(2)
# calling(0)
call2(0)
