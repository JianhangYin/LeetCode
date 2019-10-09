"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_r = a[::-1]
        b_r = b[::-1]
        result = ''
        a_p = 0
        b_p = 0
        c = 0
        while a_p < len(a) or b_p < len(b):
            a_int = int(a_r[a_p]) if a_p < len(a) else 0
            b_int = int(b_r[b_p]) if b_p < len(b) else 0
            temp = a_int + b_int + c
            if temp < 2:
                result += str(temp)
                c = 0
            else:
                result += str(temp - 2)
                c = 1
            a_p += 1
            b_p += 1
        result += str(c) if c == 1 else ''
        return result[::-1]
