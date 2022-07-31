from typing import List

# Given an array of integers nums and an integer target, return indices of the two numbers such
# that they add up to target. You may assume that each input would have exactly one solution,
# and you may not use the same element twice. You can return the answer in any order.
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.


def twoSum(nums: List[int], target: int) -> List[int]:
    d = {}
    for i, v in enumerate(nums):
        if target - v in d:
            return [d[target - v], i]
        else:
            d[v] = i
