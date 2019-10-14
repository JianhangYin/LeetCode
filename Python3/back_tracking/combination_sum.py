"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
"""


class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:
        res = []
        self.helper(candidates, target, res)
        return res

    def helper(self, candidates, target, result):
        if target < 0:
            return
        if not candidates:
            return
        if len(candidates) == 1:
            if target % candidates[0] == 0:
                temp = []
                for i in range(int(target / candidates[0])):
                    temp.append(candidates[0])
                result.append(temp)
            return
        self.helper(candidates[1:], target, result)
        temp = []
        self.helper(candidates, target - candidates[0], temp)
        for item in temp:
            item.insert(0, candidates[0])
        result += temp
        return


