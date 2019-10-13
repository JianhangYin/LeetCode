"""
Given an array nums of n integers and an integer target,
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.
"""


class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left_p = i + 1
            right_p = len(nums) - 1
            while right_p > left_p:
                if left_p > i + 1 and nums[left_p] == nums[left_p - 1]:
                    left_p += 1
                    continue
                if right_p < len(nums) - 1 and nums[right_p] == nums[right_p + 1]:
                    right_p -= 1
                    continue
                sum = nums[left_p] + nums[right_p] + nums[i]
                if sum == target:
                    return target
                if sum < target:
                    left_p += 1
                if sum > target:
                    right_p -= 1
                if abs(sum - target) < abs(res - target):
                    res = sum
        return res

