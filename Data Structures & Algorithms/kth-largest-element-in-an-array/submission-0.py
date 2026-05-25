from heapq import heapify, heappop, heappush
import numpy as np

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        for i in range(0, len(nums) - k + 1):
            x = heappop(nums)
        return x


        