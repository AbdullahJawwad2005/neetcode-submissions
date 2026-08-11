from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # this is pretty brute force
        # count in a dictionary
        # iterate over the dictionary and make lists within lists
        # then sort that and get whats best.
        
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        

        frequencies = [[] for _ in range(len(nums)+1)]
        for num, freq in counts.items():
            frequencies[freq].append(num)
        
        result = []

        for frequency in range(len(nums), 0, -1):
            for num in frequencies[frequency]:
                result.append(num)

                if len(result) == k:
                    return result

            


