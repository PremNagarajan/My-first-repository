"""

387. First Unique Character in a String

Given a string, find the first non-repeating character in it and
return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = dict()
        for c in s:
            if c in temp:
                temp[c] += 1
            else:
                temp[c] = 1
                
        for i in range(len(s)):
            if temp[s[i]] == 1:
                return i
                
        return -1
        
s = Solution()
print s.firstUniqChar("leetcode")