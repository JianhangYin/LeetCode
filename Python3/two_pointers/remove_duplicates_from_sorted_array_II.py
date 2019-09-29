"""
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""


class Solution:
    def removeDuplicates(self, nums: list) -> int:
        if len(nums) <= 2:
            return len(nums)
        left = 1
        for right in range(2, len(nums)):
            if nums[left] != nums[right] or nums[left-1] != nums[right]:
                left += 1
                nums[left] = nums[right]
        return left + 1
