# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast= head, head

        #Move fast ahead by n steps
        for _ in range(n):
            fast = fast.next
        
        if not fast:
            return head.next
        
        #move both pointers until fast reaches null
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        #once fast reaches null that means next node is nth node, remove it
        slow.next = slow.next.next
        return head