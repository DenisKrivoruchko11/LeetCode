from itertools import product
from typing import List

# Given two 1d vectors, implement an iterator to return their elements alternately.For example, given two 1d vectors:
# v1 = [1, 2]
# v2 = [3, 4, 5, 6]
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be:
# [1, 3, 2, 4, 5, 6].
# Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?


# For k lists
class ZigzagIterator:
    def __init__(self, vs: List[List[int]]):
        self.vs = [row[column] for column, row in product(range(len(max(vs, key=len))), vs) if len(row) > column]
        self.index = -1

    def next(self) -> int:
        self.index = (self.index + 1) % len(self.vs)
        return self.vs[self.index]

    def hasNext(self) -> bool:
        return self.index != len(self.vs) - 1
