"""
Given a binary tree, determine if it is height-balanced.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.calculateLevel(root.left) - self.calculateLevel(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def calculateLevel(self, tree_node: TreeNode) -> int:
        if not tree_node:
            return 0
        level_num = []
        level = 0
        queue_list = [tree_node]
        while len(queue_list) != 0:
            level += 1
            new_queue_list = []
            for item in queue_list:
                if not item.left or not item.right:
                    level_num.append(level)
                if item.left:
                    new_queue_list.append(item.left)
                if item.right:
                    new_queue_list.append(item.right)
            queue_list = new_queue_list
        return max(level_num)


