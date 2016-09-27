'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid
but "(]" and "([)]" are not.

'''
open_para = ['(', '{', '[']
close_para = [')', '}', ']']

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = list()
        for c in s:
            if c in open_para:
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if c == ')' and top != '(':
                    return False
                elif c == '}' and top != '{':
                    return False
                elif c == ']' and top != '[':
                    return False
        if len(stack) != 0:
            return False
        return True

s = Solution()
print(s.isValid('()[]{}'))
