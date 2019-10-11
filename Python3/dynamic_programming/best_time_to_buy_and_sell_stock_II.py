"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""


class Solution:
    def maxProfit(self, prices: list) -> int:
        if len(prices) < 2:
            return 0
        first_point = 0
        second_point = 1
        profit = 0
        while second_point < len(prices):
            if prices[second_point] >= prices[first_point]:
                profit += prices[second_point] - prices[first_point]
            first_point += 1
            second_point += 1
        return profit


