"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    recursive
    """
    def levelOrderBottomRecursive(self, root: TreeNode) -> list:
        if not root:
            return []
        output_list = []
        output_list_left = self.levelOrderBottomRecursive(root.left)
        output_list_right = self.levelOrderBottomRecursive(root.right)
        while len(output_list_left) != 0 or len(output_list_right) != 0:
            if len(output_list_left) == 0:
                output_list.insert(0, output_list_right.pop())
            elif len(output_list_right) == 0:
                output_list.insert(0, output_list_left.pop())
            else:
                output_list.insert(0, output_list_left.pop() + output_list_right.pop())
        output_list.append([root.val])
        return output_list
    """
    iterative
    """
    def levelOrderBottom(self, root: TreeNode) -> list:
        if not root:
            return []
        output_list = []
        temp_list1 = [root]
        temp_list2 = []
        while len(temp_list1) != 0 or len(temp_list2) != 0:
            level_list = []
            while len(temp_list1) != 0:
                current_node = temp_list1.pop(0)
                level_list.append(current_node.val)
                if current_node.left is not None:
                    temp_list2.append(current_node.left)
                if current_node.right is not None:
                    temp_list2.append(current_node.right)
            if len(level_list) != 0:
                output_list.insert(0, level_list)
            level_list = []
            while len(temp_list2) != 0:
                current_node = temp_list2.pop(0)
                level_list.append(current_node.val)
                if current_node.left is not None:
                    temp_list1.append(current_node.left)
                if current_node.right is not None:
                    temp_list1.append(current_node.right)
            if len(level_list) != 0:
                output_list.insert(0, level_list)
        return output_list


