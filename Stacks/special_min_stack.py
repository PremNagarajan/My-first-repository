class StackNode(object):
    data = None
    min_value = None

    def __init__(self, data, min_value):
        self.data = data
        self.min_value = min_value

class SpecialStack(object):
    stack = list()

    def push(self, data):
        curr = StackNode(data, None)
        if len(self.stack) == 0:
            curr.min_value = data
            self.stack.append(curr)
        else:
            top = self.stack.pop()
            if curr.data < top.min_value:
                curr.min_value = curr.data
            else:
                curr.min_value = top.min_value
            self.stack.append(top)
            self.stack.append(curr)

    def pop(self):
        return self.stack.pop().data

    def get_min(self):
        top = self.stack.pop()
        min_value = top.min_value
        self.stack.append(top)
        return min_value

stack = SpecialStack()
stack.push(3)
print stack.get_min()
stack.push(5)
print stack.get_min()
stack.push(1)
print stack.get_min()
stack.push(8)
print stack.get_min()
stack.push(2)
print stack.get_min()
stack.push(9)
print stack.get_min()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
print stack.get_min()