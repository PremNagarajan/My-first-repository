# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList(object):
    head = None

    def printList(self):
        temp = self.head
        while temp:
            print temp.val, '->' ,
            temp = temp.next
        print 'NULL'

    def push(self, data):
        newNode = ListNode(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def pop(self):
        if not self.head:
            return None
        val = self.head.val
        self.head = self.head.next
        return val

    def reverseList(self):
        if not self.head:
            return
        self.reverseUtil(self.head, None)

    def reverseUtil(self, curr, prev):
        if not curr.next:
            self.head = curr
            curr.next = prev
            return
        next = curr.next
        curr.next = prev
        self.reverseUtil(next, curr)

    def reverseIList(self):
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def length(self):
        temp = self.head
        count = 0
        while temp:
            count = count + 1
            temp = temp.next
        return count

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1.reverseIList()
        l2.reverseIList()
        if l1.length() < l2.length():
            temp = l1
            l1 = l2
            l2 = temp

        l1.printList()
        l2.printList()
        result = LinkedList()
        remainder = None
        while True:
            a = l1.pop()
            print a
            if a is None and not remainder:
                break
            a = a if a else 0
            b = l2.pop()
            b = b if b else 0
            if remainder:
                sum = a + b + remainder
            else:
                sum = a + b
            quotient = sum / 10
            remainder = sum % 10
            print quotient, remainder
            result.push(quotient)
        return result

l1 = LinkedList()
l1.push(3)
l1.push(4)
l1.push(2)
l1.printList()

l2 = LinkedList()
l2.push(4)
l2.push(6)
l2.push(5)
l2.printList()

s = Solution()
#res = s.addTwoNumbers(l1, l2)
#res.printList()
