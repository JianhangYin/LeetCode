"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        value_l1 = 0
        num_l1 = 0
        value_l2 = 0
        num_l2 = 0
        move_l1 = l1
        move_l2 = l2
        while move_l1:
            value_l1 += move_l1.val * (10 ** num_l1)
            num_l1 += 1
            move_l1 = move_l1.next
        while move_l2:
            value_l2 += move_l2.val * (10 ** num_l2)
            num_l2 += 1
            move_l2 = move_l2.next
        sum_result = str(value_l1 + value_l2)[::-1]
        head_node = ListNode(int(sum_result[0]))
        move_node = head_node
        for i in range(1, len(sum_result)):
            move_node.next = ListNode(int(sum_result[i]))
            move_node = move_node.next
        return head_node


