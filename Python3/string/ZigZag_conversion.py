class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s:
            return ''
        if numRows == 1 or len(s) <= numRows:
            return s
        res = ''
        total = 2 * (numRows - 1)
        for i in range(numRows):
            first_round = total - 2 * i
            second_round = 2 * i
            j = i
            sig = True
            while j < len(s):
                if first_round * second_round:
                    res += s[j]
                    j = j + first_round if sig else j + second_round
                    sig = not sig
                else:
                    res += s[j]
                    j = j + first_round + second_round
        return res