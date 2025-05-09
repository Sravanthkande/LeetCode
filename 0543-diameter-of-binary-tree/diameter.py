class Solution:
    def getHeight(self, root, diameter):
        if not root:
            return 0
        
        lh = self.getHeight(root.left, diameter)
        rh = self.getHeight(root.right, diameter)

        diameter[0] = max(diameter[0], lh + rh)
        return 1 + max(lh, rh)
    
    def diameterOfBinaryTree(self, root):
        diameter = [0]

        self.getHeight(root, diameter)
        return diameter[0]