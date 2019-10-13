"""
Given a column title as appear in an Excel sheet, return its corresponding column number.
"""


class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        count = 0
        for item in s[::-1]:
            res += (ord(item) - 64) * 26 ** count
            count += 1
        return res


