"""

31. Next Permutation

Implement next permutation, which rearranges numbers into the
lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the
lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and
its corresponding outputs are in the right-hand column.

1,2,3 -> 1,3,2
3,2,1 -> 1,2,3
1,1,5 -> 1,5,1

"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = None
        
        for i in xrange(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                k = i
                break
                
        if k is None:
            nums.reverse()
            return
            
        for i in xrange(len(nums)-1, k, -1):
            if nums[k] < nums[i]:
                nums[k], nums[i] = nums[i], nums[k]
                nums[k+1:len(nums)] = nums[len(nums):k:-1]
                return
        
        
s = Solution()
nums = [5, 3, 4, 9, 7, 6]
s.nextPermutation(nums)
print nums

nums = [1, 3, 4, 2]
s.nextPermutation(nums)
print nums