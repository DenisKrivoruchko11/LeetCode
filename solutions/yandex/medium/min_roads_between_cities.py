from math import inf
from queue import Queue
from typing import List


def bfs(n: int, g: List[List[int]], src: int, trg: int) -> int:
    dists = [-1] * n
    dists[src] = 0
    q = Queue()
    q.put(src)
    while not q.empty():
        v = q.get()
        if v == trg:
            return dists[v]
        for w in g[v]:
            if dists[w] == -1:
                dists[w] = dists[v] + 1
                q.put(w)
    return dists[trg]


def make_graph(n: int, cities: List[List[int]], k: int) -> List[List[int]]:
    g = [[] for _ in range(n)]
    for i in range(n):
        x1, y1 = cities[i]
        for j in range(i + 1, n):
            x2, y2 = cities[j]
            if abs(x1 - x2) + abs(y1 - y2) <= k:
                g[i].append(j)
                g[j].append(i)
    return g


def get_result(parents: List[int], src: int, trg: int) -> int:
    if src == trg:
        return 0
    elif parents[trg] == -1:
        return -1
    else:
        v = trg
        result = 1
        while parents[v] != src:
            v = parents[v]
            result += 1
        return result


def main():
    n = int(input())
    cities = [[int(c) for c in input().split(' ')] for _ in range(n)]
    k = int(input())
    src, trg = [int(c) - 1 for c in input().split(' ')]
    print(bfs(n, make_graph(n, cities, k), src, trg))
