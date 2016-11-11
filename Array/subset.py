"""

78. Subset

Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        i = 0
        no_of_subsets = 1 << len(nums)
        res = []
        
        for i in xrange(no_of_subsets):
            curr = []
            for j in xrange(len(nums)):
                if i & 1 << j:
                    curr.append(nums[j])
            res.append(curr)
            
        return res
        
print Solution().subsets([1, 2, 3])