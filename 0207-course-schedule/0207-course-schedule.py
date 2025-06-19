class Solution:
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     #make a graph from prerequisites

    #     graph = defaultdict(list)

    #     for u, v in prerequisites:
    #         graph[u].append(v)
        
    #     vis = [0] * numCourses

    #     def dfs(node):

    #         if vis[node] == 1:
    #             return False 
            
    #         if vis[node] == 2:
    #             return True 
            
    #         vis[node] = 1

    #         for neighbour in graph[node]:
    #             if not dfs(neighbour):
    #                 return False 
                
    #         vis[node] = 2
    #         return True 
        
    #     for i in range(numCourses):
    #         if not dfs(i):
    #             return False 
            
    #     return True this is a DFS approach using TC - O(v + e) and SC -O(v + e)

    def kahnsAlgo(self, v, graph):
        degree = [0] * v

        for i in range(v):
            for neighbour in graph[i]:
                degree[neighbour] += 1
            
        que = deque()

        for i in range(v):
            if degree[i] == 0:
                que.append(i)
            
        ans = []

        while que:
            node = que.popleft()
            ans.append(node)

            for neighbour in graph[node]:
                degree[neighbour] -= 1
                
                if degree[neighbour] == 0:
                    que.append(neighbour)
                
        return ans
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            graph[v].append(u)
        
        topo = self.kahnsAlgo(numCourses, graph)

        if len(topo) < numCourses:
            return False 
        return True
        #This approach using topo sort algo TC-O(v + e) and SC-O(v + e)
        