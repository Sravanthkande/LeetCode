# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        #Map to store nodes at vertical order
        node_map = defaultdict(lambda : defaultdict(list))

        #queue for BFS traversal and to store node with x and y coordinates
        queue = deque([(root, 0, 0)])

        while queue:
            node, x, y = queue.popleft()
            node_map[x][y].append(node.val)
            if node.left:
                queue.append((node.left, x-1, y+1))
            if node.right:
                queue.append((node.right, x+1, y+1))
        
        #Prepare the result by sorting keys and compiling nodes
        res = []
        for x in sorted(node_map):
            column = []
            for y in sorted(node_map[x]):
                #Sort the nodes at same position to maintain the order
                column.extend(sorted(node_map[x][y]))
            res.append(column)
        return res