"""

54. Spiral Matrix

Given a matrix of m x n elements (m rows, n columns),
return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

You should return [1,2,3,6,9,8,7,4,5]

"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        if len(matrix) == 1:
            return matrix[0]
        
        res = []
        
        left = 0
        right = len(matrix[0])-1
        top = 0
        bottom = len(matrix)-1
        
        
        while left <= right and top <= bottom:
            
            for j in xrange(left, right+1):
                res.append(matrix[top][j])
   
            for i in xrange(top+1, bottom):
                res.append(matrix[i][right])
    
            for j in reversed(xrange(left, right+1)):
                if top < bottom:
                    res.append(matrix[bottom][j])
  
            for i in reversed(xrange(top+1, bottom)):
                if left < right:
                    res.append(matrix[i][left])
                
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        
        return res
        
print Solution().spiralOrder([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]])