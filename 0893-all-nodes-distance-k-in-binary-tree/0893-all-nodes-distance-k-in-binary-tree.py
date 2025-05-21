# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        #Create a map to store the parents of each node
        parentMap = {}
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                parentMap[node.left] = node
                queue.append(node.left)
            if node.right:
                parentMap[node.right] = node
                queue.append(node.right)
        #Use BFS to find all the nodes at a distance k from the target
        result = []
        visited = set()
        queue = deque([target])
        visited.add(target)
        curDistance = 0

        #Continue BFS until the disired distance is reached
        while queue:
            if curDistance == k:
                result.extend(node.val for node in queue)
                return result
            for _ in range(len(queue)):
                node = queue.popleft()
                #check left child
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append(node.left)
                #check right child
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append(node.right)
                #Check fot Parent
                if node in parentMap and parentMap[node] not in visited:
                    visited.add(parentMap[node])
                    queue.append(parentMap[node])
            curDistance += 1
        return result