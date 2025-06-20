# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        #find middle through fast and slow pointers
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 
        
        #By the moment fast reaches end, slow will be pointing to mid

        #reverse the second half
        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        #Compare both
        first, second = head, prev

        while second:
            if first.val != second.val:
                return False 
            
            first = first.next
            second = second.next 
        
        return True