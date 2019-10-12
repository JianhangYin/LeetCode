"""
Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2.

Note:
Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
"""


class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        left_pointer = 0
        right_pointer = len(numbers) - 1
        while right_pointer > left_pointer:
            if numbers[left_pointer] + numbers[right_pointer] < target:
                left_pointer += 1
            elif numbers[left_pointer] + numbers[right_pointer] > target:
                right_pointer -= 1
            else:
                return [left_pointer + 1, right_pointer + 1]
        return []


