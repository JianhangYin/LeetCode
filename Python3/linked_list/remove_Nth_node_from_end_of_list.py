"""
Given a linked list, remove the n-th node from the end of list and return its head.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast_p = head
        slow_p = None
        count = 0
        while fast_p.next:
            count += 1
            if count == n:
                slow_p = head
            if count > n:
                slow_p = slow_p.next
            fast_p = fast_p.next
        if not slow_p:
            return head.next
        slow_p.next = slow_p.next.next
        return head

