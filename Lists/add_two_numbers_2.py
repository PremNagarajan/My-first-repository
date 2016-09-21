# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def printList(list):
    temp = list
    while temp:
        print temp.val, '->' ,
        temp = temp.next
    print 'NULL'

def push(head, data):
    temp = head
    while temp.next:
        temp = temp.next
    newNode = ListNode(data)
    temp.next = newNode

def length(head):
    temp = head
    count = 0
    while temp:
        count = count + 1
        temp = temp.next
    return count

def reverseIList(head):
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #l1.reverseIList()
        #l2.reverseIList()
        if length(l1) < length(l2):
            temp = l1
            l1 = l2
            l2 = temp

        result = None
        remainder = None

        while l1 and l2:
            a = l1.val
            b = l2.val
            if remainder:
                sum = a + b + remainder
            else:
                sum = a + b
            quotient = sum % 10
            remainder = sum / 10
            if result:
                push(result, quotient)
            else:
                result = ListNode(quotient)
            l1 = l1.next
            l2 = l2.next

        while l1:
            if remainder:
                sum = l1.val + remainder
                quotient = sum % 10
                remainder = sum / 10
                if result:
                    push(result, quotient)
                else:
                    result = ListNode(quotient)
            else:
                if result:
                    push(result, l1.val)
                else:
                    result = ListNode(l1.val)
            l1 = l1.next

        if remainder:
            if result:
                    push(result, remainder)
            else:
                result = ListNode(remainder)

        return reverseIList(result)

l1 = ListNode(5)
printList(l1)

l2 = ListNode(5)
printList(l2)

s = Solution()
res = s.addTwoNumbers(l2, l1)
printList(res)
