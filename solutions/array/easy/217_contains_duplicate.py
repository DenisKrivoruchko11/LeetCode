from typing import List

# Given an integer array nums, return true if any value appears at least
# twice in the array, and return false if every element is distinct.
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9


def contains_duplicate(nums: List[int]) -> bool:
    return len(nums) == len(set(nums))
