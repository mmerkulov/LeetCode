def is_valid_password(password: str) -> bool:
    if len(password) < 8:
        # длина
        return False
    if not any(i.isupper() for i in password):
        # существует Заглавная
        return False
    if password.lower() == password[::-1].lower():
        # не полиндром в любом регистре
        return False
    if not any(i.isdigit() for i in password):
        # есть хотя б 1 цифра
        return False
    special_chars = {'_', '#', '%'}
    if not any(char in special_chars for char in password):
        # есть хотя бы 1 спец. символ
        return False
    return True


x = 'Rewqa1_1aqwer'
print(is_valid_password(x))
