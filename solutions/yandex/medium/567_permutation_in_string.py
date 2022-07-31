from collections import defaultdict
from typing import Dict, Iterable


# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.
# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.


def update(d: Dict, pairs: Iterable, check=False) -> bool:
    for c1, c2 in pairs:
        d[c1] += 1
        d[c2] -= 1
        if d[c1] == 0:
            d.pop(c1)
        if d[c2] == 0:
            d.pop(c2)
        if check and len(d) == 0:
            return True
    return len(d) == 0


def check_inclusion(s1: str, s2: str) -> bool:
    d = defaultdict(int)
    return len(s1) <= len(s2) and (update(d, zip(s1, s2)) or update(d, zip(s2, s2[len(s1):]), True))
