"""

62. Unique Paths

A robot is located at the top-left corner of a m x n grid
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid
(marked 'Finish' in the diagram below).

How many possible unique paths are there?

For a 3 x 3 grid, there are 6 paths.

"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < n:
            return self.uniquePaths(n, m)

        DP = [1] * n
        
        for i in xrange(m-2, -1, -1):
            for j in xrange(n-2, -1, -1):
                DP[j] += DP[j+1]
                
        return DP[0]
        
        '''
        DP = [[0 for j in xrange(n)] for i in xrange(m)]
        
        DP[m-1][n-1] = 0
        
        for i in xrange(m):
            DP[i][n-1] = 1
            
        for j in xrange(n):
            DP[m-1][j] = 1
            
        for i in xrange(m-2, -1, -1):
            for j in xrange(n-2, -1, -1):
                DP[i][j] = DP[i][j+1] + DP[i+1][j]
                
        return DP[0][0]
        '''
        
s = Solution()
print s.uniquePaths(7, 3)