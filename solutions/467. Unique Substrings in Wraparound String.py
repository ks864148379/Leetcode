"""
Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.
思路：
只要记录住以某个字符结尾的最大的连续的字符串长度就可以了
一开始想得有点跑偏了
不用统计这一段里面有多少个字串
"""
class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        dp = [0 for x in range(26)]
        if len(p) == 0:
            return 0
        count = 1
        dp[ord(p[0])-ord("a")] = 1
        for i in range(1,len(p)):
            if ord(p[i])-ord("a") == (ord(p[i-1])-ord("a")+1)%26:
                dp[ord(p[i])-ord("a")] = max(dp[ord(p[i])-ord("a")],count+1)
                count += 1
            else :
                count = 1
                dp[ord(p[i])-ord("a")] = max(dp[ord(p[i])-ord("a")],count)
        ans = 0
        for i in range(26):
            ans += dp[i]
        return ans
