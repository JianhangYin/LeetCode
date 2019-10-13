"""
Given an array nums of n integers and an integer target,
are there elements a, b, c, and d in nums such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.
"""


class Solution:
    def fourSum(self, nums: list, target: int) -> list:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                p_1 = j + 1
                p_2 = len(nums) - 1
                while p_2 > p_1:
                    sum = nums[i] + nums[j] + nums[p_1] + nums[p_2]
                    if p_1 > j + 1 and nums[p_1] == nums[p_1 - 1]:
                        p_1 += 1
                        continue
                    if p_2 < len(nums) - 1 and nums[p_2] == nums[p_2 + 1]:
                        p_2 -= 1
                        continue
                    if sum < target:
                        p_1 += 1
                    elif sum > target:
                        p_2 -= 1
                    else:
                        res.append([nums[i], nums[j], nums[p_1], nums[p_2]])
                        p_1 += 1
                        p_2 -= 1
        return res

