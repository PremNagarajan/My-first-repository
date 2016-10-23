"""

169. Majority Element

Given an array of size n, find the majority element.
The majority element is the element that appears more than n/2 times.

You may assume that the array is non-empty and
the majority element always exist in the array.

"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj_index = 0
        count = 1
        index = 0
        for a in nums:
            if a == nums[maj_index]:
                count += 1
            else:
                count -= 1
            if count == 0:
                maj_index = index
                count = 1
            index += 1
                
        maj_elt = nums[maj_index]
        count = 0
        n = len(nums) / 2
        for a in nums:
            if a == maj_elt:
                count += 1
                if count >= n:
                    return maj_elt
            
s = Solution()
print s.majorityElement([1, 2, 2])