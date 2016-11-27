"""
 Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100 

解题思路：
dp[i][j]表示i，j范围内的球都破掉可以得到的最大值
"""
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [[0 for x in range(len(nums))] for x in range(len(nums)) ]
        if len(nums) == 1 :
            return nums[0]
        if len(nums) == 0 :
            return 0
        dp[0][0] = nums[0]*nums[1]
        dp[len(nums)-1][len(nums)-1] = nums[-1]*nums[-2]
        for i in range(1,len(nums)-1) :
            dp[i][i] = nums[i-1] * nums[i] * nums[i+1]
        for k in range(2,len(nums)+1) :
            for i in range(len(nums)) :
                if i + k - 1 >= len(nums) :
                    break
                for j in range(i,k+i) :
                    a = nums[i-1] if i-1>=0 else 1
                    b = nums[i+k] if i+k<len(nums) else 1
                    c = dp[i][j-1] if j-1>=i else 0
                    d = dp[j+1][i+k-1] if j+1<=i+k-1 else 0
                    dp[i][k+i-1] = max(dp[i][i+k-1],c+d+a*nums[j]*b)
        return dp[0][len(nums)-1]312. Burst Balloons
