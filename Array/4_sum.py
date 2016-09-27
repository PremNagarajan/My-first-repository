'''
Given an array S of n integers, are there elements a, b, c, and d in S
such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

'''

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        solution = list()
        nums = sorted(nums)
        for i in range(0, n):
            for j in range(i+1, n):
                k = j + 1
                l = n - 1
                while k < l:
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum == target:
                        curr = [nums[i], nums[j], nums[k], nums[l]]
                        if curr not in solution:
                            solution.append(curr)
                        k = k + 1
                        l = l - 1
                    elif sum < target:
                        k = k + 1
                    else:
                        l = l - 1
        return solution

nums = [1, 0, -1, 0, -2, 2]
target = 0
s = Solution()
print(s.fourSum(nums, target))