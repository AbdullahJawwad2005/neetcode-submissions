class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # there's a backtracking solution here where you test all posibilities
        # and each possibility ends on the last index or when the index is zero
        # and false if leaves the loop without hitting last index

        # the more efficient solution would be the greedy algorithm
        # how would that work?
        # okay so its apparently you start from the end
        # and when you start from the end thats your goal
        # when you reach something else that can reach your goal then thats your new goal
        # if the first index becomes the goal then viola
        # the issue here is that there can be multiple ways for this to happen but thats alright lets just code this for now, oh actually no if one can reach it it can reach the other

        n = len(nums)
        goal = n - 1
        for i in range(n-2, -1, -1):
            # logic here is that if the current index + amount more than the goal index
            if i + nums[i] >= goal:
                goal = i
            # then that index becomes the goal
        if goal == 0:
            return True
        return False


        