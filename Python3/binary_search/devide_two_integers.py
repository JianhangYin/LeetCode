"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sig = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sig = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        return min(max(-2147483648, sig * self.helper(dividend, divisor)), 2147483648)

    def helper(self, dividend, divisor):
        if dividend == 0 or dividend < divisor:
            return 0
        sum = divisor
        res = 1
        while sum + sum <= dividend:
            sum += sum
            res += res
        return res + self.helper(dividend - sum, divisor)

