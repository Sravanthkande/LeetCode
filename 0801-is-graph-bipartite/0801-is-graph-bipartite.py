from collections import deque 

class Solution:
    def BFS(self, i, adj, color):
        que = deque()
        que.append(i)

        color[i] = 0

        while que:
            node = que.popleft()
            for neighbor in adj[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    que.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False 
        return True 

    def isBipartite(self, graph: List[List[int]]) -> bool:
        V = len(graph)
        color = [-1] * V 

        for i in range(V):
            if color[i] == -1:
                if not self.BFS(i, graph, color):
                    return False 
        return True
        