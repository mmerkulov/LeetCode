# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
#
# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
#
# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6

def get_last_word(s):
    s = s.split()
    if not s:
        return 0
    s = s.pop()
    return len(s)


def custom_get_last_word(s):
    if len(s) <= 0:
        return 0

    if not s.replace(' ', ''):
        return 0

    if ' ' not in s:
        return len(s)

    s = s[::-1]
    s = s.lstrip()
    idx = s.find(' ')
    if idx == -1:
        return len(s)

    return idx

def lengthOfLastWord(s: str) -> int:
    word_list = s.split()
    result = len(word_list[0])
    for x in word_list:
        if len(x) > result:
            result = len(x)
    return result

s = "luffy is still  joyboy "
s = "Hello World"
# s = '        )  '
# s = 'a '
# print(get_last_word(s))
# print(custom_get_last_word(s))
print(lengthOfLastWord(s))
