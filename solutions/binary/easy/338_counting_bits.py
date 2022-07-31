from typing import List

# Given an integer n, return an array ans of length n + 1 such that for each i
# (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
# 0 <= n <= 10^5


def count_bits(n: int) -> List[int]:
    result, k = [0], 0
    for i in range(1, n + 1):
        if i == 2 ** k:
            result.append(1)
            k += 1
        else:
            result.append(1 + result[int(i - 2 ** (k - 1))])
    return result
