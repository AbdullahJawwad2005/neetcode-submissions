class KthLargest:

    # modify a class to find kth largest
    # duplicates inclusive
    # not always sorted
    # constructor with integer k and stream of integers nums
    # mlogk time means finding it with a logk search function to be called m times
    # so do you sort it beforehand, insert inside and done?
    # or do you use a data structure like a hashmap or something to help
    # wait look you don't need any more numbers than up to the kth largest
    # so remove everything before that which is pretty easy by [3:]
    # also think about how you use a binary search tree here
    # okay so what you do is use a binary search tree
    # start from the end of the array and sort it once, then add the last k starting from smallest
    # once youve added the last k then everytime you add its simple
    # okay a minheap was neccessary: where a root is i and left child is 2i+1 and right is 2i+2
    # the parent is [(i-1)//2]
    # heapify to insert a new element
    # so what you do here is pretty simple
    # 7, 6, 5, 8
    # how do you know the kth largest
    # how do you know when to remove them?


    def insert(self, arr, num):
        arr.append(num)
        index = len(arr) - 1

        while index > 0 and arr[(index-1)//2] > arr[index]:
            arr[(index-1)//2], arr[index] = arr[index], arr[(index-1)//2]
            index = (index-1)//2

    def delete(self, arr, index):
        # trade min for end
        arr[0] = arr[-1]
        arr.pop()
        index = 0
    

        while True:
            left_child = 2*index + 1
            right_child = 2*index+2
            smallest = index

            if left_child < len(arr) and arr[left_child] < arr[smallest]:
                smallest = left_child
            if right_child < len(arr) and arr[right_child] < arr [smallest]:
                smallest = right_child
            
            if smallest != index:
                arr[index], arr[smallest] = arr[smallest], arr[index]
                index = smallest
            else:
                break
        



    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = []
        for i in range(0, len(nums)):
            smallest = i
            for j in range(i, len(nums)):
                if nums[j] < nums[smallest]:
                    smallest = j
            temp = nums[i]
            nums[i] = nums[smallest]
            nums[smallest] = temp
        if len(nums) > self.k:
            nums = nums[-(self.k):]


        for i in range(0, len(nums)):
            self.insert(self.nums, nums[i])
        # how do you remove until the k smallest? sort and then remove? or 
    
        

    def add(self, val: int) -> int:
        # check if its larger than the minumum, if yes then add and then remove the minimum
        # so we also need a delete to remove one when a new one comes in? if exceeds k of course, which it always will

        if len(self.nums) < self.k:
            self.insert(self.nums, val)
        elif self.nums and val > self.nums[0]:
            self.delete(self.nums, 0)
            self.insert(self.nums, val)
        return self.nums[len(self.nums)-self.k]
        

        
