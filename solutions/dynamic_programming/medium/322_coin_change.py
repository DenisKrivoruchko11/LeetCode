from itertools import product
from math import inf
from queue import Queue
from typing import List

# You are given an integer array coins representing coins of different denominations and an
# integer amount representing a total amount of money. Return the fewest number of coins that
# you need to make up that amount. If that amount of money cannot be made up by any combination
# of the coins, return -1. You may assume that you have an infinite number of each kind of coin.
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4


def bfs_coin_change(coins: List[int], amount: int) -> int:
    q, vals = Queue(), set()
    q.put((0, 0))
    while not q.empty():
        value, count = q.get()
        if value == amount:
            return count
        else:
            for coin in coins:
                if value + coin <= amount and value + coin not in vals:
                    q.put((value + coin, count + 1))
                    vals.add(value + coin)
    return -1


def dp_coin_change(coins: List[int], amount: int) -> int:
    dp = [[0 if j == 0 else inf for j in range(amount + 1)] for _ in range(len(coins) + 1)]
    for (i, coin), j in product(enumerate(coins), range(amount)):
        dp[i + 1][j + 1] = dp[i][j + 1] if j + 1 < coin else min(1 + dp[i + 1][j + 1 - coin], dp[i][j + 1])
    return -1 if dp[-1][-1] == inf else dp[-1][-1]
