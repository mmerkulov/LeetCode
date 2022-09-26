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
def stack_method(text, moder_dict_bracket=None):
    stack_list = []
    for letter in text:
        if letter in ['(', '[', '{']:
            stack_list.append(letter)
        elif letter in [')', ']', '}']:  # x - последний элемент положенный сюда
            if not stack_list:
                return False
            last_item = stack_list.pop()
            if last_item == '(' and letter == ')':
                continue
            if last_item == '[' and letter == ']':
                continue
            if last_item == '{' and letter == '}':
                continue
            return False
    if stack_list:
        return False
    else:
        return True


# text = '(])' # False
# text = '()[' # False
# text = '([)]' # False
text = '()'  # False
# print(modern_dict_bracket)
# print(stupid_method_calculate_brackets(text, modern_dict_bracket))
# print(normal_method(text))
print(stack_method(text))
