from typing import List

# Given a binary array nums, you should delete one element from it.
# Return the size of the longest non-empty subarray containing only 1's in the resulting array.
# Return 0 if there is no such subarray.
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1


def longest_subarray(nums: List[int]) -> int:
    r = x = y = 0
    for n in nums:
        if not n:
            r, x, y = max(r, x + y), y, 0
        else:
            y += 1
    return min(max(r, x + y), len(nums) - 1)
