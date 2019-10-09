"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

IV            4
IX            9
XL            40
XC            90
CD            400
CM            900

"""


class Solution:
    def romanToInt(self, s: str) -> int:
        s2i = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        exp = ['I', 'X', 'C']
        num = 0
        for i in range(len(s) - 1):
            if s[i] not in exp:
                num += s2i[s[i]]
            elif s[i] == 'I' and s[i + 1] not in ['V', 'X']:
                num += s2i[s[i]]
            elif s[i] == 'X' and s[i + 1] not in ['L', 'C']:
                num += s2i[s[i]]
            elif s[i] == 'C' and s[i + 1] not in ['D', 'M']:
                num += s2i[s[i]]
            else:
                num -= s2i[s[i]]
        num += s2i[s[-1]]
        return num

