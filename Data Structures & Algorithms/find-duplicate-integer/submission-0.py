class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # okay so whats the problem here exactly? you have an array of n+1 of 1, to n 
        # and theres only one integer that can repeat multiple times

        # by using a set
        seen = set()

        # for loop iterate
        for n in nums:
            # if not in the set then we basically put it in
            if n not in seen:
                seen.add(n)
            # if is then this is the duplicate and we return that
            else: 
                return n
        