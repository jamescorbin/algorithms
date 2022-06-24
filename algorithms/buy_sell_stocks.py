"""
121. Best Time to Buy and Sell Stock
Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
import sys
import os
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minleft = [x for x in prices]
        maxright = [x for x in prices]
        for i in range(1, n):
            minleft[i] = (minleft[i-1]
                          if minleft[i-1] < prices[i]
                          else prices[i])
        for i in reversed(range(0, n-1)):
            maxright[i] = (maxright[i+1]
                          if maxright[i+1] > prices[i]
                          else prices[i])
        diff = [maxright[i] - minleft[i] for i in range(n)]
        ret = max(diff)
        ret = ret if ret > 0 else 0
        return ret

def max_profit(prices: List[int], k: int) -> int:
    """
    Find out maximum profit by buying and selling a share
    at most k times over n days

    Dynamic programming
    """
    n = len(prices)
    prev_profit = [0 for i in range(n)]
    for i in range(1, k + 1):
        profit = [0 for j in range(n)]
        prev_diff = float('-inf')
        for j in range(1, n):
            prev_diff = max(prev_diff,
                            prev_profit[j - 1] - prices[j - 1])
            profit[j] = max(profit[j - 1],
                            prices[j] + prev_diff)
        prev_profit = [x for x in profit]
        print(profit)
    return profit[-1]

if __name__=="__main__":
    arr = [1, 2, 6, 4, 2, 8, 4, 3, 5]
    print(arr)
    print(max_profit(arr, 2))
