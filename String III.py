print('*' * 10)
s = "Let's take LeetCode contest"
list_words = s.split(' ')
result = []
for word in list_words:
    result.append(word[::-1])
print(' '.join(result))
