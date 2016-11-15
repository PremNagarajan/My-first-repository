"""

Given an array arr[], find the maximum j – i such that arr[j] > arr[i].

Examples:

  Input: {34, 8, 10, 3, 2, 80, 30, 33, 1}
  Output: 6  (j = 7, i = 1)

  Input: {9, 2, 3, 4, 5, 6, 7, 8, 18, 0}
  Output: 8 ( j = 8, i = 0)

  Input:  {1, 2, 3, 4, 5, 6}
  Output: 5  (j = 5, i = 0)

  Input:  {6, 5, 4, 3, 2, 1}
  Output: -1 

http://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/

"""

def maximize_distance(arr):
    if not arr:
        return -1
        
    n = len(arr)
    left = [0] * n
    right = [0] * n
    
    left[0] = arr[0]
    for i in range(1, n):
        if left[i-1] > arr[i]:
            left[i] = arr[i]
        else:
            left[i] = left[i-1]
            
    right[n-1] = arr[n-1]
    for j in reversed(range(0, n-1)):
        if arr[j] > right[j+1]:
            right[j] = arr[j]
        else:
            right[j] = right[j+1]
            
    max_so_far, i, j = -1, 0, 0
    
    while i < n and j <n:
        if left[i] > right[j]:
            i += 1
        else:
            curr = j - i
            if curr > max_so_far:
                max_so_far = curr
            j += 1
    
    return max_so_far  
    
print maximize_distance([6, 5, 4, 3, 2, 1])
