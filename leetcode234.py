'''
如果要O(1)空间的话，只能把前半部分链表翻转，可以先遍历获取长度后翻转，亦可以使用快慢指针遍历时候同时翻转
'''

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        
        if not head.next.next:
            if head.val == head.next.val:
                return True
            else:
                return False
        
        slow, fast = head, head
        second = None
        pre = None
        
        while fast.next and fast.next.next:
            s = slow
            slow = slow.next
            second = slow.next
            fast = fast.next.next
            s.next = pre
            pre = s
        slow.next = pre
            
        if fast.next:
            return self.judge(slow, second)
        else:
            return self.judge(slow.next, second)
        
    def judge(self, first, second):
        while first and second:
            # print(first.val, second.val)
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
            
        return True
