'''
Merge two sorted linked lists and return it as a new list.

The new list should be made by splicing together the nodes of the
first two lists.

'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        temp = self
        while temp:
            print temp.val,
            temp = temp.next
            if temp:
                print '->',
        return ''

    def insert_at_the_end(self, data):
        temp = self
        while temp.next:
            temp = temp.next
        newNode = ListNode(data)
        temp.next = newNode

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode('1')
        head = l3
        while l1 and l2:
            if l1.val < l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        if l1:
            l3.next = l1
        else:
            l3.next = l2
        return head.next

l1 = ListNode(1)
l1.insert_at_the_end(3)
l1.insert_at_the_end(4)
l2 = ListNode(2)
l2.insert_at_the_end(5)
print l1
print l2
s = Solution()
l3 = s.mergeTwoLists(l1, l2)
print l3