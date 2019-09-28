"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        elif needle not in haystack:
            return -1
        else:
            num = 0
            while needle in haystack:
                haystack = haystack[:-1]
                num += 1
            return len(haystack) - len(needle) + 1


haystack = "sfasdfasdf"
needle = "asd"
s = Solution()
b = s.strStr(haystack, needle)
print(b)
