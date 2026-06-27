class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if not nums:
            return 0

        max_num = 1
        min_num = 1

        global_max = max(nums)

        for n in nums:
            if n == 0:
                max_num = 1
                min_num = 1
            else:
                temp = max_num
                max_num = max(n, max_num*n, min_num*n)
                min_num = min(n, temp*n, min_num*n)
                global_max = max(global_max, max_num)

            

        return global_max



        