# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        #Approach is simple iterate in head and store values < x in beforeHead and values >= x as afterHead and link them up

        before = beforeHead = ListNode(0)
        after = afterHead = ListNode(0)

        while head:

            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next 
            head = head.next 
        
        after.next = None 
        before.next = afterHead.next

        return beforeHead.next

        #This will take you TC-O(N) and SC-O(1)