import random


# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def search1(nums, target=0):
    index_answer = []
    for indx_i, i in enumerate(nums):
        for indx_j, j in enumerate(nums):
            if i + j == target and indx_i != indx_j and not index_answer:
                print(i, j)
                index_answer.append(indx_i)
                index_answer.append(indx_j)
                return index_answer


def search2(nums, target=0):
    low_idx, high_idx = 0, len(nums) - 1
    new_nums = nums.copy()
    new_nums.sort()
    while low_idx < high_idx:
        if new_nums[low_idx] + new_nums[high_idx] == target:
            idx1, idx2 = new_nums[low_idx], new_nums[high_idx]

            # нужно теперь найти index'ы значений в целевом списке
            idx1, idx2 = nums.index(idx1), nums.index(idx2)
            print(idx1, idx2)
            new_nums = []
            new_nums.append(idx1)
            new_nums.append(idx2)
            return new_nums

        if new_nums[low_idx] + new_nums[high_idx] < target:
            low_idx += 1
        else:
            high_idx -= 1
    print('Не нашлось значений')


nums = [2, 11, 7, 15, 3, 5, 14]
target = 17

print(f'nums = {nums}', f'target = {target}')

print(search1(nums, target))
# search2(nums, target)
