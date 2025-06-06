# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    #Function to check if a node is a leaf
    def isLeaf(self, root):
        return not root.left and not root.right
    
    #Function to add the left boundary of the tree
    def addLeftBoundary(self, root, res):
        cur = root.left 
        while cur:
            if not self.isLeaf(cur):
                res.append(cur.data)
            if cur.left:
                cur = cur.left 
            else:
                cur = cur.right
            
    #Function to add Right Boundary
    def addRightBoundary(self, root, res):
        cur = root.right
        temp = []
        while cur:
            if not self.isLeaf(cur):
                temp.append(cur.data)
            if cur.right:
                cur = cur.right 
            else:
                cur = cur.left
        res.extend(temp[::-1])
    
    #Function to add the leaf nodes of the tree
    def addLeaves(self, root, res):
        if self.isLeaf(root):
            res.append(root.data)
            return 
        if root.left:
            self.addLeaves(root.left, res)
        if root.right:
            self.addLeaves(root.right, res)
        
    #Fucntion to perform the boundary traversal
    def boundary(self, root):
        res = []
        if not root:
            return res 
        if not self.isLeaf(root):
            res.append(root.data)
        
        self.addLeftBoundary(root, res)
        self.addLeaves(root, res)
        self.addRightBoundary(root, res)

        return res