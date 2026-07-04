"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        Intervals = [[obj.start, obj.end] for obj in intervals]
        Intervals.sort()

        for i in range(1, len(Intervals)):
            if Intervals[i][0] < Intervals[i-1][1]:
                return False

        
        return True
