class my_queue(object):
    s1 = list()
    s2 = list()
        
    def enque(self, a):
        self.s1.append(a)
            
    def deque(self):
        if not self.s1 and not self.s2:
            print "The queue is empty"
            return
        
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
            
        return self.s2.pop()

def main():
    q = my_queue()
    q.enque(1)
    q.enque(2)
    print q.deque()
    q.enque(3)
    q.enque(4)
    print q.deque()
    q.enque(5)
    print q.deque()
    print q.deque()
    print q.deque()

main()