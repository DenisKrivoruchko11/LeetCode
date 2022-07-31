from collections import deque
from typing import List


def bfs(g: List[List[int]], start: int) -> List[int]:
    d = [-1] * len(g)
    d[start] = 0

    q = deque()
    q.append(start)

    while q:
        v = q.popleft()
        for w in g[v]:
            if d[w] == -1:
                d[w] = d[v] + 1
                q.append(w)
    return d
