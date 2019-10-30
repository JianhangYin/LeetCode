"""
1. if s == None and t == None, return True
2. if s == None or t == None, return False
3. if s != None and t != None, check if s == t
4. if s != t, check s.left == t or s.right == t.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val == t.val and self.isSametree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSametree(self, s, t):
        if not s and not t:
            return True
        elif not s or not t:
            return False
        return s.val == t.val and self.isSametree(s.left, t.left) and self.isSametree(s.right, t.right)

