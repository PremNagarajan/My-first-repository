class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        max_h = 0
        N = len(citations)
        citations = sorted(citations, reverse=True)
        temp = []
        for i in range(N):
            temp.append(min(i+1, citations[i]))
        return max(temp)
        
#citations = [25, 8, 5, 3, 3]
#citations = [10, 8, 5, 4, 3]
citations = [3, 3, 0, 6, 1, 5]
s = Solution()
print s.hIndex(citations)