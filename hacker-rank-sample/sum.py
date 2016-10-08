#!/bin/python

import sys
import os

# Complete the function below.


def  sum(numbers):
    res = 0
    for num in numbers:
        res += num
    return res
    
_numbers_cnt = 0
_numbers_cnt = int(raw_input())
_numbers_i=0
_numbers = []


#f = open(os.environ['OUTPUT_PATH'], 'w')

while _numbers_i < _numbers_cnt:
    _numbers_item = int(raw_input());
    _numbers.append(_numbers_item)
    _numbers_i+=1
    

res = sum(_numbers);
sys.stdout.write(str(res) + "\n")
#f.write(str(res) + "\n")
sys.stdout.close()
#f.close()