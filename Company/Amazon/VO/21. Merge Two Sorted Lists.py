"""
RECURSIVE METHOD!!!!
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1 and l2:
            head = l1 if l1.val < l2.val else l2
            if head == l1:
                head.next = self.mergeTwoLists(l1.next, l2)
            else:
                head.next = self.mergeTwoLists(l1, l2.next)
            return head
        else:
            return None


