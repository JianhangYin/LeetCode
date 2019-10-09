"""
Given a 32-bit signed integer, reverse digits of an integer.
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            result = - int(str(x)[:0:-1])
        else:
            result = int(str(x)[::-1])
        if 2**31 > result >= - 2**31:
            return result
        else:
            return 0

