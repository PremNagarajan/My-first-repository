"""

27. Remove Element

Given an array and a value, remove all instances of that value in place and
return the new length.

Do not allocate extra space for another array,
you must do this in place with constant memory.

The order of elements can be changed.
It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2,
with the first two elements of nums being 2.

"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        
        curr = 0
        i = 0
        
        while i < len(nums):
            if nums[i] != val:
                nums[curr] = nums[i]
                curr += 1
            i += 1
            
        return curr
        
s = Solution()
nums = [1, 2, 3, 4]
print nums[:s.removeElement(nums, 1)]