"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_pointer = 0
        right_pointer = len(s) - 1
        while left_pointer <= right_pointer:
            if s[left_pointer].isalnum() and s[right_pointer].isalnum():
                if s[left_pointer].lower() != s[right_pointer].lower():
                    return False
                else:
                    left_pointer += 1
                    right_pointer -= 1
                    continue
            if not s[left_pointer].isalnum():
                left_pointer += 1
            if not s[right_pointer].isalnum():
                right_pointer -= 1
        return True


