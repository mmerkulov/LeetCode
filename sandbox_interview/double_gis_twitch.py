
def calc_space(width: int, text: str) -> str:
    spaces = int((width - 2 - len(text)) / 2)
    text = f' ' * spaces + text + ' ' * spaces
    return text + ' ' if len(text) != width-2 else text


def print_in_box(text: str, width: int, high: int) -> None:
    if width % 2 == 0 or high % 2 == 0:
        raise Exception('Не будет по центру')
    if not 0 < len(text) < width-4:
        raise Exception(f'Text - {text} длиннее ширины - {width}')
    if high < 3:
        raise Exception(f'Высота должна быть больше 3')
    if not 0 < len(text) < 120:
        raise Exception('Текст слишком длинный, длина должна быть от 1 до 120')

    print('#' * width)
    for i in range(high - 2):
        if i == int((high - 2) / 2):
            print('#' + calc_space(width=width, text=text) + '#')
        else:
            print('#' + ' ' * (width - 2) + '#')
    print('#' * width)


print_in_box('hello, fgtj7 dfhdhj!', 27, 9)
