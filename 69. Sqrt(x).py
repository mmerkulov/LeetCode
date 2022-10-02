# Given a non-negative integer x, compute and return the square root of x.
# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
# Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
# Example 1:
# Input: x = 4
# Output: 2
#
# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.


# 1. Разбить число на десятки с права на лево
# 2. Для самого левого значения найти квадрат числа, т.е. число может быть от 1 до 99 и его возводим в квадрат
# 3. Находим два числа x, x+1 где число самое левое входит в этот промежуток между x^2 и (x+1)^2
# 4. Найденное число это первая цифра ответа

def sqrt_from_x(x):
    main_answer = []

    def get_list_dec(x):
        list_dec = []
        while x > 0:
            list_dec.append(x % 100)
            x = x // 100
        return list_dec

    def get_first_value(first_number):
        stack = []
        for key, val in DICT_DEGREE.items():
            if val <= first_number:
                stack.append(key)
        return stack[-1]

    def search_next_number_for_remainder(reminder_number, double_val):
        print('Call search_next_number_for_remainder')
        stack_list = []
        for x in range(1, 11):
            text_number = str(double_val) + str(x)
            n = int(text_number)
            if x * n <= reminder_number:
                stack_list.append(x)
                text_number = double_val
        print(stack_list)
        main_answer.append(stack_list[-1])
        print('End search_next_number_for_remainder')
        return False

    def get_next_reminder(first_answer, first_remainder, other_numbers):
        print('Call get_next_reminder')
        print(first_answer, first_remainder, other_numbers)
        double_val = first_answer * 2
        for x in other_numbers:
            text_num = str(first_remainder) + str(x)

        reminder_number = int(text_num)
        print(f'double val = {double_val}')
        print(f'reminder number = {reminder_number}')

        print('End get_next_reminder')
        return double_val, reminder_number

    # разбили число на 10-ки
    list_dec = get_list_dec(x)
    print(f'list_dec = {list_dec}')

    # Находим первое число
    first_num = list_dec[-1]
    print(f'first_num = {first_num}')

    # нужно из первого числа получить первую цифру в ответ
    first_num_answer = get_first_value(first_num)

    # Сюда будем записывать ответы
    main_answer.append(first_num_answer)

    # Получаем первый остаток от разницы между первым числом и произведением двух числел, которые являются первым числом ответа
    first_remainder_num = first_num - (main_answer[0] * main_answer[0])
    print(f'Первый остаток = {first_remainder_num}')

    # поиск остатка вычитания
    for idx, i in enumerate(reversed(list_dec)):
        if idx == 0:
            continue
        a, b = get_next_reminder(main_answer[0], first_remainder_num, list_dec[:len(list_dec) - 1])

    # поиск числа
    search_next_number_for_remainder(b, a)

    print(f'Ответ = {main_answer}')

    return main_answer


DICT_DEGREE = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
x = 4096
# print(sqrt_from_x(x))

lis = [84, 92, 4]
for idx, x in enumerate(reversed(lis)):
    print(idx, x)
