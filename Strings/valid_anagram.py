"""

242. Valid Anagram

Given two strings s and t,
write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        temp = dict()
        for c in s:
            if c in temp:
                temp[c] += 1
            else:
                temp[c] = 1
        
        for c in t:
            if c in temp:
                temp[c] -= 1
            else:
               return False
               
        for v in temp.itervalues():
            if v != 0:
                return False
        
        return True
        
s = Solution()
print s.isAnagram("ana", "naa")