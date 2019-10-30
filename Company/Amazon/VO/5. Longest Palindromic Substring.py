"""
This question is very hard for me.
There are two ways to complete this question.
1. Dynamic programming
2. Center searching
"""
class Solution:
    def longestPalindromeDP(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        start_lpd = 0
        end_lpd = 0
        for i in range(len(s)):
            start = i
            end = i
            while start >= 0:
                if start == end:
                    dp[start][end] = True
                elif start + 1 == end:
                    dp[start][end] = s[start] == s[end]
                else:
                    dp[start][end] = dp[start + 1][end - 1] and (s[start] == s[end])
                if dp[start][end] and (end - start + 1) > (end_lpd - start_lpd + 1):
                    start_lpd = start
                    end_lpd = end
                start = start - 1

        return s[start_lpd:end_lpd + 1]

    def longestPalindrome(self, s: str) -> str:
        def helper(str, l, r):
            while l >= 0 and r < len(str) and str[l] == str[r]:
                l -= 1
                r += 1
            return str[l + 1: r]
        res = ''
        for i in range(len(s)):
            even_s = helper(s, i, i + 1)
            odd_s = helper(s, i, i)
            if len(res) < len(even_s):
                res = even_s
            if len(res) < len(odd_s):
                res = odd_s
        return res