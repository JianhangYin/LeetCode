"""
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
"""


class Solution:
    def combinationSum2(self, candidates: list, target: int) -> list:
        candidates.sort()
        res = []
        self.helper(candidates, target, res, [])
        return res

    def helper(self, candidates, target, result, path):
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return
        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                return
            self.helper(candidates[i + 1:], target - candidates[i], result, path + [candidates[i]])