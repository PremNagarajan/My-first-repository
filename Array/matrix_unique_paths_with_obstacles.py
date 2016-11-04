"""

63. Unique Paths II

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids.

How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

"""

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        DP = [[0 for j in xrange(n)] for i in xrange(m)]
        
        for j in xrange(n-1, -1, -1):
            if obstacleGrid[m-1][j] == 1:
                break
            DP[m-1][j] = 1
            
        for i in xrange(m-1, -1, -1):
            if obstacleGrid[i][n-1] == 1:
                break
            DP[i][n-1] = 1
        
        for i in xrange(m-2, -1, -1):
            for j in xrange(n-2, -1, -1):
                if obstacleGrid[i][j] == 1:
                    continue
                if obstacleGrid[i][j+1] != 1:
                    DP[i][j] += DP[i][j+1]
                if obstacleGrid[i+1][j] != 1:
                    DP[i][j] += DP[i+1][j]
        
        return DP[0][0]

s = Solution()
print s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])