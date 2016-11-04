'''

53. Maximum Subarray

Find the contiguous subarray within an array (containing at least one number)
which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.


'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        
        #curr_start_index = 0
        #max_start_index = 0
        #max_end_index = 0
        
        max_so_far = nums[0]
        curr_max = nums[0]
        
        for i in range(1, len(nums)):
            curr_max = max(nums[i], nums[i]+curr_max)
            if curr_max > max_so_far:
                max_so_far = curr_max
                #max_start_index = curr_start_index
                #max_end_index = i
            #if curr_max < 0:
                #curr_start_index = i + 1
                
        if max_so_far < 0:
            largest = nums[0]
            for i in range(1, len(nums)):
                if nums[i] > largest:
                    largest = nums[i]
            #return [largest]
            return largest
                
        #return nums[max_start_index:max_end_index]
        return max_so_far
        
s = Solution()
print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print s.maxSubArray([0])