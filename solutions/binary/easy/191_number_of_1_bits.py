# Write a function that takes an unsigned integer and returns the
# number of '1' bits it has (also known as the Hamming weight).
# The input must be a binary string of length 32.


def hamming_weight(n: int) -> int:
    result = k = 0
    while 2 ** k <= n:
        if 2 ** k & n == 2 ** k:
            result += 1
        k += 1
    return result
