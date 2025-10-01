from typing import List


def single_number(nums: List[int]) -> int:
    result = {}
    for i in nums:
        if result.get(i, None):
            result[i] += 1
        else:
            result[i] = 1
    for i, k in result.items():
        if k == 1:
            return i


nums = [2, 2, 1, 3, 3, 4, 4, 1, 5]
print(single_number(nums=nums))
