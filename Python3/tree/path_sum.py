"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        return sum in self.pathSumHelper(root)

    def pathSumHelper(self, root: TreeNode) -> list:
        if not root:
            return [0]
        sum_list = []
        if root.left and root.right:
            for item in self.pathSumHelper(root.left) + self.pathSumHelper(root.right):
                sum_list.append(item + root.val)
        elif root.left:
            for item in self.pathSumHelper(root.left):
                sum_list.append(item + root.val)
        else:
            for item in self.pathSumHelper(root.right):
                sum_list.append(item + root.val)
        return sum_list

    def hasPathSumBetter(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        return self.hasPathSumBetter(root.left, sum - root.val) or self.hasPathSumBetter(root.right, sum - root.val)
