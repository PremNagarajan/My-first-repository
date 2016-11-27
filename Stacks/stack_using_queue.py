'''

225. Implement Stack using Queues

Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

# Using two queues.
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue1 = list()
        self.queue2 = list()
        self.top_element = None
        
        
    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue1.append(x)
        self.top_element = x
        
        
    def pop(self):
        """
        :rtype: nothing
        """
        while self.queue1:
            front = self.queue1.pop(0)
            if self.queue1:
                self.queue2.append(front)
                self.top_element = front
            else:
                self.queue1, self.queue2 = self.queue2, self.queue1
                return
                
        

    def top(self):
        """
        :rtype: int
        """
        return self.top_element
        

    def empty(self):
        """
        :rtype: bool
        """
        if self.queue1:
            return False
        return True
'''

# Using one queue.
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue1 = list()
        self.top_element = None
        
        
    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue1.append(x)
        self.top_element = x
        
        
    def pop(self):
        """
        :rtype: nothing
        """
        size = len(self.queue1)
        i = 0
        while self.queue1:
            front = self.queue1.pop(0)
            if i < size - 1:
                self.queue1.append(front)
                self.top_element = front
                i+=1
            else:
                return
                
        

    def top(self):
        """
        :rtype: int
        """
        if not self.empty():
            return self.top_element
        

    def empty(self):
        """
        :rtype: bool
        """
        if self.queue1:
            return False
        return True

        
stack = Stack()
stack.push(1)
print stack.top()
print stack.empty()
stack.push(2)
print stack.top()
print stack.empty()
stack.push(3)
print stack.top()
print stack.empty()
stack.pop()
print stack.top()
print stack.empty()
stack.pop()
print stack.top()
print stack.empty()
stack.pop()
print stack.top()
print stack.empty()