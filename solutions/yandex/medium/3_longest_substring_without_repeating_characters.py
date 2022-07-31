def lengthOfLongestSubstring(s: str) -> int:
    result = 0
    chars = {}
    prev = -1
    for i, c in enumerate(s):
        if c in chars and chars[c] > prev:
            result = max(result, i - 1 - prev)
            prev = chars[c]
        chars[c] = i
    return max(result, len(s) - 1 - prev)
