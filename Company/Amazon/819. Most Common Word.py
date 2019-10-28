"""
This question has two method.
1. This method is relatively tricky. We use collections.Counter. It can calculate the counter of each value
automatically. The input of Counter is a list/dictionary/void. Using for loop will automatically return the most
counted items.

2. The second method is using collections.defaultdict.
"""

from collections import Counter, defaultdict


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list) -> str:
        for punc in "!?',;.":
            paragraph = paragraph.replace(punc, ' ')
        counter_para = Counter(paragraph.lower().split())
        for item, _ in counter_para.most_common():
            if item not in banned:
                return item
        return ''

    def mostComonWord2(self, paragraph, banned):
        for punc in "!?',;.":
            paragraph = paragraph.replace(punc, ' ')
        dict = defaultdict(lambda: 0)
        max_count = 0
        res = ""
        for item in paragraph.lower().split():
            if item not in banned:
                dict[item] += 1
                if dict[item] >= max_count:
                    max_count = dict[item]
                    res = item
        return res


