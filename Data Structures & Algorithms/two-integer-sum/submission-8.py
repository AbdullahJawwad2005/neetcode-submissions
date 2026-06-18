class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            search_value = target - nums[i]
            if search_value in seen:
                j = seen[search_value] 
                return [j, i]
            seen[nums[i]] = i

        
                

        