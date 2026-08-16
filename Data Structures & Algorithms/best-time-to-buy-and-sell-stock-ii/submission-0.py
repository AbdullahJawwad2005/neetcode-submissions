class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # for loop to iterate over it
        # keep two pointers for current min and max and add their difference to a sum variable everytime 
        # the condition you add to sum and start separating the pointers on the condition that if the next pointer after max is less than current max then you make max and min that after adding the difference to sum
        total = 0
        last = 0
        first = 0
        while last != len(prices) - 1:
            if prices[last+1] < prices[last]:
                total += prices[last] - prices[first]
                first = last +1
                last = last + 1
            else:
                last += 1
        total += prices[last] - prices[first]
        return total
                

        
        # 
        