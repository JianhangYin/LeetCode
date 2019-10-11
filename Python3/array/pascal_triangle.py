"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
"""


class Solution:
    def generate(self, numRows: int) -> list:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        res = self.generate(numRows - 1)
        last_list = res[-1]
        new_list = [1]
        for i in range(len(last_list) - 1):
            new_list.append(last_list[i] + last_list[i + 1])
        new_list.append(1)
        res.append(new_list)
        return res

