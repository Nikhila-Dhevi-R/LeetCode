class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for i in prices[1: ]:
            if i < buy :
                buy = i
            """ profit = i-buy
            if (i-buy) > profit:
                profit = i-buy"""
            
            profit = max(profit, i-buy)
        return profit

