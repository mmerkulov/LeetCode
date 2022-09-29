# Given two binary strings a and b, return their sum as a binary string.
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

def sum_two_bin(a, b):
    if len(a) > len(b):
        smaller_num = b
    else:
        smaller_num = a

    a = a[::-1]
    b = b[::-1]
    c = []
    print(a)
    print(b)
    for idx, val in enumerate(smaller_num):
        # print(a[idx], b[idx])
        c.append(1 if int(a[idx]) + int(b[idx]) >= 1 else 0)


    print(c)

a = '1010'
b = '110'
# НЕ СДЕЛАЛ
#sum_two_bin(a, b)
