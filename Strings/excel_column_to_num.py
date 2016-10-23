"""

171. Excel Sheet Column Number

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 

"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        i = 0
        for c in reversed(s):
            res += (ord(c) - 64) * pow(26, i)
            i += 1
        return res
        
s = Solution()
print s.titleToNumber("AB")