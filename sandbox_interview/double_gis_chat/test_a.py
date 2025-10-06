import pytest, allure

from double_gis_chat import ResponseAnalyzer


@pytest.fixture
def sample_data():
    return [
        {"id": 1, "name": "User1", "is_active": True},
        {"id": 2, "name": "User2", "is_active": False},
        {"id": 3, "name": "User3", "is_active": True},
        {"id": 4, "is_active": True},  # без name
    ]


@pytest.fixture
def create_instance(sample_data) -> ResponseAnalyzer:
    return ResponseAnalyzer(data=sample_data)


class TestResponseAnalyzer:

    @pytest.mark('positive')
    def test_get_active_positive(self, create_instance):
        inst = create_instance
        with allure.step('Выполнить запрос'):
            response = inst.get_active()
        with allure.step('Выполнить проверку'):
            for i in response:
                assert i['is_active'], 'Ошибка'

