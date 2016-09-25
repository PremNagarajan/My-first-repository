rnums = dict()
rnums['M'] = 1000
rnums['D'] = 500
rnums['C'] = 100
rnums['L'] = 50
rnums['X'] = 10
rnums['V'] = 5
rnums['I'] = 1

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0
        for i in range(0, n):
            if i + 1 < n:
                if rnums[s[i+1]] > rnums[s[i]]:
                    ans = ans - rnums[s[i]]
                    continue
            ans = ans + rnums[s[i]]
        return ans

s = Solution()
print(s.romanToInt('MCDLXIX'))