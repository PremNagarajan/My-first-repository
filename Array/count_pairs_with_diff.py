"""

Count all distinct pairs with difference equal to k

Given an integer array and a positive integer k,
count all distinct pairs with difference equal to k.

"""

# Works only for distinct elements
def pairs(arr,k):
    #a contains array of numbers and k is the value of difference
    n = len(arr)
    l = 0
    r = l + 1
    arr = sorted(arr)
    count = 0
    
    while r < n:
        if arr[r] - arr[l] == k:
            count += 1
            l += 1
            r += 1
        elif arr[r] - arr[l] < k:
            r += 1
        else:
            l += 1

    return count
    
# Handles duplicate case
def pairs2(arr,k):
    # a contains array of numbers and k is the value of difference
    n = len(arr)
    temp = dict()
    
    for a in arr:
        if a in temp:
            temp[a] += 1
        else:
            temp[a] = 1

    count = 0
    for a in arr:
        if a+k in temp and temp[a+k] > 0:
            count += 1
        if a-k in temp  and temp[a-k] > 0:
            count += 1
        temp[a] -= 1
            
    return count
    
print pairs2([1, 5, 5, 3, 4, 2], 2)