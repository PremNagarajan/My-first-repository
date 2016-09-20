class element(object):
    index = None
    data = None
    
    def __init__(self, index, data):
        self.index = index
        self.data = data

def next_greater_element(input):
    stack = list()
    result = [-1 for e in input]
    for index in range(0, len(input)):
        data = input[index]
        curr = element(index, data)
        if not stack:
            stack.append(curr)
        else:
            while stack:
                top = stack.pop()
                if curr.data > top.data:
                    result[top.index] = curr.data
                else:
                    stack.append(top)
                    stack.append(curr)
                    break
            if not stack:
                stack.append(curr)
    print result
    
input = [8, 3, 2, 5, 9, 7, 1, 6, 10]
print input
next_greater_element(input)