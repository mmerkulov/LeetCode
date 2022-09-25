# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# visited = set()
# # собираем повторяющиеся элементы, но что бы они были в новом списке уникальны, т.е. один раз f,l,f,l => f,l
# prefix1 = [x for x in prefix if x in visited or (visited.add(x) or False)]

def search_prefix_anywhere_in_words(strs=[]):
    """ Функция находит вооообще везде совпадение, хоть какие-то, не только "с начала слова"

    :param strs: Список слов
    :return: Строку, которая содержит общий для всех элементов из списка strs общий префик
    """
    prefix = ''
    word_with_min_len = strs[0]
    for word in strs:
        if len(strs) <= 1:
            print(strs[0])
            break
        if word == word_with_min_len:
            continue
        # найти минимальную длину слова в списке
        if len(word_with_min_len) > len(word):
            word_with_min_len = word

        # проверочная переменная для цикла, что бы выходить из него, когда мы нашли нужный префикс
        check = 1
        amount_letters = len(word_with_min_len)
        while amount_letters > 0 and check == 1:
            x = word.find(word_with_min_len[:amount_letters])
            # если мы не нашли вхождение, то значит нет "всего слова" и нужно уменьшить длину поиска,
            # т.е. самое маленькое слово уменьшаем и снова смотрим вхождение
            if x == -1:
                amount_letters -= 1
            else:
                # нашли префик и нужно его добавить в список
                check = 0
                if prefix == '':
                    prefix = word_with_min_len[:amount_letters]
                # Если наш префикс большьше нового слова, то заменяем префикс на более короткое
                if len(prefix) > len(word_with_min_len[:amount_letters]):
                    prefix = word_with_min_len[:amount_letters]

    return prefix


def search_prefix_from_beginning_of_words(strs=[]):
    """

    :param strs:
    :return:
    """

    def search_min_word(list_word):
        little_word = ''
        for x in list_word:
            if len(x) < len(little_word) or little_word == '':
                little_word = x
        return little_word

    if len(strs) <= 1:
        return ''.join(strs)

    prefix = ''
    # поиск минимального слова
    word_with_min_len = search_min_word(strs)

    for word in strs:
        # if word == word_with_min_len:
        #    continue

        # проверочная переменная для цикла, что бы выходить из него, когда мы нашли нужный префикс
        check = 1
        amount_letters = len(word_with_min_len)
        while amount_letters > 0 and check == 1:
            x = word.find(word_with_min_len[:amount_letters], 0, len(word_with_min_len[:amount_letters]))
            # если мы не нашли вхождение, то значит нет "всего слова" и нужно уменьшить длину поиска,
            # т.е. самое маленькое слово уменьшаем и снова смотрим вхождение
            if x == -1:
                amount_letters -= 1
                # return ""
            else:
                # нашли префик и нужно его добавить в список
                check = 0
                if prefix == '':
                    prefix = word_with_min_len[0:amount_letters]
                # Если наш префикс большьше нового слова, то заменяем префикс на более короткое
                if len(prefix) > len(word_with_min_len[:amount_letters]):
                    prefix = word_with_min_len[:amount_letters]
        if amount_letters <= 0:
            # print('То что? После 1ого прохода сравнение слов не показало результата и надо уже выходить.')
            return ''
    return prefix


# strs = ["flower", "flow", "flight"] # Output: "fl"
# strs = ['a']  # "a"
# strs = ["dog","racecar","car"] # Output: ""
# strs = ["reflower", "flow", "flight"]  # Output: ""
strs = ["flower", "flower", "flower", "flower"]
# print(search_prefix_anywhere_in_words(strs))
print(search_prefix_from_beginning_of_words(strs))
