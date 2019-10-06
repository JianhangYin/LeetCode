"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""


class Solution:
    def maxSubArray(self, nums: list) -> int:
        if not nums:
            return float("-inf")
        middle_point = len(nums) // 2
        max_left = self.maxSubArray(nums[:middle_point])
        max_right = self.maxSubArray(nums[middle_point + 1:])
        left_max_cross = nums[middle_point]
        right_max_cross = nums[middle_point]
        left_sum = 0
        right_sum = 0
        for i in range(middle_point, -1, -1):
            left_sum += nums[i]
            if left_max_cross <= left_sum:
                left_max_cross = left_sum
        for i in range(middle_point, len(nums)):
            right_sum += nums[i]
            if right_max_cross <= right_sum:
                right_max_cross = right_sum
        max_cross = left_max_cross + right_max_cross - nums[middle_point]
        return max(max_left, max_cross, max_right)

    def maxSubArrayDP(self, nums: list) -> int:
        if not nums:
            return 0
        max_current = 0
        max_sum = nums[0]
        for item in nums:
            max_current = max(max_current + item, item)
            max_sum = max(max_sum, max_current)
        return max_sum

    def maxSubArrayDPEasyUnderstand(self, nums: list) -> int:
        if not nums:
            return 0
        max_list = [nums[0]]
        for i in range(1, len(nums)):
            max_list.append(max(max_list[i - 1] + nums[i], nums[i]))
        return max(max_list)
