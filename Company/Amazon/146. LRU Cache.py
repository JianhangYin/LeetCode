"""
This question uses OrderedDict. Not like the traditional dictionary, OrderedDict is a ordered dictionary, the data
can remember the order of the value inserted into the data set.
1. ordered_dict.pop(key): remove the key value.
2. ordered_dict[key] = value: assign the key with value.
3. ordered_dict.popitem(last=False): remove the 1st order key-value.

In this question:
When we want to change the value of key, and put it at the end of queue.
We need to pop the key first, and then assign the value.
"""
from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            res = self.cache.pop(key)
            self.cache[key] = res
            return res
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        else:
            if self.size < self.cap:
                self.size += 1
                self.cache[key] = value
            else:
                self.cache.popitem(last=False)
                self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

