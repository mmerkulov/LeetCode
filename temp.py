def func2(n):
    return n[0] + func1(n)

def func1(n):
    a = n[0]

    for v in n:
        if a < v and v > 0:
            a = v
    return a


n = [10, 2, 15, 3]
n = [-3, -2, -1, -5]
print(func2(n))