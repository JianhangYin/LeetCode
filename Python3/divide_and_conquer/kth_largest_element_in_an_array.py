"""
Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
"""
import heapq as hq


class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        nums.sort()
        return nums[-k]

    def findKthLargestHeap(self, nums: list, k: int) -> int:
        nums = [-num for num in nums]
        hq.heapify(nums)
        res = 0
        for _ in range(k):
            res = hq.heappop(nums)
        return -res

    def findKthLargestQuick(self, nums: list, k: int) -> int:
        low = 0
        high = len(nums) - 1
        res = self.quickFind(nums, low, high, k)
        return res

    def quickFind(self, nums: list, low: int, high: int, k: int) -> int:
        pivot = self.partition(nums, low, high)
        if pivot == k - 1:
            res = nums[pivot]
        elif pivot < k - 1:
            res = self.quickFind(nums, pivot + 1, high, k)
        else:
            res = self.quickFind(nums, low, pivot - 1, k)
        return res

    def partition(self, arr: list, low: int, high: int) -> int:
        divider = low - 1
        pivot = high
        for search in range(low, high):
            if arr[search] >= arr[pivot]:
                divider += 1
                arr[divider], arr[search] = arr[search], arr[divider]
        divider += 1
        arr[divider], arr[pivot] = arr[pivot], arr[divider]
        return divider
