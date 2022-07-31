from typing import List


def get_len_of_max_unique(arr: List[int]):
    result = 0
    left = 0
    d = {}
    for i in range(len(arr)):
        if arr[i] in d and d[arr[i]] >= left:
            result = max(result, i - left)
            left = d[arr[i]] + 1
            d[arr[i]] = i
    return max(result, len(arr) - left)
