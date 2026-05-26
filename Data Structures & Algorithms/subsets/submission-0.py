class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backTrack(index, path):
            res.append(path[:])
            
            
            print(path)
            for i in range(index, len(nums)):
                if nums[i] in path:
                    continue
                
                path.append(nums[i])
                backTrack(i+1, path)
                path.pop()
                
        
        backTrack(0, [])
        return res
        