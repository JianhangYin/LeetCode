"""
Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(len(num1)):
            temp = 0
            for j in range(len(num2)):
                temp += num1[i] * num2[j] * 10 ** (i + j)
            res += temp
        return str(res)

