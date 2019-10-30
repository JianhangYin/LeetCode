"""
This is a relatively easy question. But there are still two points need to be remembered.
1. enumerate(seq): returns the location and values.
2. In the dictionary in Python: the int and float can also be the key.
"""

class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        hash_table = {}
        for i, num in enumerate(nums):
            if num in hash_table:
                return [hash_table[num], i]
            hash_table[target - num] = i

