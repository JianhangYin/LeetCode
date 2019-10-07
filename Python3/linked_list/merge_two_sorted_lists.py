"""
Merge two sorted linked lists and return it as a new list.

The new list should be made by splicing together the nodes of the first two lists.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1
        if l1.val <= l2.val:
            root = l1
            cur = l1
            l1 = l1.next
        else:
            root = l2
            cur = l2
            l2 = l2.next
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                cur = l1
                l1 = l1.next
            else:
                cur.next = l2
                cur = l2
                l2 = l2.next
        if not l1:
            cur.next = l2
        else:
            cur.next = l1
        return root

    def mergeTwoListsRecursive(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        while l1 and l2:
            if l1.val <= l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1, l2.next)
                return l2

