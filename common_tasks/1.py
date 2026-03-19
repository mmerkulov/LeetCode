# Задача 1 — параметризация и фикстуры
#
# У тебя есть функция:

def is_valid_age(age: int) -> bool:
    if not isinstance(age, int) or age < 0 or age > 120:
        return False
    return True
#
# Твоя цель:
#
# Написать тест с параметризацией, который проверяет корректность функции для:
# валидных значений (0, 25, 120),
# невалидных (-1, 121, '18', None).
# Использовать pytest.mark.parametrize.
# Отдельно проверить сообщение об ошибке (например, если функция бросает исключение).
# Добавить фикстуру, которая логирует входные параметры перед тестом.

import pytest


@pytest.fixture(autouse=True)
def logger_parameters(request):
    params = getattr(request.node.callspec, "params", None)
    print(f'\nTest running: {request.node.name} with parameters {params}')



@pytest.mark.parametrize('age, result', [(0, True),(25, True),(120, True),
                                         (-1, False),(121, False),('18', False),(None, False)])
def test_check_age(age, result):
    assert is_valid_age(age=age) == result



if __name__ == "__main__":
    pytest.main([__file__, "-v"])