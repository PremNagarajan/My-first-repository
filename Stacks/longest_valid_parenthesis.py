'''

32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()",
which has length = 2.

Another example is ")()())",
where the longest valid parentheses substring is "()()", which has length = 4.
'''

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = list()
        res = 0
        stack.append(-1)
        
        i = 0
        for c in s:
            if c == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        top = stack.pop()
                        cur = i - top
                        if cur > res:
                            res = cur
                        stack.append(top)
                    else:
                        stack.append(i)
            i += 1
                
        return res
        
s = Solution()
print s.longestValidParentheses(")()())()()(")