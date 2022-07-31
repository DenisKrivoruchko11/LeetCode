from typing import List

# Given two integer arrays startTime and endTime and given an integer queryTime. The ith student
# started doing their homework at the time startTime[i] and finished it at time endTime[i]. Return
# the number of students doing their homework at time queryTime. More formally, return the number
# of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.
# startTime.length == endTime.length
# 1 <= startTime.length <= 100
# 1 <= startTime[i] <= endTime[i] <= 1000
# 1 <= queryTime <= 1000


def busy_student(start_time: List[int], end_time: List[int], query_time: int) -> int:
    return sum(1 for s, e in zip(start_time, end_time) if s <= query_time <= e)
