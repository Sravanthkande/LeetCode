# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root):
        stack = []
        nums = []
        node = root

        while True:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                if not stack:
                    break
                node = stack.pop()
                nums.append(node.data)
                node = node.right
        return nums