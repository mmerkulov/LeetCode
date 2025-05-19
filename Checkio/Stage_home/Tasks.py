def backward_string_by_word(text: str) -> str:
    symbol_list = [i for i in text]
    sub_str = ''
    result_list = []
    for i in symbol_list:
        if i != ' ':
            sub_str += i
        else:
            result_list.append(sub_str[::-1])
            result_list.append(i)  ## тут пробелы
            sub_str = ''
    if sub_str:
        result_list.append(sub_str[::-1])
    return ''.join(result_list)


def bigger_price(limit: int, data: list[dict]) -> list[dict]:
    sorted_data = sorted(data, key=lambda x: x.get('price', -1), reverse=True)
    return sorted_data[:limit]


# z = 2
# x = [
#     {"name": "bread", "price": 100},
#     {"name": "wine", "price": 138},
#     {"name": "meat", "price": 15},
#     {"name": "water", "price": 1},
# ]
# print(bigger_price(2, [{'name': 'bread', 'price': 100}, {'name': 'wine', 'price': 138}, {'name': 'meat', 'price': 15}, {'name': 'water', 'price': 1}]))


def between_markers(text: str, begin: str, end: str) -> str:
    if not begin and not end:
        return text
    begin_idx = text.find(begin) + len(begin) if text.find(begin) != -1 else None
    end_idx = text.find(end) if text.find(end) != -1 else None
    return text[begin_idx:end_idx]


between_markers("<head><title>My new site</title></head>", "<titl123e>", "</title>")


def fizzbuzz_classic():
    for i in range(1, 101):
        if i % 15 == 0:
            print('fizzbuzz')
        elif i % 5 == 0:
            print('buzz')
        elif i % 3 == 0:
            print('fizz')
        else:
            print(i)


def fizzbuzz_concat():
    for i in range(1, 101):
        output = ''
        if i % 3 == 0:
            output += 'Fizz'
        if i % 5 == 0:
            output += 'Buzz'
        print(output or i)


def popular_words(text: str, words: list) -> dict:
    words_list = text.lower().split()
    result = {}
    for word in words:
        result[word] = 0

    for word in words_list:
        if word in words:
            result[word] += 1

    return result


popular_words(
    "\nWhen I was One\nI had just begun\nWhen I was Two\nI was nearly new\n",
    ["i", "was", "three", "near"])


def second_index(text: str, symbol: str) -> int | None:
    if text.find(symbol, text.find(symbol) + 1) == -1:
        return None
    return text.find(symbol, text.find(symbol) + 1)


# print(second_index("hi mayor", " "))


def shift_list_2(target: int, lst: list):
    print(target % len(lst))
    for _ in range(target % len(lst)):
        print(f'_=>{_}')
        elm_1 = lst.pop()
        print(f'elm_1=>{elm_1}')
        lst.insert(0, elm_1)
    return lst


def shift_list_3(target: int, lst: list):
    range_lst = target % len(lst)
    return lst[len(lst) - range_lst:] + lst[:-range_lst]


def changing_direction(elements: list[int]) -> int:
    result = 0
    for i in range(len(elements) - 1):
        if elements[i] > elements[i + 1]:
            result += 1
    return 0
