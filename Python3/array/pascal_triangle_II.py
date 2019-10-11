"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.
"""


class Solution:
    def getRow(self, rowIndex: int) -> list:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        res = self.getRow(rowIndex - 1)
        new_list = [1]
        for i in range(len(res) - 1):
            new_list.append(res[i] + res[i + 1])
        new_list.append(1)
        return new_list


