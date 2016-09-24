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

s = Solution()
print(s.isMatch("aa", "a*"))

