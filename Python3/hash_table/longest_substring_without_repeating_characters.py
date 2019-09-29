"""
Given a string, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashed = {}
        start = 0
        max_length = 0
        for i, item in enumerate(s):
            if item in hashed and hashed[item] >= start:
                start = hashed[item] + 1
            else:
                max_length = max(max_length, i - start + 1)
            hashed[item] = i
        return max_length

