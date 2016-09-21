def print_intervals(intervals):
    for interval in intervals:
        print "[", interval.start, ",", interval.end, "]",
    print

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []

        intervals = sorted(intervals, key=lambda interval: interval.start)
        result = list()
        result.append(intervals[0])
        res_i = 0

        for i in range(1, len(intervals)):
            if result[res_i].end >= intervals[i].start:
                start = min(result[res_i].start, intervals[i].start)
                end = max(result[res_i].end, intervals[i].end)
                curr = Interval(start, end)
                result.pop()
                result.append(curr)
            else:
                result.append(intervals[i])
                res_i = res_i + 1

        return result

i1 = Interval(1, 3)
i2 = Interval(2, 6)
i3 = Interval(8, 10)
i4 = Interval(15, 18)

#i1 = Interval(2, 4)
#i2 = Interval(1, 3)
#i3 = Interval(2, 4)
#i4 = Interval(4, 7)

intervals = [i1, i4, i3, i2]
s=Solution()
result = s.merge(intervals)
print_intervals(result)