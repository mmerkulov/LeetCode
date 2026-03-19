def parser_my(txt:str):
    result = {}
    a = txt.split('\n')
    for i, v in enumerate(a):
        if not v.startswith(':'):
            a[i-1] = a[i-1] + ' ' + a[i]
            a.pop(i)
    for i in a:
        first_idx = i.find(":")
        second_idx =  i.find(":", 1)
        key = i[first_idx + 1: second_idx]
        val = i[second_idx+1:]
        result[key] = val
    return result

def parse_swift(text: str) -> dict:
    """
    Парсит текст в формате SWIFT, где каждая запись начинается с :код:,
    а значение может продолжаться на следующих строках.
    Возвращает словарь {код: значение} (значения объединены пробелами).
    """
    lines = text.splitlines()
    result = {}
    current_key = None
    current_value_parts = []

    for line in lines:
        line = line.rstrip('\n')
        if line.startswith(':'):
            # Если уже был начат предыдущий ключ — сохраняем его
            if current_key is not None:
                result[current_key] = ' '.join(current_value_parts).strip()

            # Парсим новый ключ и начало значения
            # Разделяем строку максимум на 3 части: ['', ключ, значение_после_второго_двоеточия]
            parts = line.split(':', 2)
            if len(parts) >= 2:
                current_key = parts[1]
                # Значение после второго двоеточия (если есть)
                if len(parts) == 3 and parts[2]:
                    current_value_parts = [parts[2]]
                else:
                    current_value_parts = []
            else:
                # Некорректная строка – сбрасываем состояние
                current_key = None
                current_value_parts = []
        else:
            # Строка продолжения значения (не начинается с ':')
            if current_key is not None and line:
                current_value_parts.append(line)

    # После цикла сохраняем последний ключ, если он был
    if current_key is not None:
        result[current_key] = ' '.join(current_value_parts).strip()

    return result


text = """:15A:
:20:1032
:22A:NEWT
:22B:CONF
:22C:AGRO310001RUAGMM
:82A:RUAGRUMMXXX
:87A:AGROPR31000
:77D:27-0-22/69-2020 26.03.2020
:15B:
:17R:B
:30T:20250922
:30V:20250922
:30P:20250923
:32B:USD1000000,
:30X:20250923
:34E:USD27397,26
:37G:1000,
:14D:ACT/365
:15C:
:57D:ACC YOUR INSTRUCTION
RUAGRUMMXXX
:15D:
:57A:/301
AGROPR31000
:15E:
:57D:ACC YOUR INSTRUCTION
RUAGRUMMXXX"""

print(parser_my(text))
print(parse_swift(text))
