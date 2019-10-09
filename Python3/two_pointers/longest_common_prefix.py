"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        if len(strs) == 0:
            return ''
        common = strs[0]
        while len(common) > 0:
            for i in range(len(strs)):
                if common not in strs[i][:len(common)]:
                    break
                if i == len(strs) - 1:
                    return common
            common = common[0:-1]
        return common



