# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common
# subsequence, return 0. A subsequence of a string is a new string generated from the original string with some
# characters (can be none) deleted without changing the relative order of the remaining characters. For example, "ace"
# is a subsequence of "abcde". A common subsequence of two strings is a subsequence that is common to both strings.
# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.


def longest_common_subsequence(text1: str, text2: str) -> int:
    dp = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]
    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            dp[i][j] = 1 + dp[i + 1][j + 1] if text1[i] == text2[j] else max(dp[i + 1][j], dp[i][j + 1])
    return dp[0][0]
