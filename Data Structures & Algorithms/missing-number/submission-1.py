class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # here we use the NOT operator (^) which cancels out duplicates, so our final number
        # is something that isnt a duplicate

        # no its saying without duplicates and you have to figure out whats not there
        # so through multiplication instead?

        # wait a second, its not 

        res = 0
        for i in range(len(nums)):
            res ^= i^nums[i]
        res ^= len(nums)
        return res

        