# Given two strings s and t, determine if they are both one edit distance apart.
# There are 3 possiblities to satisify one edit distance apart:
#   Insert a character into s to get t
#   Delete a character from s to get t
#   Replace a character of s to get t


def is_one_edit_distance(s: str, t: str) -> bool:
    if len(s) < len(t):
        return is_one_edit_distance(t, s)
    if len(s) <= len(t) + 1:
        for i in range(len(t)):
            if s[i] != t[i]:
                return s[i + 1:] == (t[i + 1:] if len(s) == len(t) else t[i:])
    return len(s) == len(t) + 1
