class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        i = 0
        j = len(height) - 1
        while i < j:
            h = min(height[i], height[j])
            b = j - i
            curr_area = h * b
            if curr_area > max_area:
                max_area = curr_area
            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1
        return max_area

        '''
        max_area = 0
        for i in range(0, len(height)):
            for j in range(i+1, len(height)):
                h = min(height[i], height[j])
                b = j-i
                curr_area = h * b
                if curr_area > max_area:
                    max_area = curr_area

        return max_area
        '''
s = Solution()
print(s.maxArea([3, 0, 0, 2, 0, 4]))