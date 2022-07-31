from functools import reduce
from typing import List

# Given an array of distinct integers nums and a target integer target, return the number of possible combinations
# that add up to target. The test cases are generated so that the answer can fit in a 32-bit integer.
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 1000
# All the elements of nums are unique.
# 1 <= target <= 1000


def combination_sum_4(nums: List[int], target: int) -> int:
    return reduce(lambda dp, v: dp + [sum(dp[v - n] for n in nums if n <= v)], range(1, target + 1), [1])[-1]
