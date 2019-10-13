"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

class Solution:
    def generateParenthesis(self, n: int) -> list:
        res = []
        self.helper('', res, 0, 0, n)
        return res

    def helper(self, cur, res, left, right, n):
        if right == n:
            res.append(cur)
        elif left - right >= 0:
            self.helper(cur + "(", res, left + 1, right, n)
            self.helper(cur + ')', res, left, right + 1, n)
        else:
            return

