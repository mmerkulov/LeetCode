def removeElement(nums: list, val: int) -> int:
    return len([x for x in nums if x != val])


nums = [0,1,2,2,3,0,4,2]
val = 2

print(removeElement(nums, val))
# не доделано