"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        level = 1
        queue_list = [root]
        while len(queue_list) != 0:
            new_queue_list = []
            for item in queue_list:
                if not item.left and not item.right:
                    return level
                if item.left:
                    new_queue_list.append(item.left)
                if item.right:
                    new_queue_list.append(item.right)
            level += 1
            queue_list = new_queue_list

