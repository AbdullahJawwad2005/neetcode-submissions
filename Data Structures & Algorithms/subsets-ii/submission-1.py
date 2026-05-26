class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backTrack(index, path):       
            res.append(path[:])
        

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backTrack(i+1, path)
                path.pop()


        backTrack(0, [])
        res = (res + [])
        return res