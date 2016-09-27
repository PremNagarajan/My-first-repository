'''
Given a linked list, remove the nth node from the end of list and
return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end,
   the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def printList(self):
        temp = self
        while temp:
            print temp.val,
            temp = temp.next
            if temp:
                print '->',

    def insert_at_the_end(self, data):
        temp = self
        while temp.next:
            temp = temp.next
        newNode = ListNode(data)
        temp.next = newNode


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = head
        for i in range(0, n):
            temp = temp.next

        prev = None
        curr = head

        while temp:
            prev = curr
            curr = curr.next
            temp = temp.next

        if prev:
            prev.next = curr.next
        else:
            head = head.next
        return head


s = Solution()
head = ListNode(1)
head.insert_at_the_end(2)
head.insert_at_the_end(3)
head.insert_at_the_end(4)
head.insert_at_the_end(5)
newHead = s.removeNthFromEnd(head, 2)
newHead.printList()