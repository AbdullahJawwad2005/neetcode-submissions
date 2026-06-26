class Solution:
    def rob(self, nums: List[int]) -> int:
        # okay just put a tracker in which makes sure that the final element doesnt go in if the start one is already

        # okay the method is two separate arrays here. 
        # one with the last index there and one without
        if len(nums) == 1:
            return nums[0]
        
        first = nums[1:]
        last = nums[:-1]

        # then run the same algo on both

        rob1 = 0
        rob2 = 0

        rob3 = 0
        rob4 = 0

        for i in range(len(first)):
            temp1 = max(rob1 + first[i], rob2)
            rob1 = rob2
            rob2 = temp1

            temp2 = max(rob3 + last[i], rob4)
            rob3 = rob4
            rob4 = temp2
        
        
        
        if rob4 > rob2:
            return rob4
        return rob2

            




        