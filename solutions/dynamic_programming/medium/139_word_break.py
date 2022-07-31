from queue import Queue
from typing import List

# Given a string s and a dictionary of strings wordDict, return true if s can be
# segmented into a space-separated sequence of one or more dictionary words. Note
# that the same word in the dictionary may be reused multiple times in the segmentation.
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.


def word_break(s: str, word_dict: List[str]) -> bool:
    q, vals = Queue(), {s}
    q.put(s)
    while not q.empty():
        cur = q.get()
        for w in word_dict:
            if w == cur[:len(w)]:
                if len(w) == len(cur):
                    return True
                elif cur[len(w):] not in vals:
                    vals.add(cur[len(w):])
                    q.put(cur[len(w):])
    return False
