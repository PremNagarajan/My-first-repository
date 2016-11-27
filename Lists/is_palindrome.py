'''

234. Palindrome Linked list.

Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def length(self, list):
        count = 0
        while list:
            count += 1
            list = list.next
        return count
    
    def reverse(self, head):
        prev, curr, next = None, head, None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    
    def compare(self, list1, list2):
        while list1 and list2:
            if list1.val != list2.val:
                return False
            list1 = list1.next
            list2 = list2.next
        return True
    
    def isPalindrome(self, list):
        if not list:
            return True
        i, n = 0, self.length(list)
        temp = list
        while i < n/2:
            temp = temp.next
            i += 1
        if temp:
            new_sub_list = self.reverse(temp)
            is_pal = self.compare(list, new_sub_list)
            self.reverse(new_sub_list)
            return is_pal