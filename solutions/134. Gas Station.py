”“”
134. Gas Station

 There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1. 


解题思路：
  n**2的思路不说了，很简单
  先做一个处理，把每个点的gas[i]-cost[i]构成一个新的数组，若为正表示从这点出发走一站有剩余，为负表示不够
  因为所有的gas station是一个circle，于是想到解这种问题的一种方法：把数组拼接成2倍的
  然后想到用前后指针
  走一步，如果总的gas还为正，那么继续往下走
  如果走一步之后总的gas为负，那么从这个station的下个station重新开始走
“”“
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        c = []
        for i in range(len(gas)) :
            c.append(gas[i] - cost[i])
        for i in range(len(gas)) :
            c.append(gas[i] - cost[i])
        st = 0
        ed = 0
        le = 0
        all = 0
    
        while(st < len(c)) :
            if le == len(gas) :
                return ed % len(gas)
            all += c[st]
            st += 1
            le += 1
            if all < 0 :
                ed = st
                le = 0
                all = 0
                
        return -1
