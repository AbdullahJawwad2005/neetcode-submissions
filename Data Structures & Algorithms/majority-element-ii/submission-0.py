class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        counter = defaultdict(int)

        for n in nums:
            counter[n] += 1

            if len(counter) > 2:
                temp = defaultdict(int)
                for k, v in counter.items():
                    counter[k] -= 1
                    if counter[k] != 0:
                        temp[k] = counter[k]
                counter = temp
        
        res = []
        for n in counter:
            if nums.count(n) > len(nums)//3:
                res.append(n)
        
        return res
        
