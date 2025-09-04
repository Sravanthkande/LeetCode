# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head

        #Traverse and maintain decreasing stack
        while curr:
            while stack and stack[-1].val < curr.val:
                stack.pop()
            
            stack.append(curr)
            curr = curr.next

        #Rebuild the linked list from stack
        for i in range(len(stack) -1):
            stack[i].next = stack[i + 1]
        
        stack[-1].next = None

        return stack[0] if stack else None