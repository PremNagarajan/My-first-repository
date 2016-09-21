class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_map = dict()
        max_so_far = 0
        curr_max = 0
        start = 0
        for i in range(0, len(s)):
            if s[i] in  hash_map:
                if curr_max > max_so_far:
                    max_so_far = curr_max
                if hash_map[s[i]] > start:
                    start = hash_map[s[i]]
                curr_max = i - start
                hash_map[s[i]] = i
            else:
                hash_map[s[i]] = i
                curr_max = curr_max + 1

        if curr_max > max_so_far:
            max_so_far = curr_max

        return max_so_far

s = Solution()
print s.lengthOfLongestSubstring('pwwkew')
