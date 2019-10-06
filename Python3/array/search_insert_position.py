"""
Given a sorted array and a target value, return the index if the target is found.

If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
"""


class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        if target <= nums[0]:
            return 0
        low_pointer = 0
        high_pointer = len(nums) - 1
        while high_pointer - low_pointer > 1:
            middle_point = (low_pointer + high_pointer) // 2
            middle_value = nums[middle_point]
            if target == middle_value:
                return middle_point
            elif target < middle_value:
                high_pointer = middle_point
            else:
                low_pointer = middle_point
        return high_pointer

