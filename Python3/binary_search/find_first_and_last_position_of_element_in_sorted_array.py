"""
Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].
"""


class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        res = [-1, -1]
        left_pointer = 0
        right_pointer = len(nums) - 1
        self.helper(nums, target, res, left_pointer, right_pointer)
        return res

    def helper(self, nums, target, result, left_pointer, right_pointer):
        while left_pointer <= right_pointer:
            mid_pointer = (left_pointer + right_pointer) >> 1
            mid_value = nums[mid_pointer]
            if target < mid_value:
                right_pointer = mid_pointer - 1
            elif target > mid_value:
                left_pointer = mid_pointer + 1
            else:
                if mid_pointer == 0 or nums[mid_pointer - 1] != target:
                    result[0] = mid_pointer
                    left_pointer = mid_pointer + 1
                if mid_pointer == len(nums) - 1 or nums[mid_pointer + 1] != target:
                    result[1] = mid_pointer
                    right_pointer = mid_pointer - 1
                if mid_pointer != 0 and nums[mid_pointer - 1] == target and mid_pointer != len(nums) - 1 and nums[mid_pointer + 1] == target:
                    self.helper(nums, target, result, left_pointer, mid_pointer - 1)
                    self.helper(nums, target, result, mid_pointer + 1, right_pointer)
                    return
        return
