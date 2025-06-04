from collections import deque

class Solution:
    def bfs(self, node, adjLs, vis):
        vis[node] = 1
        q = deque()
        q.append(node)

        while q:
            i = q.popleft()
            for adjNodes in adjLs[i]:
                if vis[adjNodes] != 1:
                    vis[adjNodes] = 1
                    q.append(adjNodes)
    def dfs(self, node, adjLs, vis):
        vis[node] = 1

        for it in adjLs[node]:
            if not vis[it]:
                self.dfs(it, adjLs, vis)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        V = len(isConnected)

        adjLs = [[] for _ in range(V)]

        for i in range(V):
            for j in range(V):
                if isConnected[i][j] == 1 and i != j:
                    adjLs[i].append(j)
                    adjLs[j].append(i)
                
        vis = [0] * V
        count = 0

        for i in range(V):
            if vis[i] == 0:
                count += 1
                self.bfs(i, adjLs, vis)
        return count
        