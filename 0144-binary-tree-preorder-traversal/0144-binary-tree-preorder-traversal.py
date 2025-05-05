# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursive(self, node, nums):
        if node is None:
            return
        nums.append(node.val)
        self.recursive(node.left, nums)
        self.recursive(node.right, nums)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nums = []
        self.recursive(root, nums)
        return nums