# Complete the function below.

def  cutSticks(lengths):
    result = []
    lengths.sort(reverse=True)
    while len(lengths) > 0:
        result.append(len(lengths))
        block_cut = lengths.pop()
        while len(lengths) > 0 and lengths[-1] <= block_cut:
            lengths.pop()
    return result