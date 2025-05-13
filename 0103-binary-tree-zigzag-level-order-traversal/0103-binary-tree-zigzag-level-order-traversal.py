# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res 
        nodeQueue = deque([root])
        leftToRight = True 

        while nodeQueue:
            size = len(nodeQueue)
            row = [0] * size 
            for i in range(size):
                node = nodeQueue.popleft()
                index = i if leftToRight else (size - 1 - i)
                row[index] = node.val
                if node.left:
                    nodeQueue.append(node.left)
                if node.right:
                    nodeQueue.append(node.right)
            leftToRight = not leftToRight 
            res.append(row)
        return res

        