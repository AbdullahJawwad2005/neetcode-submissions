class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []
        def backTracking(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            
            for i in range(0, len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backTracking(path)
                path.pop()

            
        backTracking([])
        return res
            


        