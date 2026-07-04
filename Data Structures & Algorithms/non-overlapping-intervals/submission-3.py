class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()

        remove = 0
        previous_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if previous_end > intervals[i][0]:
                previous_end = min(previous_end, intervals[i][1])
                remove+=1
            else:
                previous_end = intervals[i][1]
        
        return remove
            


        