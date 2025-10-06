# Задание (Livecoding)
#
# У нас есть REST-сервис (воображаемый), который возвращает данные в формате JSON, например:
# data = [
#     {"id": 1, "name": "Test1", "is_active": True},
#     {"id": 2, "name": "Test2", "is_active": False},
#     {"id": 3, "name": "Test3", "is_active": True},
# ]
#
# Твоя задача:
# Написать класс ResponseAnalyzer, который: Принимает на вход список таких словарей (как выше).
# Имеет методы:
# get_active() → возвращает список только активных элементов;
# get_names() → возвращает список имён (name);
# count() → возвращает количество всех элементов;
# validate_keys(required_keys: list) → проверяет, что во всех словарях есть все обязательные ключи (возвращает True/False).
#
# Пример использования:
# ra = ResponseAnalyzer(data)
# print(ra.get_active())     # [{'id': 1, 'name': 'Test1', 'is_active': True}, {'id': 3, 'name': 'Test3', 'is_active': True}]
# print(ra.get_names())      # ['Test1', 'Test2', 'Test3']
# print(ra.count())          # 3
# print(ra.validate_keys(['id', 'name', 'is_active']))  # True


class ResponseAnalyzer:

    def __init__(self, data: list):
        self.data = data

    def get_active(self) -> list:
        """Возврат только активных пользователей, т.е. is_active==True

        :return: Список с активными пользователями
        """
        return list(filter(lambda x: x['is_active'] if x.get('is_active') else None, self.data))
        # return [x for x in self.data if x.get('is_active')] # chat

    def get_names(self) -> list:
        """Вовзащает список состоящий из имён, если ключа с именем нет, будет None. В целом его можно будет фильтрануть и исключить из выборки, но это
        не уточнено в задании

        :return: Список
        """
        return list(map(lambda x: x['name'] if x.get('name', None) else None, self.data))

    def count(self) -> int:
        """Подсчёт количества элементов

        :return: Количество элементов в списке
        """
        return len(self.data)

    def validate_keys(self, required_keys: list) -> bool:
        """Не лучшее решение, но вроде рабочее. Опять нужно уточнять требования, должно быть "строгое" совпадение с required_keys или достаточно вхождения только

        :param required_keys: список ключаей
        :return: Bool
        """
        result = []
        for d in self.data:
            print(required_keys, list(d.keys()))
            if required_keys == list(d.keys()):
               result.append(True)
            else:
                result.append(False)
        return False if False in result else True

    def validate_keys_chat(self, required_keys: list) -> bool:
        required = set(required_keys)
        return all(required.issubset(d.keys()) for d in self.data)


data = [
    {"id": 1, "name": "Test1", "is_active": True},
    {"id": 2, "name": "Test2", "is_active": False},
    {"id": 3, "name": "Test3", "is_active": True},
    {"id": 4, "name": "Test4"},
    # {"id": 5, "is_active": True},
]

x = ResponseAnalyzer(data)
print(x.get_active())
print(x.get_names())
print(x.count())
print(x.validate_keys(['id', 'name', 'is_active']))
print(x.validate_keys(['id', 'name']))

