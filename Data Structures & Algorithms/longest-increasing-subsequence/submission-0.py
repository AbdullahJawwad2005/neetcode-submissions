class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # okay check all subsequences using recursion
        # subsequences are select elements with maintained order
        # so recursion whenever the next element is greater and make a counter for that and return the max

        # so the logic would be that for i to end you recurse over things and if its right then add a counter

        dp = [1]*len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])
        
        return max(dp)
        