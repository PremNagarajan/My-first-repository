"""

73. Set Matrix Zeroes


Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        first_row_has_zero = False
        for j in xrange(n):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break
        
        first_col_has_zero = False
        for i in xrange(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break
        
        for i in xrange(1, m):
            for j in xrange(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    
        for j in xrange(1, n):
            if matrix[0][j] == 0:
                for i in xrange(1, m):
                    matrix[i][j] = 0
                    
        for i in xrange(1, m):
            if matrix[i][0] == 0:
                for j in xrange(1, n):
                    matrix[i][j] = 0
                    
        if first_row_has_zero:
            for j in xrange(n):
                matrix[0][j] = 0
                
        if first_col_has_zero:
            for i in xrange(m):
                matrix[i][0] = 0


'''
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row_index = []
        column_index = []
        m = len(matrix)
        n = len(matrix[0])
        
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    if i not in row_index:
                        row_index.append(i)
                    if j not in column_index:
                        column_index.append(j)
                        
        for i in row_index:
            for j in xrange(n):
                matrix[i][j] = 0
                
        for i in xrange(m):
            for j in column_index:
                matrix[i][j] = 0
                
'''

matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
Solution().setZeroes(matrix)
print matrix