from typing import Optional

# Given the head of a singly linked list, reverse the list, and return the reversed list.
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000


class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


def recursively_reverse_list(head: Optional[ListNode], prev=None) -> Optional[ListNode]:
    if not head:
        return None
    elif not head.next:
        return ListNode(head.val, prev)
    else:
        return recursively_reverse_list(head.next, ListNode(head.val, prev))


def iteratively_reverse_list(head: Optional[ListNode]):
    result = None
    cur = head
    while cur:
        result = ListNode(cur.val, result)
        cur = cur.next
    return result


