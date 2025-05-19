# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    # Function to return the Right view of the binary tree
    def rightSideView(self, root):
        res = []
        
        # Call the recursive function to populate the right-side view
        self.recursionRight(root, 0, res)
        
        return res

    # Function to return the Left view of the binary tree
    def leftSideView(self, root):
        res = []
        
        # Call the recursive function to populate the left-side view
        self.recursionLeft(root, 0, res)
        
        return res

    # Recursive function to traverse the binary tree and populate the left-side view
    def recursionLeft(self, root, level, res):
        # Check if the current node is NULL
        if root is None:
            return
        
        # Check if the size of the result list is equal to the current level
        if len(res) == level:
            # If equal, add the value of the current node to the result list
            res.append(root.data)
        
        # Recursively call the function for the left child with an increased level
        self.recursionLeft(root.left, level + 1, res)
        
        # Recursively call the function for the right child with an increased level
        self.recursionLeft(root.right, level + 1, res)

    # Recursive function to traverse the binary tree and populate the right-side view
    def recursionRight(self, root, level, res):
        # Check if the current node is NULL
        if root is None:
            return
        
        # Check if the size of the result list is equal to the current level
        if len(res) == level:
            # If equal, add the value of the current node to the result list
            res.append(root.data)
        
        # Recursively call the function for the right child with an increased level
        self.recursionRight(root.right, level + 1, res)
        
        # Recursively call the function for the left child with an increased level
        self.recursionRight(root.left, level + 1, res)

# Main method to test the functionality
if __name__ == "__main__":
    # Creating a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(10)
    root.left.left.right = TreeNode(5)
    root.left.left.right.right = TreeNode(6)
    root.right = TreeNode(3)
    root.right.right = TreeNode(10)
    root.right.left = TreeNode(9)

    solution = Solution()

    # Get the Right View traversal
    rightView = solution.rightSideView(root)

    # Print the result for Right View
    print("Right View Traversal:", end=" ")
    for node in rightView:
        print(node, end=" ")
    print()

    # Get the Left View traversal
    leftView = solution.leftSideView(root)

    # Print the result for Left View
    print("Left View Traversal:", end=" ")
    for node in leftView:
        print(node, end=" ")
    print()
