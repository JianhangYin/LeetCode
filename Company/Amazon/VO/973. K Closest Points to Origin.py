"""
The good application of sorted() and lambda!
"""


class Solution:
    def kClosest(self, points: list, K: int) -> list:
        points = [x for x in sorted(points, key=lambda input: input[0] ** 2 + input[1] ** 2)]
        return points[:K]