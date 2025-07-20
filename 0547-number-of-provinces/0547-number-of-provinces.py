# from collections import deque

class Solution:
    # def BFS(self, start, adjLs, vis):
    #     vis[start] = True 

    #     que = deque()
    #     que.append(start)

    #     while que:
    #         node = que.popleft()

    #         for an in adjLs[node]:
    #             if not vis[an]:
    #                 vis[an] = True
    #                 que.append(an)
                
    def DFS(self, start, adjLs, vis):
        vis[start] = True

        for an in adjLs[start]:
            if not vis[an]:
                self.DFS(an, adjLs, vis)
                
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        V = len(isConnected)

        adjLs = [[] for _ in range(V)]

        for i in range(V):
            for j in range(V):
                if isConnected[i][j] == 1 and i != j:
                    adjLs[i].append(j)
                    adjLs[j].append(i)

        vis = [False] * V 
        count = 0

        for i in range(V):
            if not vis[i]:
                count += 1
                self.DFS(i, adjLs, vis)
            
        return count