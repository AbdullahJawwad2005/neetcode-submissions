class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        memo = [0]*(n+1)
        memo[1], memo[0] = cost[1], cost[0]

        for i in range(2, n):
            memo[i] = min(memo[i-1], memo[i-2]) + cost[i]
        
        memo[-1] = min(memo[n-1], memo[n-2])
        
        return memo[-1]



        