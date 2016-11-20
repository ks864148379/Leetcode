"""
463. Island Perimeter

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected 
horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected 
land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side
length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:

简单题，直接遍历一遍地图即可

"""
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dir = [[1,0],[-1,0],[0,1],[0,-1]]
        n = len(grid)
        m = len(grid[0])
        ans = 0
        for i in range(n) :
            for j in range(m) :
                if grid[i][j] == 1 :
                    ans += 4
                    for k in range(4) :
                        x = i + dir[k][0]
                        y = j + dir[k][1]
                        if x >= 0 and x < n and y >= 0 and y < m and grid[x][y] == 1 :
                            ans -= 1
        return ans

