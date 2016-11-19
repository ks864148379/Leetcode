"""
56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18]. 

解题思路：

先排序，然后从后往前维护一个连接的最大值就可以了，Hard难度名不符实

"""
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0 :
            return []
        intervals.sort(key=lambda x:x.start)
        st = intervals[0].start
        ed = intervals[0].end
        far = ed
        ans = []
        for i in range(1,len(intervals)) :
            if far < intervals[i].start :
                p = Interval(st,far)
                ans.append(p)
                st = intervals[i].start
                far = intervals[i].end
            else :
                far = max(far,intervals[i].end)
        p = Interval(st,far)
        ans.append(p)
        return ans
