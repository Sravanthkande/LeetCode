# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     nodes = []

    #     for lst in lists:
    #         while lst:
    #             nodes.append(lst.val)
    #             lst = lst.next
            
    #     nodes.sort()

    #     dummy = ListNode(0)
    #     cur = dummy

    #     for node in nodes:
    #         cur.next = ListNode(node)
    #         cur = cur.next
        
    #     return dummy.next this one is brute force using TC-O(N log N) and SC-O(N)

    def mergedLists(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        for i in range(1, len(lists)):
            lists[i] = self.mergedLists(lists[i- 1], lists[i])
        
        return lists[-1]
        #This is optimal approach using TC-O(N * K) and SC-O(1)
    
