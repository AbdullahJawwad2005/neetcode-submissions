from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # okay we need to use a maxheap here
        # so sort first and then heapify
        # after that goes in a loop
        # takes out two, if equal then goes on with life
        # if not equal then computes different and puts back
        # does until length is not more than 1
        # if length zero then returns 0 at end or is normal
        # remember the negatives properly

        for i in range(0, len(stones)):
            stones[i] = stones[i]*(-1)
        stones.sort()
        heapify(stones)
        print(stones)
        while len(stones) >= 2:
            print(stones)
            x = -heappop(stones)
            y = -heappop(stones)
            if x == y:
                continue
            else:
                heappush(stones, -abs(x-y))

        if len(stones)==0:
            return 0
        else:
            return -stones[0]


        
        