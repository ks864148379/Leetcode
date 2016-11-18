"""
135. Candy
 There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.

What is the minimum candies you must give? 

模拟一遍居然过了。。。。

后来才发现有更好的方式：

从前到后遍历一遍，从后到前在遍历一遍，这种方法更好，前扫描一遍后扫描一遍这种方法适用于很多题目中，应该记住这种方法

"""
##这中方法不好，第二遍刷的时候争取首先想到前后各遍历一遍的方法
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        de = 0
        if len(ratings) == 0 :
            return 0
        cur = 1
        ans = 1
        i = 1
        k = 1
        while( i < len(ratings)) :
            if ratings[i] > ratings[i-1] :
                cur += 1
                k = cur
                ans += cur
                i += 1
            elif ratings[i] == ratings[i-1] :
                cur = 1
                k = cur
                ans += cur
                i += 1
            else :
                i += 1
                cur = 1
                ans += cur
                de = 0
                while(i < len(ratings) and ratings[i] < ratings[i-1]) :
                    cur += 1
                    i += 1
                    ans += cur
                if cur >= k :
                    ans += cur-k+1
                cur = 1
        return ans
