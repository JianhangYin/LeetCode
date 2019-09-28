"""
Reverse a singly linked list.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        else:
            reverse_head = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return reverse_head


node_list = []
for i in range(6):
    node_list.append(ListNode(i + 1))
for i in range(6):
    if i == 5:
        node_list[i].next = None
    else:
        node_list[i].next = node_list[i + 1]
s = Solution()
result = s.reverseList(node_list[0])
print(result.val)
