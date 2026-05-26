class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backTrack(index, path):
            # base case
            if sum(path) >= target:
                if sum(path) == target:
                    res.append(path[:])
                return
            for i in range(index, len(nums)):
                # iteration 1
                path.append(nums[i])
                backTrack(i, path)
                path.pop()

                # iteration 2
        backTrack(0, [])
        return res
        