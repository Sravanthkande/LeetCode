# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     count = Count()
    #     cur = head

    #     while cur:
    #         count[cur.val] += 1
    #         cur = cur.next
        
    #     dummy = ListNode(0)
    #     newTail = dummy
    #     cur = head

    #     while cur:
    #         if count[cur.val] == 1:
    #             newTail.next = ListNode(cur.val)
    #             newTail = newTail.next
    #         cur = cur.next
        
    #     return dummy.next This is the naive approach using TC O(N) and SC O(N)

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        prev = dummy
        dummy.next = head

        while head:

            if head.next and head.val == head.next.val:

                while head.next and head.val == head.next.val:
                    head = head.next 
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next 
        
        return dummy.next

        #This is the optimal approach using TC - O(N) and SC-O(1)