# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        
        cnt, temp = 0, head
        while temp:
            cnt += 1
            temp = temp.next
        
        if cnt == n: return head.next

        res = cnt - n
        temp = head

        while res > 1:
            res -= 1
            temp = temp.next
        
        temp.next = temp.next.next
        return head