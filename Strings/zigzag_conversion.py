class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        res = ""
        leng = len(s)
        for i in range(0, numRows):
            j = i
            column = True
            while True:
                if j > leng-1:
                    break
                res = res + s[j]
                if i == 0 or i == numRows - 1:
                    x = 2*numRows - 2
                else:
                    if column:
                        x = 2*numRows - 2 - 2*i
                        column = False
                    else:
                        x = 2*i
                        column = True
                j = j + x
        return res

s = Solution()
print(s.convert("PAYPALISHIRING", 6))