'''

10. Regular Expression Matching

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "a*") -> true
isMatch("aa", ".*") -> true
isMatch("ab", ".*") -> true
isMatch("aab", "c*a*b") -> true

'''

# dp
# Time:  O(m * n)
# Space: O(m * n)
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        result = [[False for j in xrange(len(p) + 1)] for i in xrange(len(s) + 1)]
        
        result[0][0] = True
        for i in xrange(2, len(p) + 1):
            if p[i-1] == '*':
                result[0][i] = result[0][i-2]
                    
        for i in xrange(1,len(s) + 1):
            for j in xrange(1, len(p) + 1):
                if p[j-1] == '*':
                    result[i][j] = result[i][j-2] or (result[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
                else:
                    result[i][j] = result[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
                    
        return result[len(s)][len(p)]
                

'''
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s) + 1
        m = len(p) + 1
        
        # Initialize a temp matrix of size n, m
        DP = [[False for j in xrange(m)] for i in xrange(n)]
        
        DP[0][0] = True
        
        for j in xrange(1, m):
            if p[j-1] == '*':
                DP[0][j] = DP[0][j-1]
        
        for i in xrange(1, n):
            for j in xrange(1, m):
                if p[j-1] == '*':
                    DP[i][j] = DP[i][j-1] or DP[i-1][j]
                    
                elif p[j-1] == '.' or s[i-1] == p[j-1]:
                    DP[i][j] = DP[i-1][j-1]

                else:
                    DP[i][j] = False
                    
        return DP[n-1][m-1]

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(s) == 0 and len(p) == 0:
            return True

        if len(s) > 0 and len(p) > 0 and \
            (s[0] == p[0] or p[0] == '.'):
            return self.isMatch(s[1:], p[1:])

        if len(s) > 0 and len(p) > 0 and \
            p[0] == '*':
            return self.isMatch(s, p[1:]) or \
                self.isMatch(s[1:], p) or \
                self.isMatch(s[1:], p[1:])

        else:
            return False
'''
s = Solution()
print(s.isMatch("aa", "a*"))

