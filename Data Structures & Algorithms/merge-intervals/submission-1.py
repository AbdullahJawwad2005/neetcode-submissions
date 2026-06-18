class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # okay have a merged element
        # basically check if the next ending is bigger than the previous ending, if yes then that concatenates until a starting is bigger than it
        intervals.sort()
        merged = []
        for i in range(len(intervals)):
            if not merged or merged[-1][1] < intervals[i][0]:
                merged.append(intervals[i])
            else:
                if merged[-1][1] < intervals[i][1]:
                    merged[-1][1] = intervals[i][1]
            
        
        return merged
        