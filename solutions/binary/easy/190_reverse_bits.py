def reverse_bits(n: int) -> int:
    result = 0
    for k in range(32):
        if n & 2 ** k:
            result |= 2 ** (31 - k)
    return result
