class Solution:
    def isBalanced(self, root):

        #Function to check if the tree is balanced
        def dfsHeight(root):

            #Base case: if the current node is None,
            #return 0
            if not root:
                return 0
            
            #Recursively calculate the height of the left subtree
            leftHeight = dfsHeight(root.left)

            #if the left subtree is unbalanced,
            #propagate the unbalanced status
            if leftHeight == -1:
                return -1
            

            #Recursively calculate the height of the right subtree,
            rightHeight = dfsHeight(root.right)
            #if the right subtree is unbalanced,
            #propagate the unbalanced status
            if rightHeight == -1:
                return -1
            
            # Check if the difference in height between left and right subtrees is greater than 1
            # If it's greater, the tree is unbalanced,
            # return -1 to propagate the unbalance status
            if abs(leftHeight - rightHeight) > 1:
                return -1
            
            #return maximum height of the left and right subtrees,
            return max(leftHeight, rightHeight) + 1
        # Check if the tree's height difference between subtrees is less than 2
        # If not, return False; otherwise, return True
        return dfsHeight(root) != -1