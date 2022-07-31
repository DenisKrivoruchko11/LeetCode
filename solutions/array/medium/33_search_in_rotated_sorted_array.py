from typing import List

# There is an integer array nums sorted in ascending order (with distinct values). Prior to being passed
# to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that
# the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2]. Given the array
# nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1
# if it is not in nums. You must write an algorithm with O(log n) runtime complexity.
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -10^4 <= target <= 10^4


def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left < right - 1:
        middle = (left + right) // 2
        if nums[right] < nums[left] < nums[middle]:
            if target <= nums[right] or nums[middle] <= target:
                left = middle
            else:
                right = middle
        elif nums[middle] < nums[right] < nums[left]:
            if target <= nums[middle] or nums[left] <= target:
                right = middle
            else:
                left = middle
        else:
            if nums[left] < target <= nums[middle]:
                right = middle
            elif nums[middle] < target < nums[right]:
                left = middle
            else:
                break
    return left if nums[left] == target else right if nums[right] == target else -1
