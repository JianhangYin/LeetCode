"""
We need two loops to solve this problems:
1. finding the last index for each char in the string.
2. finding the index where all the char on the left has a smaller last index.
"""


class Solution:
    def partitionLabels(self, S: str) -> list:
        res = []
        max_last_seen = 0
        count = 0
        last_seen = {char: i for i, char in enumerate(S)}
        for i, char in enumerate(S):
            max_last_seen = max(max_last_seen, last_seen[char])
            count += 1
            if i == max_last_seen:
                res.append(count)
                count = 0
        return res
