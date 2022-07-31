from typing import List

# Given an integer array nums, find a contiguous non-empty subarray within the array that
# has the largest product, and return the product. The test cases are generated so that the
# answer will fit in a 32-bit integer. A subarray is a contiguous subsequence of the array.
# 1 <= nums.length <= 2 * 10^4
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


def max_product(nums: List[int]) -> int:
    max_p = min_p = r = nums[0]
    for n in nums[1:]:
        max_p, min_p = max(n, max_p * n, min_p * n), min(n, max_p * n, min_p * n)
        r = max(max_p, r)
    return r
