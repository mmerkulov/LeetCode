# Задача: Напишите функцию, которая принимает строку и возвращает:
# - словарь с частотой каждого слова (игнорируя регистр и знаки препинания)
# - самое частое слово
# - количество уникальных слов

text = "Привет, мир! Это тестовый текст. Текст для проверки работы функции м м м м."

def text_analysis(text: str) -> tuple:

    original_text = ''.join([i.lower() for i in text if i.isalpha() or i == ' '])
    words_list = original_text.split()

    d = {}
    for i in words_list:
        if not d.get(i, None):
            d[i] = 1
        else:
            d[i] += 1
    uniq_amount = 0
    uniq_word = list(d)[0]
    for i, k in d.items():
        if k == 1:
            uniq_amount +=1
        else:
            if d[uniq_word] < d[i]:
                uniq_word = i

    return d, uniq_word, uniq_amount


print(text_analysis(text=text))
