def powerset(s):
    n = len(s)
    masks = [1<<j for j in xrange(n)]
    for i in xrange(2**n):
        yield [s[j] for j in range(n) if (masks[j] & i)]
        
def  buildSubsequences( s):
    all = powerset(s)
    result = []
    for a in all:
        if a:
            result.append(''.join(a))
    return sorted(result)
    
print buildSubsequences('hello')