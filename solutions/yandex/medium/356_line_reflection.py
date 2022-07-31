from typing import List

# Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points
# symmetrically, in other words, answer whether if there exists a line that after reflecting all points over
# the given line the set of the original points is the same that the reflected ones.
# Note that there can be repeated points.
# 1 <= points.length <= 10^4
# -10^8 <= points[i][j] <= 10^8


def isReflected(points: List[List[int]]) -> bool:
    ps = set([(x, y) for x, y in points])
    mid = (min(ps)[0] + max(ps)[0]) / 2
    return all((2 * mid - x, y) in ps for x, y in ps)
