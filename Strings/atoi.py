def is_valid_number(str):
    if str.count('+') > 1 or str.count('-') > 1:
        return 0
    if '+' in str and '-' in str:
        return 0
    return 1

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        res = 0
        if not is_valid_number(str):
            return res
        str = str.lstrip(' ')
        for i in range(0, len(str)):
            if str[i] == '-' or str[i] == '+':
                continue
            if ord(str[i]) < 48 or ord(str[i]) > 57:
                break
            if str[i] == ' ':
                break
            res = res * 10 + ord(str[i]) - 48
        if str and str[0] == '-':
            res = -1 * res
        if res > 2147483647:
            res = 2147483647
        elif res < -2147483648:
            res = -2147483648
        return res


s = Solution()
print(s.myAtoi("1"))
# String value = 98993489, Int value = 98993489