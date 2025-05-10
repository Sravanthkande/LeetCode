# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMaxPathSum(self, root, maxi):
        if not root:
            return 0
        leftPath = max(0, self.findMaxPathSum(root.left, maxi))
        rightPath = max(0, self.findMaxPathSum(root.right, maxi))

        maxi[0] = max(maxi[0], leftPath + rightPath + root.val)
        return max(leftPath, rightPath) + root.val
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxi = [float("-inf")]
        self.findMaxPathSum(root, maxi)
        return maxi[0]
        