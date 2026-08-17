"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        result = sorted(intervals, key = lambda x:x.start)

        for i in range(1,len(result)):
            if result[i].start < result[i-1].end:
                return False

        return True


        