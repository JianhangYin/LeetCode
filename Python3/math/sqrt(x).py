"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        y = x // 2
        while not (y**2 <= x and (y + 1)**2 > x):
            y = int(0.5 * y + x / (2 * y))
        return y

