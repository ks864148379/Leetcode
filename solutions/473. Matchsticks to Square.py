Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

Example 1:

Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

Example 2:

Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.

Note:

    The length sum of the given matchsticks is in the range of 0 to 10^9.
    The length of the given matchstick array will not exceed 15.
“”“
思路：
看到15就想到了状态压缩dp。。。。

dp[i]表示状态i下对边长的取余
“”“
class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        if len(nums) < 4:
            return False
        all = 0
        for i in nums:
            all += i
        if all % 4 != 0:
            return False
        bian = all / 4
        dp = [-1 for x in range(2**len(nums))]
        dp[0] = 0
        for i in range(2**len(nums)):
            for j in range(len(nums)):
                if i & (1<<j) == 0 and dp[i] != -1:
                    if dp[i] + nums[j] > bian :
                        continue
                    elif dp[i] + nums[j] == bian:
                        dp[i+(1<<j)] = 0
                    else:
                        dp[i+(1<<j)] = dp[i] + nums[j]
        if dp[2**len(nums) - 1] == 0:
            return True
        else:
            return False
