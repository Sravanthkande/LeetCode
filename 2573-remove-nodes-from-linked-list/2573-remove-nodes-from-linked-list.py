# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        stack = []
        cur = head

        while cur:

            while stack and stack[-1].val < cur.val:
                stack.pop()
            
            stack.append(cur)
            cur = cur.next
        
        for i in range(len(stack) - 1):
            stack[i].next = stack[i + 1]
            
        stack[-1].next = None

        return stack[0] if stack else None