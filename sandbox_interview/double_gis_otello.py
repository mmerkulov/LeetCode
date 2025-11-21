# import uuid
#
# # Структура данных об организациях.
# organizations = {
#     1: {
#         'name': 'Организация',
#         'reviews': []
#     },
#     2: {
#         'name': 'Другая организация',
#         'reviews': []
#     },
# }
#
#
# # Необходимо напиcать функцию, которая добавляет отзыв об организации в структуру данных (выше).
# # Функция должна возвращать добавленный отзыв.
# # У организации может быть только один отзыв от каждого пользователя.
#
# # {uuid: comment}
#
# def add_review(org_id: int, user_id: str, comment: str) -> dict:
#     """Что-то пкоа делаем
#
#     :return Словарь
#     """
#     user_id_list = []
#     for i in organizations[org_id]['reviews']:
#         user_id_list.append(list(i.keys())[0])
#
#     print(f'user_id_list=>{user_id_list}')
#     if not user_id in user_id_list:
#         print('небыло, добавили')
#         organizations[org_id]['reviews'].append({user_id: comment})
#     else:
#         print('был, обновили')
#         for element in organizations[org_id]['reviews']:
#             if user_id in element:
#                 element[user_id] = comment
#     return {user_id: comment}
#
# org_id = 2
# user_id = '3'  # uuid.uuid4()
# comment = 'New comment'
# add_review(org_id=org_id, user_id=str(user_id), comment=comment)
# comment = 'New comment!!!'
# add_review(org_id=org_id, user_id=str(user_id), comment=comment)
#
# org_id = 2
# user_id = '4' # uuid.uuid4()
# comment = 'new comment'
# add_review(org_id=org_id, user_id=str(user_id), comment=comment)
#
# print(organizations)

############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################

# Структура данных об организациях.
organizations = {
    1: {
        'name': 'Организация',
        'reviews': []
    },
    2: {
        'name': 'Другая организация',
        'reviews': []
    },
}


# Необходимо напиcать функцию, которая добавляет отзыв об организации в структуру данных (выше).
# Функция должна возвращать добавленный отзыв.
# У организации может быть только один отзыв от каждого пользователя.
import uuid

def add_comment_to_organisation(user_id: str, comment: str, org_id: int) -> dict:
    obj = {user_id: comment}
    info_by_org = organizations[org_id] if organizations.get(org_id, None) else None
    if not info_by_org:
        return {'error': f'Organization with id={org_id} doesnt exist'}

    # получить только ключи
    list_users = [user_id for i in info_by_org['reviews'] for user_id in i]

    if user_id not in list_users:
        print('Add')
        info_by_org['reviews'].append(obj)
    else:
        print('Update')
        for i in info_by_org['reviews']:
            if i.get(user_id):
                i[user_id] = comment
    return obj


# user1 = str(uuid.uuid4())
# comment1 = 'user 1, comment #1'
# print(f'user1=>{user1}')
# result = add_comment_to_organisation(user_id=user1, comment=comment1, org_id=1)
# print(f'result1=>{result}')
# print(f'organizations=>{organizations}')
#
# user2 = str(uuid.uuid4())
# comment2 = 'User2, comment #2'
# print(f'user2=>{user2}')
# result = add_comment_to_organisation(user_id=user2, comment=comment2, org_id=1)
# print(f'result2=>{result}')
# print(f'organizations=>{organizations}')
#
# comment3 = 'User2, comment #3'
# result = add_comment_to_organisation(user_id=user2, comment=comment3, org_id=1)
# print(f'result2=>{result}')
# print(f'organizations=>{organizations}')


def add_comment_to_organisation_v3(user_id: str, comment: str, org_id: int) -> dict:
    # Проверка существования организации
    org = organizations.get(org_id)
    if not org:
        return {'error': f'Organization with id={org_id} doesnt exist'}

    reviews = org['reviews']
    print(reviews)
    new_review = {user_id: comment}

    # Используем enumerate для возможности удаления при обновлении
    for idx, review in enumerate(reviews):
        if user_id in review:
            # Заменяем весь словарь вместо обновления значения
            reviews[idx] = new_review
            print('Update')
            return new_review

    # Если отзыв не найден - добавляем
    reviews.append(new_review)
    print('Add')
    return new_review

user1 = str(uuid.uuid4())
comment1 = 'user 1, comment #1'
result = add_comment_to_organisation_v3(user_id=user1, comment=comment1, org_id=1)
print(f'organizations=>{organizations}')

user2 = str(uuid.uuid4())
comment2 = 'User2, comment #2'
result = add_comment_to_organisation_v3(user_id=user2, comment=comment2, org_id=1)
print(f'organizations=>{organizations}')

comment3 = 'User2, comment #3'
result = add_comment_to_organisation_v3(user_id=user2, comment=comment3, org_id=1)
print(f'organizations=>{organizations}')