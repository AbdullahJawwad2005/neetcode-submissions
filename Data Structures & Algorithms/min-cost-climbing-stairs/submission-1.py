class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # okay read the fuckass problem first Abdullah
        # so this is a cost problem as well -> the issue is that cost is not greedy, since this is DP you might have to explore all possible paths
        # how can we break this down into smaller repeated problems? 
        # start from the top, and try all recursive sums and return the minimum is probably a good soluton, lets try coding that
        # 
        #
        #

        # start from the last element, then go down to n-1 and n, and return their sums
        # how to find min, choose the local min sum at any given point
        memo = {0 : cost[0], 1 : cost[1]}
        def f(n):
            
            if n == 0:
                return memo[0]
            if n == 1:
                return memo[1]

            if n-2 not in memo:
                memo[n-2] = f(n-2)
            if n-1 not in memo:
                memo[n-1] = f(n-1)
            
            return cost[n] + min(memo[n-1], memo[n-2])
        
        n = len(cost)
        
        return min(f(n-2), f(n-1))

        # okay now convert to a memoization solution, we don't need to use repeated stuff a so have a dictionary that checks 
        # I'm guessing it would have to check if both were in memoization first, if only one wasn't then run the other while looking from dict
        # if both are you can just return that
        # how do you add to a dictionary in the first place, before returning add the stuff to a dict and use that



        