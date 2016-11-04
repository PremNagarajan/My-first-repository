"""

72. Edit Distance

Given two words word1 and word2,
find the minimum number of steps required to convert word1 to word2.
(each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

"""

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1) + 1
        n = len(word2) + 1
        
        DP = [[0 for j in xrange(n)] for i in xrange(m)]
        
        for i in xrange(m):
            DP[i][0] = i
            
        for j in xrange(n):
            DP[0][j] = j
            
        for i in xrange(1, m):
            for j in xrange(1, n):
                insert = DP[i][j-1] + 1
                delete = DP[i-1][j] + 1
                if word1[i-1] != word2[j-1]:
                    replace = DP[i-1][j-1] + 1
                else:
                    replace = DP[i-1][j-1]
                DP[i][j] = min(insert, delete, replace)
                
        return DP[m-1][n-1]
        
s = Solution()
print s.minDistance("abs", "cat")