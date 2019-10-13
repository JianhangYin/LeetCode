"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""


class Solution:
    def letterCombinations(self, digits: str) -> list:
        if not digits:
            return []
        dic = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        if len(digits) == 1:
            return dic[digits]
        sub = self.letterCombinations(digits[0:-1])
        res = []
        for item in dic[digits[-1]]:
            for item_in in sub:
                res.append(item_in + item)
        return res

