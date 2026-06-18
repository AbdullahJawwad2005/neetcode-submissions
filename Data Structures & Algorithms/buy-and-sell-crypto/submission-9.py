class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        minprice = prices[0]

        for i in range(1, len(prices)):
            try_profit = prices[i] - minprice
            best_profit = max(try_profit, best_profit)
            minprice = min(minprice, prices[i])
        
        if best_profit < 0:
            return 0
        
        return best_profit
        

        