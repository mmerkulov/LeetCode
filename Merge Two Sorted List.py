# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

list1 = [1, 2, 4]
list2 = [2, 3, 4, 5]


def merge_lists(list1, list2):
    result = []

    l1 = len(list1)
    l2 = len(list2)

    for x in list1:
        result.append(x)
    for x in list2:
        result.append(x)

    result.sort()

    print(result)
    return result


merge_lists(list1, list2)
