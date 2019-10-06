"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem,

a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: list) -> TreeNode:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            root_node = TreeNode(nums[0])
            return root_node
        if len(nums) == 2:
            root_node = TreeNode(nums[1])
            root_node.left = TreeNode(nums[0])
            return root_node
        middle_index = len(nums) // 2
        root_node = TreeNode(nums[middle_index])
        root_node.left = self.sortedArrayToBST(nums[:middle_index])
        root_node.right = self.sortedArrayToBST(nums[middle_index + 1:])
        return root_node
