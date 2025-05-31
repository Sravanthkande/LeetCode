# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def inOrder(node):
            if not node:
                return []
            return inOrder(node.left) + [node.val] + inOrder(node.right)
        
        elements = inOrder(root)
        left, right = 0, len(elements) - 1

        while left < right:
            curSum = elements[left] + elements[right]
            if curSum == k:
                return True
            elif curSum < k:
                left += 1
            else:
                right -= 1
        return False
        