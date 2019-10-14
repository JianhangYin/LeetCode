"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.
"""


class Solution:
    def permuteUnique(self, nums: list) -> list:
        nums.sort()
        res = []
        self.helper(nums, res, [])
        return res

    def helper(self, nums, res, path):
        if not nums:
            res.append(path)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                self.helper(nums[:i] + nums[i + 1:], res, path + [nums[i]])

