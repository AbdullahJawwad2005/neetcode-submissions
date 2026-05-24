class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # split array into two parts by using binary search
        # binary search across the two parts
        if len(nums) == 1:
            if nums[0]==target:
                return 0
            else:
                return -1


        start = 0
        end = len(nums) - 1
        while(start<end):
            mid = (start+end)//2
            if nums[mid]>nums[end]:
                start = mid + 1
            else:
                end = mid
        arr1 = nums[0:start]
        arr2 = nums[start:len(nums)]
        # okay now you have the two arrays
        # binary search on both
        # if you find it return the index
        # if in neither return -1

        # search through arr1
        # search through arr2 and when you find the index add the length of the previous array
        start = 0
        end = len(arr1) -1
        while(start<=end):
            print(mid)
            mid = (start+end)//2
            if arr1[mid] == target:
                return mid
            elif arr1[mid] < target:
                start = mid+1
            else:
                end = end - 1
        
        start = 0
        end = len(arr2) -1
        while(start<=end):
            mid = (start+end)//2
            print("start: ", start)
            print("mid: ", mid)
            print("end: ", end)
            if arr2[mid] == target:
                return mid + len(arr1)
            elif arr2[mid] < target:
                start = mid+1
            else:
                end = end - 1
            
        print(arr1)
        print(arr2)
        return -1
        
        