"""

64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers,

find a path from top left to bottom right which minimizes the sum of all
numbers along its path.

Note: You can only move either down or right at any point in time.

"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        DP = [[0 for j in xrange(n)] for i in xrange(m)]
        
        DP[m-1][n-1] = grid[m-1][n-1]
        
        for j in xrange(n-2, -1, -1):
            DP[m-1][j] = grid[m-1][j] + DP[m-1][j+1]
            
        for i in xrange(m-2, -1, -1):
            DP[i][n-1] = grid[i][n-1] + DP[i+1][n-1]
        
        for i in xrange(m-2, -1, -1):
            for j in xrange(n-2, -1, -1):
                DP[i][j] = grid[i][j] + min(DP[i][j+1], DP[i+1][j])
        
        return DP[0][0]
        
s = Solution()
print s.minPathSum([[1, 1, 1], [1, 1, 1], [1, 1, 1]])