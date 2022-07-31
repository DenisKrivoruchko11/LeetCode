from typing import List

# You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [start[i], end[i]]
# and secondList[j] = [start[j], end[j]]. Each list of intervals is pairwise disjoint and in sorted order. Return
# the intersection of these two interval lists. A closed interval [a, b] (with a <= b) denotes the set of real
# numbers x with a <= x <= b. The intersection of two closed intervals is a set of real numbers that are either
# empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].
# 0 <= firstList.length, secondList.length <= 1000
# firstList.length + secondList.length >= 1
# 0 <= start[i] < end[i] <= 10^9
# end[i] < start[i+1]
# 0 <= start[j] < end[j] <= 10^9
# end[j] < start[j+1]


def interval_intersection(first_list: List[List[int]], second_list: List[List[int]]) -> List[List[int]]:
    result, i, j = [], 0, 0
    while i < len(first_list) and j < len(second_list):
        fst, snd = first_list[i], second_list[j]
        left, right = max(fst[0], snd[0]), min(fst[1], snd[1])
        if left <= right:
            result.append([left, right])
        if fst[1] > snd[1]:
            j += 1
        else:
            i += 1
    return result
