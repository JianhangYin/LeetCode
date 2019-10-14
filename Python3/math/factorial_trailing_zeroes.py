"""
Given an integer n, return the number of trailing zeroes in n!.
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        m = 0
        while 5 ** m <= n:
            m += 1
            res += n // 5 ** m
        return res