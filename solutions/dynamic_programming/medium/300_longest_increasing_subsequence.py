from typing import List

# Given an integer array nums, return the length of the longest strictly increasing subsequence. A subsequence
# is a sequence that can be derived from an array by deleting some or no elements without changing the order
# of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4



def length_of_LIS(nums: List[int]) -> int:
    result, dp = 0, [0] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        dp[i] = 1 + max([dp[j] for j in range(i + 1, len(nums)) if nums[j] > nums[i]], default=0)
        result = max(result, dp[i])
    return result
