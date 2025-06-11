from collections import deque 

class Solution:
    def kahnsAlgo(self, N, adj):
        inDegree = [0] * N 
        ans = []

        for i in range(N):
            for neighbour in adj[i]:
                inDegree[neighbour] += 1

        que = deque()

        for i in range(N):
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

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            adj[v].append(u)
        
        topo = self.kahnsAlgo(numCourses, adj)

        if len(topo) < numCourses:
            return False
        return True