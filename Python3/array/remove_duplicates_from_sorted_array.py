"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""


class Solution:
    def removeDuplicates(self, nums: list) -> int:
        if len(nums) == 0:
            return 0
        left_pointer = 0
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[left_pointer]:
                count += 1
                left_pointer += 1
                nums[left_pointer] = nums[i]
        return count

