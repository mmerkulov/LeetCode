# Дана строка s, состоящая из строчных или прописных букв. Нужно определить максимальную длину палиндрома, который можно составить из букв этой строки.
#
# Буквы чувствительны к регистру, например, строка "Aa" не считается палиндромом.
#
# Пример 1:
#     Вход:  s = "abccccdd"
#     Выход: 7
# Пояснение: Самый длинный палиндром, который можно построить — "dccaccd", его длина равна 7.

def gogo(s: str) -> int:
    letters_list = [x for x in s]
    letters_dict = {}
    for i in letters_list:
        if letters_dict.get(i):
            letters_dict[i] += 1
        else:
            letters_dict[i] = 1
    print(letters_dict)

    answer = 0
    has_odd = False
    for i, k in letters_dict.items():
        if k % 2 == 0:
            answer += k
        else:
            answer += k - 1
            has_odd = True

    if has_odd:
        answer += 1

    return answer



z = 'abccccdd'
print(gogo(z))
z = 'aabc'
print(gogo(z))
z = 'ссс'
print(gogo(z))
z = 'bb'
print(gogo(z))