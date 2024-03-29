# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        l, m, r = head, head.next, None
        while m:
            r = m.next
            m.next = l
            l = m 
            m = r 
        head.next = None    
        return l
