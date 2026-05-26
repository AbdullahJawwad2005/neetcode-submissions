class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []
        used = [False]*len(nums)

        def backTracking(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            
            for i in range(0, len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                backTracking(path)
                used[i] = False
                path.pop()

            
        backTracking([])
        return res
            


        