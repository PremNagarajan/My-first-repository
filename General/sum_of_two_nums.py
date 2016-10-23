"""
371. Sum of Two Integers

Calculate the sum of two integers a and b,
but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

"""

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        carry = 0
        max_num = 0xFFFFFFFF
        while b != 0:
            sum = a ^ b
            carry = a & b
            a = sum
            b = carry << 1
            if b > max_num:
                a = (a&max_num) 
                break
        return a
        
s = Solution()
print s.getSum(-12, 8)