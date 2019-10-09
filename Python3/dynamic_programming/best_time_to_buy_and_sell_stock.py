"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
"""


class Solution:
    def maxProfit(self, prices: list) -> int:
        if len(prices) == 0:
            return 0
        max_profit = 0
        min_price = prices[0]
        for item in prices:
            min_price = min(min_price, item)
            max_profit = max(max_profit, item - min_price)
        return max_profit


