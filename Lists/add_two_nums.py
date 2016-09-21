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
        #1.reverseIList()
        #l2.reverseIList()
        if l1.length() < l2.length():
            temp = l1
            l1 = l2
            l2 = temp

        result = LinkedList()
        remainder = None

        list1 = l1.head
        list2 = l2.head
        while list1 and list2:
            a = list1.val
            b = list2.val
            if remainder:
                sum = a + b + remainder
            else:
                sum = a + b
            quotient = sum % 10
            remainder = sum / 10
            result.push(quotient)
            list1 = list1.next
            list2 = list2.next

        while list1:
            if remainder:
                sum = list1.val + remainder
                quotient = sum % 10
                remainder = sum / 10
                result.push(quotient)
            else:
                result.push(list1.val)
            list1 = list1.next

        result.reverseList()
        return result

l1 = LinkedList()
l1.push(3)
l1.push(4)
l1.push(2)
l1.push(1)
l1.printList()

l2 = LinkedList()
l2.push(4)
l2.push(6)
l2.push(5)
l2.printList()

s = Solution()
res = s.addTwoNumbers(l2, l1)
res.printList()
