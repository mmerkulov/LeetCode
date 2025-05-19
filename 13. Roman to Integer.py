class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        result = 0
        for idx in range(len(s) - 1):
            if roman_dict.get(s[idx]) < roman_dict.get(s[idx + 1]):
                result -= roman_dict.get(s[idx])
            else:
                result += roman_dict.get(s[idx])
        result += roman_dict.get(s[-1])
        return result


if __name__ == '__main__':
    e = Solution()
    s = 'MCMXCIV'
    print(e.romanToInt(s))

# s = 'asd'
# for i in range(len(s) - 1):
#     print(i, s[i], s[i + 1])
