class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minimum = prices[0]
        profit = 0
        for price in prices:
            if price < minimum:
                minimum = price
            profit = max(profit , price - minimum)
        return profit 