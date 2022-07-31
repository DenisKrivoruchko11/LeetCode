from typing import List

# You are given a sorted unique integer array nums.
# A range [a,b] is the set of all integers from a to b (inclusive).
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
# That is, each element of nums is covered by exactly one of the ranges,
# and there is no integer x such that x is in one of the ranges but not in nums.
# Each range [a,b] in the list should be output as: "a->b" if a != b
#                                                   "a"    if a == b
# 0 <= nums.length <= 20
# -231 <= nums[i] <= 231 - 1
# All the values of nums are unique.
# nums is sorted in ascending order.


def summary_ranges(nums: List[int]) -> List[str]:
    if not nums:
        return []

    result, left = [], 0
    for right in range(1, len(nums)):
        if nums[right] != nums[right - 1] + 1:
            result.append(f'{nums[left]}->{nums[right - 1]}' if left != right - 1 else f'{nums[left]}')
            left = right
    result.append(f'{nums[left]}->{nums[len(nums) - 1]}' if left != len(nums) - 1 else f'{nums[left]}')

    return result
