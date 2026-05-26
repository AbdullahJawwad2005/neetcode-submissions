class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        if not candidates:
            return

        candidates.sort()
        res = []
        def backTrack(index, path, total):
            if total == target and path not in res:
                res.append(path[:])
                return
            if total > target:
                return
            
            if index == len(candidates):
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue

                path.append(candidates[i])
                backTrack(i+1, path, total + candidates[i])
                path.pop()
                

        backTrack(0, [], 0)
        return res

        