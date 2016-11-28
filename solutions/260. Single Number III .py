"""
 Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:

    The order of the result is not important. So in the above example, [5, 3] is also correct.
    Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?


找到所有数^后的最后一位为1的位置，这个位置就是最终两个答案的不同的位置
根据这一位用a来对不同的1和0来^
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = 0
        for i in nums :
            a ^= i
        count = 0
        b = a
        while True :
            if (b&1) == 1 :
                break
            b >>= 1
            count += 1
        ans = [0,0]
        
        for i in range(len(nums)) :
            if 1 & (nums[i] >> count ) == 1 :
                ans[0] ^= nums[i]
            else :
                ans[1] ^= nums[i]
        return ans
