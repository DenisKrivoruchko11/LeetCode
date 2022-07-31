def gcd(a: int, b: int):
    if a < b:
        return gcd(b, a)

    return gcd(b, a % b) if b != 0 else a
