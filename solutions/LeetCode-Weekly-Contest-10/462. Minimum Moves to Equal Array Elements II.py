”“”
Minimum Moves to Equal Array Elements II

Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]


之前做过一个这个题的第一个版本，那个版本比这个要难一些

思路就是维护一个点的左边所有点变成这个点的代价，在从后往前维护右边所有点变成这个点的代价

前扫一遍后扫一遍和股票那个题很像
“”“
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        dp1 = [0 for x in range(len(nums))]
        dp2 = [0 for x in range(len(nums))]    
        
        for i in range(1,len(nums)) :
            dp1[i] = dp1[i-1] + (i) * (nums[i] - nums[i-1])
        for i in range(len(nums)-2,-1,-1) :
            dp2[i] = dp2[i+1] + (len(nums)-1-i) * (nums[i+1] - nums[i])
        ans = 2**32
        for i in range(len(nums)) :
            ans = min(ans,dp1[i]+dp2[i])

        return ans
