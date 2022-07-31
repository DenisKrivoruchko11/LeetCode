from collections import deque
from typing import List, Callable


def bfs(g, colors, color, v):
    q = deque()
    q.append(v)
    colors[v] = color
    while q:
        for w in g[q.popleft()]:
            if not colors[w]:
                q.append(w)
                colors[w] = color


def dfs(g, colors, color, v):
    colors[v] = color
    for w in g[v]:
        if not colors[w]:
            dfs(g, colors, color, w)


def get_components(g: List[List[int]], paint: Callable) -> List[int]:
    colors = [0] * len(g)
    color = 1
    for v in range(len(g)):
        if not colors[v]:
            paint(g, colors, color, v)
            color += 1
    return colors
