"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.
"""

class Solution:
    def threeSum(self, nums: list) -> list:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            left_p = i + 1
            right_p = len(nums) - 1
            while right_p > left_p:
                if left_p > i + 1 and nums[left_p] == nums[left_p - 1]:
                    left_p += 1
                    continue
                if right_p < len(nums) - 1 and nums[right_p] == nums[right_p + 1]:
                    right_p -= 1
                    continue
                left_v = nums[left_p]
                right_v = nums[right_p]
                if left_v + right_v == - nums[i]:
                    res.append([nums[i], left_v, right_v])
                    left_p += 1
                    right_p -= 1
                if left_v + right_v < -nums[i]:
                    left_p += 1
                if left_v + right_v > -nums[i]:
                    right_p -= 1
        return res






