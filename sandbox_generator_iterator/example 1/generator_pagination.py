# Задача 1: Генератор для пагинации
# Проблема: У вас есть API, который возвращает данные постранично. Нужно создать генератор, который будет последовательно получать все страницы.

import uuid
import random

def paginator_generator(api_url: str, limit: int = 10):
    """Генератор постраничного вывода данных от api
    
    :param api_url: эндпоинт
    :param limit: лимит
    :return: Генератор
    """
    current_page = 0
    next_page = 1

    current = 0
    while current < limit:
        current_page += 1
        next_page = next_page + 1 if current_page < limit else None
        print(f'Call this page -> {api_url}/page={current_page}')
        response_page = {
            'page': current_page,
            'next_page': next_page,
            'data': [{'user_id': str(uuid.uuid4()), 'b': random.randint(a=0, b=100), 'size': 512, 'values': [1, 2, 3]}]
        }

        yield response_page
        current += 1



def some_api():
    return 'vk.com'

for page in paginator_generator(api_url=some_api(), limit=10):
    print(page)
    # как-то обрабатываем page
    ...
    # или делаем какие-нибудь проверки
    assert page['data'][0]['user_id'] is not None
