"""
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.
"""


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        num_string = 0
        for i in range(len(S)):
            if S[i] == '(':
                num_string += 1
            else:
                num_string -= 1
            if num_string == 0:
                if i == len(S) - 1:
                    return S[1:-1]
                else:
                    return self.removeOuterParentheses(S[:i + 1]) + self.removeOuterParentheses(S[i + 1:])


a = "(()())(())"
s = Solution()
b = s.removeOuterParentheses(a)
print(b)
