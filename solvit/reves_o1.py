def revers_array(s: list[str])-> None:
    start, end = 0, len(s) - 1
    print(s)
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    print(s)


s = ['w', 'o', 'r', 'd', 'EEE']
revers_array(s)