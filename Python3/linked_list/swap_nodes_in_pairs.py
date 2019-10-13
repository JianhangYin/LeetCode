"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        if not head.next.next:
            temp = head.next
            temp.next = head
            head.next = None
            return temp
        new_head = head.next
        head.next = self.swapPairs(new_head.next)
        new_head.next = head
        return new_head



