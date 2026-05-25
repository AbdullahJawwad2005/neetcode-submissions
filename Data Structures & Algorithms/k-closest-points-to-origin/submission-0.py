from heapq import heapify, heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # use the distance formula
        # use floats to make sure you're getting the best out of things
        # you can use a minheap here
        # but its done based on another value though so how?
        # then use priority queue instead
        # but that wouldn't work either
        # its maxheap here... but you're meant to hardcode the implementation with a few changes arent you?
        # oh wait no all you're meant to do is compare it to the root!!! if you do that you're set
        heap = []
        for x,y in points:
            heappush(heap, (x*x+y*y, (x,y)))
        
        res = []
        for i in range(k):
            dis, point = heappop(heap)
            res.append(point)


        return res





        
        