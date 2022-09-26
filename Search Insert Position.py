# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2
#
# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1
#
# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

def search_position(nums, target):
    last_val = nums[-1]
    if last_val < target:
        return len(nums)

    first_val = nums[0]
    if first_val >= target:
        return 0

    # идём не с первого значения, так как первое мы уже проверили выше
    # и по этому не нужно его проверять в цикле
    for idx, n in enumerate(nums[1:]):
        # всё равно начинается с 0, по этому нужно будет помнить, что idx = idx + 1
        print(n, target)
        if target == n:
            return idx + 1
        if target < n:
            return idx + 1


list1 = [1, 3]
target = 2
print(search_position(list1, target))
