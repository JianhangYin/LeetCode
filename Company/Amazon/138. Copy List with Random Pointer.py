"""
1. This question broadens my horizon, I haven't known that the type of key in the dictionary can be a CLASS!
2. collections.defaultdict() can accept:
    - a type: such as int, list...
    - a function without parameters: such as lambda: x ** 2
"""
from collections import defaultdict

# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        new_list_dict = defaultdict(lambda: Node(0, None, None))
        new_list_dict[None] = None
        pointer = head
        while pointer:
            new_list_dict[pointer].val = pointer.val
            new_list_dict[pointer].next = new_list_dict[pointer.next]
            new_list_dict[pointer].random = new_list_dict[pointer.random]
            pointer = pointer.next
        return new_list_dict[head]