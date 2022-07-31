from typing import List

# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.
# n == nums.length
# 1 <= n <= 10^4
# 0 <= nums[i] <= n
# All the numbers of nums are unique.


def missing_number(nums: List[int]) -> int:
    return len(nums) * (len(nums) - 1) // 2 - sum(nums)
