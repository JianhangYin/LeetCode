"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow_pointer = head
        fast_pointer = head
        while fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if fast_pointer is None:
                return slow_pointer
        return slow_pointer


node_list = []
for i in range(6):
    node_list.append(ListNode(i + 1))
for i in range(6):
    if i == 5:
        node_list[i].next = None
    else:
        node_list[i].next = node_list[i + 1]
s = Solution()
result = s.middleNode(node_list[0])
print(result.val)
