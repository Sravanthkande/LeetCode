# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def validate(self, root, minVal, maxVal):
        if root is None:
            return True
        
        if root.val <= minVal or root.val >= maxVal:
            return False 
        
        left = self.validate(root.left, minVal, root.val)
        right = self.validate(root.right, root.val, maxVal)

        return left and right
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float('-inf'), float('inf'))