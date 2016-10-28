"""

56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

"""

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    
    def __str__(self):
        return '(' + str(self.start) + ', ' + str(self.end) + ')'

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return intervals

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
s = Solution()
res = s.merge([i1, i2, i3, i4])
for r in res:
    print r,