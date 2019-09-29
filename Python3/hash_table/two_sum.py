"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""


class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        hashed = {}
        for i, item in enumerate(nums):
            if item in hashed:
                return [hashed[item], i]
            hashed[target - item] = i

