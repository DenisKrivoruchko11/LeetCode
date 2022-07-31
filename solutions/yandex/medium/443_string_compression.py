from typing import List

# Given an array of characters chars, compress it using the following algorithm:
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
#   If the group's length is 1, append the character to s.
#   Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars.
# Note that group lengths that are 10 or longer will be split into multiple characters in chars.
# After you are done modifying the input array, return the new length of the array.
# You must write an algorithm that uses only constant extra space.
# 1 <= chars.length <= 2000
# chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.


def write(chars: List[str], cur: str, index: int, count: int) -> int:
    chars[index] = cur
    index += 1
    if count > 1:
        for d in str(count):
            chars[index] = d
            index += 1
    return index


def compress(chars: List[str]) -> int:
    index, count = 0, 1
    for i in range(1, len(chars)):
        if chars[i] != chars[i - 1]:
            index = write(chars, chars[i - 1], index, count)
            count = 0
        count += 1
    return write(chars, chars[-1], index, count)
