"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2.
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2.
If it does not exist, output -1 for this number.
"""


class Solution:
    def nextGreaterElement(self, nums1: list, nums2: list) -> list:
        target_dic = {}
        temp_stack = []
        for item in nums2:
            while temp_stack and item > temp_stack[-1]:
                target_dic[temp_stack.pop()] = item
            temp_stack.append(item)
        return [target_dic.get(j) for j in nums1]
