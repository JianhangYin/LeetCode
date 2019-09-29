"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
"""


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_stack = []
        t_stack = []
        for item in S:
            if item == '#':
                if s_stack:
                    s_stack.pop()
                else:
                    continue
            else:
                s_stack.append(item)
        for item in T:
            if item == '#':
                if t_stack:
                    t_stack.pop()
                else:
                    continue
            else:
                t_stack.append(item)
        return s_stack == t_stack


a = "y#fo##f"
b = "y#f#o##f"
s = Solution()
print(s.backspaceCompare(a, b))

