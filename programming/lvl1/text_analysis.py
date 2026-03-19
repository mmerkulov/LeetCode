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


# print(text_analysis(text=text))




def text_analysis_v2(text: str) -> tuple:
    import string
    # Более аккуратная очистка текста
    translator = str.maketrans('', '', string.punctuation + '«»—')
    #print(f'translator=>{translator}')
    cleaned_text = text.translate(translator).lower()
    #print(f'cleaned_text=>{cleaned_text}')
    words_list = cleaned_text.split()

    # Подсчет вручную
    word_freq = {}
    for word in words_list:
        word_freq[word] = word_freq.get(word, 0) + 1
    #print(f'word_freq=>{word_freq}')

    # Поиск самого частого слова
    most_common_word = max(word_freq, key=word_freq.get)

    # Количество уникальных слов
    unique_words_count = len(word_freq)

    return word_freq, most_common_word, unique_words_count


def run_text_analysis():
    test_cases = [
        "Привет, мир! Мир большой.",
        "hello world hello",
        "one",
        "word1 word2 word1",  # слова с цифрами
        # ""  # пустая строка
    ]

    for test in test_cases:
        print(f"Текст: '{test}'")
        result = text_analysis_v2(test)
        print(f"Результат: {result}")
        print("-" * 50)

    for test in test_cases:
        print(f"Текст: '{test}'")
        result = text_analysis(test)
        print(f"Результат: {result}")
        print("-" * 50)


run_text_analysis()