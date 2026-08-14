import heapq



class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(size, root):
            n = size 
            while True:
                largest = root
                left = 2*root + 1
                right = 2*root + 2

                if left < size and nums[left] > nums[largest]:
                    largest = left
                if right < size and nums[right] > nums[largest]:
                    largest = right
                
                if largest == root:
                    break
                
                nums[largest], nums[root] = nums[root], nums[largest]
                root = largest
        
        for i in range(len(nums)//2-1, -1, -1):
            heapify(len(nums), i)
        
        print(nums)
        
        for end in range(len(nums) - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]
            heapify(end, 0)
        
        return nums

            


        
        # what I think they're saying is first heapify the array into a max heap (negativify)

        # then swap first and last elements and decrement the end of a heap to another variable

        # then heapify again and keep decrementing until its finished


        # denegativify it then
        