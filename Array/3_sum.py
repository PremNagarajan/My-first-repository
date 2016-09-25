'''
Given an array S of n integers,
Are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],
[-4, -1, -1, 0, 1, 2]
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = list()
        n = len(nums)
        nums = sorted(nums)
        for i in range(0, n-2):
            j = i + 1
            k = n - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    curr = [nums[i], nums[j], nums[k]]
                    if curr not in res:
                        res.append(curr)
                    j = j + 1
                    k = k - 1
                elif sum < 0:
                    j = j + 1
                else:
                    k = k - 1
        return res

s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))