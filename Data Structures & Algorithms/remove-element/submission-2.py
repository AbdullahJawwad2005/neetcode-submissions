class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        first = 0
        last = len(nums) - 1

        while first <= last:
            if nums[first] == val:
                nums[first] = nums[last]
                last -= 1
            else:
                first += 1

        return first


        