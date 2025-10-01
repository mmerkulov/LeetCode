def is_palindrome(s: str) -> bool:
    # Напишите здесь свой код
    letter = ''.join([x for x in s if x.isalnum()]).lower()
    return letter == letter[::-1]
z = 'Race a car'
z = " "
z = 'A man, a plan, a canal: Panama'
print(is_palindrome(z))


# print(len(' '), len(' ' )%2)