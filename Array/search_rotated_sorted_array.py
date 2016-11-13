"""

33. Search in Rotated Sorted Array

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = low + ((high - low) / 2)
            
            if nums[mid] == target:
                return mid
                
            elif (nums[low] <= nums[mid] and nums[low] <= target <= nums[mid]) or \
                 (nums[low] > nums[mid] and not nums[mid] <= target <= nums[high]):
                high = mid - 1
            
            else:
                low = mid + 1
        
        return -1
        
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in xrange(len(nums)):
            if nums[i] == target:
                return i
        return -1
'''

print Solution().search([4,5,1,2,3],4)