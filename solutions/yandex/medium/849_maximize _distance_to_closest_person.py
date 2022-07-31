from typing import List


# You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat,
# and seats[i] = 0 represents that the ith seat is empty (0-indexed). There is at least one empty seat, and at least
# one person sitting. Alex wants to sit in the seat such that the distance between him and the closest person to him
# is maximized. Return that maximum distance to the closest person.
# 2 <= seats.length <= 2 * 10^4
# seats[i] is 0 or 1.
# At least one seat is empty.
# At least one seat is occupied.


def max_dist_to_closest(seats: List[int]) -> int:
    result = prev = -1
    for i in range(len(seats)):
        if seats[i]:
            result = i if prev == -1 else max(result, (i - prev) // 2)
            prev = i
    return max(result, len(seats) - 1 - prev)
