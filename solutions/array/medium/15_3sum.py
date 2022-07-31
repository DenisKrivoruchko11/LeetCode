from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    d = {num: i for i, num in enumerate(nums)}

    result = set()
    for i, n in enumerate(nums):
        for j, m in enumerate(nums[i + 1:], start=i + 1):
            if 0 - n - m in d and i != d[0 - n - m] != j:
                result.add(sorted((n, m, 0 - n - m)))

    return [list(e) for e in result]


if __name__ == '__main__':
    print(three_sum([0, 0]))
