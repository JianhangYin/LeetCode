"""
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.
"""


class Solution:
    def removeDuplicates(self, S: str) -> str:
        temp_stack = []
        for item in S:
            if temp_stack and item == temp_stack[-1]:
                temp_stack.pop()
            else:
                temp_stack.append(item)
        return ''.join(temp_stack)

