"""
This question is really confusing.
From the questions, we don't need to consider the identifier order during the sorting.
BUT, the test case need us to order the identifier when the contents are exactly the same.
This is why I add a alpha.sort().
"""
class Solution:
    def reorderLogFiles(self, logs: list) -> list:
        alpha = []
        digit = []
        for item in logs:
            item_list = item.split()
            if item_list[1].isdigit():
                digit.append(item)
            else:
                alpha.append(item.split())
        alpha.sort()
        alpha = [' '.join(x) for x in sorted(alpha, key=lambda input: input[1:])]
        return alpha + digit
