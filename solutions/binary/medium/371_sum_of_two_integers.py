# Given two integers a and b, return the sum of the two integers without using the operators + and -.
# -1000 <= a, b <= 1000


def get_sum(a: int, b: int) -> int:
    result = prev = 0
    for i in range(12):
        count = len([x for x in [a, b, prev] if x & 2 ** i == 2 ** i])
        if count % 2 == 1:
            result |= 2 ** i
        prev = 2 ** (i + 1) if count > 1 else 0
    return result | ~(2 ** 12 - 1) if result & 2 ** 11 == 2 ** 11 else result
