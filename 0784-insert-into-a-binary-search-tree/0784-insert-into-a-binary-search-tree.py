# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursive(self, node, val):
        if node is None:
            return TreeNode(val)
        
        if val < node.val:
            node.left = self.recursive(node.left, val)
        elif val > node.val:
            node.right = self.recursive(node.right, val)
        
        return node

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.recursive(root, val)
        