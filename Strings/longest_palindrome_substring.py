class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length:
            max_len = 1
            max_string = s[0]
        else:
            return

        new_string = '#'
        for i in range(0, length):
            new_string = new_string + s[i] + '#'
        s = new_string
        length = len(s)

        # Palindrome of odd length
        for i in range(0, length):
            curr_len = 1
            curr_string = s[i]
            start = i - 1
            end = i + 1
            while start >= 0 and end < length:
                if s[start] == s[end]:
                    curr_len = curr_len + 2
                    curr_string = s[start] + curr_string + s[end]
                    if curr_len > max_len:
                        max_len = curr_len
                        max_string = curr_string
                    start = start - 1
                    end = end + 1
                else:
                    break
            i = i + 1

        '''
        # Palindrome of even length
        for i in range(0, length):
            curr_len = 0
            curr_string = None
            start = i
            end = i + 1
            while start >= 0 and end < length:
                if s[start] == s[end]:
                    curr_len = curr_len + 2
                    if curr_string:
                        curr_string = s[start] + curr_string + s[end]
                    else:
                        curr_string = s[start] + s[end]
                    if curr_len > max_len:
                        max_len = curr_len
                        max_string = curr_string
                    start = start - 1
                    end = end + 1
                else:
                    break
            i = i + 1
        '''

        return max_string.replace('#', '')

s = Solution()
string = "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"
print(s.longestPalindrome(string))

