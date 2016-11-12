"""

90. Subsets II

Given a collection of integers that might contain duplicates, nums,
return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        i = 0
        no_of_subsets = 1 << len(nums)
        res = []
        nums.sort()
        
        for i in xrange(no_of_subsets):
            curr = []
            for j in xrange(len(nums)):
                if i & 1 << j:
                    curr.append(nums[j])
            if curr not in res:
                res.append(curr)
            
        return res
        
print Solution().subsetsWithDup([4,4,4,1,4])