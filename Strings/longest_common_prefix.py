"""

14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i in xrange(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or strs[0][i] != string[i]:
                    return string[:i]

        return strs[0]

'''
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
'''

s = Solution()
print(s.longestCommonPrefix(['priya', 'prem']))