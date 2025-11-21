# Ты тестируешь REST API регистрации пользователей.
# Сервис имеет 2 эндпоинта:
#
# POST /register — создаёт пользователя и возвращает:
# {"id": 101, "name": "test_user"}
#
# DELETE /users/{id} — удаляет пользователя и возвращает:
# {"deleted": true}
import json
import responses
import requests
import pytest
import uuid


class MyUser:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


URL = 'https://mytwitter.com/'


@pytest.fixture
def mock_response_delete():
    deleted_users = set()
    def request_delete_callback(request):

        if not request.params['user_id']:
            body = {'deleted': False, 'error': 'Missing user_id'}
            status = 400
        elif request.params['user_id'] in deleted_users:
            body = {'deleted': False, 'error': f'User {request.params['user_id']} not found'}
            status = 400
        else:
            body = {'deleted': True, 'user_id': request.params['user_id']}
            status = 200

        return status, {"Content-Type": "application/json"}, json.dumps(body)

    with responses.RequestsMock() as rsps:
        rsps.add_callback(
            method=responses.DELETE,
            url=URL + 'api/v1/user',
            callback=request_delete_callback,
            content_type='application/json'
        )
        yield rsps


@pytest.fixture
def mock_response_post():
    def request_post_callback(request):
        # Парсим тело запроса
        payload = json.loads(request.body.decode('utf-8'))
        name = payload.get("name")
        age = payload.get("age")

        # Формируем динамический ответ
        resp_body = {
            "user_id": str(uuid.uuid4()),
            "status": "success",
            'data': {"name": name,
                     "age": age, }
        }
        return 201, {"Content-Type": "application/json"}, json.dumps(resp_body)

    with responses.RequestsMock() as rsps:
        rsps.add_callback(
            method=responses.POST,
            url=URL + 'api/v1/register',
            callback=request_post_callback,
            content_type='application/json'
        )

        yield rsps


@pytest.fixture(scope='session')
def some_client():
    client = requests.Session()
    yield client
    client.close()


@pytest.fixture
def some_user(some_client, mock_response_post, mock_response_delete):
    user = MyUser(name='Anton', age=30)
    response = some_client.post(url=URL + 'api/v1/register', json={'name': user.name, 'age': user.age})
    user = response.json()
    yield user
    some_client.delete(url=URL + 'api/v1/user', params={'user_id': user['user_id']})


class TestMyCode:
    def test_register_positive(self, some_user):
        user = some_user
        assert user['user_id'], 'Отсутствует user_id'
        assert user['data']['name'] == 'Anton'
        assert user['data']['age'] == 30

    # def test_delete_positive(self, some_client, some_user):
    #     client = some_client
    #     user = some_user
    #
    #     response = client.delete(url=URL + "api/v1/user", params={"user_id": user["user_id"]})
    #     data = response.json()
    #
    #     assert response.status_code == 200
    #     assert data["deleted"] is True
    #     assert data["user_id"] == user["user_id"]
    #
    # def test_delete_twice_positive(self, some_client, some_user):
    #     client = some_client
    #     user = some_user
    #
    #     response = client.delete(url=URL + "api/v1/user", params={"user_id": user["user_id"]})
    #     data = response.json()
    #     print(f'response1=>{response}')
    #     data = response.json()
    #     print(f'data1=>{data}')
    #
    #     assert response.status_code == 200
    #     assert data["deleted"] is True
    #     assert data["user_id"] == user["user_id"]
    #
    #     response = client.delete(url=URL + "api/v1/user", params={"user_id": user["user_id"]})
    #     print(f'response2=>{response}')
    #     data = response.json()
    #     print(f'data2=>{data}')
