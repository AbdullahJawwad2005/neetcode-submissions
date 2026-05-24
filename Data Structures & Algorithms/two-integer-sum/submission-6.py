class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            difference  = target - nums[i]
            if difference in seen:
                if seen[difference] > i:
                    return [i, seen[difference]]
                else:
                    return [seen[difference], i]
            else:
                seen[nums[i]] = i
        
                

        