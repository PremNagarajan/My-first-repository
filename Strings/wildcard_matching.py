'''

44. Wildcard Matching

Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "*") -> true
isMatch("aa", "a*") -> true
isMatch("ab", "?*") -> true
isMatch("aab", "c*a*b") -> false

'''
#Iterative solution
class Solution(object):
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        s_ptr, p_ptr, last_s_ptr, last_p_ptr = 0, 0, -1, -1
        
        while s_ptr < len(s):
            if p_ptr < len(p) and (s[s_ptr] == p[p_ptr] or p[p_ptr] == '?'):
                s_ptr += 1
                p_ptr += 1
            elif p_ptr < len(p) and p[p_ptr] == '*':
                p_ptr += 1
                last_s_ptr = s_ptr
                last_p_ptr = p_ptr
            elif last_s_ptr != -1:
                last_s_ptr += 1
                s_ptr = last_s_ptr
                p_ptr = last_p_ptr
            else:
                return False
                
        while p_ptr < len(p) and p[p_ptr] == '*':
            p_ptr += 1
        
        return len(p) == p_ptr

    '''
    
    # DP solution
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        DP = [[False for j in xrange(len(p)+1)] for i in xrange(len(s)+1)]
        
        DP[0][0] = True
        
        for j in xrange(1, len(p)+1):
            if p[j-1] == '*':
                DP[0][j] = DP[0][j-1]

        for i in xrange(1, len(s)+1):
            for j in xrange(1, len(p)+1):
                if p[j-1] == '*':
                    DP[i][j] = DP[i][j-1] or DP[i-1][j]
                    
                elif p[j-1] == '?' or s[i-1] == p[j-1]:
                    DP[i][j] = DP[i-1][j-1]

                else:
                    DP[i][j] = False
        return DP[len(s)][len(p)]
        
        
    # Recursive solution
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
print s.isMatch("aa", "a*")