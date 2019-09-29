"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
"""

class Solution:
    def singleNumber(self, nums: list) -> int:
        hashed = {}
        for item in nums:
            if item in hashed:
                hashed[item] = False
            else:
                hashed[item] = True
        for key, value in hashed.items():
            if value:
                return key

