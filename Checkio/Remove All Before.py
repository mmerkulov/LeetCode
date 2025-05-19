from collections.abc import Iterable


def remove_all_before(array: list, board: int) -> Iterable:
    try:
        idx = array.index(board)
        return array[idx:]
    except ValueError:
        return array


def replace_first(items: list) -> Iterable:
    if not items:
        return []
    items.append(items.pop(0))
    return items


def max_digit(value: int) -> int:
    return max(int(i) for i in str(value))


def beginning_zeros(a: str) -> int:
    z = 0
    for i in a:
        if i != '0':
            break
        else:
            z += 1
    return z


def between_markers(text: str, start: str, end: str) -> str:
    return text[text.index(start) + 1:text.index(end)]


def split_pairs1(text: str) -> Iterable[str]:
    result = []
    if len(text) == 0:
        return text
    for i, k in enumerate(text, start=1):
        print(i)
        if i % 2 != 0:
            result.append(text[i - 1:i + 1])
    if len(text) % 2 == 1:
        result[len(result) - 1] = result[len(result) - 1] + '_'
    return result


def split_pairs(text: str):
    text += '_' if len(text) % 2 == 1 else ''
    return [text[i:i + 2] for i in range(0, len(text), 2)]


def correct_sentence(text: str) -> str:
    print()
    return text[0].upper() + text[1:] + '.' if text[-1] != '.' else text.capitalize()


def nearest_value(values: set[int], one: int) -> int:
    result = None
    x = sorted(values)
    if x[0] > one:
        return x[0]
    elif x[-1] < one:
        return x[-1]

    for i in range(len(x) - 1):
        if x[i] == one:
            return one
        if x[i] < one < x[i + 1]:
            if one - x[i] <= x[i + 1] - one:
                result = x[i]
            else:
                result = x[i + 1]
    return result


print(nearest_value({4, 7, 10, 11, 12, 17}, 20))
