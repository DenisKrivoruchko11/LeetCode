from typing import List


def max_area(height: List[int]) -> int:
    left, right, result = 0, len(height) - 1, 0
    while left < right:
        result = max(result, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return result
