"""
Given a collection of distinct integers, return all possible permutations.
"""


class Solution:
    def permute(self, nums: list) -> list:
        res = []
        self.helper(nums, res, [])
        return res

    def helper(self, nums, res, path):
        if not nums:
            res.append(path)
            return
        for i in range(len(nums)):
            self.helper(nums[:i] + nums[i + 1:], res, path + nums[i])

