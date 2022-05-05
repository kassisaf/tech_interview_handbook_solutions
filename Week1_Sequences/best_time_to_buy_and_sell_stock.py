"""
121. Best Time to Buy and Sell Stock [Easy]
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to
  sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_current = 0
        max_global = 0

        for day in range(len(prices) - 1):
            # Kadane's algorithm
            max_current += prices[day + 1] - prices[day]
            if max_current > max_global:
                max_global = max_current

            if max_current < 0:
                max_current = 0

        return max_global


if __name__ == "__main__":
    assert Solution.maxProfit(None, prices=[7,1,5,3,6,4]) == 5
    assert Solution.maxProfit(None, prices=[7,6,4,3,1]) == 0
