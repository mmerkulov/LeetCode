# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

strs = ["flower", "flow", "flight"]
reference_word = strs[0]
prefix = []
prefix1 = []
for word in strs[1:]:
    for idx, x in enumerate(word):  # x = f , l , o , w ;; f, l , i , g , h , t
        if reference_word[idx] == x:
            prefix.append(x)

print(prefix)
prefix1 = [x for x in prefix if prefix.count(x) > 1 and x not in prefix1]
print(prefix1)