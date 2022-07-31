from functools import reduce
from typing import List, Optional

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 10^4


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    vals = []
    for i in range(len(lists)):
        while lists[i]:
            vals.append(lists[i].val)
            lists[i] = lists[i].next
    return reduce(lambda r, v: ListNode(v, r), sorted(vals, reverse=True), None)
