"""
Given a sorted linked list, delete all duplicates such that each element appear only once.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        a_list = [head.val]
        a_node = head
        while a_node:
            b_node = a_node.next
            while b_node and b_node.val in a_list:
                b_node = b_node.next
            a_list.append(b_node and b_node.val)
            a_node.next = b_node
            a_node = b_node
        return head



