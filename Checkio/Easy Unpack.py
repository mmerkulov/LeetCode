def easy_unpack(data: tuple) -> tuple:
    result = (data[0], data[2], data[-2])
    print(result)
    return result

x = (1, 2, 3, 4, 5, 6, 7, 9)
x = (6, 3, 7)
easy_unpack(data=x)