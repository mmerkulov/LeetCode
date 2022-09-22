# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.
#
# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Решение №1 через преобразование числа в строку, типа ревер сделали
def check_polindrom_1(s='121'):
    revers_s = s[::-1]
    if s == revers_s:
        return True
    else:
        return False


# Решение через число
def check_polindrom_2(s=123):
    x, y = s, 0
    f = lambda: (y * 10) + x % 10
    while x > 0:
        x, y = x // 10, f()
    return y == s


print(check_polindrom_2(123454321))
