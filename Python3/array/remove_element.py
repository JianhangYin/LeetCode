"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""


class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        num_total = len(nums)
        pointer_num = 0
        pointer = 0
        while pointer_num < len(nums):
            if nums[pointer] != val:
                pointer += 1
            else:
                nums.append(nums.pop(pointer))
                num_total -= 1
            pointer_num += 1
        return num_total





