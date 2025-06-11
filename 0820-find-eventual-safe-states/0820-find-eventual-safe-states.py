class Solution:
    def kahnsAlgo(self, V, adj):
        inDegree = [0] * V
        ans = []
        for i in range(V):
            for neighbour in adj[i]:
                inDegree[neighbour] += 1
        
        que = deque()
        for i in range(V):
            if inDegree[i] == 0:
                que.append(i)
        
        while que:
            node = que.popleft()
            ans.append(node)

            for neighbour in adj[node]:
                inDegree[neighbour] -= 1
                if inDegree[neighbour] == 0:
                    que.append(neighbour)
        return ans

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)

        adjRev = [[] for _ in range(V)]

        for i in range(V):
            for j in graph[i]:
                adjRev[j].append(i)
        res = self.kahnsAlgo(V, adjRev)
        res.sort()
        return res