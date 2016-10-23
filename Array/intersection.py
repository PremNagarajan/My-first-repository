"""

349. Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].Given

"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if nums1 and nums2:
            return list(set(nums1).intersection(set(nums2)))
        return []
        
s = Solution()
print s.intersection([1, 2, 2, 1], [2, 2])