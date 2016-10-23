"""

217. Contains Duplicate

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice
in the array, and it should return false if every element is distinct.

"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp = dict()
        for n in nums:
            if n in temp:
                return True
            else:
                temp[n] = 1
        return False
                    
s = Solution()
print s.containsDuplicate([1, 2, 2])