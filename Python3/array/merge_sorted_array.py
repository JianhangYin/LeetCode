"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
"""


class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        point1_t = n + m - 1
        point1_h = m - 1
        point2_h = n - 1
        while point2_h >= 0:
            if point1_h >= 0:
                if nums2[point2_h] >= nums1[point1_h]:
                    nums1[point1_t] = nums2[point2_h]
                    point2_h -= 1
                else:
                    nums1[point1_t] = nums1[point1_h]
                    point1_h -= 1
                point1_t -= 1
            else:
                nums1[point1_t] = nums2[point2_h]
                point2_h -= 1
                point1_t -= 1
