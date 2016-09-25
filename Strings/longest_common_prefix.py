class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        res = ''
        j = 0
        if n == 1:
            return strs.pop()

        while n > 1:
            for i in range(0, n-1):
                if j == len(strs[i]) or \
                   j == len(strs[i+1]) or \
                   strs[i][j] != strs[i+1][j]:
                    return res
            res = res + strs[i][j]
            j = j + 1
        return res

s = Solution()
print(s.longestCommonPrefix(['priya', 'prem']))