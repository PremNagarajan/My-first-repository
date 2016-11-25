"""
69. Sqrt(x)

Implement int sqrt(int x)

"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
            
        low, high = 1, x/2
        while low <= high:
            mid = low + (high - low) / 2
            temp = mid * mid
            if temp == x:
                return mid
            elif temp > x:
                high = mid - 1
            else:
                low = mid + 1
        return high

print Solution().mySqrt(0)
print Solution().mySqrt(1)
print Solution().mySqrt(2)
print Solution().mySqrt(4)
print Solution().mySqrt(16)
print Solution().mySqrt(25)