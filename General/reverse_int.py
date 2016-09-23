class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        neg = False
        if x < 0:
            neg = True
            x = -1 * x
        while x:
            rem = x % 10
            res = res * 10 + rem
            x = x / 10
        if neg:
            res = -1 * res
        if res > 2147483647 or res < -2147483648:
            return 0
        return res

s = Solution()
print(s.reverse(1))