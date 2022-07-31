from typing import List

# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum. A subarray is a contiguous part of an array.
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4


def max_subarray(nums: List[int]) -> int:
    result = nums[0]
    for i in range(1, len(nums)):
        nums[i] += max(nums[i - 1], 0)
        result = max(result, nums[i])
    return result
