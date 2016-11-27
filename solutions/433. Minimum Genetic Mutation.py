"""
A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

Note:

    Starting point is assumed to be valid, so it might not be included in the bank.
    If multiple mutations are needed, all mutations during in the sequence must be valid.
    You may assume start and end string is not the same.

简单BFS
"""
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        ma = [[0 for x in range(len(bank)+1)] for x in range(len(bank)+1) ]
        for i in range(len(bank)) :
            for j in range(len(bank)) :
                if len(bank[i]) != len(bank[j]) :
                    continue 
                u = 0
                for k in range(len(bank[i])) :
                    if bank[i][k] != bank[j][k] :
                        u += 1
                if u == 1 :
                    ma[i][j] = 1
                    ma[j][i] = 1
                    
        for i in range(len(bank)) :
            if end == bank[i] :
                end = i
            if len(start) != len(bank[i]) :
                continue
            u = 0
            for k in range(len(start)) :
                if bank[i][k] != start[k] :
                    u += 1
            if u == 1:
                ma[len(bank)][i] = 1
                ma[i][len(bank)] = 1

        queue = []
        vis = [-1 for x in range(len(bank)+1)]
        vis[len(bank)] = 0
        queue.append(len(bank))
        while len(queue) > 0 :
            q = queue.pop(0)
            for i in range(len(bank)) :
                if ma[q][i] == 1 and vis[i] == -1 :
                    queue.append(i)
                    vis[i] = vis[q] + 1
                    if i == end :
                        return vis[i]
        return -1
