from typing import Tuple


def update(num_int: int, num_str: str, cur_int: int, cur_str: str) -> Tuple[int, str]:
    return num_int % cur_int, num_str + cur_str * (num_int // cur_int)


def intToRoman(num: int) -> str:
    d = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

    result = ''
    for k in sorted(d.keys(), reverse=True):
        num, result = update(num, result, k, d[k])
        cur = k // 5 if k // 5 in d else k // 10
        if cur in d:
            num, result = update(num, result, k - cur, d[cur] + d[k])

    return result
