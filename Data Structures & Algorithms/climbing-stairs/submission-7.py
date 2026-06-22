class Solution:
    def climbStairs(self, n: int) -> int:
        # a recursive problem
        # tries both cases of adding one and zero and recurses
        # base case is if more than target then return zero
        # if equals to target then return one

        memo = {}
        def recursive_solve(curr, target):
            if curr in memo:
                return memo[curr]
            elif curr > target:
                memo[curr] = 0
            elif curr == target:
                memo[curr] = 1
            else:
                one = recursive_solve(curr+1, target)
                two = recursive_solve(curr+2, target)
                memo[curr] = one + two

            return memo[curr]
        

        return recursive_solve(0, n)

        