class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        done = set()
        for i in range(len(nums)):
            if nums[i] not in done:
                done.add(nums[i])
            else:
                return True
        return False
        