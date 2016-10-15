import sys

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def printList(self):
        temp = self
        while temp:
            sys.stdout.write(str(temp.val))
            #print temp.val
            temp = temp.next
            #if temp:
                #sys.stdout.write('->')

    def insert_at_the_end(self, data):
        temp = self
        while temp.next:
            temp = temp.next
        newNode = ListNode(data)
        temp.next = newNode
        
    def push(self, data):
        temp = self
        while temp.next:
            temp = temp.next
        newNode = ListNode(data)
        temp.next = newNode
        
    def delete_greater_than(self, x):
        new_list_head = ListNode(self.val)
        new_list = new_list_head
        temp = self
        while temp.next:
            if temp.val > x:
                new_list.next = temp.next
            else:
                new_list.next = temp
            temp = temp.next
        return new_list_head.next

def list_length(head):
    temp = head
    count = 0
    while temp:
        count = count + 1
        temp = temp.next
    return count

def removeNodes(list, x):
    
    if list_length(list) == 0:
        return
        
    new_list_head = ListNode(list.val)
    new_list = new_list_head
    temp = list
    while temp.next:
        if temp.val > x:
            sys.stdout.write(str(new_list.val))
            new_list.next = None
        else:
            new_list.next = temp
            new_list = new_list.next
        temp = temp.next
    return new_list_head.next
    
    
l1 = ListNode(0)
l1.push(3)
l1.push(4)
l1.push(2)
l1.push(1)

removeNodes(l1, 2)