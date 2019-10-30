"""
This question is using DFS to iterate the tree.
By adding a variable called level to judge if we run from left to right or right to left.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list:
        res = []
        level = 0
        self.DFS(res, level, root)
        return res

    def DFS(self, res, level, node):
        if not node:
            return
        if len(res) < level + 1:
            res.append([])
        if level % 2 == 0:
            res[level].append(node.val)
        else:
            res[level].insert(0, node.val)
        level += 1
        self.DFS(res, level, node.left)
        self.DFS(res, level, node.right)
