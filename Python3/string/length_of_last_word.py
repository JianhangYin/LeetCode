"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        len_x = 0
        for item in s[::-1].strip():
            if item.isspace():
                return len_x
            else:
                len_x += 1
        return len_x

