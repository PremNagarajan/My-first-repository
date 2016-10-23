"""

136. Single Number

Given an array of integers, every element appears twice except for one.
Find that single one.
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = 0
        for i in nums:
            r = r^i
        return r
        
s = Solution()
print s.singleNumber([1, 2, 2])