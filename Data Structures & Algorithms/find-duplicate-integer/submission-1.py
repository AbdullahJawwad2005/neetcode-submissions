class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # okay so whats the problem here exactly? you have an array of n+1 of 1, to n 
        # and theres only one integer that can repeat multiple times

        i = 0
        n = nums[i]
        nums[i] = 0
        i = n
        while True:
            n = nums[i]
            if nums[n] == 0 or i==n:
                return nums[i]
            nums[i] = 0 
            i = n
            

            

        