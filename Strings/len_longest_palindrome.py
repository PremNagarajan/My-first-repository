"""
409. Longest Palindrome

Given a string which consists of lowercase or uppercase letters,
find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = dict()
        
        for c in s:
            if c not in temp:
                temp[c] = 1
            else:
                temp[c] += 1
            
        seen_odd = False
        odd_len = 0
        even_len = 0
        
        for value in temp.itervalues():
            if value % 2 == 0:
                even_len += value
            else:
                if not seen_odd:
                    seen_odd = True
                    odd_len = value
                else:
                    if value > odd_len:
                        even_len = even_len + odd_len - 1
                        odd_len = value
                    else:
                        even_len = even_len + value - 1

        return even_len + odd_len    
        
s = Solution()
string = "abbcbaadcbb"
print s.longestPalindrome(string)