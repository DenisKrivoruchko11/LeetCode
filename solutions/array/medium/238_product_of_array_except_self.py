from typing import List

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the
# elements of nums except nums[i]. The product of any prefix or suffix of nums is guaranteed to fit in a
# 32-bit integer. You must write an algorithm that runs in O(n) time and without using the division operation.
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


def product_except_self(nums: List[int]) -> List[int]:
    result = []
    p = 1
    for num in nums:
        result.append(p)
        p *= num
    p = 1
    for i in range(len(nums)):
        result[-i - 1] *= p
        p *= nums[-i - 1]
    return result
