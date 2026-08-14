import heapq



class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # maxheap then sort using that
        heapq.heapify(nums)
        collect = nums
        store = []
        while collect:
            store.append(heapq.heappop(collect))
        return store


        
        # what I think they're saying is first heapify the array into a max heap (negativify)

        # then swap first and last elements and decrement the end of a heap to another variable

        # then heapify again and keep decrementing until its finished


        # denegativify it then
        