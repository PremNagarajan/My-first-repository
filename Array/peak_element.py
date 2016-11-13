"""

162. Find Peak Element

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] != num[i+1],
find a peak element and return its index.

The array may contain multiple peaks,
in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -infinity.

For example, in array [1, 2, 3, 1],
3 is a peak element and your function should return the index number 2.

"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = low + (high - low) / 2
            
            if (mid == 0 or nums[mid-1] < nums[mid]) and \
               (mid+1 == len(nums) or nums[mid] > nums[mid+1]):
                return mid
            elif mid > 0 and nums[mid-1] > nums[mid]:
                high = mid
            else:
                low = mid + 1
            
        return low
        
print Solution().findPeakElement([1,2,3,1])