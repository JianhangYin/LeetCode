"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0, 1, 2]
        if n < 3:
            return memo[n]
        for i in range(3, n + 1):
            memo.append(memo[i - 1] + memo[i - 2])
        return memo[n]
