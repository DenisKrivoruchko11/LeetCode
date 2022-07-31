from typing import Optional


class Node:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_sum(head: Optional[Node]):
    if not head:
        return 0
    elif not head.left and not head.right:
        return head.val
    else:
        return get_sum(head.left) + get_sum(head.right)
