def num_decodings(s: str) -> int:
    result = 1
    for c in s[:-1]:
        if c ==