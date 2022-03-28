import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #minimize buy price
        #maximize sell price
        #profit is buy price - sell price
        max_profit = -math.inf
        min_buy = math.inf
        profit = -math.inf
        
        for price in prices:
            min_buy = min(min_buy, price)
            profit = price - min_buy
            max_profit = max(max_profit, profit)
        return max_profit