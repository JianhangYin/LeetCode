"""
This question is very very tricky. We can brute force search.
But we will meet the problem of TLE.
So we can find that the frequency of the cells - 14.
"""


class Solution:
    def prisonAfterNDays(self, cells: list, N: int) -> list:
        if N == 0:
            return cells
        days = 1
        res = []
        time_limit = 14 if not N % 14 else N % 14
        while days <= time_limit:
            res.append(0)
            for row in range(1, len(cells) - 1):
                res.append(1 if cells[row - 1] == cells[row + 1] else 0)
            res.append(0)
            cells = res
            res = []
            days += 1
        return cells
