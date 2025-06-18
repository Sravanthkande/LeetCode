# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #Edge case
        if not head or not head.next:
            return head
            
        odd = head
        even = head.next

        #store first even node to link after
        firstEven = head.next

        while even and even.next:

            #link alternate odd node and even nodes 
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next
        #now the links are organized according to odd and even nodes
        #now link odd.next to fistEven to return the order
        odd.next = firstEven
        return head
        