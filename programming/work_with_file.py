# Задача: Напишите скрипт, который:
# - читает CSV файл с данными о товарах (название, цена, количество)
# - фильтрует товары по цене и количеству
# - создает новый CSV с результатами
# - генерирует отчет в текстовом файле
import random


def create_test_file():
    with open('products.csv', 'w', encoding='utf-8') as file:
        file.write('name,price,amount\n')
        for i in range(101):
            name = 'name-'+str(i)
            price = random.randint(10, 10000)
            amount = random.randint(1, 20)
            file.write(name + ',' + str(price) + ',' + str(amount)+'\n')


def work(file: str = 'products.csv'):

    work_list = []
    with open(file, 'r', encoding='utf-8') as f:
        headers = f.readline().strip().split(',')
        for line in f:
            value = line.strip().split(',')
            row_dict = dict(zip(headers, value))
            work_list.append(row_dict)

    new_work_list = sorted(work_list, key=lambda a: int(a['price']) * int(a['amount']), reverse=True)

    with open('filtered_file.csv', 'w', encoding='utf-8') as f1:
        f1.write(','.join(headers) + '\n')
        for d in new_work_list:
            row = d['name'] + ',' + d['price'] + ',' + d['amount']
            f1.write(row+'\n')


create_test_file()
work()

# x = [{'name': 'name-0', 'price': '2213', 'amount': '4'}, {'name': 'name-1', 'price': '4558', 'amount': '14'}, {'name': 'name-2', 'price': '5984', 'amount': '14'}]
# for i in x:
#     filter = int(i['price']) * int(i['amount'])
#     print(filter, i['price'], i['amount'])
#
# z = sorted(x, key=lambda a: int(a['price']) * int(a['amount']), reverse=True)
# print(z)
# # sorted_data = sorted(data, key=lambda x: x.get('price', -1), reverse=True)