"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
"""


class Solution:
    def trap(self, height: list) -> int:
        max_left = 0
        max_right = 0
        left = 0
        right = len(height) - 1
        water = 0
        while left < right:
            if height[left] < height[right]:
                max_left = max(height[left], max_left)
                water += max_left - height[left]
                left += 1
            else:
                max_right = max(height[right], max_right)
                water += max_right - height[right]
                right -= 1
        return water


a = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
s = Solution()
print(s.trap(a))
