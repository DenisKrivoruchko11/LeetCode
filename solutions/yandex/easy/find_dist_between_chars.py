from math import inf


def find_dist(s: str, c1='X', c2='Y'):
    x = y = inf
    result = inf
    for i, c in enumerate(s):
        if c == c1:
            x = i
        if c == c2:
            y = i
        result = min(result, abs(x - y))
    return result
