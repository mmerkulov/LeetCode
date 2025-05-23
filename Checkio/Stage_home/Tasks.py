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


def fold_char(text: str):
    if not text:
        return 'empty'
    amount = 0
    answer = ''
    for i in range(1, len(text)):
        amount += 1
        if text[i - 1] != text[i]:
            answer += text[i - 1] + str(amount)
            amount = 0
    answer += text[-1] + str(amount + 1 if amount != 0 else 1)
    return answer


def fold_char3(text: str):
    answer = {}
    for char in text:
        if char not in answer:
            answer[char] = 1
        else:
            answer[char] += 1
    return ''.join([f'{key}{value}' for key, value in answer.items()])


# x = 'AAAAAGGGGHHHTTLLLLLLDDDFF'  # A5G4H3T2L6D3
# # x = 'AAABB'
# print(fold_char(x))
# x = 'AAAC'
# print(fold_char(x))
# print(fold_char3(x))


def changing_direction(elements: list[int]) -> int:
    if len(elements) < 3:
        return 0
    result = 0
    prev_direct = '+' if elements[0] < elements[1] else '-' if elements[0] > elements[1] else '='
    for idx in range(1, len(elements)):
        current_direct = '+' if elements[idx - 1] < elements[idx] else '-' if elements[idx - 1] > elements[idx] else '='
        if current_direct != prev_direct:
            print(elements[idx - 1], elements[idx], prev_direct, current_direct)
            result += 1
            prev_direct = current_direct
    print(result)
    return result

def changing_direction2(elements: list[int]) -> int:
    if len(elements) < 3:
        return 0
    dirs = []
    for i, j in zip(elements[:-1], elements[1:]):
        print(i, j)
        if j > i and (not dirs or dirs[-1] == '-'):
           dirs.append('+')
        if j < i and (not dirs or dirs[-1] == '+'):
           dirs.append('-')
    return len(dirs) - 1





# changing_direction2([1, 2, 3, 4, 5])  # 0
# changing_direction2([1, 2, 3, 2, 1])  # 1
# changing_direction2([1, 2, 2, 1, 2, 2]) # 2
changing_direction2([6, 6, 6, 4, 1, 2, 5, 9, 7, 8, 5, 9, 4, 2, 6])  # 7

# z = [1, 2, 3, 4]
# z1 = [2, 3, 4]
# for i, j in zip(z, z[1:]):
#     print(i, j)
