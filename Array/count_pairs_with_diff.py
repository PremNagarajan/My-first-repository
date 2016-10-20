# Complete the function below.

def  countPairs(numbers, k):
    count = 0
    numbers = sorted(numbers)
    
    l = 0
    r = 0
    prev_l = None
    prev_r = None
    while r < len(numbers):
        if (numbers[r] - numbers[l]) == k:
            if prev_l and prev_r:
                if numbers[r] == prev_r or numbers[l] == prev_l:
                    l += 1
                    r += 1
                    continue
            count += 1
            l += 1
            r += 1
            prev_l = numbers[l]
            prev_r = numbers[r]
        elif (numbers[r] - numbers[l]) > k:
            l += 1
            #prev_l = numbers[l]
        else:
            r += 1
            #prev_r = numbers[r]
    
    return count

print countPairs([1, 5, 3, 4, 2], 1)