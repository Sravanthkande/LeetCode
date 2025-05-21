# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0 
        
        ans = 0

        q = deque([(root, 0)])
        first = last = 0

        while q:
            mmin = q[0][1]
            size = len(q)
            for i in range(size):
                curId = q[0][1] - mmin
                node = q[0][0]
                q.popleft()

                if i==0:
                    first = curId
                if i == size-1:
                    last = curId 
                
                if node.left:
                    q.append((node.left, curId*2+1))
                if node.right:
                    q.append((node.right, curId*2+2))
            ans = max(ans, last - first + 1)
        return ans