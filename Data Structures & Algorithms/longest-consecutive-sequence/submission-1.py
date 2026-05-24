class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # okay so see for the elements that are in an array what
        # exactly combines to form the longest sequence of integers
        # that are consecutive in order
        # need to deal with repeats
        # okay one thing that we could do at the start is sort them
        # then use a set. see if theres a duplicate first then skip if is
        # if is not and is one more than previous then add

        # [2, 3, 4, 4, 5, 10, 20]
        # okay no how about make an array that has len of list
        if len(nums) == 0:
            return 0

            
        nums.sort()
        collections = [[nums[0]]]
        
        j = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]+1:
                collections[j].append(nums[i])
            elif nums[i] == nums[i-1]:
                continue
            else:
                collections.append([nums[i]])
                j = j + 1
            print(collections)
        maximum = collections[0]
        for i in range(len(collections)):
            if len(collections[i]) > len(maximum):
                maximum = collections[i]
        
        return len(maximum)



        