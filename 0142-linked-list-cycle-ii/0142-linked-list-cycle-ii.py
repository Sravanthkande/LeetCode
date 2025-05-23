# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #define slow and fast pointers from tortoise and hare algo
        slow, fast = head, head

        while fast and fast.next:
            #move slow pointe one step and fast pointer two steps
            slow = slow.next
            fast = fast.next.next

            #at any point both slow and fast pointers are equal
            if slow == fast:
                #update slow to head
                slow = head
                #if slow and fast are not equal
                while slow != fast:
                    #move slow and fast one step
                    slow = slow.next
                    fast = fast.next
                #return slow
                return slow 
        return None