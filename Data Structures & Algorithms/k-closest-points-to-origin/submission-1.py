from heapq import heapify, heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        for x,y in points:
            heappush(heap, (x*x+y*y, (x,y)))
        
        res = []
        for i in range(k):
            dis, point = heappop(heap)
            res.append(point)


        return res





        
        