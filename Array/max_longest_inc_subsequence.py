'''

Dynamic Programming | Set 14 (Maximum Sum Increasing Subsequence)
Given an array of n positive integers.

Write a program to find the sum of maximum sum subsequence of the given array
such that the intgers in the subsequence are sorted in increasing order.

For example,

if input is {1, 101, 2, 3, 100, 4, 5},
then output should be 106 (1 + 2 + 3 + 100),

if the input array is {3, 4, 5, 10}, then output should be 22 (3 + 4 + 5 + 10)

and if the input array is {10, 5, 4, 3}, then output should be 10

'''

class Solution(object):
    def lengthOfMLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        n = len(nums)
        dp = [num for num in nums]
        
        for i in range(1, n):
            for j in range(0, i):
                if nums[j] < nums[i] and dp[i] < dp[j] + nums[i]:
                    dp[i] = dp[j] + nums[i]
                    
        for curr_max in dp:
            if max < curr_max:
                max = curr_max
                
        return max
            
s = Solution()
print s.lengthOfMLIS([1, 101, 2, 3, 100, 4, 5])
print s.lengthOfMLIS([3, 4, 5, 10])
print s.lengthOfMLIS([10, 5, 4, 3])