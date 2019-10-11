"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        temp = [n]
        while n != 1:
            n = self.helper(n)
            if n in temp:
                return False
            else:
                temp.append(n)
        return True

    def helper(self, n):
        res = 0
        for item in str(n):
            res += int(item) ** 2
        return res


