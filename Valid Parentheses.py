# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
#   Open brackets must be closed by the same type of brackets.
#   Open brackets must be closed in the correct order.
#   Every close bracket has a corresponding open bracket of the same type.
# Example 1:
# Input: s = "()"
# Output: true
#
# Example 2:
# Input: s = "()[]{}"
# Output: true
#
# Example 3:
# Input: s = "(]"
# Output: false


def stupid_method_calculate_brackets(text, current_dict):
    for letter in text:
        if letter == '(':
            modern_dict_bracket['('] = modern_dict_bracket['('] + 1
        if letter == ')':
            modern_dict_bracket[')'] = modern_dict_bracket[')'] + 1
        if letter == ']':
            modern_dict_bracket[']'] = modern_dict_bracket[']'] + 1
        if letter == '[':
            modern_dict_bracket['['] = modern_dict_bracket['['] + 1
        if letter == '{':
            modern_dict_bracket['{'] = modern_dict_bracket['{'] + 1
        if letter == '}':
            modern_dict_bracket['}'] = modern_dict_bracket['}'] + 1

    if modern_dict_bracket['('] == modern_dict_bracket[')']:
        if modern_dict_bracket['['] == modern_dict_bracket[']']:
            if modern_dict_bracket['{'] == modern_dict_bracket['}']:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def normal_method(text, moder_dict_bracket=None):
    amount_brackets = 0

    for idx, letter in enumerate(text):  # как-то до ПРЕДПОСЛЕДНЕГО нужно идти
        # открывашки
        if letter not in ['(', '[', '{'] and idx == 0:
            return False

        # логика
        # если latter = (, то следующий должен быть )
        # если latter = [, то следующий должен быть ]
        # если latter = {, то следующий должен быть }
        if letter == ')' and text[idx - 1] == '(':
            amount_brackets -= 1
        elif letter == ']' and text[idx - 1] == '[':
            amount_brackets -= 1
        elif letter == '}' and text[idx - 1] == '{':
            amount_brackets -= 1
        else:
            amount_brackets += 1
            continue

    if amount_brackets != 0:
        return False
    else:
        return True


modern_dict_bracket = {'(': 0, ')': 0, '[': 0, ']': 0, '{': 0, '}': 0}
list_bracket = [['(', ')'], ['[', ']'], ['{', '}']]
text = '(]'
print(modern_dict_bracket)
# print(stupid_method_calculate_brackets(text, modern_dict_bracket))
print(normal_method(text))
