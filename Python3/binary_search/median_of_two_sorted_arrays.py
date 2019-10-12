"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
"""


class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        if len(nums1) >= len(nums2):
            nums1, nums2 = nums2, nums1
        n = len(nums1)
        m = len(nums2)
        total = (n + m + 1) // 2
        left_start = 0
        left_end = n
        while left_end >= left_start:
            n_p = (left_start + left_end) // 2
            m_p = total - n_p

            n_left = float("-inf") if n_p == 0 else nums1[n_p - 1]
            n_right = float("inf") if n_p == n else nums1[n_p]
            m_left = float("-inf") if m_p == 0 else nums2[m_p - 1]
            m_right = float("inf") if m_p == m else nums2[m_p]

            if n_left > m_right:
                left_end = n_p - 1
            if n_right < m_left:
                left_start = n_p + 1
            if n_left <= m_right and n_right >= m_left:
                if (n + m) % 2 == 0:
                    return (max(n_left, m_left) + min(n_right, m_right)) / 2
                else:
                    return max(n_left, m_left)

