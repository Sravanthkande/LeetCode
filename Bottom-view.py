from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def bottomView(self, root):
        # List to store the result
        ans = []

        # Check if the tree is empty
        if not root:
            return ans

        # Dictionary to store the bottom view nodes
        # based on their vertical positions
        mpp = {}

        # Queue for BFS traversal, each
        # element is a pair containing node
        # and its vertical position
        q = deque([(root, 0)])

        # BFS traversal
        while q:
            # Retrieve the node and its vertical
            # position from the front of the queue
            node, line = q.popleft()

            # Update the dictionary with the node's data
            # for the current vertical position
            mpp[line] = node.data

            # Process left child
            if node.left:
                # Push the left child with a decreased
                # vertical position into the queue
                q.append((node.left, line - 1))

            # Process right child
            if node.right:
                # Push the right child with an increased
                # vertical position into the queue
                q.append((node.right, line + 1))

        # Transfer values from the
        # dictionary to the result list
        for key in sorted(mpp.keys()):
            ans.append(mpp[key])

        return ans

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

    # Get the Bottom View traversal
    bottom_view = solution.bottomView(root)

    # Print the result
    print("Bottom View Traversal: ")
    for node in bottom_view:
        print(node, end=" ")
