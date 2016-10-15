class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        #res = ""
        #n = len(s)
        #for i in reversed(range(n)):
        #    res = res + s[i]
        #return res
        return s[::-1]
        
s = Solution()
print s.reverseString("hello")
        