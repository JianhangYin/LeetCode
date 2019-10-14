"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
"""


class Solution:
    def search(self, nums: list, target: int) -> int:
        left_pointer = 0
        right_pointer = len(nums) - 1
        while right_pointer > left_pointer:
            mid_pointer = (left_pointer + right_pointer) // 2
            mid_value = nums[mid_pointer]
            if nums[left_pointer] < nums[right_pointer]:
                if target < mid_value:
                    right_pointer = mid_pointer
                elif target > mid_value:
                    left_pointer = mid_pointer
                else:
                    return mid_pointer
            else:
                if target > nums[left_pointer]:
                    if target > mid_value:
                        if mid_value > nums[left_pointer]:
                            left_pointer = mid_pointer
                        else:
                            right_pointer = mid_pointer
                    elif target < mid_value:
                        right_pointer = mid_pointer
                    else:
                        return mid_pointer
                elif target < nums[right_pointer]:
                    if target > mid_value:
                        left_pointer = mid_pointer
                    elif target < mid_value:
                        if mid_value < nums[right_pointer]:
                            right_pointer = mid_pointer
                        else:
                            left_pointer = mid_pointer
                    else:
                        return mid_pointer
                elif target == nums[left_pointer]:
                    return left_pointer
                else:
                    return right_pointer
        return -1

