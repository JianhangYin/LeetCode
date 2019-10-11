"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""


class Solution:
    def maxArea(self, height: list) -> int:
        length = len(height) - 1
        left_pointer = 0
        right_pointer = length
        max_area = length * min(height[left_pointer], height[right_pointer])
        while right_pointer > left_pointer:
            if height[left_pointer] > height[right_pointer]:
                right_pointer -= 1
            else:
                left_pointer += 1
            max_area = max(max_area, (right_pointer - left_pointer) * min(height[left_pointer], height[right_pointer]))
        return max_area

