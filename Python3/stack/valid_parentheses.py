"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stack_list = []
        for item in s:
            if item in ['(', '[', '{']:
                stack_list.append(item)
            else:
                if len(stack_list) == 0:
                    return False
                out_stack = stack_list.pop()
                if (item == ')' and out_stack == '(') or (item == '}' and out_stack == '{') or (item == ']' and out_stack == '['):
                    continue
                else:
                    return False
        if len(stack_list) == 0:
            return True
        else:
            return False


a = "]"
s = Solution()
b = s.isValid(a)
print(b)
