from itertools import product
from typing import List

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# 1 <= n <= 8


def generate_parenthesis(n: int) -> List[str]:
    result = []
    for c in range(n):
        for left, right in product(generate_parenthesis(c), generate_parenthesis(n - 1 - c)):
            result.append(f'({left}){right}')
    return [''] if n == 0 else result
