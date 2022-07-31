from typing import List, Tuple


def dfs(g: List[List[int]], colors: List[int], result: List[int], v: int) -> bool:
    colors[v] = 1
    for w in g[v]:
        if colors[w] == 0 and not dfs(g, colors, result, w) or colors[w] == 1:
            return False
    colors[v] = 2
    result.append(v)
    return True


def top_sort(g: List[List[int]]) -> Tuple[bool, List[int]]:
    colors = [0] * len(g)
    result = []
    for v in range(len(g)):
        if not colors[v] and not dfs(g, colors, result, v):
            return False, []
    result.reverse()
    return True, result
