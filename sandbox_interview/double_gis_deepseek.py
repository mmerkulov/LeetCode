"""
Тебе нужно протестировать сервис геокодирования (преобразование адреса в координаты).
Сначала напиши код, потом протестируй его.
"""


class ExceptionCash(Exception):
    raise 'Max limit in cache 100'


class GeocodingService:
    """
    Сервис геокодирования 2GIS
    """

    def __init__(self):
        # Кэш для ускорения повторных запросов
        self.cache: dict = {}
        # Список поддерживаемых городов
        self.supported_cities: list = ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург']

    def geocode(self, address: str, city: str = None) -> dict:
        """
        Преобразует адрес в координаты

        Args:
            address: Адрес для геокодирования
            city: Город для уточнения поиска

        Returns:
            dict: {
                'success': bool,
                'lat': float,  # Широта
                'lon': float,  # Долгота
                'precision': str  # Точность совпадения
            }
        """
        # Проверка кэша
        cache_key = f"{city}_{address}" if city else address
        if cache_key in self.cache:
            return self.cache[cache_key]

        # Валидация входных данных
        if not address or not address.strip():
            return {'success': False, 'error': 'Адрес не может быть пустым'}

        if city and city not in self.supported_cities:
            return {'success': False, 'error': f'Город {city} не поддерживается'}

        # Имитация логики геокодирования
        result = self._simulate_geocoding(address, city)
        # self.cache[cache_key] = result
        # заменил присвоение на добавления кэша с проверкой на лимит
        self.add_address_to_cash(cache=self.cache, cache_key=cache_key, data=result)
        return result

    def _simulate_geocoding(self, address: str, city: str) -> dict:
        """
        Имитация реального геокодирования
        В реальности здесь был бы вызов API 2GIS
        """
        # Простая логика для демонстрации
        address_lower = address.lower()

        if 'кремль' in address_lower:
            return {'success': True, 'lat': 55.751244, 'lon': 37.618423, 'precision': 'building'}
        elif 'эрмитаж' in address_lower:
            return {'success': True, 'lat': 59.939831, 'lon': 30.314559, 'precision': 'building'}
        elif 'ленина' in address_lower:
            return {'success': True, 'lat': 55.010101, 'lon': 82.010101, 'precision': 'street'}
        elif 'невский' in address_lower and city == 'Санкт-Петербург':
            return {'success': True, 'lat': 59.934280, 'lon': 30.335098, 'precision': 'street'}
        else:
            return {'success': False, 'error': 'Адрес не найден'}

    def batch_geocode(self, addresses: list) -> list:
        """
        Пакетное геокодирование нескольких адресов
        """
        results = []
        for address in addresses:
            if isinstance(address, dict) and 'address' in address:
                result = self.geocode(address['address'], address.get('city'))
            else:
                result = self.geocode(address)
            results.append(result)
        return results

    def get_supported_cities(self) -> list:
        """
        Получить список доступных городов
        :return: Список поддерживаемых городов
        """
        return self.supported_cities if self.supported_cities else []

    def clear_cache(self) -> None:
        """
        Очистка кэша
        :return: None
        """
        if self.cache:
            self.cache = {}

    @staticmethod
    def add_address_to_cash(cache: dict, cache_key: str, data: dict) -> None:
        """
        Добавляем адрес в кэш с проверкой на наличие данных в кэше и ограничением на 100 элементов
        :param cache: Кэш с адресами
        :param cache_key: Ключ кэша
        :param data: Данные
        :return: None
        """
        if len(cache) < 100 and not cache.get(cache_key, None):
            cache[cache_key] = data
        else:
            raise ExceptionCash


import pytest


@pytest.fixture
def setup_method() -> GeocodingService:
    """Подготовка перед каждым тестом"""
    return GeocodingService()


class TestGeocodingService:
    """Тесты для сервиса геокодирования 2GIS"""

    # ТВОЙ КОД ЗДЕСЬ:
    # 1. Напиши unit-тесты для каждого метода
    def test_unit_get_supported_cities(self, setup_method):
        service = setup_method
        assert service.get_supported_cities(), 'Список городов должен быть!'

    def test_unit_clear_cache(self, setup_method):
        service = setup_method
        service.cache = {'City': 'City'}
        assert service.cache, 'Пустой кэш'
        service.clear_cache()
        assert not service.cache, 'Кэш не пустой!'

# 2. Добавь параметризованные тесты для разных сценариев
# 3. Протестируй граничные случаи
# 4. Проверь работу с кэшем
# 5. Добавь тесты на ошибки
