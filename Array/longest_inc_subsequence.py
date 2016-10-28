'''

300. Longest Increasing Subsequence

Given an unsorted array of integers,
find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.

Note that there may be more than one LIS combination,
it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

For example, length of LIS for { 10, 22, 9, 33, 21, 50, 41, 60, 80 } is 6 and
LIS is {10, 22, 33, 50, 60, 80}

'''

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        n = len(nums)
        dp = [1 for i in xrange(n)]
        
        for i in range(1, n):
            for j in range(0, i):
                if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    
        for curr_max in dp:
            if max < curr_max:
                max = curr_max
                
        return max
        
s = Solution()
print s.lengthOfLIS([10, 22, 9, 33, 21, 50, 41, 60, 80])