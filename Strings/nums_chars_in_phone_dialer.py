'''
Letter Combinations of a Phone Number.

Given a digit string, return all possible letter combinations that
the number could represent.

A mapping of digit to letters (just like on the telephone buttons)
is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''
nums = dict()
nums[0] = ''
nums[1] = ''
nums[2] = ['abc']
nums[3] = ['def']
nums[4] = ['ghi']
nums[5] = ['jkl']
nums[6] = ['mno']
nums[7] = ['pqrs']
nums[8] = ['tuv']
nums[9] = ['wxyz']

class Solution(object):
    def letters(self, digits, curr, n, res):
        if curr == n:
            return
        print 'curr', curr
        print 'nums[curr]', nums[curr]
        print 'len(nums[curr])', len(nums[curr])
        for i in range(0, len(nums[curr])):
            res[curr] = res[curr] + nums[digits[curr]][i]
            print res[curr]
            self.letters(digits, curr + 1, n, res)


    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        n = len(digits)
        res = [''] * n
        print 'before', res
        self.letters(digits, 0, n, res)
        return res

#s = Solution()
#print(s.letterCombinations('23'))

# hashTable[i] stores all characters that correspond to digit i in phone
hashTable = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

# A recursive function to print all possible words that can be obtained
# by input number[] of size n.  The output words are one by one stored
# in output[]
def printWordsUtil(number, curr_digit, output, n):
    if curr_digit == n:
        output = output + ' '
        print output
        return

    # Try all 3 possible characters for current digir in number[]
    # and recur for remaining digits
    for i in range(0, len(hashTable[number[curr_digit]])):
        output = output + hashTable[number[curr_digit]][i]
        printWordsUtil(number, curr_digit+1, output, n);
        if number[curr_digit] == 0 or number[curr_digit] == 1:
            return

# A wrapper over printWordsUtil().  It creates an output array and
# calls printWordsUtil()
def printWords(number, n):
    result = ''
    printWordsUtil(number, 0, result, n);


number = [2, 3]
n = len(number)
printWords(number, n)