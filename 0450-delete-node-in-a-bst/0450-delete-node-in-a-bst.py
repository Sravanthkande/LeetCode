# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def connector(self, root):
        if not root.left:
            return root.right
        elif not root.right:
            return root.left 
        
        leftChild = root.left 
        left_in_rightSubtree = root.right 

        while left_in_rightSubtree.left:
            left_in_rightSubtree = left_in_rightSubtree.left 
        
        left_in_rightSubtree.left = leftChild 
        return root.right 

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if root.val == key:
            return self.connector(root)
        
        node = root
        while node:
            if node.val > key:
                if node.left and node.left.val == key:
                    node.left = self.connector(node.left)
                    break
                else:
                    node = node.left
                
            else:
                if node.right and node.right.val == key:
                    node.right = self.connector(node.right)
                    break 
                else:
                    node = node.right 
            
        return root