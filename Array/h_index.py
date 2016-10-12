class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        max_h = 0
        i = 0
        for i in range(len(citations)):
            print citations[i]
        return max_h
            
        
        
citations = [3, 0, 6, 1, 5]
s = Solution()
print s.hIndex(citations)