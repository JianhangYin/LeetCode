"""
Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""

class Solution:
    def majorityElement(self, nums: list) -> int:
        maj = nums[0]
        count = 1
        for item in nums[1:]:
            if item != maj and count == 0:
                maj = item
                count += 1
            elif item == maj:
                count += 1
            else:
                count -= 1
        return maj

