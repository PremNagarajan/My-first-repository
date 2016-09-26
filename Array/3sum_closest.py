'''
3Sum Closest

Given an array S of n integers,
Find three integers in S such that the sum is closest to a given number,
target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = list()
        n = len(nums)
        nums = sorted(nums)
        closest = None
        for i in range(0, n-2):
            j = i + 1
            k = n - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    return target
                elif sum < target:
                    j = j + 1
                else:
                    k = k - 1
                if closest is None:
                    closest = sum
                elif abs(sum - target) < abs(closest - target):
                    closest = sum
        return closest

s = Solution()
print(s.threeSumClosest([0, 2, 1, -3], 1))