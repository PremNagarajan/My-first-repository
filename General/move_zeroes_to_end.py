"""

283. Move Zeroes
Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function,
nums should be [1, 3, 12, 0, 0].

"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_index = 0
        found_zero = False
        for i in range(len(nums)):
            if not found_zero and nums[i] == 0:
                found_zero = True
                zero_index = i
            if nums[i] != 0 and found_zero:
                nums[zero_index] = nums[i]
                nums[i] = 0
                zero_index += 1
                
s = Solution()
nums = [1, 0, 0, 1]
s.moveZeroes(nums)
print nums