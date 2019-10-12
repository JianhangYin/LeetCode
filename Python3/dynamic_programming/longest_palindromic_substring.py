"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
"""

class Solution:
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


