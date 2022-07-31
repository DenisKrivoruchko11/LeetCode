from queue import Queue
from typing import List

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the
# non-zero elements. Note that you must do this in-place without making a copy of the array.
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1


def move_zeroes(nums: List[int]) -> None:
    q = Queue()
    for i, n in enumerate(nums):
        if n == 0:
            q.put(i)
        elif not q.empty():
            nums[q.get()] = n
            nums[i] = 0
            q.put(i)
