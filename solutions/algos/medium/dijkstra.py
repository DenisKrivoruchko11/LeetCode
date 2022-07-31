from math import inf
from typing import List, Tuple


def dijkstra(g: List[List[Tuple[int, float]]], src: int) -> List[float]:
    used = [False] * len(g)
    dists = [inf] * len(g)
    dists[src] = 0
    front = {src}
    v = src
    while v != -1:
        used[v] = True
        front.remove(v)
        for w, e in g[v]:
            if not used[w]:
                dists[w] = min(dists[w], dists[v] + e)
                front.add(w)
        v = min(front, key=lambda i: dists[i], default=-1)
    return dists


def dijkstra1(g: List[List[Tuple[int, float]]], src: int) -> List[float]:
    used = [False] * len(g)
    dists = [inf] * len(g)
    dists[src] = 0
    for _ in range(len(g)):
        v = min(range(len(g)), key=lambda i: dists[i])
        if dists[v] == inf:
            break
        used[v] = True

        for w, e in g[v]:
            dists[w] = min(dists[w], dists[v] + e)
    return dists
