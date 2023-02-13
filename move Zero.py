from typing import List


def moveZero(nums: List[int]) -> None:
    zero_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:            # т.к. мы ищем не нулевые значения,
            # то смещение идёт
            nums[i], nums[zero_pos] = nums[zero_pos], nums[i]
            zero_pos += 1


nums = [0, 1, 0, 3, 12]
moveZero(nums)
print(nums)