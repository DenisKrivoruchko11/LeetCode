from functools import reduce

# You are climbing a staircase. It takes n steps to reach the top. Each time you can
# either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# 1 <= n <= 45


def climb_stairs(n: int) -> int:
    return reduce(lambda p, _: (p[1], p[0] + p[1]), range(n), (0, 1))[1]
