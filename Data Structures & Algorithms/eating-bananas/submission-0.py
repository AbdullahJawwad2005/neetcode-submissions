from math import ceil


class Solution:
    def calculate(self, arr, value):
        amount = 0
        for i in range(len(arr)):
            amount = amount + ceil(arr[i]/value)
        return amount
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        start = 1
        end = max(piles)

        while(start<end):
            mid = (start+end)//2
            amount = self.calculate(piles, mid)

            if amount <=h:
                end = mid
            else:
                start = mid + 1
        return start




        