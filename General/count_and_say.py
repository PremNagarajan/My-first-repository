"""

38. Count and Say

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        seq = '1'
        for i in xrange(n-1):
            seq = self.getSeq(seq)
        return seq
        
    def getSeq(self, seq):
        res = ""
        i = 0
        while i < len(seq):
            curr_cnt = 1
            while i+1 < len(seq) and seq[i] == seq[i+1]:
                curr_cnt += 1
                i += 1
            res = res + str(curr_cnt) + seq[i]
            i += 1
        return res
        
print Solution().countAndSay(4)