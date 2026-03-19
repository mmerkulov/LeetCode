import datetime
import json
from functools import wraps
from collections import OrderedDict

def generate_json_config(size=9999999):
    with open('app_config.json', 'w', encoding='utf-8') as f:
        f.write('{\n')
        for i in range(size + 1):
            if i < size:
                row = f'"{i}": "parameter-{i}",\n'
                f.write(row)
            else:
                row = f'"{i}": "parameter-{i}"\n'
                f.write(row)
        f.write('}\n')

generate_json_config()


def lru_my_cache(max_size:int=128):

    def _decorator(func):
        cache = OrderedDict()

        @wraps(func)
        def _wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key in cache:
                cache.move_to_end(key)
                return cache[key]

            if len(cache) >= max_size:
                cache.popitem(last=True)

            result = func(*args, **kwargs)
            cache[key] = result
            return result

        _wrapper.cache_info = lambda: {
            'size': len(cache),
            'maxsize': max_size,
            'keys': list(cache.keys())
        }

        return _wrapper

    return _decorator


def my_cache(func):

    cache = {}

    @wraps(func)
    def _wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))

        if key in cache:
            return cache[key]

        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return _wrapper



@my_cache
def read_json_config():
    with open('app_config.json', 'r', encoding='utf-8') as f:
        return json.load(f)




def benchmark():
    start = datetime.datetime.now()
    read_json_config()
    delta = datetime.datetime.now() - start
    print(f'Время работы #1 = {delta}')

    start = datetime.datetime.now()
    read_json_config()
    delta = datetime.datetime.now() - start
    print(f'Время работы #2 = {delta}')



benchmark()