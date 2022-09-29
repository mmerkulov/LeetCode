# Given a non-negative integer x, compute and return the square root of x.
# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
# Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
# Example 1:
# Input: x = 4
# Output: 2
#
# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.



# 1. Разбить число на десятки с права на лево
# 2. Для самого левого значения найти квадрат числа, т.е. число может быть от 1 до 99 и его возводим в квадрат
# 3. Находим два числа x, x+1 где число самое левое входит в этот промежуток между x^2 и (x+1)^2
# 4. Найденное число это первая цифра ответа


s = 'iamstring'

a = s[3:5:1]
print(a)







