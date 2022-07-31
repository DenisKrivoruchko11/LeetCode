from typing import List

# Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.


def find_max(nums: List[int]) -> int:
    start = left = result = 0
    for i in range(len(nums)):
        if not nums[i]:
            right = i - start
            result = max(result, left + 1 + right)
            left = right
            start = i + 1

    return max(result, left + 1 + len(nums) - max(start, 1))
