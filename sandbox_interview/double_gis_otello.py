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
#         'reviews': [{'1': "New comments"}, {'2': "New comments!"}]
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

