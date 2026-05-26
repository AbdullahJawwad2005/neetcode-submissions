class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        # do you need used here?
        # you need to check if similar is already in res 
        # but thats inefficient, a normal backtracking without a loop would work fine?
        # 
        #

        def backTrack(index, path):
            # base case
            if index == len(nums):
                if path not in res:
                    res.append(path[:])
                return

            for i in range(index, len(nums)):
                path.append(nums[i])
                backTrack(i+1, path)
                path.pop()

                backTrack(i+1, path)

        backTrack(0, [])
        res = (res + [])
        return res