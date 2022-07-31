from typing import List


def dfs(g: List[List[int]], colors: List[int], v: int) -> bool:
    colors[v] = 1
    for w in g[v]:
        if colors[w] == 0 and dfs(g, colors, w) or colors[w] == 1:
            return True
    colors[v] = 2
    return False


def find_loop(g: List[List[int]]):
    colors = [0] * len(g)
    return any(dfs(g, colors, v) for v in range(len(g)))
