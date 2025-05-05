# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursive(self, root, nums):
        if not root:
            return
        self.recursive(root.left, nums)
        self.recursive(root.right, nums)
        nums.append(root.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nums = []
        self.recursive(root, nums)
        return nums
        