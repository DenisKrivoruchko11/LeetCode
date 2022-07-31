# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
# non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters
# and numbers. Given a string s, return true if it is a palindrome, or false otherwise.
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.

def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isdigit() and not s[left].isalpha():
            left += 1
            continue
        if not s[right].isdigit() and not s[right].isalpha():
            right -= 1
            continue
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
