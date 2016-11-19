"""
452. Minimum Number of Arrows to Burst Balloons

There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons. 

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

解题思路：

和56题比较像

56题是维护一个能伸到的最大值

这个题要维护的是能伸到的最小值

"""

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda s : s[0])
        ans = 0 
        if len(points) == 0 :
            return 0
        ans = 1
        st = points[0][0]
        ed = points[0][1]
        for i in range(1,len(points)) :
            u = points[i][0]
            v = points[i][1]
            if u > ed :
                ans += 1
                st = u
                ed = v
            else :
                st = u
                ed = min(ed,v)
        return ans
