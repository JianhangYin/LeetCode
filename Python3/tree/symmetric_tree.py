"""
 Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
      self.val = x
      self.left = None
      self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            return self.symmeticHelp(root.left, root.right)

    def symmeticHelp(self, left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None or left.val != right.val:
            return False
        else:
            return self.symmeticHelp(left.left, right.right) and self.symmeticHelp(left.right, right.left)
