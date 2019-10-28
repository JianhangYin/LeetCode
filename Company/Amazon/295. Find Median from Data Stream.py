"""
We divide this list into two group, group one is the small one, group two is the larger one.
We use heapq to build the maximum heap for smaller one, and minimum heap for larger one.
We need to make sure the larger one is equal to smaller one or 1 item longer than the smaller one.

1. the minimum heap is built directly by heappush.
2. the maximum heap is built by minus list by heappush
"""
import heapq


class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heapq.heappush(small, -heapq.heappushpop(large, num))
        if len(large) < len(small):
            heapq.heappush(large, -heapq.heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
