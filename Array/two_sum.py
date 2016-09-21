class NumsWithIndex(object):
    data = None
    index = None

    def __init__(self, data, index):
        self.data = data
        self.index = index

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers = list()
        for i in range(0, len(nums)):
            numbers.append(NumsWithIndex(nums[i], i))

        numbers = sorted(numbers, key=lambda x: x.data)

        i = 0
        j = len(numbers) - 1
        while i < j:
            sum = numbers[i].data + numbers[j].data
            if (sum == target):
                return [numbers[i].index, numbers[j].index]
            elif (sum < target):
                i = i+1
            else:
                j = j-1

nums = [3, 2, 4]
target = 6
s = Solution()
print s.twoSum(nums, target)