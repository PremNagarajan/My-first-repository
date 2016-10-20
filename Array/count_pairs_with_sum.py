"""
Count pairs with given sum

Given an array of integers, and a number ‘sum’,
find the number of pairs of integers in the array whose sum is equal to ‘sum’.

Below is the Algorithm.

1) Create a map to store frequency of each number in the array.

2) In the next traversal, for every element check if it can be combined with
any other element (other than itself!) to give the desired sum.
Increment the counter accordingly.

3) After completion of second traversal, we’d have twice the required value
stored in counter because every pair is counted two times.
Hence divide count by 2 and return.

"""

def countPairs(arr, k):
    temp = dict()
    for a in arr:
        if a in temp:
            temp[a] += 1
        else:
            temp[a] = 1
        
    count = 0    
    for a in arr:
        if k-a in temp:
            count += temp[k-a]
            
        if k-a == a:
            count -= 1
            
    return count / 2
    
arr = [1, 5, 7, -1, 5]
k = 6
print countPairs(arr, k)