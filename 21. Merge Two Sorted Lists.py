from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_llist(head):
    curr = head

    while curr:
        if not curr.next:
            print(curr.val)
        else:
            print(curr.val, end=" --> ")
        curr = curr.next


def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummyNode = ListNode(-1)
    temp = dummyNode

    curr1, curr2 = list1, list2

    while curr1 and curr2:
        if curr1.val < curr2.val:
            temp.next = curr1
            curr1 = curr1.next
        else:
            temp.next = curr2
            curr2 = curr2.next
        temp = temp.next

    # Attach the remaining nodes
    temp.next = curr1 if curr1 else curr2
    return dummyNode.next


# list1 = [1, 2, 3]
list1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=None)))
# list2 = [1, 3, 4]
list2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4, next=None)))

# a = mergeTwoLists(list1, list2)


print_llist(mergeTwoLists(list1, list2))
