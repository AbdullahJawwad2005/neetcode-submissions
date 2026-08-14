class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 1
        candidate = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == candidate:
                cnt += 1
            else:
                cnt -= 1
            
            if cnt == 0:
                candidate = nums[i]
                cnt += 1
            print(candidate, cnt)
            
        return candidate
            
        