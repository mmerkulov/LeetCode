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


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    dummyNode = ListNode(-1)
    temp = dummyNode

    curr = head
    while curr:

        if curr.val != temp.val:
            temp.next = curr
            temp = temp.next
        curr = curr.next

    temp.next = None
    return dummyNode.next

def delete_duplicates_deepseek(head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next  # Пропускаем дубликат
        else:
            curr = curr.next  # Переходим к следующему только если нет дубликата
    return head


list2 = ListNode(val=1, next=ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=3, next=None)))))
list1 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=3, next=None)))
list3 = ListNode(val=-1, next=ListNode(val=0, next=ListNode(val=0, next=ListNode(val=0, next=ListNode(val=3, next=ListNode(val=3, next=None))))))
print_llist(delete_duplicates(list3))
print_llist(delete_duplicates_deepseek(list3))