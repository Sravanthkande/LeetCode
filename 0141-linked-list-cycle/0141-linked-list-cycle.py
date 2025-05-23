# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #define slow and fast pointer from tortoise and hare algo
        slow, fast = head, head 

        while fast and fast.next:
            #move slow pointer on step and fast pointer two steps
            slow = slow.next
            fast = fast.next.next

            #if at any movement both slow and fast pointers are equal return cycle exits
            if slow == fast:
                return True 
        return False