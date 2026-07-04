"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        Intervals = [[obj.start, obj.end] for obj in intervals]

        Intervals.sort()

        if not Intervals:
            return 0

        starts = []
        ends = []
        for i in range(len(Intervals)):
            starts.append(Intervals[i][0])
            ends.append(Intervals[i][1])

        ends.sort()

        s = 0
        e = 0

        rooms = 0
        max_rooms = 0

        while s < len(Intervals):
            print(s, e)
            if starts[s] < ends[e]:
                rooms += 1
                max_rooms = max(rooms, max_rooms)
                s += 1
            elif starts[s] >= ends[e]:
                rooms -= 1
                e += 1


        
        return max_rooms



