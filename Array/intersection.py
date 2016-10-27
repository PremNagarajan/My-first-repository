"""

349. Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].Given

"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        i = 0
        j = 0
        n1 = len(nums1)
        n2 = len(nums2)
        res = []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        return res
        
s = Solution()
print s.intersection([1, 2, 2, 1], [2, 2])