"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
"""


class Solution:
    def convertToTitle(self, n: int) -> str:
        res = []
        while n > 0:
            if n == 26:
                res.append('Z')
                break
            res.append(chr(n % 26 + 64))
            n = n // 26
        return ''.join(res[::-1])
