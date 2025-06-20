# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        prev = dummy
        dummy.next = head

        while head and head.next:

            first = head
            second = head.next

            #initial order prev -> first -> second
            prev.next = second           #this will link prev -> second
            first.next = second.next     #this will link first -> second.next 
            second.next = first          #this will connect two nodes second -> first

            #the order will prev -> second -> first
        
            #After move pointers
            prev = first
            head = first.next 

        return dummy.next