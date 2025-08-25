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
    return 0



z = 'abccccdd'
gogo(z)
z = 'aabc'
gogo(z)
