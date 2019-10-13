"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
"""


class Solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        pointer = len(nums) - 2
        while pointer >= 0:
            if nums[pointer] >= nums[-1]:
                for j in range(pointer + 1, len(nums)):
                    temp = nums[j]
                    nums[j] = nums[j - 1]
                    nums[j - 1] = temp
            else:
                for j in range(pointer + 1, len(nums)):
                    if nums[j] > nums[pointer]:
                        temp = nums[j]
                        nums[j] = nums[pointer]
                        nums[pointer] = temp
                        return
            pointer -= 1
        return



